from django.core.management.base import BaseCommand, CommandError
from VTAT_TOOL.models import Repository, RepositoryData, Genre, TestLogs
import datetime
import os
import re       
import git
import subprocess
from django.core.files import File


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.stdout.write('Successfully closed poll')
        

        def run_script_multiple(file_id,log_fp):
            success_iterations = 0
            fail_iterations = 0
            file_ide = RepositoryData.objects.filter(id=file_id)

            if file_ide:
                if file_ide:
                    file_obj = RepositoryData.objects.get(id=file_id)
                    cmd = file_obj.testcase_action
                    
                    if cmd == " ":
                        return {"success_iterations": success_iterations, "fail_iterations": fail_iterations, "status": 1}
                    parent_names = []
                    def parent_name(parentID):
                        parentID = RepositoryData.objects.get(id=parentID)
                        if parentID.parent:
                            parent_names.append(parentID.parent.testcase_name)
                            return parent_name(parentID.parent_id)
                        else:
                            return  parent_names

                    parent_names = parent_name(file_obj.id)
                    print ("parent_names",parent_names)


                    #if file_obj.parent and file_obj.parent.testcase_name == "runtest":
                    if "runtest" in parent_names:
                        os.chdir("/opt/ltp")
                        print (os.getcwd())
                        cmd = file_obj.testcase_action
                        print("cmd",cmd)
                    elif file_obj.parent and file_obj.parent.testcase_name == "testscripts":
                        os.chdir("/opt/ltp/testscripts")
                        cmd = file_obj.testcase_action
                    else:
                        pass
                    test_parent_name = parent_names[0]
                    parent_names = []


                    print("cmd", cmd)
                    print("88888888888888888888888")
                    if os.path.isfile(file_obj.log_name):
                        os.remove(file_obj.log_name)
                    process = subprocess.Popen(
                        cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
                    out, err = process.communicate()

                    print ("out is",out)
                    print ("err is",err)
                    print(file_obj.log_name)
                    print("//////////////////////////////////")
                    
                    with open(str(file_obj.log_name), "a") as fr:
                        fr.write('\nTest Name: {}'.format(test_parent_name))
                        fr.write('\nSubTest Name: {}\n'.format(file_obj.testcase_name))
                        fr.close()
                    
                    with open(str(file_obj.log_name), "r") as fr:
                        lines = fr.readlines()


                        #print("lines", lines)
                        if lines:
                            lines_data = ''.join(lines)
                            # lines_data = ''
                            # for line_data in lines:
                            #     lines_data=lines_data+line_data
                            log_fp.writelines(str(lines_data))#.encode('utf-8').strip())
                            if re.search(r"error|exception", fr.read(), re.I):
                                print("re")
                                fail_iterations += 1
                                return {"success_iterations": success_iterations, "fail_iterations": fail_iterations, "status": 0}
                            else:
                                print("err,", err)
                                if str(err).encode('utf-8') != '':
                                    log_fp.write(str(err).encode('utf-8'))
                                    fail_iterations += 1
                                    return {"success_iterations": success_iterations, "fail_iterations": fail_iterations, "status": 0}
                                else:
                                    success_iterations += 1
                                    return {"success_iterations": success_iterations, "fail_iterations": fail_iterations, "status": 1}
                        else:
                            fail_iterations += 1
                            return {"success_iterations": success_iterations, "fail_iterations": fail_iterations, "status": 0}
                        #fr.close()
                        os.chdir(BASE_DIR)
                # except Exception as e:
                    #fail_iterations +=1
                    # return
                    # {"success_iterations":success_iterations,"fail_iterations":fail_iterations,"status":-1}

            else:
                fail_iterations += 1
                return {"success_iterations": success_iterations, "fail_iterations": fail_iterations, "status": -1}



        repo=git.Repo("/var/lib/jenkins/workspace/Kibana/")
        hcommit = repo.head.commit
        print(hcommit)
        print(hcommit.diff('HEAD~1'))
        #print(dir(hcommit.diff('HEAD~1')))
        #print(dir(hcommit))
        print(hcommit.parents[0])
        #print(dir(hcommit.parents))

        # x=repo.git.diff(hcommit,hcommit.parents[0])
        # print(dir(x))
        dic = {}
        for diff_added in hcommit.diff('HEAD~1').iter_change_type('M'):
            #print(diff_added)
            #print(dir(diff_added))
            print ("\n")
            #print (diff_added.a_path)
            x=repo.git.diff(hcommit,hcommit.parents[0],diff_added.a_path)
            print(str(x))
            #print('\n'.join(str(x).split("\n")))

            #print(dir(x))
            for i in str(x).split("\n"):
                match = re.match(r'^-[a-zA-Z0-9_\s]+',i,re.DOTALL)
                if match:
                    testcase = diff_added.a_path.split("/")[-1]
                    print (match)
                    if dic.has_key(testcase):
                        dic[testcase].append(match.group()[1:])
                    else:
                        dic[testcase]=[]
                        dic[testcase].append(match.group()[1:])


        print (dic.items())
        print ("success")
        
        repo = Repository.objects.get(repository_name = 'LTP_NEW')
        #for key,val in dic.items():
        new_testcase_ids = []
        for key,value in dic.items():
            if key == "fs":
                repo_modules = RepositoryData.objects.get(repository_id=repo.id,testcase_name="filesystem")
            else:
                repo_modules = RepositoryData.objects.get(repository_id=repo.id,testcase_name=key)
            #print (repo_modules.get_children())
            #print (repo_modules.get_descendant_count())
            for testcase_val in value:
                log_file = "/tmp/"+testcase_val.replace(" ","_")+".log"
                test_action = "./runltp -p -l "+log_file+" -f "+key+" -s "+testcase_val
                print (test_action)
                print(log_file)
                r=RepositoryData.objects.create(repository_id=repo.id, parent=repo_modules, testcase_name=testcase_val, test_iterations="1", testcase_action=test_action, log_name=log_file)
                r.save()
                new_testcase_ids.append(r.id)

        for file_id in new_testcase_ids:
            plan_exec_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file = "/tmp/file_" + str(file_id)+"_"+plan_exec_start+".txt"
            log_fp = open(log_file, "a+")
            script_res = run_script_multiple(file_id, log_fp)
            print("script result", script_res)
            plan_exec_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_fp.close()

            fp = open(log_file)
            result = TestLogs()
            result.log_testcase_id = file_id
            result.log_file_name.save("file_"+str(file_id)+"_"+plan_exec_start+".txt", File(fp))
            fp.close()
            result.success_iterations = script_res["success_iterations"]
            result.Fail_iterations = script_res["fail_iterations"]
            result.script_exec_start = plan_exec_start
            result.script_exec_end = plan_exec_end

            if script_res["status"] == 1:
                result.script_status = "Pass"
            else:
                result.script_status = "Pass"
            result.save()
            continue

        self.stdout.write("Done !!")


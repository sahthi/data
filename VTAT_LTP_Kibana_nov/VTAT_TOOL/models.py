from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey

from django.db.models.signals import post_delete
from django.dispatch import receiver
import json
import ast

def get_upload_to(instance, filename):
    return 'uploads/excel_sheets/%s/%s/%s' % (instance.user,instance.repository_name, filename)

class Repository(models.Model):
    user = models.ForeignKey(User)
    repository_name = models.CharField(max_length=30, unique=True)
    repository_description = models.CharField(max_length=50, blank = True)
    repository_file = models.FileField(upload_to=get_upload_to)
    # repository_readme = models.FileField(upload_to=get_upload_to,blank = True)
    # updated_readme = models.FileField(upload_to=get_upload_to,blank=True)

    def __str__(self):
        return self.repository_name


class RepositoryData(MPTTModel):
    repository = models.ForeignKey(Repository)
    testcase_name = models.CharField(max_length = 50)
    parent = TreeForeignKey('self', null = True, blank = True, related_name = 'children', db_index = True)
    test_iterations = models.CharField(max_length = 50, default = 1)
    testcase_action = models.CharField(max_length = 100,blank = True)
    log_name = models.CharField(max_length = 100,blank = True)


    class MPTTMeta:
        order_insertion_by = ['testcase_name']

    def __str__(self):
        return str(self.testcase_name+"_"+str(self.id))

def get_upload_to_log(instance,filename):
    #return 'uploads/logs/%s/%s' %(instance.log_testcase,filename)
    return 'uploads/logs/%s' %(filename)

class TestLogs(models.Model):
    log_testcase = models.ForeignKey(RepositoryData)
    script_exec_start = models.CharField(max_length = 50,blank = True)
    script_exec_end = models.CharField(max_length = 50,blank = True)
    script_status = models.CharField(max_length = 30,blank = True)
    success_iterations = models.CharField(max_length = 20,blank = True)
    Fail_iterations = models.CharField(max_length = 20,blank = True)
    log_file_name = models.FileField(upload_to = get_upload_to_log,blank = True)
    

    def __str__(self):
        return str(self.id)
        
class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

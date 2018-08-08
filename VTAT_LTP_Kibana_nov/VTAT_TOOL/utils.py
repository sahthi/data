def transMPTTTable(instance, branches, i_max):

    row_query_instance = []
    row_query_instance_table = []
    sudo_row = []
    i = 0
    j = 0
    right = []
    num_device = []

    for i in range(i_max):
        row_query_instance.append(None)
        sudo_row.append(["sudo",1,1])

    for branch in branches:

        if (len(right)>0):
            last_right = int(right[len(right)-1])
            right_for_iter = list(right)

            for r in right_for_iter:
                if r < int(branch.rght):
                    right.pop()

            if last_right < int(branch.rght):
                j = j + 1

                ###
                device = instance.objects.get(rght=last_right)
                num_device.append(device.device_set.all().count())
                ###

                row_query_instance_table.append(row_query_instance)
                row_query_instance = []

                for i in range(i_max):
                     row_query_instance.append(None)

            row_query_instance[len(right)] = [branch,1,1]

        else:
            row_query_instance[0] = [branch,1,1]

        ind = '_'
        print (ind * len(right) + branch.name)
        print ("last: ", branch.rght)

        right.append(branch.rght)
    ##
    device = instance.objects.get(rght=right.pop())
    num_device.append(device.device_set.all().count())
    ##

    row_query_instance_table.append(row_query_instance)
    row_query_instance_table.insert(0, sudo_row)
    row_query_instance_table.append(sudo_row)

    max_row = len(row_query_instance_table)
    max_col = len(row_query_instance_table[0])
    row_count = 1
    row_span_number = 1
    col_count = 1

    for j in range(max_col):
        for i in range(max_row):

            if j == (max_col - 1):
                if row_query_instance_table[i][j]:
                    row_query_instance_table[i][j][1] = 1
                    row_query_instance_table[i][j][2] = 1
                    row_query_instance_table[i][j].append(7)#

            elif row_query_instance_table[i][j]:
                if row_query_instance_table[i][(j+1)]:
                    row = i-row_count

                    if row_query_instance_table[row][(j+1)]:
                        row_query_instance_table[row][j][2] = row_span_number
                        row_count = 1
                        row_span_number = 1
                if row_query_instance_table[i][(j+1)] == None:
                    row = i-row_count

                    if row_query_instance_table[row][(j+1)]:
                        row_query_instance_table[row][j][2] = row_span_number
                        row_count = 1
                        row_span_number = 1

                    for jj in range(max_col,0,-1):
                        if row_query_instance_table[i][(jj-1)] == None:
                            col_count = col_count + 1
                        else:
                            break

                    row_query_instance_table[i][j][1] = col_count
                    row_query_instance_table[i][j].append(7)#
                    col_count = 1
            elif row_query_instance_table[i][j] == None:

                check = list(row_query_instance_table[i])

                if check[j:max_col].count(None) < (max_col - j) :
                    row_span_number = row_span_number + 1

                row_count = row_count +  1

    row_query_instance_table.pop(0)
    row_query_instance_table.pop()

    return_value_list = zip(row_query_instance_table, num_device)
    return return_value_list
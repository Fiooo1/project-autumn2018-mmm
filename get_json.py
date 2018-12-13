import json

def get_json_file(file_name):
    #a = ''
    #with open() as task:
    #    for line in task:
    #        a += line
    file_name = file_name.decode()
    print("file_name =", file_name)
    a = json.loads(file_name)
    #print(a)
    #b = a["task"]
    task = a
    flag = 2
    '''
    for i in range(len(b)):
        if flag < 2:
            flag += 1
        else:
            if b[i] != "$":
                task += b[i]
            else:
                task += a["$" + b[i+1] + "$"]
                flag = 0
    '''
    task = list(task)
    for i in range(len(task)):
        if task[i] == ' ':
            task[i] = '\,'
        if task[i] == '\n':
            task[i] = ' \\\ '
    return ''.join(task)
    #return task






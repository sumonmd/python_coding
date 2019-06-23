import os.path

filepath = 'deptname.txt'
if not os.path.isfile(filepath):
    print("There is no file ")
else:

    with open(filepath,'r') as file:
        text = file.read().splitlines()
        i=1
        for txt in text:
            print(i,".",txt)
            i+=1
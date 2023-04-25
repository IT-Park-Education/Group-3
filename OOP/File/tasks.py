import os
file_name = 'OOP/File/test.txt'
if not os.path.exists(file_name):
    f = open(file_name, 'w')
    f.write('1234')
    f.close()
else:
    print('File exists: %s' % file_name)
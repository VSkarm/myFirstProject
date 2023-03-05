# file1 = open('workearly.txt', 'w+')
# for i in range(10):
#     file1.write("This line is %d\r\n"%(i+1))
# file1.close()
file1 = open('workearly.txt', 'r')
if file1.mode == 'r':
    contents = file1.read()
    print(contents)
file1.close()
file1 = open('workearly.txt', 'r')

f2 = file1.readline()

print(f2," des edw tin prwth grammi!")

#WRITE DATA
file1 = open('workearly.txt', 'a')
file1.write('This will add a new line in our file!')
file1.close()

#FILE HANDLING
from os import path
import shutil
import datetime
import time

print('file exists!'+ str(path.exists('workearly.txt')))
print('file exists!'+ str(path.exists('learn_python.txt')))
print('directory exists!'+ str(path.exists('my_directory')))

print('Is it a file\t', str(path.isfile('workearly.txt')))
print("Is it a dir? \t", str(path.isdir('my-dir')))

#=================  COPY FILES ==========================#
if path.exists('workearly.txt'):
    src = path.realpath('workearly.txt')
head, tail = path.split(src)
print('Head\t',head,"\nTail\t",tail)
dst = src +'.bak'
shutil.copy(src,dst)
shutil.copystat(src, dst)
t = time.ctime(path.getmtime('workearly.txt.bak'))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime('workearly.txt.bak')))
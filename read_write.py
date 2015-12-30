# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:08:05 2015

@author: OJL
"""
#print f file content
def print_file(f):
    f.seek(0,0) #move f file beginning
    lines = f.readlines()
    for line in lines:
        print line

f1 = open(r'src.txt', 'r')
lines = f1.readlines()
print '\n' + "-" * 20 + "src file content" +  "-" * 20 + '\n'
print_file(f1)
f1.close()
 
f2 = open(r'des.txt', 'a+') #use mode a+ to append data and read file 

print '\n' + "-" * 20 + "des file before content" +  "-" * 20 + '\n'
print_file(f2)
    
f2.writelines(lines)
print '\n' + "-" * 20 + "des file after content" +  "-" * 20 + '\n'
print_file(f2)
#
#
f2.close()
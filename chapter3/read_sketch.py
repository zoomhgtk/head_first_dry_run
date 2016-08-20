import os

print os.getcwd()

os.chdir('/Users/harry/python_head_first/chapter3')

print os.getcwd()

stream1 = open('sketch.txt')

print stream1.readline(),
print stream1.readline(),



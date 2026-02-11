with open('bts.txt','w')as file:
    file.write("2! 3! Hello, we are BTS!.")
file.close()
with open('bts.txt','r')as file:
    data=file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print (word)
        file.close()

        new_file = open('Seven_File.txt','x')
new_file.close()
import os
print("Checking if my_file exists of not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")
    my_file = open("my_file.txt","w")
    my_file.write("BTS is the ARMY!!!!! ")
    my_file.close()
os.remove('bts.txt')    
os.rmdir('folder1')

outputFile = open('UpdatedFile2.txt',"w")
inputFile = open('BTSintroduction.txt',"r")
lines_seen_so_far = set()
print("Eliminating duplicate lines....")
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)
inputFile.close()
outputFile.close()

with open('bts.txt')as fp:
    data1 = fp.read()
with open('BTSintroduction.txt') as fp:
        data2 = fp.read()
data1 += "\n"
data1 += data2
print("Merging two files....")
with open ('Merged2File.txt','w') as fp:
    fp.write(data1)


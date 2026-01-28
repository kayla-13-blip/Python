file1 = open('Codingal123.txt','r')
file2 = open('Codingalupdated.txt','w')
for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)
file2.close()    
file1.close()    
file = open('Codingal123.txt','r')
print(file.read())
file.close()
file = open('Codingal123.txt','r')
print("\n Read in parts\n")
print(file.read(8))
file.close()
file = open('Codingal123.txt','a')
file.write("Hi! ! am penguin and i am 1 yr old.")
file.close()



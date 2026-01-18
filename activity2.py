file_read = open('coding.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('coding.txt','w')
file_write.write("File in Write Mode -")
file_write.write("I am Penguin. ! am 1 yr.")
file_write.close()

file_append = open('coding.txt','a')
file_append.write("\nFile in Append Mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr.old")
file_append.close()



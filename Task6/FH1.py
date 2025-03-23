# import os

#for using excepton method close file as
# try:
#     f=open("f.txt",mode='w',buffering=20, encoding='utf-8') #this 2 line code is us                            \ed
#     print(f)
#     print("file has been oppened")
    
# finally:
#     f.close()
#     print("file closed")


# print("File name is:",f.name)  #these  4 line are the file object variables code example (fileob.name,fileob.encoding,fileob.mode,fileob.closed)
# print("File encoding is:",f.encoding)
# print("File buffering size is:",f.buffer)
# print("File mode is:",f.mode)


# f.close()  #these both line are used to close file and check it
# print("File is open or closed:",f.closed)


 
# print(f.readable())     #these method are used to check file mode
# print(f.writable())

# print(os.path.isfile('ahsan')) #it show false because this file is not present in current dirrectory
# print(os.path.isfile('f.txt')) #it show true because this file present in current dirrectory





















#for read txt
f = open('f.txt','r')
data = f.read()
print(data)
f.close()


#binary reat
f = open('f.txt','rb')
data1 = f.read()
print(data1)
f.close
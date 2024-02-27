#1-we open the file 
#2-in which mode(r,w,a,x) operation will be done on the file
#3-close
#open("abc.txt")-by default it will use read operation
fp=open("abc.txt","r")
line=fp.read()
print(line)
fp.close()

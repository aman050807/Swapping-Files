from fileinput import filename
def swapfiles ():
    file1=open("C:/Users/Dell/Desktop/python programs projects/Class-98/file1.txt")
    file2=open("C:/Users/Dell/Desktop/python programs projects/Class-98/file2.txt")
    with open(file1,'r') as a:
        data_a=a.read()
    
    with open(file2,'r')as b:
        data_b=b.read()

    with open(file1,'w') as a:
        a.write(data_b)

    with open(file1,'w') as a:
        b.write(data_b)

swapfiles()    
try:
    file1=open('sample.txt', 'r+')
    n=1
    read_file=file1.readline(1)
    print('Reading File Data :')
    for line in file1:

        print('Line',n,':',line.strip())
        n=n+1
except FileNotFoundError:
    print("File Not Exist")

file1.close()

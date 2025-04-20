n=1
user_input=input("Enter text to Written on file: ")
file1=open('output.txt', 'w')
file1.write(user_input + '\n')
print("Data Sucessfully Written to Txt File. ")
file1.close()

more_input=input("Enter Additional text to Written on file: ")
file1=open('output.txt', 'a')
file1.write(more_input + '\n')
file1.close()

file1=open('output.txt', 'r')
print("Final Content of the File: ")
for line in file1:
    print('Line:',n, line.strip())
    n=n+1

file1.close()

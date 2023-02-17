print("=======================:|| Read function||:=======================")
f = open("file.txt","r")
text = f.read()
print(text)
f.close()


print("=======================:|| Readline function||:=======================")

f = open("file.txt","r")
text = f.readline()
print(text)
f.close()

print("=======================:|| Readline function||:=======================")


f = open("file.txt","r")
text = f.readline(15)
print(text)
f.close()


print("=======================:|| Readlines function||===")
f = open("file.txt","r")
content = f.readlines()
print(content)
f.close()


fw=open("c:\\data\\test.txt","w")
fw.write("This is my first file operation.\n")
fw.write("This is my second line.\n")
fw.write("This is my third line.\n")
fw.close()
fr=open("c:\\data\\test.txt","r")
for line in fr:
    print(line.strip())
fr.close()

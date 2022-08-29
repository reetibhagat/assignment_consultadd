# 6. Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.



file1 = open ("doc.txt", "w")
L = ["Hello I am a file \n","Where you need to return the data string \n","Which is of even length \n"]
file1.writelines(L)
file1.close()
file2 = open("doc.txt", "r+")
text = file2.readlines()
words = []
for line in text:
    words += line.split(" ")
    words.remove("\n")
print(words)
even_len_string = []
for i in words: # checking even string
    if len(i) % 2 == 0:
        even_len_string.append(i)
print(even_len_string)
listToStr = ' '.join([str(elem) for elem in even_len_string])
print(listToStr)
file2.close()
with open("doc.txt", "a") as document1:
    f = ["even length string is : \n",listToStr]
    document1.writelines(f)



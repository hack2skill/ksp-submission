import pandas as pd
import re
import csv
df = pd.read_fwf('UCO.txt')
df.to_csv("text.csv")

myFile = open('text.csv')
print("The content of CSV file is:")

text = myFile.readline()
#pattern = re.search("^[0-9a-zA-Z].*Cr$", text)
#print(text)
#print(pattern)

stlist=[]
while text !="":
    pattern1 = re.search("Cr", text)
    pattern2 = re.search("Total", text)
    if pattern1 and not pattern2:
        stlist.append(text)
    text = myFile.readline()
myFile.close()

print(stlist)

for i in stlist:
   f=open("uco.csv", "a")
   f.write(i)
   f.close()


#print(df)

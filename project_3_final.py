# open a file 
file = input("please input file as .txt: ")
import os.path
if os.path.exists(file):
    print("it exists)
else:
    file = input("please name file that exists: ")
        
with open(file) as file_doc:
    file_content = file_doc.read()
print(file_content)

# find the annotation 
import re
file_annotation = re.findall(r"\[\[.+?\]\]\(\(.+?\)\)", file_content)
print(file_annotation)

# save the output as new lines (optimal version)
with open('output.txt', "a+") as f:
    for item in file_annotation:
        f.write(str(item + '\n'))


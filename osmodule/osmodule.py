import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

files= os.listdir()
files.remove("osmodule.py")
print(files)
createIfNotExist('pdfs')
createIfNotExist('others')

pdfext=[".pdf"]
pdf=[file for file in files if os.path.splitext(file)[1].lower() in pdfext]
print(pdf)

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in pdfext) and os.path.isfile(file):
        others.append(file)

print(others)

move("pdfs", pdf)
move("others",others)
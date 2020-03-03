# FindFiles, första funktionen
# FindFileExt, andra funktionen
# FindInfo, tredje funktionen
#
#
# Saker som behöver fixas
# #1: Optimera FindInfo med de två for loopar
# Kanske kan kombinera de två i en enda loop
# #2: Ska se om jag kan kombinera FindFileExt med FindInfo
# Det gäller när man filtrerar extension, då de båda gör typ samma sak
#
#
# pip install PyPDF2
import os
import os.path
import re
from pathlib import Path
import PyPDF2
import time
import datetime


def FindFiles(road):
    list_of_files = []
    # går igenom alla mappar och filer från road, neråt
    for root, dirs, files in os.walk(road, topdown=True):
        # för varje fil som kommer upp, lägg det i en lista
        for name in files:
            try:
                value = os.path.join(root, name)
            except UnicodeDecodeError:
                print(root, dirs, files, name)
            else:
                list_of_files.append(value)
    return list_of_files


def FindFileExt(ext, folder):
    list = []
    # listar alla filer i directory (folder)
    oslist = os.listdir(folder)
    for i in range(len(oslist)):
        # appendar alla filer som har ext, txt (.txt, .pdf etc)
        if oslist[i].endswith(ext):
            list.append(oslist[i])
            print(list)
    return list


def FindInfo(pattern, folder, ext):
    file_list = []
    # går igenom alla mappar och filler från folder
    for root, dirs, files in os.walk(folder, topdown=True):
        # går igenom varje fil
        for file in files:
            # jämnför om de slutar med en extension
            if file.endswith(ext):
                file_list.append(os.path.join(root, file))
    for i in range(len(file_list)):
        # testar om filen finns, och om man har permission
        abspath = Path(file_list[i])
        try:
            pat = abspath.resolve(strict=True)
        except FileNotFoundError:
            continue
        except PermissionError:
            continue
        # välj en fil och skicka den till ReadFile för att läsa den
        file = ReadFile(file_list[i], ext)
        if file is not None:
            if pattern in file:
                print(type(file))
                print(file_list[i] + " contains " + pattern)


def FindMod(file, date):
    # behöver fixa denna
    # just nu jämnför den bara en fil
    # fun bör returna true eller false
    modtime = os.path.getmtime(file)
    text = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(modtime))
    d = datetime.datetime(int(text[0:4]), int(text[5:7]), int(text[8:10]),
                          0, 0, 0)
    # ans = str(input("Format: YYYY-MM-DD"))
    w = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]),
                          0, 0, 0)
    if d >= w:
        print("ye")


def FindDif():
    list1 = []
    list2 = []

    file1 = ReadFile("C:/Python Code/test.txt", None)
    for word in file1.split():
        list1.append(word)
    file2 = ReadFile("C:/Python Code/test2.txt", None)
    for w in file2.split():
        list2.append(w)
    # count och få liknelse
    count = len(list1) + len(list2)
    same = set(list1).intersection(list2)
    dif1 = set(list1).difference(list2)
    dif2 = set(list2).difference(list1)

    val1 = round((len(same) / count) * 100, 1)
    val2 = round((len(dif1) / count) * 100, 1)
    val3 = round((len(dif2) / count) * 100, 1)

    return val1, val2, val3


def ReadFile(file_list, ext):
    # När man läser filerna så kan det ge problem med decoding
    # Använder flera try except med olika encoding ifall någon inte funkar
    # if stats för att välja fil typ
    if file_list.endswith(".txt"):
        f = open(file_list, "r")
        try:
            file = f.read()
        except UnicodeDecodeError:
            f.close()
            f = open(file_list, "r", encoding="utf-8")
            try:
                file = f.read()
            except UnicodeDecodeError:
                f.close()
                f = open(file_list, "r", encoding="latin-1")
                try:
                    file = f.read()
                except UnicodeDecodeError:
                    print("send help")
        f.close()
    elif file_list.endswith(".pdf"):
        # creating an object
        file = open(file_list, 'rb')

        # creating a pdf reader object
        try:
            fileReader = PyPDF2.PdfFileReader(file)
        except PyPDF2.utils.PdfReadError:
            return None

        f = []
        file = ""
        i = 0
        while True:
            try:
                f.append(fileReader.getPage(i))
            except IndexError:
                break
            i += 1

        # print the number of pages in pdf file
        for x in range(len(f)):
            file = file + f[x].extractText()
    return file


def DictCrypt():
    encrypt = {"a": "3", "b": "&", "c": "b", "d": "@", "e": "}", "f": "y",
                    "g": "!", "h": "x", "i": "q", "j": "k", "k": "#", "l": "w",
                    "m": "p", "n": "9", "o": "7", "p": "?", "q": "6", "r": "(",
                    "s": ")", "t": "=", "u": "2", "y": "*", "v": "€", "x": "^",
                    "z": "5", "å": "£", "ä": "4", "ö": ">", " ": "k"}
    return encrypt


def Encrypt():
    link = r"C:\Junk\Junk2\data.txt"
    en = DictCrypt()
    file = ReadFile(link, None)
    folder = r"C:/Junk/Junk2/"
    f = open(folder + "encry" + "data.txt", "w")
    for i in file:
        try:
            f.write(en[i])
        except KeyError:
            f.write("\n")
    f.close()


def Decrypt():
    link = r"C:/Junk/Junk2/"
    name = "encrydata.txt"
    en = DictCrypt()
    de = dict(zip(en.values(), en.keys()))
    file = ReadFile(link + name, None)
    f = open(link + name[6:], "w")
    for i in file:
        try:
            f.write(de[i])
        except KeyError:
            f.write("\n")
    f.close()


# FindFiles(str(r"C:\Python Code"))
# Att söka från C: tar lång tid
# FindInfo("a", r"C:/", ".pdf")
print(FindDif())

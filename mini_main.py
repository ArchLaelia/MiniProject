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
import os
import os.path
import re
from pathlib import Path


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


def FindInfo(pattern, folder):
    file_list = []
    # går igenom alla mappar och filler från folder
    for root, dirs, files in os.walk(folder, topdown=True):
        # går igenom varje fil
        for file in files:
            # jämnför om de slutar med en extension
            if file.endswith(".txt"):
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
        file = ReadFile(file_list[i])
        if pattern in file:
            print(file_list[i] + " contains " + pattern)


def ReadFile(file_list):
    # När man läser filerna så kan det ge problem med decoding
    # Använder flera try except med olika encoding ifall någon inte funkar
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
    return file


# FindFiles(str(r"C:\Python Code"))
# Att söka från C: tar lång tid
FindInfo("a", r"C:/")

import EncryptionMethod as enc
import os

def save(text, filename, keystore, textstore):
    if filename == '':
        return 'Error1'
    filename = filename + '.txt'

    #getfile path to application
    path = os.path.abspath(textstore)

    #create directory path
    datah = os.path.join(path, filename)

    #create a new file in directory and add encrypted text
    temp = enc.encryptedTxt(text)
    with open(datah, 'w') as file:
        file.write(temp.enctext)
    hold = temp.getkeys()
    hold2 = ''
    for i in range(len(hold)):
        hold2+=str(hold[i])

    #add key to key file
    hold = os.path.join(keystore, "keys_ENCRYPTAPPDATA.txt")
    try:
        with open(hold, "a") as file:
            file.write(hold2 + '^')
        temp.wipe()
    except FileNotFoundError:
        return 'Error2'


def retrieve(title, direct, textpath):
    titleadd = os.path.abspath(textpath)
    title = titleadd + '/' + title

    try:
        file = open(direct + '/' + 'keys_ENCRYPTAPPDATA.txt', 'r')
    except:
        return 'Error2'
    keys = file.read()
    keys = keys.split("^")

    file2 = open(title, 'r')
    text = file2.read()

    while '' in keys:
        keys.remove('')
    for key in keys:
        hold = []
        for char in key:
            hold += [int(char)]
        final = enc.unencrypt(text, hold)
        if final != False:
            return final
    return 'Error1'

def getFiles(filepath):
    final = os.listdir(os.path.abspath(filepath))
    final.remove('.DS_Store')
    while '.txt' in final:
        final.remove('.txt')
    return final

def deleteFile(filename, textpath):
    direct = os.path.abspath(textpath)
    path = os.path.abspath(os.path.join(direct, filename))
    os.remove(path)

def clearFiles(keyextension, textpath):
    #delete keys first
    try:
        os.remove(os.path.join(keyextension, "keys_ENCRYPTAPPDATA.txt"))
    except:
        pass
    #delete all files in text
    files = getFiles(textpath)
    for file in files:
        os.remove(os.path.join(os.path.abspath(textpath), file))

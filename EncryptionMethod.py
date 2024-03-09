import random
class encryptedTxt:
    def __init__(self, text, key = None):
        if key == None:
            self.__key = self.__randlist(31)
            self.__mult = self.__randlist(10)
        else:
            self.__key = key[0: 31]
            self.__mult = key[31: 41]
        self.enctext = self.__encrypt("encrypted: " + text)
        
    def __str__(self):
        return self.enctext
    
    __repr__ = __str__

    def getkeys(self):
        if self.__key == None:
            return "No Keys"
        else:
            return self.__key + self.__mult
    
    def wipe (self):
        self.__key = None
        self.__mult = None


    def __encrypt(self, txt):
        newtxt = ''
        for i in range(len(txt)):
            s = i % 31
            m = i % 10
            shift = (ord(txt[i])+(self.__key[s]*self.__mult[m]))%127
            if shift == 10:
                shift = 200
            elif shift == 13:
                shift = 300
            newtxt += chr(shift)
        return newtxt

    def __randlist(self, length):
        ret = []
        for i in range(length):
            ret+=[random.randint(1,9)]
        return ret

def unencrypt(txt, keys):
    key = keys[0: 31]
    mult = keys[31: 41]
    oldtxt = ''
    for i in range(len(txt)):
        s = i % 31
        m = i % 10
        if ord(txt[i]) == 200:
            move = 10
        elif ord(txt[i]) == 300:
            move = 13
        else:
            move = ord(txt[i])
        shift = (move-(key[s]*mult[m]))%127
        oldtxt += chr(shift)
    if oldtxt[0:11] != "encrypted: ":
        return False
    print('end')
    return oldtxt[11:]


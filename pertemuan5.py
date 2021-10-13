import string, re, numpy
from collections import OrderedDict
from typing import Match 

def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))
text = "DALAM".upper()
plain = re.sub("\s+",'',text)
keyword1 = "raghni sandiko".upper()
keyword2 = "selamat tinggal".upper()
keyword3 = "sugiono".upper()

chars = string.ascii_uppercase                                      # pl['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chiperKey1 = removeDupWithOrder(re.sub("\s+",'',keyword1)+chars)    # k1['r', 'a', 'g', 'h', 'n', 'i', 's', 'd', 'k', 'o', 'b', 'c', 'e', 'f', 'j', 'l', 'm', 'p', 'q', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chiperKey2 = removeDupWithOrder(re.sub("\s+",'',keyword2)+chars)    # k2['s', 'e', 'l', 'a', 'm', 't', 'i', 'n', 'g', 'b', 'c', 'd', 'f', 'h', 'j', 'k', 'o', 'p', 'q', 'r', 'u', 'v', 'w', 'x', 'y', 'z']
chiperKey3 = removeDupWithOrder(re.sub("\s+",'',keyword3)+chars)    # k3['s', 'u', 'g', 'i', 'o', 'n', 'a', 'b', 'c', 'd', 'e', 'f', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y', 'z']


# mix K1 only
# kata : coba
# jadi : cuql
def methodZigzag(plain):
    # OUTPUT = None
    for idp, charp in enumerate(plain):
        # for idc, charc in enumerate(chars):
        def salt1():
            indexC1 = chars.index(charp)
            indexC2 = chars.index(list(chiperKey1)[indexC1])
            indexC3 = chars.index(list(chiperKey2)[indexC2])
            return list(chiperKey3)[indexC3]
        def salt2():
            indexC2 = chars.index(charp)
            indexC3 = chars.index(list(chiperKey2)[indexC2])
            indexC1 = chars.index(list(chiperKey3)[indexC3])
            return list(chiperKey1)[indexC1]
        def salt3():
            indexC3 = chars.index(charp)
            indexC1 = chars.index(list(chiperKey3)[indexC3])
            indexC2 = chars.index(list(chiperKey1)[indexC1])
            return list(chiperKey2)[indexC2]

        switch = {
            0: salt1(),
            1: salt2(),
            2: salt3()
        }
        
        # OUTPUT.join(switch.get(idp%3))
        print(idp, charp, idp%3, switch.get(idp%3)) #debuging purpose
        # return "".join("c")
methodZigzag(plain)
# print(OUTPUT)


"""
pl=[ c, o, b, a]
#   k1 >=c =i =g =c
#   k1 >=c3(c2(c1(pl)))

#   k2 >=h =d =j =o
#   k2 >=c1(c3(c2(pl)))

#   k3 >=u =u =u =b
#   k3 >=c2(c1(c3(pl)))

#   k1 >=l =p =r =a
#   k1 >=c3(c2(c1(pl)))

# chiperKey1 = k3(k2(k1(plain)))
# chiperKey2 = k1(k3(k2(plain)))
# chiperKey3 = k2(k1(k3(plain)))
def k1:
    def c1(charX): #-> c
        return c1(charX) #-> g
    def c2(c1): #-> g
        pl = plain()
        c2 = pl(c1) #-> i
        return c2
    def c3(c2): #-> i
        pl = plain()
        c3 = pl(c2) # -> c
        return c3
def k2:
    def c2(charX):
        return c2(charX)
    def c3(c2):
        pl = plain()
        c3 = pl(c2)
        return c3
    def c1(c3):
        pl = plain()
        c1 = pl(c3)
        return c1
def k3:
    def c3(charX):
        return c3(charX)
    def c1(c3):
        pl = plain()
        c1 = pl(c3)
        return c1
    def c2(c1):
        pl = plain()
        c2 = pl(c1)
        return c2
"""
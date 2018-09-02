import enchant
from enchant.checker import SpellChecker
def spellenchant(user):
    d = enchant.Dict("en_US")
    chkr = SpellChecker("en_US")
    chkr.set_text(user)
    abc=[]
    z=[]
    for err in chkr:
            abc.append(err.word)
            print(abc)
            print(len(abc))
    length = len(abc)
    for i in range(length):
        abcd=d.suggest(abc[i])
        z.append(abcd)
    return z

def wrongwords(text):
    d = enchant.Dict("en_US")
    chkr = SpellChecker("en_US")
    chkr.set_text(text)
    listofwrongwords=[]
    for err in chkr:
            listofwrongwords.append(err.word)
    return listofwrongwords

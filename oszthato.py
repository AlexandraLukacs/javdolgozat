import random

def szamok_lista():
    szam_lista=[]
    for i in range(0, 50, 1):
        szamok: int= int(random.randint(1,100))
        if i < 49:
            print(szamok, end=", ")
        else:
            print(szamok, end=" ")
    szam_lista.append(szamok)
    return szam_lista


def hettelOszthato(lista):
    db: int= 0
    for i in range(0, len(lista), 1):
        if i % 7 == 0:
            db += 1
    return db


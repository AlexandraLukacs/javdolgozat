from Auto import Auto

def fajlbeolv():
    kocsi_lista=[]
    f=open("auto.txt", "r", encoding="utf=8")
    f.readline()
    fajl_lista=f.readlines()
    f.close()
    for i in range(0, len(fajl_lista), 1):
        aktsor=fajl_lista[i].strip().split(" ")
        auto=Auto(aktsor[0], aktsor[1])
        print(auto.nev, auto.gyart_datum)
        kocsi_lista.append(auto)
    return kocsi_lista

def kor(lista, auto:str):
    ev: int= 2024
    for i in range(0, len(lista), 1):
        if auto == lista[i]:
            eves: int= (ev-lista[i].gyartas_datum)
    print(f"\n{lista[i].nev} - {eves}")


def flotta(lista):
    db= len(lista)
    return db
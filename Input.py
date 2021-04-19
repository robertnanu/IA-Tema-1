import Graph
from typing import List, Tuple
from os import listdir
from os.path import isfile, join


def obtineCombinatii(sir):
    """
        Split-uieste datele de intrare astfel incat acestea sa fie citite corect
        @param sir: sirul pe care vrem sa-l despartim
    """
    combinatii = sir.strip().split("\n")
    listaCombinatii = [aici.strip().split() for aici in combinatii]
    return listaCombinatii

def ReadFolder(folder: str) -> List[str]:
    """
        Citeste un input folder si returneaza toate fisierele gasite in acesta
        @param folder: folder-ul din care scoatem fisierele de intrare
    """
    onlyFiles = [f for f in listdir(folder) if isfile(join(folder, f))]

    return onlyFiles

def ReadFile(filepath: str):
    """
        Citeste datele dintr-un anumit fisier si initializeaza datele necesare
        @param filepath: fisierul din care se va citi
    """
    with open(filepath, "r") as f:
        continutFisier = f.read()
        siruriStari = continutFisier.split("stare_initiala")
        combinatieCulori = obtineCombinatii(siruriStari[0])
        start = []
        siruriVase = siruriStari[1].split("stare_finala")
        start = obtineCombinatii(siruriVase[0])
        scop = []
        scop = obtineCombinatii(siruriVase[1])
    Graph.combinatiiCulori = combinatieCulori
    Graph.stareInitiala = [(int(i[0]), int(i[1]), i[2]) if i[1] != '0' else (int(i[0]), 0, "nedefinit") for i in start]
    Graph.stareFinala = [(int(a), b) for a, b in scop]
       
"""
f = open('date_intrare.txt', 'r')



continutFisier = f.read()
siruriStari = continutFisier.split("stare_initiala")
### aici sunt combinatiile
#print(siruriStari[0])
combinatieCulori = obtineCombinatii(siruriStari[0])
start = []
siruriVase = siruriStari[1].split("stare_finala")
### aici sunt cantitatile din vase
#print(siruriVase[0])
start = obtineCombinatii(siruriVase[0])
scop = []
#for scop in siruriVase:
#self.scopuri.append(obtineCombinatii(scop))
scop = obtineCombinatii(siruriVase[1])
#print("Combinatii culori:", self.combinatii)
#print("Cantitati vase: ", self.vase)
#print("Stari finale dorite: ", self.scop)

print(start)
print(combinatieCulori)
print(scop)

f.close()
"""
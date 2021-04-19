import Graph
import os

fout = None

def CreateDirectory(dir: str):
    """
        Creeaza un directory nou pentru output, daca acesta nu exista, in prealabil
        @param dir: directory-ul care trebuie creat
    """
    if not os.path.exists(dir):
        os.mkdir(dir)

def afiseazaSolutie(nod:Graph.Nod):
    """
        Afiseaza o solutie valida
        @param nod: informatiile mentinute in fiecare nod, despre vase
    """
    fout.write("\n\n\n\n\n\n\nTrebuie sa afisez nod\n")
    nod.afisDrum(fout)
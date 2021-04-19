from typing import List, Tuple
import copy

# {a, b, c} = a + b -> c
combinatiiCulori:List[Tuple[str, str, str]] = None
# {a, b, c} = a - cap max; b - cap act; c - culoare
stareInitiala:List[Tuple[int, int, str]] = None
# {a, b} = a - cant act; b - culoare
stareFinala:List[Tuple[int, str]] = None

def combinaCulori(col1:str, col2:str, cant1:int, cant2:int) -> str:
    """
        Functie care imi combina culorile, daca este posibil
        @para col1, col2: reprezinta 2 culori
        @param cant1: reprezinta cata apa de col1
        @param cant2: reprezinta cata apa de col2
    """
    if cant1 == 0:
        return col2
    if cant2 == 0:
        return col1
    if col1 == col2:
        return col1
    for c1, c2, c3 in combinatiiCulori:
        if (col1 == c1 and col2 == c2) or (col1 == c2 and col2 == c1):
            return c3
    return "nedefinit"


class Nod:
    def __init__(self, dist:int, predecesor:"Nod", vase:List[Tuple[int, int, str]]):
        """
            @param dist: lungimea drumului
            @param predecesor: starea precedenta
            @param vase: capacitatea maxima a vasului (0), capacitatea actuala a vasului (1), culoarea apei din vas (2)
        """
        self.dist = dist
        self.predecesor = predecesor
        self.vase = vase

    def isFinal(self):
        """
            Returneaza True daca vasul meu coincide cu o stare finala
        """
        for cant, culoare in stareFinala:
            ok = False
            for _, c, cul in self.vase:
                if c == cant and cul == culoare:
                    ok = True
            if not ok:
                return False
        return True

    def isInPath(self, x:"Nod") -> bool:
        """
            Returneaza True daca starea mea se gaseste deja anterior in drum
        """
        act = self
        while act is not None:
            if sorted(act.vase) == sorted(x.vase):
                return True
            act = act.predecesor
        return False

    def genereazaSuccesori(self) -> "List[Nod]":
        """
            Retunreaza toti succesorii posibili ai unei anumite pozitii
        """
        succesori = []
        for i in range(len(self.vase)):
            if self.vase[i][1] == 0:
                continue
            for j in range(len(self.vase)):
                if i == j:
                    continue 
                if self.vase[j][1] == self.vase[j][0]:
                    continue
                newVase = copy.deepcopy(self.vase)
                apaVarsata = min(self.vase[i][1], self.vase[j][0] - self.vase[j][1])
                newVase[i] = (self.vase[i][0], self.vase[i][1] - apaVarsata, self.vase[i][2])
                newCol = combinaCulori(self.vase[i][2], self.vase[j][2], apaVarsata, self.vase[j][1])
                newVase[j] = (self.vase[j][0], self.vase[j][1] + apaVarsata, newCol)

                succesor = Nod(1 + self.dist, self, newVase)

                if not self.isInPath(succesor):
                    succesori.append(succesor)

        return succesori
        

    def toString(self):
        """
            Transforma sirul sub forma unui sir de caractere dorit
        """
        sir = f"distanta: {self.dist}\nvase: {self.vase}\n"
        return sir

    def obtineDrum(self):
        """
            Obtine drumul deja parcurs
        """
        l = []
        nod = self
        while nod is not None:
            l.insert(0, nod)
            nod = nod.predecesor
        #l = l[::-1]
        return l

    def afisDrum(self, g):  # returneaza si lungimea drumului
        """
            Afiseaza o solutie, alaturi de lungimea parcursa in gasirea acesteia
        """
        l = self.obtineDrum()
        for stare in l:
            g.write(stare.toString())
        return len(l)


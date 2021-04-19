from typing import Callable, List, Tuple
import Graph

def estimarePenala(nod:Graph.Nod) -> int:
    """
        Euristica banala, va returna intotdeauna 0
        @param nod: informatiile stocate in nod, despre vase
    """
    return 0

def estimareAdmisibila1(nod:Graph.Nod) -> int:
    """
        Euristica admisibila 1, va returna cate culori lipsesc pana in starea finala
        @param nod: informatiile stocate in nod, despre vase
    """
    nr_culori_lipsa = 0 
    for cant, col in Graph.stareFinala:
        ok = False
        for cap, act, c in nod.vase:
            if c == col and act != 0:
                ok = True
        if ok == False:
            nr_culori_lipsa += 1
    return nr_culori_lipsa

def estimareAdmisibila2(nod:Graph.Nod) -> int:
    """
        Euristica admisibila 2, va returna numarul de vase care lipsesc pana cand starea finala va fi completata
        @param nod: informatiile stocate in nod, despre vase
    """
    nr_culori_lipsa = 0 
    for cant, col in Graph.stareFinala:
        ok = False
        for cap, act, c in nod.vase:
            if c == col and act == cant:
                ok = True
        if ok == False:
            nr_culori_lipsa += 1
    return nr_culori_lipsa

def estimareInadmisibila(nod:Graph.Nod) -> int:
    """
        Euristica inadmisibila, va returna o estimare gresita
        @param nod: informatiile stocate in nod, despre vase
    """
    if nod.isFinal():
        return 10
    else:
        return 5 * estimareAdmisibila2(nod) - 10 * estimareAdmisibila1(nod)

ListaEstimari:List[Tuple[Callable, str]] = [
    (estimarePenala, "estimarea penala"),
    (estimareAdmisibila1, "estimare admisibila 1"),
    (estimareAdmisibila2, "estimare admisibila 2"),
    (estimareInadmisibila, "estimare inadmisibila")
]
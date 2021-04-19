from typing import Callable
import Graph
import time
import AfiseazaSolutii
from typing import List, Tuple

def uniform_cost(nod:Graph.Nod, estimare:Callable, nrSolutii:int, timeout:float):
    """
        @nod: nodul
        @param estimare: functia de estimare
        @nrSolutii: numarul de solutii cerute
        @timeout: timeout in secunde
    """
    states = [nod]

    time_start = time.time()
    
    def ElapsedTime() -> float:
        return time.time() - time_start

    visited_nodes = 0
    aduna = 0
    t = 0
    while states != [] and nrSolutii > 0:
        if ElapsedTime() > timeout:
            break

        act = states[0]
        states.pop(0)
        visited_nodes += 1

        if act.isFinal():
                AfiseazaSolutii.afiseazaSolutie(act)
                t += 1
                time_final = time.time()  
                durata = round(1000 * (time_final - time_start)) + aduna
                if durata == 0:
                    AfiseazaSolutii.fout.write("Starea initiala este egala cu starea finala.\n")
                aduna = durata
                AfiseazaSolutii.fout.write("Timpul gasirii solutie a fost de: " + str(durata) + " ms!\n")
                print("Am gasit sol")
                nrSolutii -= 1

        for urm in act.genereazaSuccesori():
            states.append(urm)
    if t == 0:
        AfiseazaSolutii.fout.write("\n\n\nNu au fost gasite solutii!\n")
    AfiseazaSolutii.fout.write("Detalii UCS")

def SlowAStar(nod:Graph.Nod, estimare:Callable, nrSolutii:int, timeout:float):
    """
        @nod: nodul
        @param estimare: functia de estimare
        @nrSolutii: numarul de solutii cerute
        @timeout: timeout in secunde
    """
    states = [nod]

    time_start = time.time()
    
    def ElapsedTime() -> float:
        return time.time() - time_start

    def EstimateTotalDistance(act: Graph.Nod) -> int:
        return act.dist + estimare(act)

    

    visited_nodes = 0
    aduna = 0
    t = 0
    while states != [] and nrSolutii > 0:
        if ElapsedTime() > timeout:
            break

        states.sort(key=EstimateTotalDistance)

        act = states[0]
        states.pop(0)
        visited_nodes += 1
        if act.isFinal():
            AfiseazaSolutii.afiseazaSolutie(act)
            t += 1
            time_final = time.time()  
            durata = round(1000 * (time_final - time_start)) + aduna
            if durata == 0:
                AfiseazaSolutii.fout.write("Starea initiala este egala cu starea finala.\n")
            aduna = durata
            AfiseazaSolutii.fout.write("Timpul gasirii solutie a fost de: " + str(durata) + " ms!\n")
            print("Am gasit sol")
            nrSolutii -= 1
        for urm in act.genereazaSuccesori():
            states.append(urm)
    
    if t == 0:
        AfiseazaSolutii.fout.write("\n\n\nNu au fost gasite solutii!\n")
    AfiseazaSolutii.fout.write("Detalii A*")

def OptimizedAStar(nod:Graph.Nod, estimare:Callable, nrSolutii:int, timeout:float):
    """
        @nod: nodul
        @param estimare: functia de estimare
        @param nrSolutii: numarul de solutii cerute
        @param timeout: timeout in secunde
    """
    opened = [nod]
    closed: List[Graph.Nod] = []

    time_start = time.time()
    
    def ElapsedTime() -> float:
        return time.time() - time_start

    def IsInClosed(act: Graph.Nod) -> bool:
        for el in closed:
            if el.vase == act.vase:
                return True
        return False

    def EstimateTotalDistance(act: Graph.Nod) -> int:
        return act.dist + estimare(act)
    
    def FindAndUpdateInOpen(act: Graph.Nod) -> bool:
        for i in range(len(opened)):
            if opened[i].vase == act.vase:
                if opened[i].dist > act.dist:
                    opened[i] = act
                return True
        return False
    aduna = 0
    t = 0
    while opened != []:
        if ElapsedTime() > timeout:
            AfiseazaSolutii.fout.write("A* nu a gasit nicio solutie datorita timeout-ului")
            return
            
        opened.sort(key=EstimateTotalDistance)

        act = opened[0]
        opened.pop(0)
        closed.append(act)

        for urm in act.genereazaSuccesori():
            if urm.isFinal():
                AfiseazaSolutii.afiseazaSolutie(urm)
                t += 1
                time_final = time.time()  
                durata = round(1000 * (time_final - time_start)) + aduna
                if durata == 0:
                    AfiseazaSolutii.fout.write("Starea initiala este egala cu starea finala.\n")
                aduna = durata
                AfiseazaSolutii.fout.write("Timpul gasirii solutie a fost de: " + str(durata) + " ms!\n")
                print("Am gasit sol")
                return
            if IsInClosed(urm):
                continue
            if not FindAndUpdateInOpen(urm):
                opened.append(urm)
    if t == 0:
        AfiseazaSolutii.fout.write("\n\n\nNu au fost gasite solutii!\n")
    AfiseazaSolutii.fout.write("Detalii A* Optimizat")

def IDAStar(nod:Graph.Nod, estimare:Callable, nrSolutii:int, timeout:float):
    """
        @nod: nodul
        @param estimare: functia de estimare
        @nrSolutii: numarul de solutii cerute
        @timeout: timeout in secunde
    """

    time_start = time.time()
    
    def ElapsedTime() -> float:
        return time.time() - time_start

    def EstimateTotalDistance(act: Graph.Nod) -> int:
        return act.dist + estimare(act)


    visited_nodes = 0
    total_nodes = 0

    def SearchForPath(node: Graph.Nod, max_distance: int):
        nonlocal visited_nodes, total_nodes, ElapsedTime, timeout

        if ElapsedTime() > timeout:
            return None, float("inf")

        visited_nodes += 1

        if EstimateTotalDistance(node) > max_distance:
            return None, EstimateTotalDistance(node)
        
        if node.isFinal():
            return node, node.dist
            
        min_cost = float('inf')

        for urm in node.genereazaSuccesori():
            total_nodes += 1
            if node.isInPath(urm):
                continue
            
            final_node, best_est = SearchForPath(urm, max_distance)

            if final_node is not None:
                return final_node, best_est

            min_cost = min(min_cost, best_est)
        
        return None, min_cost

    ans = []

    visited_nodes = 0
    current_estimation = 0
    aduna = 0
    t = 0
    while True:
        if ElapsedTime() > timeout:
            break
        
        final_node, current_estimation = SearchForPath(nod, current_estimation)
        total_nodes += 1

        if final_node is not None:
            AfiseazaSolutii.afiseazaSolutie(final_node)
            t += 1
            time_final = time.time()  
            durata = round(1000 * (time_final - time_start)) + aduna
            if durata == 0:
                AfiseazaSolutii.fout.write("Starea initiala este egala cu starea finala.\n")
            aduna = durata
            AfiseazaSolutii.fout.write("Timpul gasirii solutie a fost de: " + str(durata) + " ms!\n")
            AfiseazaSolutii.fout.write("Detalii IDA*")
            print("Am gasit sol")
            return
    if t == 0:
        AfiseazaSolutii.fout.write("\n\n\nNu au fost gasite solutii!\n")
        AfiseazaSolutii.fout.write("Detalii IDA*")
        return

listaCautari:List[Tuple[Callable, str]] = [
    (uniform_cost, "UCS"),
    (SlowAStar, "A_Star"),
    (OptimizedAStar, "A_Star_Optimizat"),
    (IDAStar, "IDA_Star")
]
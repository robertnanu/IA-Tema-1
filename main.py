from typing import Callable
import AfiseazaSolutii
import Graph
import Estimari
import Cautari
import Input

def process(cautare: Callable, estimare: Callable, nr_sol: int, timeout: float, file: str, file_out: str):
    """
        Executa un anumit algoritm, cu o anumita euristica si un timeout
        @param cautare: ce algoritm sa folosim
        @param estimare: ce euristica sa folosim
        @param nr_sol: numarul de solutii dorite
        @param timeout: timeout-ul in secunde pentru algoritm
        @param file: de unde extrag datele de intrare
        @param file_out: unde afisez solutiile
    """
    Input.ReadFile(file)
    nod = Graph.Nod(0, None, Graph.stareInitiala)

    AfiseazaSolutii.fout = open(file_out, "w")

    # Executam algoritm-ul.
    cautare(nod, estimare, nr_sol, timeout)

def main():
    """
        Aici incepe programul
    """
    
    # Folder-ul pentru input.
    folder = input("In ce fisier putem gasi date de intrare?\n $ ")
    try:
        files_in_folder = Input.ReadFolder(folder)
    except:
        print("Folder-ul specificat nu a fost gasit. Se opreste executia...")
        return
    

    #files_in_folder = Input.ReadFolder("D:\IA\Tema1\date_input.txt")

    # Folder-ul pentru output.
    output_folder = input("Alegeti un folder in care sa salvam solutiile obtinute!\n $ ")
    try:
        AfiseazaSolutii.CreateDirectory(output_folder)
    except:
        print("Nu s-a putut crea folder-ul. Se opreste executia...")
        return

    # Citim numarul de solutii.
    nr_solutions = int(input("Cate solutii sa afiseze algoritmul (A*/IDA* obtin doar prima solutie)?\n $ "))
    if nr_solutions <= 0:
        raise IOError("Numar invalid de solutii, va rugam incercati din nou...")
    
    # Alegem estimarea dorita.
    print("Acestea sunt estimarile valabile:")
    for id, (_, description) in enumerate(Estimari.ListaEstimari):
        print("  %d. %s" % (id + 1, description))
    estimation_id = int(input("Care estimare doriti sa o folosim in algoritm?\n $ "))
    estimation_fn = Estimari.ListaEstimari[estimation_id - 1][0]

    # Alegem algoritmul dorit.
    print("Algoritmii de cautare valabili:")
    for id, (_, description) in enumerate(Cautari.listaCautari):
        print("  %d. %s" % (id + 1, description))
    search_alg_id = int(input("Care cautare doriti sa o folosim?\n $ "))
    search_alg_fn = Cautari.listaCautari[search_alg_id - 1][0]

    # Alegem timeout-ul dorit.
    timeout = float(input("Ce timeout sa aiba algoritm-ul (in secunde)?\n $ "))

    # Iteram peste fiecare fisier de input.
    for file in files_in_folder:
        # daca ceva nu functioneaza, block-ul try catch va arunca o eroare
        try:

            # Citim datele din fisier.
            print("Procesare date input din fisierul \"%s\" ... " % file, end='')
          
            # Procesam file-ul.
            process(search_alg_fn, estimation_fn, nr_solutions, timeout, folder + '/' + file, output_folder + '/' + file)
    
        # Ceva nu a functionat.
        except Exception as exp:
            print(exp.args)
            print(("Ceva nu este in regula cu date de intrare din fisier \"%s\"." +
                    "Va rugam verificati informatia introdusa si incercati din nou. Se ignora testul...") % file)
        
if __name__ == "__main__":
    main()
"""

AfiseazaSolutii.fout = open("fisier.txt", 'w')

Graph.combinatiiCulori = [('a','b','c')]

Graph.stareFinala = [(2, 'c')]

nod = Graph.Nod(0, None, [(1, 1, 'a'), (2, 1, 'b')])

e = Estimari.estimarePenala

#Cautari.uniform_cost(nod, e, 2, 1000)

#Cautari.SlowAStar(nod, e, 2, 1000)

Cautari.OptimizedAStar(nod, e, 2, 1000)

#Cautari.IDAStar(nod, e, 2, 1000)
"""
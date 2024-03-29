import random


semilla = input("Introduzca una semilla (int): ")
random.seed(semilla)



def generate_random(num_libros_quiere_leer, num_libros_catalogo):
        
   
    libros_quiere_leer = set() #tria llibres que vol llegir aleatoriament
    while len(libros_quiere_leer) < num_libros_quiere_leer:
        numero = random.randint(0, num_libros_quiere_leer + num_libros_catalogo)
        libro = f"Libro{numero}"
        libros_quiere_leer.add(libro)

    # Convierteix el set a una lista 
    libros_quiere_leer = list(libros_quiere_leer)

    libros_catalogo=[]
    for i in range (num_libros_catalogo + num_libros_quiere_leer):
        libro = f"Libro{i}"
        if libro not in libros_quiere_leer:
            libros_catalogo.append(libro)


    # Lista de meses
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    # Escribe el contenido del archivo
    with open("random_problem.pddl", "w") as file:
        file.write(f"(define (problem PlanLectura_Problema)\n")
        file.write(f"  (:domain PlanLectura)\n\n")
        file.write(f"  (:objects\n")
        file.write(f"    {' '.join(libros_quiere_leer + libros_catalogo)} - libros_catalog\n")
        file.write(f"    {' '.join(meses)} - mes\n")
        file.write(f"  )\n\n")
        file.write(f"  (:init\n")
        
        paginas=[] #llista que sap quantes pagines te cada llibre
        for libro in libros_quiere_leer:
            num = random.randint(100, 800)
            file.write(f"    (quiere_leer {libro})\n")
            #file.write(f"    (=(paginas_libro {libro}) {num})\n")
            x = [libro,num]
            paginas.append(x)


        for libro in libros_catalogo:
            num = random.randint(100, 800)
            #file.write(f"    (=(paginas_libro {libro}) {num})\n")
            x = [libro,num]
            paginas.append(x)

        libros = []
        llegits = []
        m = [] #que el usuari no hagi llegit més d'un llibre per mes
        for _ in range(random.randint(0,num_libros_quiere_leer)): #hay entre 0 y un num que el usuario ya ha leido 
            libro_leido = random.choice(libros_catalogo)
            mes_lectura = random.choice(meses)
            if (libro_leido not in libros) and (mes_lectura not in m):
                libros.append(libro_leido)
                file.write(f"    (leido {libro_leido})\n")
                file.write(f"    (mes_lectura {libro_leido} {mes_lectura})\n")
                x = [libro_leido, mes_lectura]
                llegits.append(x)
                m.append(mes_lectura)

        predecesors=[]
        for _ in range(random.randint(0, num_libros_catalogo//2)): #hi haura 0 o mes llibres amb predecesor
            libro1 = random.choice(libros_quiere_leer + libros_catalogo)
            numero = int(libro1[5:]) #agafem el numero del llibre
            if numero == num_libros_catalogo+num_libros_quiere_leer: #ultim numero
                libro1=f"Libro{numero-1}" # el predecessor
            else:
                numero += 1 
            libro2 = f"Libro{numero}"
            if (libro1, libro2) and (libro2, libro1) not in predecesors: # mirem que un llibre no pot ser predecessor del mateix llibre més d'una vegada
                file.write(f"    (predecesor {libro1} {libro2})\n")
                predecesors.append((libro1, libro2))

        #paralels=[]
        x = random.randint(0, num_libros_catalogo//2)
        print(x)
        i=0
        numero = 2
        while i <= x or numero >= num_libros_catalogo:
            libro1 = f"Libro{numero-1}"
            libro2 = f"Libro{numero}"
            print(2)
            if libro1 and libro2 not in predecesors:
                    
                file.write(f"    (paralelos {libro1} {libro2})\n")
                i+=1
            numero+=1
        """ for _ in range(random.randint(0, num_libros_catalogo//2)): #hi haura 0 o mes llibres amb predecesor
            libro1 = random.choice(libros_quiere_leer + libros_catalogo)
            numero = int(libro1[5:]) #agafem el numero del llibre
            if numero == num_libros_catalogo+num_libros_quiere_leer:
                libro1=f"Libro{numero-1}"
            else:
                numero += 1 
            libro2 = f"Libro{numero}"
            #if libro2 not in paralels:
            file.write(f"    (paralelos {libro1} {libro2})\n")
                #predecesors.append(libro1)"""
        

        for mes in range(len(meses)):
            mes_anterior = meses[mes-1]
            file.write(f"    (mes_anterior {mes_anterior} {meses[mes]})\n")

        for mes in meses: 
            num = 0
            for l in llegits: #itera en els llibres llegits per l'usuari
                if mes == l[1]: #si l'usuari ha llegit llibre en aquest mes
                    for p in paginas: 
                        if p[0]==l[0]:
                            num = p[1]
            #file.write(f"    (=(pagines_mes {mes}){num})\n") #escriurà que aquell mes ja ha llegit x pagines
                
        file.write(f"  )\n\n")
        file.write(f"  (:goal (forall (?l - libros_catalog) (imply (quiere_leer ?l) (leido ?l))))\n)\n")

    print("Archivo de problema PDDL generado con éxito. Su nombre es: random_problem.pddl")





num_libros_quiere_leer = random.randint(3,7) #numero de llibres que vol llegir (entre 1 i 5)
num_libros_catalogo = random.randint(8,12) #numero de llibres totals,+ els que vol llegir (entre 5,12)
generate_random(num_libros_quiere_leer, num_libros_catalogo)
 
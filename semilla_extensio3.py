import random


semilla = input("Introduzca una semilla (int): ")
random.seed(semilla)



def generate_random(num_libros_quiere_leer, num_libros_catalogo):
        
   
    libros_quiere_leer = set() #tria llibres que vol llegir aleatoriament
    while len(libros_quiere_leer) < num_libros_quiere_leer:
        numero = random.randint(1, num_libros_quiere_leer + num_libros_catalogo)
        libro = f"Libro{numero}"
        libros_quiere_leer.add(libro)

    # Convierteix el set a una lista 
    libros_quiere_leer = list(libros_quiere_leer)

    libros_catalogo=[]
    for i in range (num_libros_catalogo + num_libros_quiere_leer):
        libro = f"Libro{i+1}"
        if libro not in libros_quiere_leer:
            libros_catalogo.append(libro)


    # Lista de meses
    meses = ["Previo", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    # Escribe el contenido del archivo
    with open("random_problem.pddl", "w") as file:
        file.write(f"(define (problem PlanLectura_Problema)\n")
        file.write(f"  (:domain PlanLectura)\n\n")
        file.write(f"  (:objects\n")
        file.write(f"    {' '.join(libros_quiere_leer + libros_catalogo)} - libros_catalog\n")
        file.write(f"    {' '.join(meses)} - mes\n")
        file.write(f"  )\n\n")
        file.write(f"  (:init\n")
        
        paginas={} #diccionari que sap quantes pagines te cada llibre
        for libro in libros_quiere_leer:
            num = random.randint(100, 400)
            file.write(f"    (quiere_leer {libro})\n")
            file.write(f"    (=(paginas_libro {libro}) {num})\n")
            paginas[libro] = num


        for libro in libros_catalogo:
            num = random.randint(100, 400)
            file.write(f"    (=(paginas_libro {libro}) {num})\n")
            paginas[libro] = num


        libros = []
        for _ in range(random.randint(0,num_libros_quiere_leer)): #hay entre 0 y un num que el usuario ya ha leido 
            libro_leido = random.choice(libros_catalogo)
            if libro_leido not in libros: # si el llibre no ha estat ja declarat com a llegit
                libros.append(libro_leido)
                file.write(f"    (leido {libro_leido})\n")
                file.write(f"    (mes_lectura {libro_leido} Previo)\n")
                

        predecesors=[]
        for _ in range(random.randint(0, num_libros_catalogo//2)): #hi haura 0 o mes llibres amb predecesor
            libro1 = random.choice(libros_quiere_leer + libros_catalogo)
            numero1 = int(libro1[5:]) #agafem el numero del llibre
            libro1 = f"Libro{numero1}"
            
            libro2 = random.choice(libros_quiere_leer + libros_catalogo)
            numero2 = int(libro2[5:]) #agafem el numero del llibre
            libro2 = f"Libro{numero2}"
            
            if numero1 == numero2:
                continue
            
            if (libro2, libro1) in predecesors or (libro1, libro2) in predecesors: # mirem que un llibre no pot ser predecessor del mateix llibre si l'altre ho és del mateix
                file.write(f"    (predecesor {libro1} {libro2})\n")
                predecesors.append((libro1, libro2))

        visited = set()
        def trobar_predecessor(librox, libroy):

            for predecesor in predecesors:
                if predecesor in visited:
                    continue

                if (librox == predecesor[1] and libroy == predecesor[0]) or (librox == predecesor[0] and libroy == predecesor[1]):
                    return True
                
                elif librox == predecesor[0]:
                    visited.add(predecesor)
                    return trobar_predecessor(predecesor[1], libroy)
                    
                elif librox == predecesor[1]:
                    visited.add(predecesor)
                    return trobar_predecessor(predecesor[0], libroy)
                        
            return False
        
        paralels=[]
        for _ in range(random.randint(0, num_libros_catalogo//2)): #hi haura 0 o mes llibres amb predecesor
            libro1 = random.choice(libros_quiere_leer + libros_catalogo)
            numero1 = int(libro1[5:]) #agafem el numero del llibre
            libro1 = f"Libro{numero1}"
            
            libro2 = random.choice(libros_quiere_leer + libros_catalogo)
            numero2 = int(libro2[5:]) #agafem el numero del llibre
            libro2 = f"Libro{numero2}"
            
            if numero1 == numero2 or (libro2, libro1) in predecesors or (libro1, libro2) in predecesors or trobar_predecessor(libro1, libro2):
                continue
            else:
                paralels.append((libro1, libro2))
            
        primeros = []
        restantes = []

        for libros in paralels:
            if libros[0] in libros_quiere_leer or libros[1] in libros_quiere_leer:
                primeros.append(libros)
            else:
                restantes.append(libros)

        # Concatenar las listas de primeros y restantes
        paralels_ordenados = primeros + restantes

        visited = set()
        def cadena_predecessor(librox):
            for predecesor in predecesors:
                if predecesor in visited:
                    continue
                
                if librox == predecesor[0]:
                    visited.add(predecesor)
                    if predecesor[1] in libros_quiere_leer:
                        return True
                    else:
                        return cadena_predecessor(predecesor[1])
            
            if predecesors:  # Añadir una comprobación para evitar errores si predecesors está vacío
                visited.add(predecesor)
                
            return False 

        for i, libros in enumerate(paralels_ordenados):
            if (libros[1] in libros_quiere_leer or cadena_predecessor(libros[1])) and libros[0] not in libros_quiere_leer:
                libros_quiere_leer.append(libros[0])
            elif (libros[1] in libros_quiere_leer or cadena_predecessor(libros[1])) and libros[0] in libros_quiere_leer:
                continue
            elif libros[0] in libros_quiere_leer:
                paralels_ordenados[i] = (libros[1], libros[0])     
            
        for libro in paralels_ordenados: 
            file.write(f"    (paralelos {libro[0]} {libro[1]})\n")
        
        file.write(f"    (mes_anterior Previo Enero)\n")
        for mes in range(1, len(meses)):
            mes_anterior = meses[mes - 1]
            if meses[mes] != 'Previo' and meses[mes] != 'Enero':    
                file.write(f"    (mes_anterior {mes_anterior} {meses[mes]})\n")
                file.write(f"    (mes_anterior Previo {meses[mes]})\n")

        for mes in meses: 
            if mes != 'Previo':
                file.write(f"    (=(pagines_mes {mes})0)\n") #escriurà que aquell mes ja ha llegit x pagines
                
        file.write(f"  )\n\n")
        file.write(f"  (:goal (forall (?l - libros_catalog) (imply (quiere_leer ?l) (leido ?l))))\n")
        file.write(f"  (:metric maximize (pagines_mes))\n)")
    print("Archivo de problema PDDL generado con éxito. Su nombre es: random_problem.pddl")



num_libros_quiere_leer = random.randint(3,7) #numero de llibres que vol llegir (entre 1 i 5)
num_libros_catalogo =  random.randint(8,12) #numero de llibres totals,+ els que vol llegir (entre 5,12)
generate_random(num_libros_quiere_leer, num_libros_catalogo)
 

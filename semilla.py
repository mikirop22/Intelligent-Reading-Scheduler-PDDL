import random


semilla = 8
random.seed(semilla)



def generate_random(num_libros_quiere_leer, num_libros_catalogo):
    

    # Lista de libros
    libros_quiere_leer = [f"Libro{i}" for i in range(1, num_libros_quiere_leer + 1)]
    libros_catalogo = [f"Libro{i}" for i in range(num_libros_quiere_leer + 1, num_libros_quiere_leer + num_libros_catalogo + 1)]

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
        

        for libro in libros_quiere_leer:
            file.write(f"    (quiere_leer {libro})\n")
            file.write(f"    (=(paginas_libro {libro}) {random.randint(100, 300)})\n")


        for libro in libros_catalogo:
            file.write(f"    (=(paginas_libro {libro}) {random.randint(100, 300)})\n")

        for _ in range(random.randint(0,num_libros_quiere_leer)): #hay entre 0 y un num que el usuario ya ha leido 
            libro_leido = random.choice(libros_catalogo)
            mes_lectura = random.choice(meses)
            file.write(f"    (leido {libro_leido})\n")
            file.write(f"    (mes_lectura {libro_leido} {mes_lectura})\n")

        predecesors=[]
        for _ in range(random.randint(0, num_libros_catalogo/2)): #hi haura 0 o mes llibres amb predecesor
            libro1 = random.choice(libros_quiere_leer + libros_catalogo)
            numero = int(libro1[5:]) #agafem el numero del llibre
            if numero == num_libros_catalogo+num_libros_quiere_leer:
                numero = numero-1
            numero += 1
            libro2 = f"Libro{numero}"
            if libro1 not in predecesors:
                file.write(f"    (predecesor {libro1} {libro2})\n")
                predecesors.append(libro1)

        paralels=[]
        for _ in range(random.randint(0, num_libros_catalogo/2)): #hi haura 0 o mes llibres amb predecesor
            libro1 = random.choice(libros_quiere_leer + libros_catalogo)
            numero = int(libro1[5:]) #agafem el numero del llibre
            if numero == num_libros_catalogo+num_libros_quiere_leer:
                numero = numero-1
            numero += 1
            libro2 = f"Libro{numero}"
            if libro1 not in paralels:
                file.write(f"    (paralels {libro1} {libro2})\n")
                predecesors.append(libro1)
        

        for mes in range(len(meses)):
            mes_anterior = meses[mes-1]
            file.write(f"    (mes_anterior {mes_anterior} {meses[mes]})\n")

        for mes in meses: 
            file.write(f"    (=(lectura_mes {mes})0)\n")

        file.write(f"  )\n\n")
        file.write(f"  (:goal (forall (?l - libros_catalog) (imply (quiere_leer ?l) (leido ?l))))\n)\n")

    print("Archivo de problema PDDL generado de nuevo: random_problem.pddl")



num_libros_quiere_leer = random.randint(1,5)
num_libros_catalogo = random.randint(5,12)
generate_random(num_libros_quiere_leer, num_libros_catalogo)
 
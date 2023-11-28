import random

def generate_random_pddl_problem(num_libros_quiere_leer, num_libros_catalogo):
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
        
        # Condiciones iniciales aleatorias
        for libro in libros_quiere_leer:
            file.write(f"    (quiere_leer {libro})\n")
            file.write(f"    (=(paginas_libro {libro}) {random.randint(100, 300)})\n")

        for libro in libros_catalogo:
            file.write(f"    (=(paginas_libro {libro}) {random.randint(100, 300)})\n")

        for _ in range(num_libros_quiere_leer):
            libro_leido = random.choice(libros_quiere_leer)
            mes_lectura = random.choice(meses)
            file.write(f"    (leido {libro_leido})\n")
            file.write(f"    (mes_lectura {libro_leido} {mes_lectura})\n")

        for _ in range(num_libros_quiere_leer):
            libro1 = random.choice(libros_quiere_leer)
            libro2 = random.choice(libros_quiere_leer)
            if libro1 != libro2:
                file.write(f"    (predecesor {libro1} {libro2})\n")

        for _ in range(num_libros_quiere_leer):
            libro = random.choice(libros_catalogo)
            file.write(f"    (quiere_leer {libro})\n")

        for mes in meses:
            mes_anterior = random.choice(meses)
            file.write(f"    (mes_anterior {mes_anterior} {mes})\n")

        file.write(f"  )\n\n")
        file.write(f"  (:goal (forall (?l - libros_catalog) (imply (quiere_leer ?l) (leido ?l))))\n)\n")

    print("Archivo de problema PDDL generado: random_problem.pddl")

# Ejemplo de uso con 5 libros que se quieren leer y 10 en el catálogo
generate_random_pddl_problem(5, 10)

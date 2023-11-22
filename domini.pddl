(define (domain PlanLectura)
    (:requirements :strips :typing :adl :fluents)

    (:types libros_catalog mes - object
            ;l_leido l_porleer - libros_catalog
    )


    (:predicates
        (predecesor ?l1 - libros_catalog ?l2 - libros_catalog)
        (leido ?l - libros_catalog)
        (quiere_leer ?l - libros_catalog)
        (paralelos ?l1 - libros_catalog ?l2 - libros_catalog)
        (mes_lectura ?l - libros_catalog ?m - mes)
        (mes_anterior ?m1 - mes ?m2 - mes)
        (mes_finalizado ?m - mes)
    )


    (:functions 
        (libros_leidos) ;?l - libros_catalog)
        (mes_leido ?m - mes)
    )


    ; 1. leer predecesor


    (:action leer
        :parameters (?l1 - libros_catalog ?m1 - mes ?l2 - libros_catalog ?m2 - mes)
        :precondition (and 
                      (not(leido ?l1))
                      (leido ?l2)
                      (predecesor ?l2 ?l1)
                      (mes_lectura ?l2 ?m2)
                      (mes_anterior ?m2 ?m1)
                      )
                      
        :effect (and (leido ?l1)
                    (mes_lectura ?l1 ?m1)
                )
    )


    (:action leer_sin_predecesor
        :parameters (?l1 - libros_catalog ?m1 - mes)
        :precondition (and 
                        (quiere_leer ?l1)
                        (not (leido ?l1))
                        (not (exists (?l2 - libros_catalog) (predecesor ?l2 ?l1)))
                      )

        :effect (and (leido ?l1)
                 (mes_lectura ?l1 ?m1)
    )
    )

    

)
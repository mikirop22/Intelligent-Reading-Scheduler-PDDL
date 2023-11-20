(define (domain recomendacion_libros)
    (:requirements :strips :typing :adl :fluents)

    (:types libros_catalog meses - object
            ;l_leido l_porleer - libros_catalog
    )


    (:predicates
        (predecesor ?l1 - libros_catalog ?l2 - libros_catalog)
        (leido ?l - libros_catalog)
        (paralelos ?l1 - libros_catalog ?l2 - libros_catalog)
        (porleer ?l - libros_catalog)
        (mes ?m - meses)
    )

    (:functions 
        (libros_leidos)
    
    )

    (:action leer
        :parameters (?l - libros_catalog)
        :precondition (and 
                        (not(leido ?l))
                        (porleer ?l)
                      )

        :effect (and 
                    (increase (libros_leidos) 1)
                    (leido ?l)
                    (not(porleer ?l))
        )        
    )

)
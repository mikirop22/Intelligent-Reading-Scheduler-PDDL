(define (domain recomendacion_libros)
    (:requirements :strips :typing :adl :fluents)

    (:types libros_catalog mes - object
            ;l_leido l_porleer - libros_catalog
    )


    (:predicates
        (predecesor ?l1 - libros_catalog ?l2 - libros_catalog)
        (leido ?l - libros_catalog)
        ;(paralelos ?l1 - libros_catalog ?l2 - libros_catalog)
        (mes_lectura ?l - libros_catalog ?m - mes)
        (mes_anterior ?m1 - mes ?m2 - mes)
    )



    (:functions 
        (libros_leidos) ;?l - libros_catalog)
        ;(mes_lectura ?l - libros_catalog)
    )


    ; 1. leer predecesor

    (:action leer
        :parameters (?l1 - libros_catalog ?m1 - mes ?l2 - libros_catalog ?m2 - mes) 
        :precondition (and 
                        (not(leido ?l1))
                        (mes_lectura ?l2 ?m2)
                        (mes_anterior ?m2 ?m1) 
                        (imply (predecesor ?l2 ?l1) (mes_anterior ?m2 ?m1))
                        
                        ;(imply (not (predecesor ?l2 ?l1)) (not (= ?m2 ?m1)))
                      )

        :effect (and 
                    (increase (libros_leidos) 1)
                    (mes_lectura ?l1 ?m1)
                    (leido ?l1)
                    
        )        
    )
    

)
(define (problem libros_recomendacion)
    (:domain recomendacion_libros)

    (:objects Harry1 Harry2 Harry3 Spiderman HanselyGrettel - libros_catalog
            Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre - meses
    )

    (:init
        (= (libros_leidos) 2)
        (leido Harry1)
        (leido Harry2)
        (porleer Harry3)
        (porleer HanselyGrettel)
        (porleer Spiderman)
    )

    ;(:metric minimize (libros_leidos))

    (:goal (forall (?l - libros_catalog) (leido ?l)))

)
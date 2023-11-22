(define (problem PlanLectura_Problema)
    (:domain PlanLectura)

    (:objects Harry1 Harry2 Harry3 Spiderman HanselyGrettel - libros_catalog
            Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre - mes
    )

    (:init
        (mes_anterior Enero Febrero)
        (mes_anterior Febrero Marzo)
        (mes_anterior Marzo Abril)
        (mes_anterior Abril Mayo)
        (mes_anterior Mayo Junio)
        (mes_anterior Junio Julio)
        (mes_anterior Julio Agosto)
        (mes_anterior Agosto Septiembre)
        (mes_anterior Septiembre Octubre)
        (mes_anterior Octubre Noviembre)
        (mes_anterior Noviembre Diciembre)
        (mes_anterior Diciembre Enero)
        ;(= (libros_leidos) 2)
        (leido Harry1)
        (mes_lectura Harry1 Enero)
        (predecesor Harry1 Harry2)
        ;(leido Harry2)
        ;(mes_lectura Harry2 Febrero)
        (predecesor Harry2 Harry3)
        (quiere_leer Harry3)
        (quiere_leer HanselyGrettel)
        
    )

    (:goal (forall (?l - libros_catalog) (imply (quiere_leer ?l) (leido ?l))))

    ;(:metric minimize (libros_leidos))

)
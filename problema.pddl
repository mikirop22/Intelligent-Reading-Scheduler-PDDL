(define (problem PlanLectura_Problema)
    (:domain PlanLectura)

    (:objects Harry1 Harry2 Harry3 Spiderman1 Spiderman2 Spiderman3 Spiderman4 Spiderman5 
                HanselyGrettel Vengadores CapitanAmerica IronMan 
                StarWarsJedi StarWarsDark StarWars1 - libros_catalog
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
        ;(mesactual Febrero)
        ;(= (libros_leidos) 2)
        (leido Harry1)
        (mes_lectura Harry1 Enero)
        (predecesor Harry1 Harry2)
        ;(leido Harry2)
        ;(mes_lectura Harry2 Febrero)
        ;(quiere_leer Harry2)
        (predecesor Harry2 Harry3)
        (quiere_leer Harry3)
        (quiere_leer HanselyGrettel)
        ;(leido Spiderman1)
        ;(mes_lectura Spiderman1 Febrero)
        
        (predecesor Spiderman1 Spiderman2)
        (predecesor Spiderman2 Spiderman3)
        (predecesor Spiderman3 Spiderman4)
        (predecesor Spiderman4 Spiderman5)
        (leido Spiderman3)
        (mes_lectura Spiderman3 Febrero)
        (quiere_leer Spiderman5)

        ;(quiere_leer Vengadores)
        ;(predecesor CapitanAmerica Vengadores)
        ;(predecesor IronMan Vengadores)

        (quiere_leer StarWars1)
        (paralelos StarWarsJedi StarWars1)
        (paralelos StarWarsDark StarWars1)
        
    )

    (:goal (forall (?l - libros_catalog) (imply (quiere_leer ?l) (leido ?l))))

    ;(:metric minimize (libros_leidos))

)
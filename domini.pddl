(define (domain PlanLectura)
  (:requirements :strips :typing :adl :fluents)

  ;; Tipos
  (:types llibre mes - object)

  ;; Predicados
  (:predicates
    (llegit ?llibre - llibre)
    (vol-llegir ?llibre - llibre)
    (predecesor ?predecesor - llibre ?llibre - llibre)
    (mes_valid ?mes - mes)
    (mes_anterior ?mes_anterior - mes ?mes - mes)
    (pla_lectura ?llibre - llibre ?mes - mes)
    (llegir_seguent ?llibre -llibre)
    (llegir_aquest ?llibre -llibre)
  )

(:functions
  (mesos ?mes - mes)
)

(:action llegir
  :parameters (?llibre - llibre ?mes - mes)
  :precondition (and (vol-llegir ?llibre) 
                     (mes_valid ?mes) 
                     (or (not (exists (?predecesor - llibre) (predecesor ?predecesor ?llibre)))
                         (exists (?predecesor - llibre ?mes_anterior -mes) (and (predecesor ?predecesor ?llibre) 
                                                             (llegit ?predecesor) 
                                                             (pla_lectura ?predecesor ?mes_anterior)
                                                             ))
                     )
                )
  :effect (and (llegit ?llibre) 
               (not (vol-llegir ?llibre)) 
               )
)


  (:action llegir_pre
    :parameters (?llibre - llibre ?mes -mes)
    :precondition (and (mes_valid ?mes) 
                       (exists (?next_llibre - llibre) (and (predecesor ?llibre ?next_llibre) (vol-llegir ?next_llibre)))
                  )
    :effect (and (llegit ?llibre) 
                 )
  )

  (:action canviar_mes
      :parameters (?mes_anterior - mes ?nou_mes - mes)
      :precondition (and (mes_valid ?mes_anterior) (mes_anterior ?mes_anterior ?nou_mes))
      :effect (and (not(mes_valid ?mes_anterior))
                   (mes_valid ?nou_mes)
              )
  )
  
)
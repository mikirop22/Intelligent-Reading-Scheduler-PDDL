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
    (pla-lectura ?llibre -llibre ?mes - mes)
  )

(:functions
  (mesos ?mes - mes)
)

(:action llegir
  :parameters (?llibre - llibre ?mes - mes)
  :precondition (and (vol-llegir ?llibre) 
                     (<(mesos ?mes)4) 
                     (or (not (exists (?predecesor - llibre) (predecesor ?predecesor ?llibre)))
                         (exists (?predecesor - llibre) (and (predecesor ?predecesor ?llibre) (llegit ?predecesor)))
                     )
                )
  :effect (and (llegit ?llibre) 
               (not (vol-llegir ?llibre)) 
               (pla-lectura ?llibre ?mes)
               (increase (mesos ?mes) 1)
               )
)


  (:action llegir_pre
    :parameters (?llibre - llibre ?mes -mes)
    :precondition (and (<(mesos ?mes)4) 
                       (exists (?next_llibre - llibre) (and (predecesor ?llibre ?next_llibre) (vol-llegir ?next_llibre)))
                  )
    :effect (and (llegit ?llibre) 
                 (pla-lectura ?llibre ?mes)
                 (increase (mesos ?mes) 1)
                 )
  )

  (:action canviar_mes
      :parameters ()
      :precondition (and )
      :effect (and )
  )
  
)
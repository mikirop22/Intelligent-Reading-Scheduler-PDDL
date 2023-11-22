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

(:action llegir
  :parameters (?llibre - llibre ?mes - mes)
  :precondition (and (vol-llegir ?llibre) 
                     ;(mes_valid ?mes) 
                     (or (not (exists (?predecesor - llibre) (predecesor ?predecesor ?llibre)))
                         (exists (?predecesor - llibre) (and (predecesor ?predecesor ?llibre) (llegit ?predecesor)))
                     )
                )
  :effect (and (llegit ?llibre) 
               (not (vol-llegir ?llibre)) 
               (pla-lectura ?llibre ?mes))
)


  (:action llegir_pre
    :parameters (?llibre - llibre ?mes -mes)
    :precondition (and ;(mes_valid ?mes) 
                       (exists (?next_llibre - llibre) (and (predecesor ?llibre ?next_llibre) (vol-llegir ?next_llibre)))
                  )
    :effect (and (llegit ?llibre) (pla-lectura ?llibre ?mes))
  )

  ;; Acciones 
)
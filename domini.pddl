(define (domain PlanLectura)
  (:requirements :strips :typing :adl :fluents)

  ;; Tipos
  (:types llibre mes - object)

  ;; Predicados
  (:predicates
    (llegit ?llibre - llibre)
    (vol-llegir ?llibre - llibre)
    (predecesor ?libre - llibre ?predecesor - llibre)
    (mes_valid ?mes - mes)
    (pla-lectura ?llibre -llibre ?mes - mes)
  )

    (:action llegirpos
    :parameters (?llibrepre - llibre ?llibre - llibre ?mes -mes)
    :precondition (and (predecesor ?llibrepre ?llibre) (llegit ?llibrepre) (vol-llegir ?llibre) (mes_valid ?mes) )
                      ;;(forall (?predecesor - llibre) (llegit ?predecesor)))
                     ;;(not (predecesor ?llibre ?predecesor))    (and (llegit ?predecesor)))))
    :effect (and (llegit ?llibre) (not (vol-llegir ?llibre)) (pla-lectura ?llibre ?mes))
  )



  ;; Acciones

  
)
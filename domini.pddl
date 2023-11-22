(define (domain PlanLectura)
  (:requirements :strips :typing :adl)

  ;; Tipos
  (:types llibre mes - object)

  ;; Predicados
  (:predicates
    (llegit ?llibre - llibre)
    (vol-llegir ?llibre - llibre)
    (predecesor ?libre - llibre ?predecesor - llibre)
    (mes_valid ?mes - mes))

  (:action llegir
    :parameters (?llibrev - llibre ?mes_ - mes)
    :precondition (and (mes_valid ?mes_)
                       (vol-llegir ?llibrev)
                       (forall (?l - llibre)
                               (predecesor ?l ?llibrev)
                               (imply (llegit ?l))))
    :effect (and (not (mes_valid ?mes_))
                 (not (vol-llegir ?llibrev))
                 (llegit ?llibrev))
  )
)




  ;  (:action llegirpos
   ; :parameters (?llibrepre - llibre ?llibre - llibre ?mes -mes)
   ; :precondition (and (predecesor ?llibrepre ?llibre) (llegit ?llibrepre) (vol-llegir ?llibre) (mes_valid ?mes) )
                      ;;(forall (?predecesor - llibre) (llegit ?predecesor)))
                     ;;(not (predecesor ?llibre ?predecesor))    (and (llegit ?predecesor)))))
    ;:effect (and (llegit ?llibre) (not (vol-llegir ?llibre)) (pla-lectura ?llibre ?mes))
  ;)



  ;; Acciones

  
)
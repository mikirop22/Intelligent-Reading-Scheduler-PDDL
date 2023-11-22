(define (domain PlanLectura)
  (:requirements :strips :typing :adl)

  ;; Tipos
  (:types llibre mes - object)

  ;; Predicados
  (:predicates
    (llegit ?llibre - llibre)
    (vol-llegir ?llibre - llibre)
    (predecesor ?libre - llibre ?predecesor - llibre)
    (mes_valid ?mes - mes)
    (mes_anterior ?mes1 - mes ?mes2 - mes))

  (:action llegir
    :parameters (?llibrev - llibre ?mes_ - mes)
    :precondition (and (mes_valid ?mes_)
                       (vol-llegir ?llibrev)
                       (forall (?l - llibre)
                               (imply (predecesor ?l ?llibrev)(llegit ?l))))
    :effect (and (not (mes_valid ?mes_))
                 (not (vol-llegir ?llibrev))
                 (llegit ?llibrev))
  )

  (:action llegir_necessari
      :parameters (?anterior - llibre ?l - llibre ?m - mes)
      :precondition (and (predecesor ?anterior ?l)
                         (mes_valid ?m)
                         (vol-llegir ?l)
                         (not(llegit ?anterior))
                         (not(llegit ?l)))
      :effect (and (llegit ?anterior) (not (mes_valid ?m)))
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

  

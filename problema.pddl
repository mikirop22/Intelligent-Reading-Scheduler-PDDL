(define (problem PlanLectura_problema)
  (:domain PlanLectura)

  ;; Objetos
  (:objects
    llibre1 llibre2 llibre3 llibre45 llibre70 - llibre
    gener febrer març abril maig juny juliol agost setembre octubre novembre desembre - mes
  )

  ;; Inicialización
  (:init
    (mes_valid gener)
    (mes_valid febrer)
    ;(llegit llibre1)
    (vol-llegir llibre2)
    ;(vol-llegir llibre45)
    (vol-llegir llibre70)
    (predecesor llibre1 llibre2)
    ;(predecesor llibre2 llibre3)
    (predecesor llibre45 llibre70)
  )

  ;; Meta
  (:goal (forall (?llibre - llibre) (imply(vol-llegir ?llibre) (llegit ?llibre))))
  ;;(:goal (forall (?llibre - llibre)(imply (vol-llegir ?llibre)(and (llegit ?llibre)(forall (?predecesor - llibre)(imply (predecesor ?llibre ?predecesor)(llegit ?predecesor)))))))
)


import random

random.seed(11)

text = """(define (problem PlanLectura-problema)
  (:domain PlanLectura)
  (:objects"""

for i in range(random.randint(5,15) + 7):
    text += "libro"+
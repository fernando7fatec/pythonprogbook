
# -------------------------------------
# Livro Python Programming - John Zelle
# Capitulo 3
# Página 62 
# Exercicio de programação  
# -------------------------------------
import math

class ProgramExerciseCh3:
    # program exercises 1
    def calcularVolumeEsfera(raio):
        V = 4/3*(math.pi)*(raio**3) 
        return V 

    # program exercises 1
    def calcularAreaEsfera(raio):
        A = 4*(math.pi)*(raio**2)
        return A

    

pe = ProgramExerciseCh3

# raio
r = 3.6

print(" Area da Esfera : ")
print(pe.calcularAreaEsfera(r))
print(" Volume da Esfera : ")
print(pe.calcularAreaEsfera(r))
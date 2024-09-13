# -------------------------------------
# Livro Python Programming - John Zelle
# Capitulo 3
# Página 62 
# Exercicio de programação  
# -------------------------------------

# Escreva um programa em python
# que calcule a distancia de um
# relâmpago que aconteceu no ponto A
# medida pelo tempo
# que o som levou para chegar até o
# ponto B

def distanciaRelampago(tempoEmSegundosTrovao):
    # velocidade do som
    # 340.29 metros por segundo
    fltMs = 340.29

    # Calcula a distancia entre o relampago, ponto A
    # e a chegada do som, Ponto B, 
    # baseado no tempo que o som leva para chegar.
    fltDistancia = fltMs * tempoEmSegundosTrovao
    return fltDistancia

print(" A distancia do Relampago em metros é : ")
print(round(distanciaRelampago(3)))
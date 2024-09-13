# -------------------------------------
# Livro Python Programming - John Zelle
# Capitulo 3
# Página 62 
# Exercicio de programação  
# -------------------------------------
import math
class PizzaCalc:

    def calculateArea(pizza_ratio):
        A = math.pi*pizza_ratio**2 
        return A

a = PizzaCalc.calculateArea(12)
intCustoPorCm2 = 20 / a
print(f" O custom por cm2 da pizza é {intCustoPorCm2}")
import math
base = float(input('digite a base do reatangulo:'))
altura = float(input('digite a altura do retangulo: '))
area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base**2 + altura**2)**0.5
print(f'area do retangulo:{area:.4f}')
print(f'perimetro do retangulo:{perimetro:.4f}')
print(f'diagonal do retangulo:{diagonal:.4f}')

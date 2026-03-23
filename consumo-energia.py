# Calculadora de Consumo de Energia

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (W): "))
horas_dia = float(input("Horas de uso por dia: "))

consumo = (potencia * horas_dia * 30) / 1000
custo = consumo * 0.75

print("\nResultado:")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f}/mês")
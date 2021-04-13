dia = int(input("Quantos dias o carro esta alugado: "))
km = float(input("Quantos KM foi rodado com o carro: "))

pago = (dia * 60) + (km * 0.15)

print(f"O total a pagar pelo aluguem do carro é R${pago:.2f}")

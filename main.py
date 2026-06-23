usina = "Usina Solar Alpha"
geracao = 850
meta = 1000

print("Monitoramento da Usina")
print("----------------------")
print(f"Usina: {usina}")
print(f"Geração atual: {geracao} kWh")
print(f"Meta diária: {meta} kWh")

if geracao >= meta:
    print("Desempenho OK")
else:
    print("Desempenho abaixo da meta")

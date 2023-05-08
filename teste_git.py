def input_float(texto):
    valor = input(texto)
    valor = valor.replace(',', '.')
    return float(valor)


def calcular_lucro(valor_custo, taxa_categoria, valor_final, imposto):
    taxa_valor = valor_final * (taxa_categoria / 100)
    valor_imposto = valor_final * (imposto / 100)
    custo_total = valor_custo + taxa_valor + 5 + valor_imposto
    lucro = valor_final - custo_total
    porcentagem_lucro = (lucro / valor_final) * 100

    return lucro, porcentagem_lucro


valor_custo = input_float("Digite o valor de custo do produto: ")
taxa_categoria = input_float("Digite a taxa da categoria (em porcentagem): ")
imposto = input_float("Digite o imposto a ser pago(em porcentagem): ")
valor_final = input_float("Digite o valor final de venda do produto: ")

lucro, porcentagem_lucro = calcular_lucro(
    valor_custo, taxa_categoria, valor_final, imposto)

print(f"\nLucro: R$ {lucro:.2f}")
print(f"Porcentagem de lucro: {porcentagem_lucro:.2f}%")

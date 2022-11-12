def somaImposto(taxaImposto, custo):
    taxa = (custo*taxaImposto)/100
    return custo + taxa


imposto = int(input(" taxa de imposto sobre o produto: "))
valor = float(input(" valor do produto: "))
print(f"o custo do meu produto eh de R${somaImposto(imposto, valor)}")
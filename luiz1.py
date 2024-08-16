
#define a função calcular juros atraso e diz quais variavéis serão usadas para tal cálculo
def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
#define a variável da taxa diária baseada no valor da taxa anual dividido pelo número de dias do ano
taxa_juros_diaria = taxa_juros_anual / 365 / 100

#define como será calculado o valor dos juros
juros = valor_principal * taxa_juros_diaria * dias_atraso

#define como será calculado o valor final, baseado no valor inicial somado com o valor dos juros
valor_total = valor_principal + juros
#como é uma função, termina sua sintaxe retornando o valor
return valor_total, juros

#define os valores iniciais, o juros anual, o tempo atrasado e o valor original a ser pago
valor_principal = 1000.00
taxa_juros_anual = 5.0
dias_atraso = 30
#chama a função para que ela calcule os valores
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
#exibe ao usuário o valor total a ser pago e o valor em juros que já está incluso
print(f"Valor total a ser pago: R${valor_total:.2f}")
print(f"Valor dos juros: R${juros:.2f}")

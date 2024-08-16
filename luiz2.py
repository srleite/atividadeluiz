#define a função que irá calcular a área
def calcular_area_comodos():
#define a area total como 0 para não haver conflitos nas próximas operações
total_area = 0

#garante que o processo será repetido até que o usuário digite os inputs desejados
while True:

#pede para o usuário a largura e o comprimento do cômodo através de um input
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

#define como a área do cômodo será calculada e já mostra a mesma ao usuário
area_comodo = largura * comprimento
print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")

#soma a área do cômodo à área total para que mais cômodos possam ser adicionados
total_area += area_comodo

#pergunta se o usuário deseja adicionar mais cômodos à área total e se sim os procedimentos acima se repetem
mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()
if mais_comodos != 's':
break

return total_area

#depois de colocar todos os cômodos o programa mostra ao usuário a área total que foi calculada
area_total = calcular_area_comodos()
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")
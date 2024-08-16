#define a função e coloca os valores base para começar os cálculos
def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):
total_notas = 0
num_alunos = len(notas)
aprovados = []
reprovados = []

#soma as notas do aluno ao seu total de notas(para casos onde cada aluno tem mais de uma nota)
for aluno, nota in notas.items():
total_notas += nota
#define como o programa vai aprovar ou reprovar os alunos
if nota >= nota_minima_aprovacao:
aprovados.append(aluno)
else:
reprovados.append(aluno)

#calcula a média da turma e encerra a função
media_turma = total_notas / num_alunos

return media_turma, aprovados, reprovados

#cria a base de notas para o programa usar na função
notas = {
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}
#define a nota mínima para aprovação
nota_minima_aprovacao = 70
#chama a função que calcula a média e aprovação dos alunos e os apresenta ao usuário
media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")
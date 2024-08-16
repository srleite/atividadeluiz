#define a função principal do programa
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):

#define quais valores levarão a cada diagnóstico baseado no valor da glicemia em jejum e após refeições
if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:
return "Diabetes"
elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
return "Pré-diabetes"
else:
return "Normal"

#pede ao usuário os valores da glicemia do paciente, respectivamente em jejum e após refeições
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

#define como o resultado será apresentado e em seguida apresenta-o ao usuário
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
print(f"O diagnóstico é: {resultado}")
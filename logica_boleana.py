#Revisando a Logica Booleana

#----simulador de critérios escolares----

#1 . Dados de exemplo do aluno
nota_final = 7.5
frequencia = 0.85 #frequemcia decimal  (85%)
historico_ruim = False #historico ruim do aluno (true ou false)
eh_atleta = True # O aluno é atleta (True ou Flase)

print('=== Analise Cdastral do aluno ===')


#-----------------------------------------------


passou_por_media = nota_final >= 7.0
passou_por_frequencia = frequencia >= 0.75
aprovado_regular = passou_por_media and passou_por_frequencia


print(f"Passou por media:  {passou_por_media}")
print(f"Passou por frequência: {passou_por_frequencia}")
print(f"Aprovado Regular: {aprovado_regular}")


#--------------------------------------------------
# Cenário 2: Operador OR (Bolsa de incentivo)
# Critério: Nota fantastica (>= 9.0) OU sre atleta da escola
#--------------------------------------------------
nota_fantastica = nota_final >= 9.0
eh_atleta = eh_atleta #Já é um valor booleano
bolsa_incentivo = nota_fantastica or eh_atleta

print(f"Nota Fantástica: {nota_fantastica}")
print(f"É Atleta: {eh_atleta}")
print(f"Bolsa de incentivo: {bolsa_incentivo}")


#--------------------------------
#Cenário 3: Operador  NOT (Ficha Limpa)
#Critério: O aluno NÃo pode ter um histórico ruim para ser monitor
#--------------------------------

pode_ser_monitor = not historico_ruim
print(f"3. Elegivel para monitor: {pode_ser_monitor}")


#-------------------------------------------------------------------
# Cenário 4: misturando tudo (Aprovação de aluno Atleta)
# Critério: (Nota >= 6.0 E presença >= 70%) E ser atleta
#-------------------------------------------------------------------

aprovacao_especial = (nota_final >= 6.0 and frequencia >= 0.70) and eh_atleta
print(f"4. Aprovado pelo critério especial de atleta? {aprovacao_especial}")

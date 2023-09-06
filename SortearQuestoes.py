import random

# Lista de todas as questões disponíveis
questoes_disponiveis_integral = [i for i in range(1, 71)]

# Número de questões desejadas no conjunto
numero_de_questoes_desejadas = 25  # Por exemplo, selecione 3 questões

# Certifique-se de que o número de questões desejadas não seja maior do que o número total de questões disponíveis
if numero_de_questoes_desejadas > len(questoes_disponiveis_integral):
    print("Número de questões desejadas é maior do que o número total de questões disponíveis.")
else:
    # Use random.sample para selecionar aleatoriamente o número desejado de questões
    conjunto_de_questoes = random.sample(questoes_disponiveis_integral, numero_de_questoes_desejadas)

    # Imprima o conjunto de questões selecionadas
    print("Conjunto de Questões Selecionadas de Integral:")
    print(conjunto_de_questoes)
    #for questao in conjunto_de_questoes:
    #    print(questao)


# Lista de todas as questões disponíveis
questoes_disponiveis_limite = [i for i in range(1, 25)]

# Número de questões desejadas no conjunto
numero_de_questoes_desejadas = 15  # Por exemplo, selecione 3 questões

# Certifique-se de que o número de questões desejadas não seja maior do que o número total de questões disponíveis
if numero_de_questoes_desejadas > len(questoes_disponiveis_limite):
    print("Número de questões desejadas é maior do que o número total de questões disponíveis.")
else:
    # Use random.sample para selecionar aleatoriamente o número desejado de questões
    conjunto_de_questoes = random.sample(questoes_disponiveis_limite, numero_de_questoes_desejadas)

    # Imprima o conjunto de questões selecionadas
    print("Conjunto de Questões Selecionadas de Limite:")
    print(conjunto_de_questoes)
    #for questao in conjunto_de_questoes:
    #    print(questao)

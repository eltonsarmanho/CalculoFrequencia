import pandas as pd;

def load():
    # Use a breakpoint in the code line below to debug your script.
    dataset = pd.read_csv('Dataset/frequencia_resp_1.csv')
    dataset.drop(columns=['Carimbo de data/hora'],inplace=True)
    print(dataset.info())

    dataset['Nome'] = dataset['Nome'].str.upper()


    return dataset;

def generaeLaTex(dataset):
    curso = 'Orientação Pedagógica para o Preenchimento do Relatório de Atividades'
    for nome in dataset['Nome']:
        #string = "\para{\textbf{\color{azul} {0}}}{\color{azul}{1}}{part}{6}{}".format(nome,curso)
        string = "\para{\\textbf{\color{azul}"+nome+"}}{\color{azul}"+curso+"}{part}{6}{}"
        print(string)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataset = load()
    generaeLaTex(dataset)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

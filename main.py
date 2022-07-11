import pandas as pd;

def load():
    # Use a breakpoint in the code line below to debug your script.
    dataset = pd.read_csv('Dataset/Curso.csv',sep=',')
    #dataset.drop(columns=['Carimbo de data/hora'],inplace=True)
    print(dataset.head())

    dataset['Nome'] = dataset['Nome'].str.upper()


    return dataset;

def generaeLaTex(dataset):

    for nome,local,curso,inicio,fim in zip(dataset['Nome'],dataset['Local'],dataset['Curso'],dataset['Inicio'],dataset['Fim']):
        #string = "\para{\textbf{\color{azul} {0}}}{\color{azul}{1}}{part}{6}{}".format(nome,curso)
        data = inicio[0:5]+' a '+fim[0:5]+' de 2022'
        cidade = local
        curso = curso
        string = "\para{\\textbf{\color{azul}"+nome+"}}{\color{azul}"+curso+"}{part}{"+data+"}{"+cidade+"}{}"
        print(string)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataset = load()
    generaeLaTex(dataset)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

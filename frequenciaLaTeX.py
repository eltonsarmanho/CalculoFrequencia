import pandas as pd;
from tkinter import filedialog
import csv
import chardet

def load():
    # Use a breakpoint in the code line below to debug your script.
    filepath= filedialog.askopenfilename(initialdir="/home/eltonss/Downloads", title="Select file",
                                               filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))


    dataset = pd.read_csv(filepath,sep=';',encoding='utf-8')
    print(dataset.shape)
    print(dataset.head())
    return dataset;


def getColumn(index,dataset):
    # calling the .columns
    list_of_column_names = list(dataset.columns)
    # displaying the list of column names
    return list_of_column_names[index];

def generaeLaTex(dataset):

    for nome,email,frequencia in zip(dataset[getColumn(0,dataset)],
                                           dataset[getColumn(1,dataset)],
                                           dataset[getColumn(2,dataset)]):
        data = '27/02 a 3/03 de 2023'
        cidade = 'Cametá'
        curso = 'Curso de LaTex Básico'
        string = "\para{\\textbf{"+nome.upper()+"}}{"+curso.upper()+"}{part}{6}{}"
        print(email)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataset = load()
    generaeLaTex(dataset)


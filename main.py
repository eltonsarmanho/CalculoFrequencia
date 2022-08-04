import pandas as pd;
from tkinter import filedialog
import csv
import chardet

def load():
    # Use a breakpoint in the code line below to debug your script.
    filepath= filedialog.askopenfilename(initialdir="/home/eltonss/Downloads", title="Select file",
                                               filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))

    charenc, delimiter = getInfoCSV(filepath)
    dataset = pd.read_csv(filepath,sep=delimiter,encoding=charenc)

    print(dataset.head())
    return dataset;

def getInfoCSV(filepath):
    delimiter = ''
    charenc = ''
    with open(filepath, encoding='latin-1') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        rawdata = open(filepath, 'rb').read()
        result = chardet.detect(rawdata)
        charenc = result['encoding']
        delimiter = dialect.delimiter

    return charenc, delimiter

def getColumn(index,dataset):
    # calling the .columns
    list_of_column_names = list(dataset.columns)
    # displaying the list of column names
    return list_of_column_names[index];

def generaeLaTex(dataset):


    for nome,local,curso,inicio,fim in zip(dataset[getColumn(0,dataset)],
                                           dataset[getColumn(4,dataset)],
                                           dataset[getColumn(1,dataset)],
                                           dataset[getColumn(5,dataset)],
                                           dataset[getColumn(6,dataset)]):
        data = inicio[0:5]+' a '+fim[0:5]+' de 2022'
        cidade = local
        curso = curso
        string = "\para{\\textbf{\color{azul}"+nome.upper()+"}}{\color{azul}"+curso.upper()+"}{part}{"+data+"}{"+cidade+"}{}"
        print(string)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataset = load()
    generaeLaTex(dataset)


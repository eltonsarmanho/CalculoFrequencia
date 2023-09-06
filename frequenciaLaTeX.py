import pandas as pd;
from tkinter import filedialog
import csv
import chardet
import glob

def load():
    # Use a breakpoint in the code line below to debug your script.
    filepath= filedialog.askopenfilename(initialdir="/home/eltonss/Downloads", title="Select file",
                                               filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))


    dataset = pd.read_csv(filepath,sep=',',encoding='utf-8')
    print(dataset.shape)
    print(dataset.head())
    return dataset;

def mergeCSV():
    files = ["/home/eltonss/Downloads/Frequência - Aula 1.csv",
             "/home/eltonss/Downloads/Frequência - Aula 2.csv",
             "/home/eltonss/Downloads/Frequência - Aula 3.csv",
             "/home/eltonss/Downloads/Frequência - Aula 4.csv"
             ]
    csv_files = glob.glob('/home/eltonss/Downloads/Frequencia*.{}'.format('csv'))
    #print(csv_files)
    df_csv_append = pd.DataFrame()

    df_csv_concat = pd.concat([pd.read_csv(file) for file in csv_files ], ignore_index=True)
    df_csv_concat['Nome (Em Maiúscula)'] = df_csv_concat['Nome (Em Maiúscula)'].str.upper()
    df_csv_concat['Nome (Em Maiúscula)'] = df_csv_concat['Nome (Em Maiúscula)'].str.lstrip()
    df_csv_concat['Nome (Em Maiúscula)'] = df_csv_concat['Nome (Em Maiúscula)'].str.rstrip()

    df_csv_concat['E-mail'] = df_csv_concat['E-mail'].str.lstrip()
    df_csv_concat['E-mail'] = df_csv_concat['E-mail'].str.rstrip()

    df_map = dict(zip(df_csv_concat['Nome (Em Maiúscula)'],df_csv_concat['E-mail']))
    #print(df_map )
    value_counts = df_csv_concat['Nome (Em Maiúscula)'].value_counts(dropna=False,sort=True)
    # solution here
    df_val_counts = pd.DataFrame(value_counts)

    df_value_counts_reset = df_val_counts.reset_index()
    df_value_counts_reset.columns = ['Nome', 'counts']  # change column names

    filter = df_value_counts_reset['counts']>=2
    df = df_value_counts_reset[filter]
    #print(df.sort_values(by=['Nome']))
    #print(df.info())
    return df,df_map


def generaeLaTex():
    df, df_map= mergeCSV()
    for nome in df['Nome']:
        data = '05/06 a 08/06 de 2023'
        cidade = 'Cametá'
        curso = 'Curso de LaTex Básico'
        string = "\para{\\textbf{"+nome.upper()+"}}{"+curso.upper()+"}{part}{6}{}"
        #print(string)
        print(df_map[nome])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generaeLaTex()


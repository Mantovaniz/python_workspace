import pandas as pd
from pathlib import Path
from pandas.core.frame import DataFrame 
import datetime, time, calendar

try:
    import common
    DATA = common.dataDirectory()
except ImportError:
    DATA = Path().resolve() / 'expirados_Historico' #configura o diretório

ARQUIVO1 = DATA / 'NomeDoArquivo_EmOutraPasta.xlsx' #diretório + nome do arquivo
ARQUIVO2 = 'NomeDoArquivo_NaMesmaPasta.xlsx'

df_arquivo1 = pd.DataFrame(pd.read_excel(ARQUIVO1, 'Sheet1', header=None)) #leitura dos dados da planilha do excel e inserção em um dataframe
df_arquivo1 = df_arquivo1.drop(df_arquivo1.index[[0,1,2]]) #exclui linhas que não são necessárias
df_arquivo1 = pd.DataFrame(df_arquivo1, columns = [0, 1, 2, 3, 4] ) #inserção de uma nova coluna que armazenará a data

for i in df_arquivo1[4]:   #busca a data do último sábado e insere no dataframe de expirados na 4º coluna
    today = datetime.date.today()
    lastSaturday = today - datetime.timedelta(days=2)
    format = "%d/%m/%Y"
    df_arquivo1[4]= lastSaturday.strftime(format)

df_arquivo2 = pd.DataFrame(pd.read_excel(ARQUIVO2, 'Sheet1', header=None))
df_arquivo2 = df_arquivo2.drop(df_arquivo2.index[[0]])
df_arquivo2 = df_arquivo2.append(df_arquivo1)
df_arquivo2.columns = ['A', 'B', 'C', 'D', 'E'] #monta o cabeçalho

df_arquivo2.to_excel(ARQUIVO2, sheet_name='Sheet1', index = False)  #"escreve" o dataframe no excel

import pandas as pd

dados = {
    'cargos': ['assistente', 'analista', 'gerente', 'diretor'],
    'salarios': [1000, 2000, 5000, 10000]
}

dados_bi =pd.DataFrame(dados)

dados_bi.to_csv('meus_dados.csv',index=False,sep=';',encoding='utf-8') 

print ("arquivo criado com sucesso")
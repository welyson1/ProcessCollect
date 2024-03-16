import pandas as pd
import json
import re

# Carregar o arquivo Excel
df = pd.read_excel('dados_processos.xlsx')

# Função para dividir os valores separados por ;
def split_values(value):
    if pd.isnull(value):
        return []
    else:
        values = [v.strip() for v in value.split(';')]
        return [v if '(' not in v else extract_file_and_link(v) for v in values if v]

# Função para extrair o nome do arquivo e o link
def extract_file_and_link(text):
    match = re.search(r'\((.*?)\)', text)
    if match:
        return {
            "descricao": text.split('(')[0].strip(),
            "url": match.group(1)
        }
    else:
        return text

# Converter DataFrame em um dicionário
data = []
for _, row in df.iterrows():
    process = {
        "ID do Processo": int(row["ID do Processo"]),
        "Nome do Processo": row["Nome do Processo"],
        "Descrição": row["Descrição"],
        "Atividades": split_values(row["Atividades"]),
        "Fluxo de Sequência (BPMN)": extract_file_and_link(row["Fluxo de Sequência (BPMN)"]),
        "Participantes": split_values(row["Participantes"]),
        "Documentos Relacionados": split_values(row["Documentos Relacionados"]),
        "Setor": row["Setor"],
        "Unidade": row["Unidade"],
        "Relações de Processos": split_values(row["Relações de Processos"]),
        "Mapeado?": row["Processo Mapeado"],
        "Data de Criação": str(row["Data de Criação"]),
        "Última Atualização": str(row["Última Atualização"])
    }
    data.append(process)

# Serializar o dicionário em JSON
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Escrever o JSON em um arquivo
with open('processos.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

print("Arquivo JSON criado com sucesso.")
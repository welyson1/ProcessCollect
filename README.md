# ProcessCollect

O ProcessCollect é um aplicativo web projetado para visualizar e gerenciar processos dentro de uma organização. Ele permite aos usuários filtrar processos com base em vários critérios, visualizar detalhes do processo e visualizar relacionamentos entre processos usando grafos.

## Funcionalidades
- Filtrar processos por intervalo de datas, setor e termo de pesquisa.
- Visualizar informações detalhadas sobre cada processo.
- Visualizar relacionamentos entre processos usando gráficos.

## Tecnologias Utilizadas
- HTML
- CSS
- JavaScript
- Cytoscape.js (para visualização de gráficos)
- Python

## Configuração inicial
Para executar o aplicativo localmente:
1. Clone este repositório em sua máquina local.
2. Abra o pasta do projeto no seu editor de código.

## Uso da ferramenta
1. Ao abrir o aplicativo, você verá uma lista de processos no lado esquerdo e detalhes do processo com uma visualização de gráfico no lado direito.
2. Use a seção de filtros para filtrar os processos com base no intervalo de datas, setor e termo de pesquisa.
3. Clique em um processo da lista para visualizar seus detalhes e gráfico de relacionamentos.

## Hierarquia de pastas
```
root/
│
├── app_xlsxToJson.py
├── dados_processos.xlsx
├── index.html
├── logo.png
└── processos.json
```
Nesta estrutura:
- **root/**: Pasta raiz do seu projeto.
    - **app_xlsxToJson.py**: O script Python para converter o arquivo Excel em JSON.
    - **dados_processos.xlsx**: O arquivo Excel contendo os dados dos processos.
    - **index.html**: Página HTML com a ferramenta.
    - **logo.png**: Imagem de logotipo.
    - **processos.json**: O arquivo JSON resultante após a execução do script Python.

## Arquivo app_xlsxToJson.py

Este é um script Python para processar dados de processos empresariais contidos em um arquivo Excel e convertê-los em um formato JSON. Ele é útil para organizar e estruturar informações relacionadas a processos, como atividades, participantes, documentos relacionados, etc., para análise ou integração com outros sistemas.

## Pré-requisitos

Antes de executar este script, certifique-se de ter instalado o Python (versão 3.x) em seu ambiente. Além disso, é necessário ter as bibliotecas Pandas e openpyxl instaladas. Você pode instalá-las utilizando pip:

```
pip install pandas openpyxl
```

## Uso

1. **Prepare os dados**: O script espera que os dados dos processos estejam em um arquivo Excel com o nome 'dados_processos.xlsx'. Certifique-se de que o arquivo esteja presente no mesmo diretório que o script.

2. **Execute o script**: Execute o script Python utilizando o interpretador Python:

```
python processos.py
```

3. **Saída**: O script irá processar os dados e gerar um arquivo JSON chamado 'processos.json', contendo as informações estruturadas dos processos.

## Funcionalidades

- **Divisão de Valores**: A função `split_values()` divide os valores separados por ';' em uma lista de strings.
- **Extração de Arquivo e Link**: A função `extract_file_and_link()` extrai o nome do arquivo e o link de uma string no formato "(nome_do_arquivo link)".
- **Conversão para JSON**: Os dados processados são convertidos em um dicionário Python e serializados em formato JSON utilizando a biblioteca json.
- **Escrita em Arquivo**: O JSON resultante é escrito em um arquivo chamado 'processos.json'.

## Estrutura do JSON Gerado (processos.json)

O arquivo JSON gerado terá a seguinte estrutura:

```json
[
    {
        "ID do Processo": int,
        "Nome do Processo": string,
        "Descrição": string,
        "Atividades": [string],
        "Fluxo de Sequência (BPMN)": {"descricao": string, "url": string},
        "Participantes": [string],
        "Documentos Relacionados": [string],
        "Setor": string,
        "Unidade": string,
        "Relações de Processos": [string],
        "Mapeado?": string,
        "Data de Criação": string,
        "Última Atualização": string
    },
    ...
```

## Arquivo index.html

### carregarDadosJSON()
- Esta função carrega os dados do arquivo JSON `processos.json`.
- Utiliza a função `fetch()` para obter os dados do arquivo JSON.
- Os dados são armazenados na variável `processos`.
- Chama outras funções para preencher o filtro de setores, preencher a lista de processos e exibir o gráfico geral.

### preencherFiltroSetor()
- Preenche o filtro de setores com base nos setores presentes nos dados dos processos.
- Adiciona opções ao elemento `select` com o id `sector`.

### preencherListaProcessos()
- Preenche a lista de processos no lado esquerdo da tela.
- Cria elementos HTML para cada processo e os adiciona à lista.

### exibirDetalhesProcesso(processo)
- Exibe os detalhes de um processo selecionado.
- Atualiza a seção de detalhes do processo com informações como nome, descrição, atividades, etc.
- Renderiza o gráfico de relações para o processo selecionado.

### abrirBPMN(url) e abrirDocumento(url)
- Funções auxiliares para abrir links para o diagrama de fluxo de sequência BPMN e documentos relacionados em uma nova guia do navegador.

### aplicarFiltros()
- Aplica os filtros selecionados pelo usuário aos dados dos processos.
- Filtra os processos com base na data de criação, setor e termo de pesquisa.
- Chama a função `atualizarListaProcessos()` para atualizar a lista de processos com os resultados filtrados.

### atualizarListaProcessos(processosFiltrados)
- Atualiza a lista de processos com os resultados filtrados após aplicar os filtros.
- Limpa a lista atual e preenche-a com os processos filtrados.

### Event Listeners
- Os event listeners são adicionados aos elementos de entrada de filtro (data de início, data de término, setor e termo de pesquisa) para acionar a função `aplicarFiltros()` quando houver mudanças nesses elementos.

### window.onload
- Chama a função `carregarDadosJSON()` quando a página é carregada completamente para inicializar o aplicativo.

## Créditos
- Cytoscape.js: [https://js.cytoscape.org/](https://js.cytoscape.org/)

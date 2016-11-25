# S3 Fetcher

Projeto criado para extrair arquivos da Amazon S3.

## Como Usar

Passo a passo de como utilizar o projeto.

### Criando o `.env`

Crie um arquivo `.env` no mesmo diretório do `settings.py`. Esse arquivos deve conter as variáveis de ambiente usados pelo projeto.
Um exemplo de `.env` está no arquivo `.env-example`.

```
AWS_KEY=key
AWS_SECRET=secret
BUCKET_NAME=bucket
AWS_DIR=documentos
DOWNLOAD_PATH=downloads
PROCESSOS_FILE='processos.txt'
```

### Criando o `processos.txt`.

Para rodar o projeto é necessário criar um arquivo contendo os números dos processos que serão buscados no S3.
O nome desse aquivo deve ser salvo na variável `PROCESSOS_FILE` no `.env'.

Exemplo de `processos.txt`

```
80036972820168050191
80005962020168050114
80012264520168050189
80007402420168050104
80003792820168050194
08527360620168205001
```

### Rodando o projeto

1 - Instalar as requisitos do projeto:

```
pip install -r requirements.txt
```

2 - Rodar o `fetcher.py`

```
python app/fetcher.py
```


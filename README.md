<br id="topo">

<h1 align="center">Projeto IA - Python</h1>

> **Projeto Integrador 6º Semestre ADS - 2023**

<p align="center">
    <a href="#objetivo">Informações</a> |
    <a href="#tecnologias">Tecnologias</a>
</p>

<span id="objetivo">

## 🚀 Informações

> **Projeto em desenvolvimento**

Esse repositório contém os programas desenvolvidos em Python para o Projeto IA (Projeto integrador do grupo Codelab da FATEC de São José dos Campos). As outras partes que compõe esse projeto podem ser encontrados no repostório pai [clicando aqui](https://github.com/CodeLabFatec/ProjetoIA).

<br />

> Estratégia de branches e commits

As branches e commits desse projeto seguem o seguinte padrão estabelecido pelo [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/) e com exemplos de utilização detalhados [neste repositório](https://github.com/iuricode/padroes-de-commits).

<br>

> Instalação

1. Clone o repositório:
    ```bash
    git clone https://www.github.com/CodeLabFatec/ProjetoIA-Python.git
    ```

2. Entre no diretório do projeto:
    ```bash
    cd ProjetoIA-Python
    ```

### Aplicação IA


Para instalar e executar o projeto siga as instruções abaixo:


1. Para instalar as dependências:
    ```bash
    cd ia

    pip install -r requirements.txt
    ```
2. Crie uma cópia do arquivo `.env.example` chamado `.env`:
   ```bash
   cd src

   cp .env.example .env
   ```

3. Abra o arquivo `.env` e insira as informações de conexão com o banco de dados:
    ```plaintext
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_DATABASE=
    ```

4. Para rodar a aplicação IA digite abaixo:
    ```bash
    python main.py
    ```

### Aplicação Flask

Para instalar e executar o projeto siga as instruções abaixo:

1. Para instalar as dependências:
    ```bash
    cd flask/src

    pip install -r requirements.txt
    
    python3 -m venv env
    ```

2. Crie uma cópia do arquivo `.env.example` chamado `.env`:
   ```bash
   cp .env.example .env
   ```

3. Abra o arquivo `.env` e insira as informações de conexão com o banco de dados:
    ```plaintext
    FLASK_ENV=
    LOGGING_LEVEL=
    DATABASE_URL=
    ```

4. Para rodar a aplicação Flask digite abaixo:
    ```bash
    startdev.bat
    ```

<br>

<span id="tecnologias">

## 🛠️ Tecnologias

Foram usadas as seguintes ferramentas, linguagens e tecnologias para a execução do projeto:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

<br />

→ [Voltar ao topo](#topo)

<br>

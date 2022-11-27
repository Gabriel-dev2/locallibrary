# Locallibrary

# (English)

## Overview

- This is a repository for a sample django's project for studies

## Requirements
- Python 3.10 
- (Optional) pipenv

## Instructions to execute this project
**To execute this project is needed the installation of some dependencies:**

### (Option 1) To execute this project directly using python you need to install django framework
- In case you don't have pip installed, you can follow this tutorial in the link
    [pip doc](https://pip.pypa.io/en/stable/installation/)

**To install django use this command:**
        
        pip install django

**After the installation you can now run the project using the following command on terminal linux:**

        python3 manage.py runserver

**Or on windows you can use this:**

        py -3 manage.py runserver

### (Option 2) To execute the project using a virtualenv you should install pipenv

**To install pipenv:**

        pip install pipenv

**To install Pipfile's dependencies:**

        pipenv install --dev

**To execute the project using pipenv:**

        pipenv run python manage.py runserver

### (Option 3) Run project using docker:


**Docker build image command:**
        
        docker build -t "locallibrary:Dockerfile" . 

**Run created docker image:**

        docker run -p 8000:8000 locallibrary:Dockerfile



# (Portugês)(Brasil)

## Visão geral

- Este é um repositório de exemplo para um projeto de estudos do django

## Requisitos
- Python 3.10 
- (Opicional) pipenv

## Instruções para executar este projeto
**Para executar este projeto é necessário a instalação de algumas dependências:**

### (Opcional 1) Para executar este projeto diretamente usando python você precisa instalar o framework django
- No caso de você não ter o pip isntalado, você pode seguir o tutorial que está nesse link
    [pip doc](https://pip.pypa.io/en/stable/installation/)

**Para instalar o django use este comando:**
        
        pip install django

**Após a instalação você já pode executar o projeto usando o seguinte comando no terminal linux:**

        python3 manage.py runserver

**Ou no windows você pode usar este comando:**

        py -3 manage.py runserver

### (Opção 2) Para executar o projeto usando um ambiente virtual (virtualenv) você precisa instalar o pipenv

**Para instalar o pipenv:**

        pip install pipenv

**Para instalar as dependências que estão no Pipfile:**

        pipenv install --dev

**Para executar o projeto usando o pipenv:**

        pipenv run python manage.py runserver

### (Opção 3) Execute o projeto usando Docker:


**Comando para criação de imagem Docker do projeto:**
        
        docker build -t "locallibrary:Dockerfile" . 

**Executar a imagem Docker criada como um container Docker:**

        docker run -p 8000:8000 locallibrary:Dockerfile


## Authors

* **Gabriel Lucas** - *Initial work* - [Gabriel](mailto:gabriel23costalima@outlook.com)
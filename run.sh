#!/bin/bash

# Parar o script se algo falhar
set -e

VENV_DIR="venv"

# Criar ambiente virtual se não existir
if [ ! -d "$VENV_DIR" ]; then
  echo "Criando ambiente virtual..."
  python3 -m venv $VENV_DIR
fi

# Ativar o venv
source $VENV_DIR/bin/activate

# Instalar pacotes
echo "Instalando pacotes do requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# Verificar se o .env existe
if [ ! -f ".env" ]; then
  echo "Arquivo .env não encontrado! Crie um com as variáveis ORACLE_USERNAME, ORACLE_PASSWORD e ORACLE_DSN."
  exit 1
fi

# Rodar o projeto
echo "Executando main.py..."
python main.py

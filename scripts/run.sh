#!/bin/bash

set -e

VENV_DIR="venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "Criando ambiente virtual..."
  python3 -m venv $VENV_DIR
fi

source $VENV_DIR/bin/activate

echo "Instalando pacotes do requirements.txt..."
pip install --upgrade pip
pip install -r ../requirements.txt

if [ ! -f "../.env" ]; then
  echo "Arquivo .env não encontrado! Crie um usando o env-example como modelo"
  exit 1
fi

echo "Executando main.py..."
python ../src/main.py

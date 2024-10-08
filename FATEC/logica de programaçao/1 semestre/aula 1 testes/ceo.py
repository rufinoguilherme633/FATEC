# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_URihy2uBXq8j8MRAclLysxc9nRYm1Ac
"""

import json;
import numpy as np
import requests


def verificarCep(cep):
  url = f'https://viacep.com.br/ws/{cep}/json/'
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return {"erro": "CEP não encontrado"}

pessoa = {
    "nome":None,
    "idade":None,
    "cep":None
}
pessoas = np.array([])

nome = input("Digite seu nome");
idade = int(input("Qual a sua idade"));
cep = input("qual o cep");

cepValidado = verificarCep(cep)

print(f"Olá {nome}, você tem {idade} anos e mora no {cepValidado.get('logradouro')}")
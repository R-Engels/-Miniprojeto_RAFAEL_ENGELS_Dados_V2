import csv
from datetime import datetime
import matplotlib.pyplot as plt

# ==============================================================================
# SPRINT 1: IMPORTAÇÃO DOS DADOS
# Lógica: Realiza a leitura e extração estruturada do CSV nativamente por DictReader
# ==============================================================================
caminho_arquivo = 'Base Varejo.csv'
registros = []

with open(caminho_arquivo, mode='r', encoding='utf-8') as f:
    leitor = csv.DictReader(f, delimiter=';')
    for linha in leitor:
        # Remoção de chaves ou colunas vazias geradas por delimitadores extras no CSV
        linha_limpa = {k: v for k, v in linha.items() if k is not None and k != ''}
        registros.append(linha_limpa)

total_registros_inicial = len(registros)
colunas = list(registros[0].keys()) if total_registros_inicial > 0 else []



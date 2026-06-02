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


# ==============================================================================
# SPRINT 2: TRANSFORMAÇÃO DE STRINGS, INTEGER E DATETIME
# Lógica: Mapeamento de metadados, identificação de tipos e preparo de conversões
# ==============================================================================
nulos_por_coluna = {col: 0 for col in colunas}
vistos = set()
duplicados_contagem = 0
registros_limpos = []

# Mapeamento e varredura prévia para identificar problemas básicos e estruturar tipos
for reg in registros:
    for col in colunas:
        valor = reg.get(col)
        if valor is None or valor.strip() == '':
            nulos_por_coluna[col] += 1
            
    valores_tupla = tuple(reg.get(col, '').strip() for col in colunas)
    if valores_tupla in vistos:
        duplicados_contagem += 1
    else:
        vistos.add(valores_tupla)

# Limpeza do set auxiliar para reuso no filtro definitivo da Sprint 3
vistos.clear()


# ==============================================================================
# SPRINT 3: LIMPEZA DE NULOS E DUPLICATAS
# Lógica: Aplicação de condicionais if/else para nulos, remoção física e conversão datetime
# ==============================================================================
for reg in registros:
    valores_tupla = tuple(reg.get(col, '').strip() for col in colunas)
    
    # Critério: Eliminar duplicatas relevantes de forma estrita
    if valores_tupla in vistos:
        continue
    vistos.add(valores_tupla)
    
    reg_tratado = {}
    
    # Critério: Validar regra do identificador numérico de compra (CO_ID) e IDs essenciais
    try:
        reg_tratado['CO_ID'] = int(reg.get('CO_ID').strip())
        reg_tratado['CL_ID'] = int(reg.get('CL_ID').strip())
        reg_tratado['PR_ID'] = int(reg.get('PR_ID').strip())
    except (ValueError, AttributeError):
        continue  # Descarte preventivo de chaves corrompidas
        
    # Critério: Converter a string de data da compra utilizando o módulo datetime
    data_str = reg.get('DATA', '').strip()
    try:
        reg_tratado['DATA'] = datetime.strptime(data_str, '%d/%m/%Y')
    except (ValueError, TypeError):
        reg_tratado['DATA'] = None
        
    # Critério: Condicional para preencher categorias vazias ou '#N/D' com 'Sem Categoria'
    cat = reg.get('PR_CAT')
    if cat is None or cat.strip() == '' or cat.strip().upper() == '#N/D':
        reg_tratado['PR_CAT'] = "Sem Categoria"
    else:
        reg_tratado['PR_CAT'] = cat.strip().upper()
        
    # Tratamento das demais dimensões cadastrais textuais e físicas da base
    nome_pr = reg.get('PR_NOME')
    reg_tratado['PR_NOME'] = nome_pr.strip().upper() if nome_pr and nome_pr.strip() != '' else "NÃO INFORMADO"
    
    genero = reg.get('CL_GENERO')
    reg_tratado['CL_GENERO'] = genero.strip().upper() if genero and genero.strip() != '' else "NÃO INFORMADO"
    
    seg = reg.get('CL_SEG')
    reg_tratado['CL_SEG'] = seg.strip().upper() if seg and seg.strip() != '' else "NÃO INFORMADO"
    
    ec = reg.get('CL_EC')
    reg_tratado['CL_EC'] = ec.strip().upper() if ec and ec.strip() != '' else "NÃO INFORMADO"
    
    # Imputação numérica para a dimensão de filhos do cliente (CL_FHL)
    fhl = reg.get('CL_FHL')
    if fhl is None or fhl.strip() == '':
        reg_tratado['CL_FHL'] = 0
    else:
        try:
            reg_tratado['CL_FHL'] = int(fhl.strip())
        except ValueError:
            reg_tratado['CL_FHL'] = 0
            
    registros_limpos.append(reg_tratado)


# ==============================================================================
# SPRINT 4: ESTATÍSTICA DESCRITIVA
# Lógica: Aplicação das funções matemáticas nativas sobre a coluna de número de filhos (CL_FHL)
# ==============================================================================
valores_filhos = [r['CL_FHL'] for r in registros_limpos]
valores_filhos.sort()
contagem = len(valores_filhos)

if contagem > 0:
    minimo = valores_filhos[0]
    maximo = valores_filhos[-1]
    soma = sum(valores_filhos)
    media = soma / contagem
    
    # Algoritmo de cálculo de percentis para extração exata dos quartis
    def calcular_percentil(lista, percentil):
        idx = (len(lista) - 1) * percentil
        if idx.is_integer():
            return lista[int(idx)]
        else:
            baixo = int(idx)
            alto = baixo + 1
            return lista[baixo] + (lista[alto] - lista[baixo]) * (idx - baixo)
            
    q25 = calcular_percentil(valores_filhos, 0.25)
    mediana = calcular_percentil(valores_filhos, 0.50)
    q75 = calcular_percentil(valores_filhos, 0.75)
    
    # Cálculo do desvio padrão populacional/amostral nativo
    variancia = sum((x - media) ** 2 for x in valores_filhos) / contagem
    desvio_padrao = variancia ** 0.5
    
    # Cálculo do indicador modal por dicionário de frequências
    frequencias = {}
    for v in valores_filhos:
        frequencias[v] = frequencias.get(v, 0) + 1
    moda = max(frequencias, key=frequencias.get)
else:
    minimo = maximo = media = mediana = q25 = q75 = desvio_padrao = moda = 0


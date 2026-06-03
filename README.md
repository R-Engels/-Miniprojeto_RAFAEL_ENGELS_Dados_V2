# Análise Exploratória de Dados - Base Varejo
**Aluno:** Rafael Engels | **Turma:** T2

Este projeto realiza de forma nativa e estruturada a extração, limpeza de strings inválidas, tratamento de duplicatas, análise estatística descritiva e plotagem de dados da base de varejo utilizando Python.

---

## 📂 Arquivos Incluídos no Repositório
* `Base Varejo.csv` - Base bruta original posicionada na raiz do projeto.
* `analise_varejo.py` - Script Python principal contendo a inteligência de processamento dividida por sprints.
* `df_limpo.csv` - Arquivo final gerado após a execução dos tratamentos e filtragens.
* `1._compras_por_genero.png` - Gráfico de barras contendo a volumetria transacionada por gênero.
* `2._top_categorias.png` - Gráfico de pizza contendo o market share das top 5 categorias de produtos.

---

## 🛠️ Instruções de Execução
1. Certifique-se de possuir o Python instalado em seu ambiente.
2. Instale o pacote Matplotlib para renderização das imagens:
   ```bash
   pip install matplotlib

Bloco de Conclusões e Insights (Reflexão Teórica)

1. Qualidade Cadastral Inicial e Higienização
Durante o processo de análise de consistência da base de dados, foram identificadas e expurgadas 96.553 linhas duplicadas idênticas. Adicionalmente, detetou-se a presença de registos corrompidos contendo a string de erro #N/D no campo de categorias de produtos (PR_CAT). A estratégia adotada envolveu a interceção e o tratamento condicional destas anomalias, substituindo-as pelo rótulo padrão "Sem Categoria". Esta higienização garantiu a integridade das transações para as fases seguintes sem distorcer as métricas do ERP.

2. Análise Descritiva do Perfil de Clientes (Coluna CL_FHL)
A modelação estatística descritiva aplicada à variável CL_FHL (número de filhos) revelou que a mediana e a moda encontram-se fixadas em 0, enquanto a média calculada é de 1.15. O cálculo do desvio padrão resultou em 1.42, com o terceiro quartil (75%) posicionado em 2.0. Estes parâmetros evidenciam que o maior volume de vendas do estabelecimento está concentrado em clientes sem filhos registados, exibindo uma dispersão moderada para agregados familiares de até 4 filhos.

3. Dinâmica de Mercado e Dominância de Categorias
A agregação dos dados volumétricos por categoria de negócio revelou que a categoria "ALIMENTOS" assume a liderança absoluta em volume de vendas, seguida de forma estreita por "HIGIENE" e "LIMPEZA". Este comportamento estatístico traça o perfil do estabelecimento como um varejo de bens de consumo essenciais de alta recorrência.

4. Avaliação Crítica e Limitações da Base
Embora a base higienizada emita relatórios operacionais precisos, nota-se a ausência crítica de dados financeiros de margens e preços unitários. Esta lacuna estrutural impossibilita o cálculo de faturamento líquido ou o cruzamento de rentabilidade por segmento. Recomenda-se a inclusão destes campos em sprints futuras para viabilizar análises preditivas de receita.
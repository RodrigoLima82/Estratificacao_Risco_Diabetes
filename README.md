# Estratificando riscos usando registros eletrônicos de pacientes diabéticos

Tipicamente, dez por cento dos pacientes geram cerca de 70% das despesas de saúde (dado dos EUA). Ao identificar quais as pessoas são de alto risco ou a probabilidade de se tornarem de alto risco, as equipes de saúde podem intervir para melhorar seus resultados e reduzir os respectivos custos de saúde.

Um dos problemas mais comuns e que refletem as inadequações no sistema de saúde são as readmissões hospitalares. Nos Estados Unidos sozinho, o tratamento de pacientes diabéticos readmitidos excede 300 milhões de dólares por ano (https://www.diabetes.org/). A readmissão hospitalar é uma das principais preocupações no tratamento do diabetes, com milhões de dólares sendo gastos no tratamento de pacientes diabéticos que precisam ser readmitidos em um hospital após receberem alta. 

Identificação precoce de pacientes que enfrentam um alto risco de readmissão pode permitir que os profissionais de saúde conduzam investigações adicionais e possivelmente impeçam futuras readmissões.
Sendo assim, proposta aqui é utilizar os registros eletrônicos de dados médicos dos pacientes, tais como: resultados dos exames, nível de insulina, diagnósticos de outras doenças, etc... a fim de prever se um paciente pode ou não ser readmitido. Aliás, iremos além: vamos identificar os pacientes diabéticos de alto risco por meio de estratificação de risco de registros médicos eletrônicos.

Já estamos vivendo uma “nova medicina” que está sendo “guiada” pelo processamento de um grande volume de informações através de algoritmos poderosos de “machine learning”, uma das áreas da “inteligência artificial”!
Para isso, vamos treinar e comparar o desempenho de alguns algoritmos de aprendizado de máquina e decidir qual deles usar para prever o risco de readmissão para o paciente.

Usarei o melhor modelo treinado para estratificar a população em três grupos de risco:

- Alto Risco (probabilidade de readmissão > 0,7)
- Risco Médio (0,3 < Probabilidade de readmissão < 0,7)
- Baixo Risco (probabilidade de readmissão < 0,3)

O conjunto de dados, "Diabetes 130-US hospitals for years 1999-2008", foi baixado do UCI Machine Learning Repository: Diabetes 130-US hospitals for years 1999-2008 Data Set

Os dados representam 10 anos (1999-2008) de atendimento clínico em 130 hospitais dos EUA e redes de distribuição integradas com 100.000 observações e 50 recursos (variáveis) que representam os registros eletrônicos com resultados de exames dos pacientes e dados sobre cada hospital. Descrição completa do trabalho:

Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records

Créditos: Data Science Academy - https://www.datascienceacademy.com.br/

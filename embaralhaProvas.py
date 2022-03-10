from operator import index
import random
import string
import os


def buscaEstados(dic):
    return list(dic.keys())


def buscaCapitais(dic):
    return list(dic.values())


def completaEnunciado(numQ, uf):
    return '{0}. Qual é a capital do(e) {1}?\n'.format(numQ, uf)


def completaRespostas(letras, listaRespQuestao):
    valorResp = ''
    i = 0
    for resp in listaRespQuestao:
        valorResp += '\t{0}. {1}\n'.format(letras[i], resp)
        i += 1
    valorResp += '\n'
    return valorResp

def completaCabecalho(nCab):
    return 'Nome:\n\nData:\n\nPeríodo:\n\n\t\t\tQuiz - Estados e Capitais (Versão {0})\n\n'.format(nCab)


def completaGabarito(respCorr, letras, listaRespQuestao, nQue):
    indexL = listaRespQuestao.index(respCorr)
    letraCerta = letras[indexL]
    gabarito = str(nQue) + '. ' + letraCerta + '\n'
    return gabarito


def criaPasta(pasta):
    if os.path.exists(pasta):
        for fileName in os.listdir(pasta):
            os.unlink(os.path.join(pasta, fileName))
    else:
        os.makedirs(pasta)


def gravaArquivo(pasta, arq, info):
    with open(os.path.join(pasta, arq), 'w') as fileArq:
        fileArq.write(info)


strNumQuestoes = 3
strNumRespostas = 5
strNumProvas = 4

numQuestoes = 3
numRespostas = 5
numProvas = 4

letras = list(string.ascii_uppercase[:numRespostas])

capitaisEstados = { 'Acre (AC)': 'Rio Branco',
                    'Amapá (AP)': 'Macapá',
                    'Amazonas (AM)': 'Manaus',
                    'Pará (PA)': 'Belém',
                    'Rondônia (RO)': 'Porto Velho',
                    'Roraima (RR)': 'Boa Vista',
                    'Tocantins (TO)': 'Palmas',
                    'Alagoas (AL)': 'Maceió',
                    'Bahia (BA)': 'Salvador',
                    'Ceará (CE)': 'Fortaleza',
                    'Maranhão (MA)': 'São Luís',
                    'Paraíba (PB)': 'João Pessoa',
                    'Pernambuco (PE)': 'Recife',
                    'Piauí (PI)': 'Teresina',
                    'Rio Grande do Norte (RN)': 'Natal',
                    'Sergipe (SE)': 'Aracaju',
                    'Distrito Federal (DF)': 'Brasília',
                    'Goiás (GO)': 'Goiânia',
                    'Mato Grosso (MT)': 'Cuiabá',
                    'Mato Grosso do Sul (MS)': 'Campo Grande',
                    'Espírito Santo (ES)': 'Vitória',
                    'Minas Gerais (MG)': 'Belo Horizonte',
                    'Rio de Janeiro (RJ)': 'Rio de Janeiro',
                    'São Paulo (SP)': 'São Paulo',
                    'Paraná (PR)': 'Curitiba',
                    'Santa Catarina (SC)': 'Florianópolis',
                    'Rio Grande do Sul (RS)': 'Porto Alegre'}

camGabarito = './Gabarito'
camProva = './Prova'

criaPasta(camGabarito)
criaPasta(camProva)

perguntasDefinitivo = []
estados = buscaEstados(capitaisEstados)
estadosSelecionados = random.sample(estados, k=numQuestoes)

for estado in estadosSelecionados:
    respostaCorreta = capitaisEstados[estado]
    capitais = buscaCapitais(capitaisEstados)
    capitais.remove(respostaCorreta)
    respostasLista = random.sample(capitais, k=numRespostas - 1)
    respostasLista.append(respostaCorreta)

    perguntasParcial = []
    perguntasParcial.append(estado)
    perguntasParcial.append(respostasLista)

    perguntasDefinitivo.append(perguntasParcial)

nP = 1
for nProvas in range(numProvas):
    nQ = 1
    versaoProva = random.sample(perguntasDefinitivo, k=len(perguntasDefinitivo))
    strVersao = completaCabecalho(nP)
    strGabarito = ''
    for nQuestoes  in versaoProva:
        strQuestao = completaEnunciado(nQ, nQuestoes[0])
        listaRespQuestao = []
        listaRespQuestao = random.sample(nQuestoes[1], k=len(nQuestoes[1]))
        strResposta = completaRespostas(letras, listaRespQuestao)
        strVersao += strQuestao + strResposta

        respostaCorreta = capitaisEstados[nQuestoes[0]]
        strGabarito += completaGabarito(respostaCorreta, letras, listaRespQuestao, nQ)
        nQ += 1
    
    gravaArquivo(camProva, 'Prova_versao_' + str(nP) + '.txt', strVersao)
    gravaArquivo(camGabarito, 'Gabarito_versao_' + str(nP) + '.txt', strGabarito)
    nP += 1
from operator import index
import random
import string
import os


def buscaEstados(dic):
    '''retorna uma lista dos estados do brasil'''
    return list(dic.keys())


def buscaCapitais(dic):
    '''retorna uma lista com as capitais do brasil'''
    return list(dic.values())


def completaEnunciado(numQ, uf):
    '''formata string do enunciado das questoes'''
    return '{0}. Qual é a capital do(e) {1}?\n'.format(numQ, uf)


def completaRespostas(letras, listaRespQuestao):
    '''formata string das respostas das questoes'''
    valorResp = ''
    i = 0
    for resp in listaRespQuestao:
        valorResp += '\t{0}. {1}\n'.format(letras[i], resp)
        i += 1
    valorResp += '\n'
    return valorResp

def completaCabecalho(nCab):
    '''formata string do cabecalho da prova'''
    return 'Nome:\n\nData:\n\nPeríodo:\n\n\t\t\tQuiz - Estados e Capitais (Versão {0})\n\n'.format(nCab)


def completaGabarito(respCorr, letras, listaRespQuestao, nQue):
    '''formata string do gabarito da prova'''
    indexL = listaRespQuestao.index(respCorr)
    letraCerta = letras[indexL]
    gabarito = str(nQue) + '. ' + letraCerta + '\n'
    return gabarito


def criaPasta(pasta):
    '''cria pastas para salvar arquivos ou deleta os arquivos existentes nelas'''
    if os.path.exists(pasta):
        for fileName in os.listdir(pasta):
            os.unlink(os.path.join(pasta, fileName))
    else:
        os.makedirs(pasta)


def gravaArquivo(pasta, arq, info):
    '''salva arquivos no formato txt'''
    with open(os.path.join(pasta, arq), 'w') as fileArq:
        fileArq.write(info)


def verificaInputs(msg, limite):
    '''Verifica se o usuario esta digitando apenas numeros'''
    boolValor = True
    while boolValor:
        valor = input(msg)
        if valor.isnumeric():
            if int(valor) > 0 and int(valor) <= limite:
                return int(valor)


# lista com todos Estados e Capitais
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

# variavel para iniciar a aplicação
iProg = '1'
while iProg == '1': # loop para rodar aplicação
    iProg = input('Digite 1 para geras as versões das provas ou qualquer tecla para sair: ')
    if iProg == '1':
        camGabarito = './Gabarito' # caminho para salvar arquivos do Gabarito
        camProva = './Prova' # caminho para salvar arquivos da Prova

        # input para usuario digitar informações
        numQuestoes = verificaInputs('Digite quantas questões terá na prova: ', 27)
        numRespostas = verificaInputs('Digite quantas respostas terá cada questão: ', 27)
        numProvas = verificaInputs('Digite quantas versões terá de cada prova: ', 999999)

        # cria caminho ou deleta arquivos dentro do diretorio
        criaPasta(camGabarito)
        criaPasta(camProva)

        # lista com sequencia de letras
        letras = list(string.ascii_uppercase[:numRespostas])

        perguntasDefinitivo = [] # instancia lista de perguntas
        estados = buscaEstados(capitaisEstados) # carrega lista com estados 
        estadosSelecionados = random.sample(estados, k=numQuestoes) # random dos estados conforme 
        # preenchido pelo usuário

        for estado in estadosSelecionados: # loop nos estados selecionados
            respostaCorreta = capitaisEstados[estado] # carrega resposta correta
            capitais = buscaCapitais(capitaisEstados) # carrega lista com capitais
            capitais.remove(respostaCorreta) # remove resposta correta da lista de capitais
            respostasLista = random.sample(capitais, k=numRespostas - 1) # randon das capitais
            # conforma preenchido pelo usuário
            respostasLista.append(respostaCorreta) # retonar resposta correta na lista de capitais

            perguntasParcial = [] # instancia variavel de perguntas parcial
            perguntasParcial.append(estado) # adiciona estado na lista parcial
            perguntasParcial.append(respostasLista) # adiciona respostas na lista parcial

            perguntasDefinitivo.append(perguntasParcial) # adiciona lista parcial na definitiva

        nP = 1 # contador numero de provas
        for nProvas in range(numProvas): # loop nas versões de provas
            nQ = 1 # contador numero de questões
            versaoProva = random.sample(perguntasDefinitivo, k=len(perguntasDefinitivo)) # altera
            # sequencia da ordens das questoes
            strVersao = completaCabecalho(nP) # carrega padrao de cabeçalho
            strGabarito = '' # instancia string gabarito
            for nQuestoes  in versaoProva: # loop nas perguntas da versão vigente
                strQuestao = completaEnunciado(nQ, nQuestoes[0]) # carrega padrão enunciado
                listaRespQuestao = [] # instancia Lista de resposta da questao
                listaRespQuestao = random.sample(nQuestoes[1], k=len(nQuestoes[1])) # altera ordem
                # das respostas da questão
                strResposta = completaRespostas(letras, listaRespQuestao) # carrega padrao de resposta
                strVersao += strQuestao + strResposta # junta questao e reposta na string

                respostaCorreta = capitaisEstados[nQuestoes[0]] # carrega resposta correta da questao
                strGabarito += completaGabarito(respostaCorreta, letras, listaRespQuestao, nQ)
                # carrega padrão gabarito
                nQ += 1
            
            gravaArquivo(camProva, 'Prova_versao_' + str(nP) + '.txt', strVersao)
            # grava arquivos prova
            gravaArquivo(camGabarito, 'Gabarito_versao_' + str(nP) + '.txt', strGabarito)
            # grava arquivos gabarito
            nP += 1
        
        print('Arquivos gerados.')

    else:
        print('Até mais!')
        break
#coding: iso8859-1

import webbrowser 
from os.path import abspath

class Relatorio(object):
  
    
    __html = None
    __tabela = None

    __cod = []
    __quantidade = []
    __unidade = []
    __descricao = []
    __copia = []
    __valor_unit = []
    empresa = f'HEC'
    cliente = f'Cliente não informado'
    texto = f'   O escritor de IA da Smodin é fácil de usar. Forneça seu prompt com algumas palavras e gere facilmente artigos e ensaios livres de plágio, exclusivos e de alta qualidade em minutos. Digite o que deseja escrever em uma ou duas frases pequenas, com pelo menos os caracteres mínimos necessários para que a ferramenta funcione, e clique no botão gerar texto. Nosso AI Writer criará o conteúdo que você pode revisar, editar em partes ou usar apenas as partes que você gostou, continuar aprimorando o texto original ou continuar gerando a partir da semente original. Este gerador de texto de IA fácil de usar pode ser usado por todos os níveis de ensino para produzir ensaios e artigos e também para redação, marketing, criação de páginas, redação de parágrafos, manchetes, listas e muito mais. Não há necessidade de software ou habilidades de programação.'
    box = ''
    
    def __init__(self, local = abspath("modelo_relatorio.html")):
        arq = open(local, "r")
        self.__html = "<LINHA>".join(arq.readlines())
        arq.close()

    def setDados(self, cod, qtd, unid, desc, copia, valor_unit):
        self.__cod.append(cod)
        self.__quantidade.append(int(qtd))
        self.__unidade.append(unid)
        self.__descricao.append(desc)
        self.__copia.append(copia)
        self.__valor_unit.append(float(valor_unit))

    def __getTabela(self):
        self.__tabela = self.__html[self.__html.find("{{LOOP_IN}}"):self.__html.find("{{LOOP_FIM}}")]
        self.__tabela = self.__tabela.replace("{{LOOP_IN}}\n", "")
        self.__tabela = self.__tabela[:self.__tabela.rfind("</tr>")+6]
        self.__html = self.__html.replace(self.__html[self.__html.find("{{LOOP_IN}}"):self.__html.find("{{LOOP_FIM}}")+12],
                                          "{{LOOP_AQUI}}")

    def __setValorTabela(self):
        self.__getTabela()
        temp = modelo = self.__tabela
        self.__tabela = ""
        for p in range(len(self.__quantidade)):
            temp = temp.replace("{{COD}}", str(self.__cod[p]))
            temp = temp.replace("{{QUANTIDADE}}", str(self.__quantidade[p]))
            temp = temp.replace("{{UNIDADE}}", str(self.__unidade[p]))
            temp = temp.replace("{{DESCRIÇÃO}}", str(self.__descricao[p]))
            temp = temp.replace("{{COPIA}}", str(self.__copia[p]))
            temp = temp.replace("{{VALOR_UNITARIO}}", "%.2f" %self.__valor_unit[p])
            temp = temp.replace("{{TOTAL}}", "%.2f" %(self.__quantidade[p] * self.__valor_unit[p]))
            self.__tabela += temp
            temp = modelo
      
    def __saveDadosHtml(self):
        self.__setValorTabela()
        self.__html = self.__html.replace("{{LOOP_AQUI}}", self.__tabela)
        self.__html = self.__html.replace("{{NOME_DA_EMPRESA}}", self.empresa)
        self.__html = self.__html.replace("{{NOME_DO_CLIENTE}}", self.cliente)
        self.__html = self.__html.replace("{{TEXTO}}", self.texto)
        self.__html = self.__html.replace("{{BOX}}", self.box)
        total = 0
        for p in range(len(self.__quantidade)):
            total += (self.__quantidade[p] * self.__valor_unit[p])
        self.__html = self.__html.replace("{{TOTAL_GERAL}}", "%.2f" %(total))
        self.__html = self.__html.split("<LINHA>")

    def savePDF(self):
        """
        Implementar o salvamento do PDF aqui buscando a não necessidade
        de salvar o HTML.
        """
        self.__saveDadosHtml()
        arq = open("resul.html", "w")
        arq.writelines(self.__html)
        arq.close()
        return

qtd = [1, 2, 3, 4, 5, 6, 7, 8, 9]
unid = ["cx", "unid", "algo", "cx", "unid", "algo", "cx", "unid", "algo"]
desc = ["safsafsadfsadf", ";asrklbjsafoyiasnckf", "asdoynascfklhnasfdkl", "asopfsyadfopasopynsfd",
        "safsafsadfsadf", ";asrklbjsafoyiasnckfhasf", "asdoynascfklhnasfdkl", "asopfsyadfopasopynsfd",
        "Vamos voltar ao nosso quarto. Imagine que temos uma bola de futebol muito especial dentro do quarto. Ela pode reproduzir outras bolas de futebol. Ela possui todo aquele poder e energia. É completamente auto-suficiente não precisando de nada além dela para existir, porque ela é tudo o que existe. Essa bola de futebol é Alguma Coisa Eterna."]
valor = [9, 8, 7, 6, 5, 4, 3, 2, 1, ]
copia = ["safsafsadfsadf", ";asrklbjsafoyiasnckf", "asdoynascfklhnasfdkl", "asopfsyadfopasopynsfd",
        "safsafsadfsadf", ";asrklbjsafoyiasnckfhasf", "asdoynascfklhnasfdkl", "asopfsyadfopasopynsfd",
        "Vamos voltar ao nosso quarto."]
total = ['11', '22', '33', '44', '55', '66', '77', '88', '99']

arq = Relatorio()
for x in range(9):
    arq.setDados(qtd[x], qtd[x], unid[x], copia[x], copia[x], valor[x])
arq.savePDF()

webbrowser.open('documento2.html')  


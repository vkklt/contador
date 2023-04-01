import string
import nltk

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

freq = {}	

with open("domcasmurro.txt", encoding='utf-8') as arq:

    inicio = False
    for linha in arq:
        linha = linha[:-1]
        if linha == "I":
            inicio = True
        if not inicio or linha == "" : continue
        linha = linha.lower()
        for pont in string.punctuation:
            linha = linha.replace(pont,'')
        for palavra in linha.split(" "):
            if palavra in stopwords or len(palavra) < 3 : continue
            if palavra not in freq:
                freq[palavra] = 0
            freq[palavra] += 1

cont = 1 

for chave,valor in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{cont:3} - [{chave}] => {valor}")
    cont += 1
    if cont > 30:
        break

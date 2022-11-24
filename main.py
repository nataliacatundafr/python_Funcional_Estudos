lista=[]
valorLista=[]
media=0

def produtos():
    produto = input("Produto: ")
    lista.append(produto)
produtos()
def valores():
    valor = input("Valor: ")
    valorLista.append(valor)
valores()

def pergunte():
    digite = input("Adiciona: sim ou não: ")
    while digite=="sim":
        produtos()
        valores()
        digite = input("Adiciona: sim ou não: ")
    if digite == "não":
        print(lista+valorLista)

pergunte()






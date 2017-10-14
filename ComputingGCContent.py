def main():
    chain = []
    stringc = ""
    linea = ""
    rosalind = []
    cont = 0
    conttotal = []
    input()
    file = open('rosalind_gc.txt')
    for linea in file.readlines():
        if linea.find('>') == -1:
            stringc = stringc+linea.rstrip('\n')
        else:
            rosalind.append(linea)
            if stringc != "":
                chain.append(stringc)
                stringc = ""
    chain.append(stringc)
    for i in chain:
        for j in range(0,len(i)):
            if i[j] == 'G' or i[j] == 'C':
                cont = cont+1
        conttotal.append(cont/len(i)*100)
        cont = 0
    ordena(rosalind,conttotal)

def ordena(rosalind,conttotal):
    for i in range(0,len(conttotal)-1):
        print("i: ",i)
        for j in range(i+1,len(conttotal)):
            print("j: ",j)
            if conttotal[i] > conttotal[j]:
                aux = conttotal[i]
                conttotal[i] = conttotal[j]
                conttotal[j] = aux
                aux_rosalind = rosalind[i]
                rosalind[i] = rosalind[j]
                rosalind[j] = aux_rosalind
        print("p: ",conttotal)
    print(conttotal,'\n',rosalind)
main()

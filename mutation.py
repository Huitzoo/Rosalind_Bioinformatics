def main():
    chain = []
    count = 0
    file = open('rosalind_hamm.txt')
    for linea in file.readlines():
        chain.append(linea.rstrip('\n'))
    for i in range(0,len(chain[0])):
        if chain[0][i] != chain[1][i]:
            count = count + 1
    print(count)
main()

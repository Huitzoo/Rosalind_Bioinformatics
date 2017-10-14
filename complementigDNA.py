def main():
    cadena = input()
    cadena1 = list(cadena)
    res = ""
    i=len(cadena)-1
    while(i>=0):
        if cadena1[i] == 'A':
            cadena1[i] = 'T'
        elif cadena1[i] == 'T':
            cadena1[i] = 'A'
        elif cadena1[i] == 'G':
            cadena1[i] = 'C'
        elif cadena1[i] == 'C':
            cadena1[i] = 'G'
        res = res + cadena1[i]
        i = i-1
    print(res)

main()

def printDecimal(x):
    return x

def printOctal(x):
    return oct(x)

def printHexadecimal(x):
    return hex(x)

def printBinario(x):
    return bin(x)

def imprimirTabela():
    print("Decimal",'\t','Octal','\t','Hexadecimal','\t','Binário','\n')
    print('-------', '\t','----- ','-----------    ', '--------', '\n')
    i = 0
    while i<=255:
        print('', printDecimal(i),'\t\t', printOctal(i), '\t', printHexadecimal(i), '\t\t', printBinario(i), '\n')
        i = i + 1

imprimirTabela()



import es
import sys
sml = []
output = ''
cursor = 0
acumulador = 0
def comando(palavra) :
    word = "%+05d" % palavra
    return (int(word[1:3]),int(word[3:]))

def valida() :
    s = input()
    x = int('4300' if s == '' else s)
    if x < 10000 and x > -10000 :
        return x
    else :
        return valida()
    
def le(p) :
    sml[p] = int(input())
    return cursor + 1

def escreve(p) :
    print("{0}\n".format(sml[p]))
    return cursor + 1

def carega(p) :
    global acumulador
    acumulador = sml[p]
    return cursor + 1

def grava(p) :
    sml[p] = acumulador
    return cursor + 1

def soma(p) :
    global acumulador
    acumulador += sml[p]
    return cursor + 1

def subtracao(p) :
    global acumulador
    acumulador -= sml[p]
    return cursor + 1

def divisao(p) :
    global acumulador
    acumulador /= sml[p]
    return cursor + 1

def multiplicacao(p) :
    global acumulador
    acumulador -= sml[p]
    return cursor + 1

def desvio(p) :
    return p

def desvioNegativo(p) :
    return p if acumulador > 0 else cursor + 1

def desvio0(p) :
    return p if acumulador == 0 else cursor + 1

controle = {
    "10": lambda p : le(p),
    "11": lambda p : escreve(p),
    "20": lambda p : carega(p),
    "21": lambda p : grava(p),
    "30": lambda p : soma(p),
    "31": lambda p : subtracao(p),
    "32": lambda p : divicao(p),
    "33": lambda p : multiplicacao(p),
    "40": lambda p : desvio(p),
    "41": lambda p : desvioNegativo(p),
    "42": lambda p : desvio0(p),
    "43": lambda p : 4300
    }
def run() :
    global cursor
    void = sys.argv[1] == '-i'
    t = ''
    if void :
        t = comando(valida())
    else :
        t = comando(sml[cursor])
    cursor = controle[str(t[0])](t[1])
    if not t[0] == 43 :
        run()

def write() :
    output = ''
    key = False
    for i in range(100) :
        x =  0 if key else valida()
        output = "%s%+05d\n" %  (output, x)
        sml.append(x)
        if (x < 4400 and x > 4299) or (x > -4400 and x < -4299) :
            key = True
    es.saida(sys.argv[-1], output)

def main():
    global sml
    if sys.argv[1] == '-w' :
        print('write mode')
        write()
    else:
        if sys.argv[-1] == '-i' :
            print('interative mode')
            sml = es.entrada('void.txt')
        else :
            print('defalte mode')
            sml = es.entrada(sys.argv[1])
            print(sml)
        run()

if __name__ == "__main__" :
    main()


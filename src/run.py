import es
import sys
sml = ''
void = sys.argv[1] == '-i' 
if void :
    sml = es.entrada('void.txt')
else :
    sml = es.entrada(sys.argv[1])
cursor = 0
acumulador = 0
def comando(palavra) :
    word = "%+05d" % palavra
    return (int(word[1:3]),int(word[3:]))

def valida() :
    x = int(input())
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

def subtração(p) :
    global acumulador
    acumulador -= sml[p]
    return cursor + 1

def divisão(p) :
    global acumulador
    acumulador /= sml[p]
    return cursor + 1

def multiplicação(p) :
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
    "31": lambda p : subtração(p),
    "32": lambda p : divição(p),
    "33": lambda p : multiplicação(p),
    "40": lambda p : desvio(p),
    "41": lambda p : desvioNegativo(p),
    "42": lambda p : desvio0(p),
    "43": lambda p : 4300
    }
def run() :
    global cursor
    global void
    t = ''
    if void :
        t = comando(valida())
    else :
        t = comando(sml[cursor])
    cursor = controle.get(str(t[0]))(t[1])
    if not t[0] == 43 :
        run()

def main():
    run()

if __name__ == "__main__" :
    main()


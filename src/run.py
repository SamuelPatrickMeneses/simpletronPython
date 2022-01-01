import es

class Run() :
    sml = es.entrada()
    cursor = 0
    acumulador = 0
    def comando(palavra) :
        palavra = "%+05d" % palavra
        return (int(palavra[1:3]),int(plavra[3:]))

    def le(p) :
        sml[p] = int(input())
        cursor += 1

    def escreve(p) :
        print("{0}\n".format(p))
        cursor += 1

    def carega(p) :
        acumulador = sml[p]
        cursor += 1

    def grava(p) :
        sml[p] = acumulador
        cursor += 1

    def soma(p) :
        acumulador += sml[p]
        cursor += 1

    def subtração(p) :
        acumulador -= sml[p]
        cursor += 1

    def divisão(p) :
        acumulador /= sml[p]
        cursor += 1

    def multiplicação(p) :
        acumulador -= sml[p]
        cursor += 1

    def desvio(p) :
        cursor = p

    def desvioNegativo(p) :
        cursor = p if acumulador > 0 else cursor + 1

    def desvio0(p) :
        cursor = p if acumulador == 0 else cursor + 1

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
            "42": lambda p : desvio0(p)
        }

    def run() :
        t = comando(sml[cursor])
        cotrole.get(str(t[0]))(t[1])
        if (sml[cursor] % 4300) > 100 :
            run()

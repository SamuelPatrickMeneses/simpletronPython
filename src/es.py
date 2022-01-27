def entrada(p) :
    leitor = open(p)
    linhas = leitor.readlines()
    for i, linha in enumerate(linhas) :
        linhas[i] = int(linha)
    leitor.close()
    return linhas
def saida(p, out) :
    writer  = open(p, 'w')
    writer.write(out)
    writer.close()

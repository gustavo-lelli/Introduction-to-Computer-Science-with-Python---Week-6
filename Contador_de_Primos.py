def eh_Primo(fator):
    i=2
    counter=0

    while(i<=fator):
        if(fator%i==0):
            counter+=1
        i+=1

    if(counter==1):
        return 1
    else:
        return 0


def n_primos(n):
    qntd=0
    fator=2

    while(fator<=n):
        qntd+=eh_Primo(fator)
        fator+=1

    return qntd;

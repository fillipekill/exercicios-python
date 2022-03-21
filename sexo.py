def is_triangulo(um, dois, tres):
    maior, segundo_menor, menor_de_todos = 0,0,0
    if um <= dois:
        if um <= tres:
            menor_de_todos = um
            if dois <= tres:
                segundo_menor = dois
                maior = tres
            else:
                segundo_menor = tres
                maior = dois

    if dois <= um:
        if dois <= tres:
            menor_de_todos = dois
            if tres <= um:
                segundo_menor = tres
                maior = um
            else:
                segundo_menor = um
                maior = tres

    if tres <= dois:
        if tres <= um:
            menor_de_todos = tres
            if dois <= um:
                segundo_menor = dois 
                maior = um
            else:
                segundo_menor = um
                maior = dois

    if maior <= (segundo_menor + menor_de_todos):
        return True
    else:
        return False
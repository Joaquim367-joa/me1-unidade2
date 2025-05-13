def analisar_numeros(lista):
    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)
    pares = [num for num in lista if num % 2 == 0]
    quantidade_pares = len(pares)

    return media, maior, menor, quantidade_pares

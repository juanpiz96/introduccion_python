texto='esta lloviendo'

resultado={}
for letra in texto:
    if resultado.get(letra):
        resultado[letra]+= 1
    else:
        resultado[letra] = 1
print(resultado)
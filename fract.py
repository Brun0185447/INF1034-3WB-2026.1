def mostra_palavra_rec(palavra):
    if palavra == "":
        return
    print("antes da chamada rec:", palavra)
    mostra_palavra_rec(palavra[:-1])
    print("depois da chamada rec:", palavra)
    return


def mostra_palavra_for(palavra):
    for i in range(len(palavra)):
        #print(i, len(palavra) - i, palavra[:len(palavra) - i])
        print(palavra[:len(palavra) - i])

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

mostra_palavra_for("ola, tudo bem?")

mostra_palavra_rec("ola, tudo bem?")


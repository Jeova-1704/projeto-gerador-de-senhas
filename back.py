# Importando da bliblioteca "Strings" as 'variables' respectivas a letras minusculas, letras maisculas, numeros e caracteres especiais
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
# Importando o metodo choices que embaralha a senha com varios caracteres diferentes para tornala mais segura
from random import choices
# importando uma bliblioteca para copiar a senha para a área de tranferencia
import pyperclip
# importação da bliblioteca de interace grafica
import PySimpleGUI as sg


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Função que avalia os TRUE e FALSE para gerar a senha de acordo com as especificações acima que foram passadas e no final gera a senha que é retornada

def gerar_senha(num_caracteres, letras_maiusculas, letras_minusculas, numeros, simbolos):
    combinacao = ""
    if letras_maiusculas:
        combinacao += ascii_uppercase
    
    if letras_minusculas:
        combinacao += ascii_lowercase
    
    if numeros:
        combinacao += digits

    if simbolos:
        combinacao += punctuation
    num_caracteres = int(num_caracteres)
    senha = ''.join(choices(combinacao, k=num_caracteres))

    return str(senha)

# Avalia o nivel de segurança de uma senha baseada em um sistema de pontuação de 0 a 10, onde 10 é uma senha muito boa e 0 uma senha facil de ser quebrada
#Sitema funciona avaliando em ordem: o tamanho da senha -> se ela tem letras minusculas -> se ela tem letras maisculas -> se ela tem caracteres especiais -> se tem números
def avaliar_seguranca(senha):
    pontos = 0

    if len(senha) <= 5:
        pontos += 0.5
        for carac in senha:
            if carac in ascii_lowercase:
                pontos += 1
                break
        for carac in senha:
            if carac in ascii_uppercase:
                pontos += 1
                break

        for carac in senha:
            if carac in punctuation:
                pontos += 2
                break

        for carac in senha:
            if carac in digits:
                pontos += 2
                break

    elif 5 < len(senha) <= 10:
        pontos += 1
        for carac in senha:
            if carac in ascii_lowercase:
                pontos += 2
                break
        for carac in senha:
            if carac in ascii_uppercase:
                pontos += 2
                break
        for carac in senha:
            if carac in punctuation:
                pontos += 2
                break
        for carac in senha:
            if carac in digits:
                pontos += 2
                break

    elif len(senha) > 10:
        pontos += 2
        for carac in senha:
            if carac in ascii_lowercase:
                pontos += 2
                break
        for carac in senha:
            if carac in ascii_uppercase:
                pontos += 2
                break

        for carac in senha:
            if carac in punctuation:
                pontos += 2
                break

        for carac in senha:
            if carac in digits:
                pontos += 2
                break

    if pontos <= 5:
        return "Senha Fraca"

    elif 5 < pontos <= 7:
        return "Senha intermediaria"

    elif 7 < pontos:
        return "Senha Forte"

        
# Função simples onde copia a varivel de321 senha onde foi guardada a senha gerada e deixa na área de tranferencia
def copiar(senha):
    pyperclip.copy(senha)
    


# Esse código abaixo é um codigo de teste onde ele só funciona se for executado esse arquiov, é uma forma de testar para ver se os comandos acima estão funcionando corretamente
if __name__ == '__main__':
    num_caracteres = 7
    letras_maiusculas = True
    letras_minusculas = True
    numeros = True
    simbolos = False

    senha = gerar_senha(num_caracteres, letras_maiusculas, letras_minusculas, numeros, simbolos)
    print(f'Senha gerada: {senha}')
    nivel_seguranca = avaliar_seguranca(senha)
    print(f'Nível de segurança: {nivel_seguranca}')
    copiar(senha)









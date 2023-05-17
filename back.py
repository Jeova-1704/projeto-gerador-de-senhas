#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
"""Importação das blibliotecas para o projeto"""
#para ter acesso facilitado em variaveis que já possuem letras maisculas, minusculas, números e símbolos
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
# Para embaralhar uma senha com os caracteres escolhidos
from random import choices
# Para copiar a senha para a área d tranferencia
import pyperclip
# Para implmentar interface gráfica
import PySimpleGUI as sg
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
"""Sistema de POO para uma melhor visualização do código e correção e futuras novas implementações"""
#Classe principla onde recebe os códigos em TRUE, FALSE e quantidade de caracteres a ser gerados pela senha
class GeradorSenha:
    def __init__(self, num_caracteres, letras_maiusculas, letras_minusculas, numeros, simbolos):
        self.num_caracteres = int(num_caracteres)
        self.letras_maiusculas = letras_maiusculas
        self.letras_minusculas = letras_minusculas
        self.numeros = numeros
        self.simbolos = simbolos

# Função que gera a senha baseada nas configurações recebidas no __init__
    def gerar_senha(self):
        combinacao = ""
        if self.letras_maiusculas:
            combinacao += ascii_uppercase

        if self.letras_minusculas:
            combinacao += ascii_lowercase

        if self.numeros:
            combinacao += digits

        if self.simbolos:
            combinacao += punctuation

        senha = ''.join(choices(combinacao, k=self.num_caracteres))
        return senha

# Metodo que avalia o nivel de segurança de uma senha baseada em um sistema de segurança do código com pontuação, onde dependendo dos casos recebe um ponto e no final verifica quantos pontos recebeu e dar um nivel de segurança adequado
    @staticmethod
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
            pontos += 2
            for carac in senha:
                if carac in ascii_lowercase:
                    pontos += 1
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
            return "Senha Fraca", "Red"
        elif 5 < pontos <= 7:
            return "Senha intermediaria", "Orange"
        elif 7 < pontos:
            return "Senha Forte", "Green"

# Copia a senha para a área de tranferencia
    @staticmethod
    def copiar(senha):
        pyperclip.copy(senha)


if __name__ == '__main__':
    num_caracteres = 9
    letras_maiusculas = True
    letras_minusculas = True
    numeros = True
    simbolos = False

    gerador = GeradorSenha(num_caracteres, letras_maiusculas, letras_minusculas, numeros, simbolos)
    senha = gerador.gerar_senha()
    print(senha)
    print(gerador.avaliar_seguranca(senha))

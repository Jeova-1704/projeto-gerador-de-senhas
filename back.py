from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choices
import pyperclip
import PySimpleGUI as sg


class GeradorSenha:
    def __init__(self, num_caracteres, letras_maiusculas, letras_minusculas, numeros, simbolos):
        self.num_caracteres = int(num_caracteres)
        self.letras_maiusculas = letras_maiusculas
        self.letras_minusculas = letras_minusculas
        self.numeros = numeros
        self.simbolos = simbolos

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

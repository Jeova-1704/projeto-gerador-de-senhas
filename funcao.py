from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random
import pyperclip

class GeradorSenhas:
    def __init__(self, num_caracteres, letras_maiusculas, letras_minusculas, numeros, simbolos):
        self.num_caracteres = num_caracteres
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

        senha = ''.join(random.choices(combinacao, k=self.num_caracteres))

        return senha

    def avaliar_seguranca(self, senha):
        self.pontos = 0

        if len(senha) <= 5:
            self.pontos += 0.5
            for carac in senha:
                if carac in ascii_lowercase:
                    self.pontos += 1
                    break
            for carac in senha:
                if carac in ascii_uppercase:
                    self.pontos += 1
                    break

            for carac in senha:
                if carac in punctuation:
                    self.pontos += 2
                    break

            for carac in senha:
                if carac in digits:
                    self.pontos += 2
                    break

        elif 5 < len(senha) <= 10:
            self.pontos += 1
            for carac in senha:
                if carac in ascii_lowercase:
                    self.pontos += 2
                    break
            for carac in senha:
                if carac in ascii_uppercase:
                    self.pontos += 2
                    break
            for carac in senha:
                if carac in punctuation:
                    self.pontos += 2
                    break
            for carac in senha:
                if carac in digits:
                    self.pontos += 2
                    break

        elif len(senha) > 10:
            self.pontos += 2
            for carac in senha:
                if carac in ascii_lowercase:
                    self.pontos += 2
                    break
            for carac in senha:
                if carac in ascii_uppercase:
                    self.pontos += 2
                    break

            for carac in senha:
                if carac in punctuation:
                    self.pontos += 2
                    break

            for carac in senha:
                if carac in digits:
                    self.pontos += 2
                    break

        if self.pontos <= 5:
            return 'Senha Fraca'
        elif 5 < self.pontos <= 7:
            return 'Senha Intermediaria'
        elif 7 < self.pontos:
            return 'Senha Forte'
        
    def copiar(self):
        pyperclip.copy(senha)
    



if __name__ == '__main__':
    # uso da classe
    gerador = GeradorSenhas(num_caracteres=4, letras_maiusculas=True, letras_minusculas=True, numeros=False, simbolos=False)
    senha = gerador.gerar_senha()
    print(f'Senha gerada: {senha}')
    nivel_seguranca = gerador.avaliar_seguranca(senha)
    print(f'Nível de segurança: {nivel_seguranca}')
    gerador.copiar()
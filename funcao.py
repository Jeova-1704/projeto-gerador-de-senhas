# Codigo feito com o POO para facilitar a execução e tratar o problema de uma forma mais simples 

# Importando da bliblioteca "Strings" as 'variables' respectivas a letras minusculas, letras maisculas, numeros e caracteres especiais
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
# Importando o metodo choices que embaralha a senha com varios caracteres diferentes para tornala mais segura
from random import choices
# importando uma bliblioteca para copiar a senha para a área de tranferencia
import pyperclip

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Código da parte de POO para criar um codigo que faça a senha, avalie o nivel de seguraça dela e cópie para a área de segurança

#Classe gerador onde fica resposnsavel por toda a parte da senha, avaliação e copia
class GeradorSenhas:
    #recebe TRUE ou FALSE para avaliar se é ou não para gerar com as letras maisculas e minusculas, numeros e simbolos 
    def __init__(self, num_caracteres, letras_maiusculas, letras_minusculas, numeros, simbolos):
        self.__num_caracteres = num_caracteres
        self.__letras_maiusculas = letras_maiusculas
        self.__letras_minusculas = letras_minusculas
        self.__numeros = numeros
        self.__simbolos = simbolos

# Função que avalia os TRUE e FALSE para gerar a senha de acordo com as especificações acima que foram passadas e no final gera a senha que é retornada
    def gerar_senha(self):
        combinacao = ""
        if self.__letras_maiusculas:
            combinacao += ascii_uppercase
    
        if self.__letras_minusculas:
            combinacao += ascii_lowercase
    
        if self.__numeros:
            combinacao += digits

        if self.__simbolos:
            combinacao += punctuation

        senha = ''.join(choices(combinacao, k=self.__num_caracteres))

        return senha

# Avalia o nivel de segurança de uma senha baseada em um sistema de pontuação de 0 a 10, onde 10 é uma senha muito boa e 0 uma senha facil de ser quebrada
#Sitema funciona avaliando em ordem: o tamanho da senha -> se ela tem letras minusculas -> se ela tem letras maisculas -> se ela tem caracteres especiais -> se tem números
    def avaliar_seguranca(self, senha):
        self.__pontos = 0

        if len(senha) <= 5:
            self.__pontos += 0.5
            for carac in senha:
                if carac in ascii_lowercase:
                    self.__pontos += 1
                    break
            for carac in senha:
                if carac in ascii_uppercase:
                    self.__pontos += 1
                    break

            for carac in senha:
                if carac in punctuation:
                    self.__pontos += 2
                    break

            for carac in senha:
                if carac in digits:
                    self.__pontos += 2
                    break

        elif 5 < len(senha) <= 10:
            self.__pontos += 1
            for carac in senha:
                if carac in ascii_lowercase:
                    self.__pontos += 2
                    break
            for carac in senha:
                if carac in ascii_uppercase:
                    self.__pontos += 2
                    break
            for carac in senha:
                if carac in punctuation:
                    self.__pontos += 2
                    break
            for carac in senha:
                if carac in digits:
                    self.__pontos += 2
                    break

        elif len(senha) > 10:
            self.__pontos += 2
            for carac in senha:
                if carac in ascii_lowercase:
                    self.__pontos += 2
                    break
            for carac in senha:
                if carac in ascii_uppercase:
                    self.__pontos += 2
                    break

            for carac in senha:
                if carac in punctuation:
                    self.__pontos += 2
                    break

            for carac in senha:
                if carac in digits:
                    self.__pontos += 2
                    break

        if self.__pontos <= 5:
            return 'Senha Fraca'
        elif 5 < self.__pontos <= 7:
            return 'Senha Intermediaria'
        elif 7 < self.__pontos:
            return 'Senha Forte'
        
# Função simples onde copia a varivel de321 senha onde foi guardada a senha gerada e deixa na área de tranferencia
    def copiar(self):
        pyperclip.copy(senha)
    


# Esse código abaixo é um codigo de teste onde ele só funciona se for executado esse arquiov, é uma forma de testar para ver se os comandos acima estão funcionando corretamente
if __name__ == '__main__':
    # uso da classe
    gerador = GeradorSenhas(num_caracteres=7, letras_maiusculas=True, letras_minusculas=True, numeros=True, simbolos=False)
    senha = gerador.gerar_senha()
    print(f'Senha gerada: {senha}')
    nivel_seguranca = gerador.avaliar_seguranca(senha)
    print(f'Nível de segurança: {nivel_seguranca}')
    gerador.copiar()
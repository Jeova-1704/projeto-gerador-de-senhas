
# Importando Backend 
import back
# Importando PySimpleGui
import PySimpleGUI as sg


def tela_login():
    sg.theme('DarkGrey11')
    layout=[
    [sg.HSeparator(),sg.Text('Tela de Login',font='Helvetica 16 bold'),sg.HSeparator()],
    [sg.Text("",size=(10,5))],
    [sg.Text("Usuário :",font="Helvetica 15 bold"),sg.InputText(" ",size=(20,1),key='-usuario-')],
    [sg.Text("Senha :",font="Helvetica 15 bold"),sg.InputText(" ",size=(20,1))],
    [sg.Text("",size=(10,2))],
    [sg.Button("Entrar",font="helvetica 10 bold"),sg.Button("Sair",button_color="Red",font="helvetica 10 bold",size=(5,1))],
    ]
    return sg.Window('Tela Login', layout=layout, element_justification='c',size=(500,350), finalize=True)

def tela_principal():
    sg.theme('DarkGrey11')
    layout=[
        [sg.HSeparator(),sg.Text('Gerador de Senha',font='Helvetica 16 bold'),sg.HSeparator()],
        [sg.Text(f'Olá {nome_usuario} !',font='Helvetica 12 bold',text_color='LightBlue')],
        [sg.Text(' ')],
        [sg.Text('Quantidade de caracteres:',font=("Helvetica 12")),sg.Slider(range=(1, 50), orientation='h', size=(20,20), default_value=50,key=('-SLIDER-'))],
        [sg.Text('')],
        [sg.Checkbox('Letras Maiúsculas (ABC)',key="-MAIUSC-")],
        [sg.Checkbox('Letras Minúsculas (abc)',key="-MINUSC-")],
        [sg.Checkbox('Números (123)',key="-NUM-")],
        [sg.Checkbox('Caracteres Especiais (!@#)',key="-CHAR-")],
        [sg.Button('Gerar Senha',font=('Helvetica 12 bold'))],
        [sg.Text('',size=(14,1)),sg.Text(f'{senha_gerada}',font=('Helvetica 14 bold'), key='-SENHA-'),sg.Button('Copiar Senha')],
        [sg.Text('',size=(15,1)),sg.Text('Senha Forte',text_color='Green')],
        
        ]
    return sg.Window('Tela Principal', layout=layout, element_justification='l',size=(500,550), finalize=True)

janela_login , janela_principal = tela_login(),None


senha_gerada = " "
nivel_seguranca = " "

while True:
    Window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break

    if event == "Entrar":
        nome_usuario = values['-usuario-']
        janela_login.hide()
        janela_principal = tela_principal()
        janela_principal.un_hide()
        
    if event == 'Gerar Senha':
        
        # Retorno das checkbox ( True / False )
        slider_quantidade_caracteres = values['-SLIDER-']
        checkbox_maiusculo = values['-MAIUSC-']
        checkbox_minusculo = values['-MINUSC-']
        checkbox_numero = values['-NUM-']
        checkbox_caractere = values['-CHAR-']

        # adicionar resultado da senha aqui
        senha_gerada = back.gerar_senha(slider_quantidade_caracteres, checkbox_maiusculo, checkbox_minusculo, checkbox_numero, checkbox_caractere)

        #Nivel de segurança:
        nivel_seguranca = back.avaliar_seguranca(senha_gerada)
        


        # Atualiza a janela e faz aparecer a senha na tela
        janela_principal['-SENHA-'].update(senha_gerada)
        janela_principal.hide()
        janela_principal.un_hide()

    # O QUE ACONTECE AO CLICAR NO BOTÃO COPIAR SENHA 
    if event == "Copiar Senha":
        back.copiar(senha_gerada)
        sg.popup_ok("Senha Copiada com sucesso ✔!")



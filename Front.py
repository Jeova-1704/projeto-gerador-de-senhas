
# Importando Backend 
import back
# Importando PySimpleGui
import PySimpleGUI as sg

# criando layout da janela de login

def tela_login():
    sg.theme('DarkGrey11')
    layout=[
    [sg.HSeparator(),sg.Text('Tela de Login',font='Helvetica 16 bold'),sg.HSeparator()],
    [sg.Text("",size=(10,5))],
    [sg.Text("Usuário :",font="Helvetica 15 bold"),sg.InputText(" ",size=(20,1),key='-usuario-')],
    [sg.Text("Senha :",font="Helvetica 15 bold"),sg.InputText(" ",size=(20,1))],
    [sg.Checkbox('Usar Tema Claro',key="-TEMA_CLARO-")],
    [sg.Text("",size=(10,2))],
    [sg.Button("Entrar",font="helvetica 10 bold"),sg.Button("Sair",button_color="Red",font="helvetica 10 bold",size=(5,1))],
    ]
    return sg.Window('Tela Login', layout=layout, element_justification='c',size=(500,350), finalize=True)

# criando layout da janela principal

def tela_principal():
    tema_claro = values["-TEMA_CLARO-"]
    if tema_claro:
        sg.theme('Lightblue')
        coluna = [sg.Text(f'{senha_gerada}',text_color="#1C1C1C",background_color="#4682B4",pad=((75,0),(20,0)),size=(20,3),auto_size_text=True,font=('Helvetica 14 bold'), key='-SENHA-'),sg.Button('Copiar Senha',pad=((5,0),(16,0)),font="Helvetica 10 bold")]
    else:
        sg.theme('DarkGrey11')
        coluna = [sg.Text(f'{senha_gerada}',background_color="#1C1C1C",pad=((75,0),(20,0)),size=(20,3),auto_size_text=True,font=('Helvetica 14 bold'), key='-SENHA-'),sg.Button('Copiar Senha',pad=((5,0),(16,0)),font="Helvetica 10 bold")]
    coluna_slider = [sg.Text('Quantidade de caracteres:',font=("Helvetica 12"),pad=((0, 0), (16, 0))),sg.Slider(range=(1, 50), orientation='h', size=(20,20), border_width=(3),default_value=50,key=('-SLIDER-'))]
    
    layout=[
        [sg.HSeparator(),sg.Text('Gerador de Senha',font='Helvetica 16 bold'),sg.HSeparator()],
        [sg.Text(f'Olá {nome_usuario} !',font='Helvetica 12 bold',pad=(190,1))],
        [coluna_slider],
        [sg.Text('')],
        [sg.Checkbox('Letras Maiúsculas (ABC)',key="-MAIUSC-")],
        [sg.Checkbox('Letras Minúsculas (abc)',key="-MINUSC-")],
        [sg.Checkbox('Números (123)',key="-NUM-")],
        [sg.Checkbox('Caracteres Especiais (!@#)',key="-CHAR-")],
        [sg.Button('Gerar Senha',font=('Helvetica 12 bold'))],
        [coluna],
        [sg.Text(f'{nivel_seguranca}', key="-SEGURANCA-", justification='center',pad=((73,0),(0,0)))], 
        [sg.Button("Voltar",pad=((5,0),(20,0)),font="Helvetica 10 bold"),sg.Button("Sair",font="Helvetica 10 bold",size=(5,1),button_color="Red",pad=((10,0),(20,0)))]     
        ]
    return sg.Window('Gerador de Senhas', layout=layout, element_justification='l',size=(500,500), finalize=True)

# definindo os valores das janelas iniciais
janela_login , janela_principal = tela_login(),None

# valores da senha gerada e o seu respectivo nivel de seguranca (ainda nao foram criados)
senha_gerada = " "
nivel_seguranca = " "

# iniciando programa aqui
while True:
    # constante leitura de eventos 
    Window, event, values = sg.read_all_windows()
    # encerrando programa ao fechar janela 
    if event == sg.WIN_CLOSED:
        break
    
    # o que acontece ao clicar no botao "Entrar" na janela de login
    if event == "Entrar" and Window==janela_login:
        nome_usuario = values['-usuario-']
        janela_login.hide()
        janela_principal = tela_principal()
        janela_principal.un_hide()
    
    # o que acontece ao clicar no botão sair
    if event == "Sair":
        # popup surge para confirmar a acao de saida
        confirmacao_sair = sg.popup_ok_cancel('Você quer realmente sair ?')
        # encerrando o programa
        if confirmacao_sair == "OK":
            break
    # o que acontece ao clicar no botao "Voltar"
    if event == "Voltar":
        janela_principal.hide()
        janela_login.un_hide()


    # o que acontece ao clicar no botão "Gerar Senha" na janela principal
    if event == 'Gerar Senha' and Window==janela_principal:
        try:
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

            # Define a cor com base no nivel de segurança:
            if nivel_seguranca == "Senha Fraca":
                fonte_color = 'Red'
            elif nivel_seguranca == "Senha intermediaria":
                fonte_color = 'Orange'
            else:
                fonte_color = 'Green'

            # Atualiza a janela e faz aparecer a senha na tela
            janela_principal['-SEGURANCA-'].update(nivel_seguranca, text_color = fonte_color)
            janela_principal['-SENHA-'].update(senha_gerada)
            janela_principal.hide()
            janela_principal.un_hide()
            # abrindo excecao caso o usuario nao selecione nenhum checkbox
        except:
            sg.popup_ok('Escolha no mínimo 1 opção de caracteres')

    # O QUE ACONTECE AO CLICAR NO BOTÃO COPIAR SENHA na janela principal
    if event == "Copiar Senha" and Window==janela_principal:
        back.copiar(senha_gerada)
        sg.popup_ok("Senha Copiada com sucesso ✔!")



import funcao

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
        [sg.Text(f'Olá {nome_usuario}',font='Helvetica 10 bold')],
    ]
    return sg.Window('Tela Principal', layout=layout, element_justification='c',size=(500,550), finalize=True)




janela_login , janela_principal = tela_login(),None
nome_usuario = Values['-usuario-']


while True:
    Window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == "Entrar":
        janela_login.hide()
        janela_principal = tela_principal()
        janela_principal.un_hide()
        




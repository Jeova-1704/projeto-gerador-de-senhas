import funcao

import PySimpleGUI as sg




def tela_login():
    sg.theme('Reddit')
    layout=[
    [sg.HSeparator(),sg.Text('Tela de Login',font='Helvetica 16 bold'),sg.HSeparator()],   
    ]
    return sg.Window('Tela Login', layout=layout, element_justification='l',size=(500,550), finalize=True)

janela_login = tela_login()



while True:
    Window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break





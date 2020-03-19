import PySimpleGUI as sg

sg.ChangeLookAndFeel('Dark')

WIN_W = 61
WIN_H = 22
filename = None

file_new  = 'Novo       (CTRL+N)'
file_open = 'Abrir       (CTRL+O)'
file_save = 'Salvar     (CTRL+S)'

sg.Text()
menu_layout = (
    ['Arquivo', [file_new, file_open, file_save, 'Salvar como', '---', 'Sair']],
    ['Editar', ['Tornar caixa alta', 'Tornar caixa baixa']],
    ['Ver', ['Palavras escritas', 'Minimizar', 'Maximizar']],
    ['Ajuda', ['Autores']],
)

layout = [
    [sg.MenuBar(menu_layout)],
    [sg.Text('> Novo arquivo <', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
    [sg.Multiline(font=('Consolas', 12), text_color='white', size=(WIN_W, WIN_H), key='_BODY_')]]

window = sg.Window(
    'PYPad',
    layout=layout,
    margins=(0, 0),
    resizable=True,
    return_keyboard_events=True,
    icon='',
)

window.read(timeout=1)
window['_BODY_'].expand(expand_x=True, expand_y=True)


def new_file() -> str:
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> Novo arquivo <')
    filename = None
    return filename


def open_file() -> str:
    try:
        filename: str = sg.popup_get_file('Open File', no_window=True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename, 'r') as f:
            window['_BODY_'].update(value=f.read())
        window['_INFO_'].update(value=filename)
    return filename


def save_file(filename: str):
    if filename not in (None, ''):
        with open(filename, 'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)
    else:
        save_file_as()


def save_file_as() -> str:
    try:
        filename: str = sg.popup_get_file(
            'Save File',
            save_as=True,
            no_window=True,
            default_extension='.txt',
            file_types=(('Text', '.txt'),),
        )
    except:
        return
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename, 'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)
    return filename


def tornar_caixa_baixa():
    window['_BODY_'].update(value=str(values['_BODY_']).lower())


def tornar_caixa_alta():
    window['_BODY_'].update(value=str(values['_BODY_']).upper())


def palavras_contador():
    texto = [t for t in values["_BODY_"].split(" ") if t != "\n"]
    palavras_contadas = len(texto)
    sg.PopupOK(f'Palavras escritas: {palavras_contadas}', title='Palavras escritas', auto_close=True, auto_close_duration=5)


def exibir_autores():
    sg.PopupOK('''
            Mikael Rolim -> github.com/Mikael-R

            Agradecimentos:
            Eder Cruz -> youtube.com/channel/UCz1ipXWkAYjcS4jie_IKs6g
            Jhonatan de Souza -> youtube.com/devaprender
            ''', title='Autor', auto_close=True, auto_close_duration=5)


while True:
    event, values = window.read()

    if event in (None, 'Sair'):
        window.close()
        exit()
        break
    if event in (file_new, 'n:78'):
        filename = new_file()
    if event in (file_open, 'o:79'):
        filename = open_file()
    if event in (file_save, 's:83'):
        save_file(filename)
    if event in ('Salvar como'):
        filename = save_file_as()
    if event == 'Tornar caixa alta':
        tornar_caixa_alta()
    if event == 'Tornar caixa baixa':
        tornar_caixa_baixa()
    if event == 'Palavras escritas':
        palavras_contador()
    if event == 'Minimizar':
        window.minimize()
    if event == 'Maximizar':
        window.maximize()
    if event == 'Autores':
        exibir_autores()

from hashlib import new
import random
import PySimpleGUI as sg
import os

from PySimpleGUI.PySimpleGUI import Combo, EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED, Output

class Gen_PassWd:
    def __init__(self):
        sg.theme('DarkBlack')
        layout = [
            [sg.Text('Where', size=(10,1)),
            sg.Input(key='site', size=(20,1))],
            [sg.Text('Login', size=(10,1)),
            sg.Input(key='user', size=(20,1))],
            [sg.Text('Number of chars'), sg.Combo(values=list(range(30)), key='total_chars', default_value=1,size=(3,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Generate')]
        ]
        self.win = sg.Window('Password Generator', layout)

    def Init(self):
        while True:
            even, val = self.win.read()
            if even == sg.WINDOW_CLOSED:
                break
            if even == 'Generate':
                new_pwd = self.generate_pwd(val)

    def generate_pwd(self, val):
        char_list='QWERTYUIOPÇLKJHGFDSAMNBVCXZqwertyuiopçlkjhgfdsazxcvbnm!@#$%&¨*'
        chars = random.choices(char_list, k=int(val['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def savePwd(self):
        pass


gen = Gen_PassWd()
gen.Init()
















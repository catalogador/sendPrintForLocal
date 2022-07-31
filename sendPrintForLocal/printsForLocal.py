import pyautogui
import keyboard
import pyscreenshot as ImageGrab
import os


nomePrint=0

def printTela(nomePrint):
    imagem = ImageGrab.grab()
    imagem.save(f'C:/Users/polon/OneDrive/Área de Trabalho/prints/screenShot{nomePrint}.png')

def attCaminho():
    dir_path = (r'C:/Users/polon/OneDrive/Área de Trabalho/prints')
    res = []
    for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                res.append(path)
    return res
while True:  
    try:  
        if keyboard.is_pressed('q'):
            res = attCaminho()
            indice = len(res)-1
            printTela(nomePrint)
            nomePrint = nomePrint + indice + 1          
            
    except:
        break  


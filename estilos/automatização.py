import pyautogui
from time import sleep
import webbrowser

# Passo 1: Abre o navegador padrão
webbrowser.open('https://www.google.com')

# Espera alguns segundos para o navegador abrir
sleep(2)

# Passo 2: Digita "Kaboom" na barra de pesquisa do Google
pyautogui.write('Kabum')

sleep(1)

pyautogui.press('enter')

pyautogui.moveTo(400, 420)

sleep(1)

pyautogui.click()

# Passo 3: Pressiona "Enter" para pesquisar
pyautogui.press('enter')
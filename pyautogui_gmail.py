 import pyautogui as pa
import time

pa.PAUSE = 1
pa.press("win")
pa.write("chrome")
pa.press("enter")

pa.write("gmail.com")
pa.press("enter")

# retorna a posição do mouse
# espera 3 segundos antes de capturar a coordenada no mouse
import time

time.sleep(3)
pa.location()
####################

# Localiza a posição de uma imagem na tela. A imagem precisa ser exatamente igual.
pa.locateOnScreen("caminho para uma imagem a ser localizada")
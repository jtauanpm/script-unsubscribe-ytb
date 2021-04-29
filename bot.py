import pyautogui
import pyperclip
import time

# Altere aqui caso o bot esteja muito rápido em relação ao carregamento das páginas no broswer 
wait = 5

pyautogui.PAUSE = 1
pyautogui.alert("A execução vai começar, não mexa em nada !")

# Abrir navegador
pyautogui.press("winleft")
pyautogui.write("Edge") # Altere aqui para trocar o navegador
pyautogui.press("Enter")

# Entrar no yotube
link = "https://www.youtube.com/"
pyperclip.copy(link)
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(wait)

# Ir em inscrições
pyautogui.click(110,264)
time.sleep(wait)
pyautogui.click(1195,192)
time.sleep(wait)

# Cancelar inscrição
pyautogui.click(1238,243)
pyautogui.click(748,452)

# Atualizar página
pyautogui.press("f5")
time.sleep(wait)

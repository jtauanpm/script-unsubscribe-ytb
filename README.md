# Bot para cancelar inscrição em canais do youtube

Para a implementação do código foram usadas as bibliotecas time, pyautogui e pyperclip do Python (A instalação delas é necessária).
---
## Aqui está um Gif demonstrando a sua execução (sem repetição).
![Gif Bot](https://github.com/jonathan-maia/bot-unsubscribe-ytb/blob/main/gif.gif)
---

### Para que funcione em outro computaddor, talvez seja necessárias algumas alterações :
**Abrindo o navegador :** No meu caso, usei o Microsoft Edge. Para usar outro navegador, mude o texto entre aspas no arquivo bot.py onde está epecificado (pyautogui.write("Nome-Navegador")).

**Posições de click do mouse :** Para obter a posição de click do mouse no seu computador, é necessário rodar o arquivo pos_mouse.py, colocar o mouse no local desejado, e após 7 segundos, será retornado o valor de X e Y onde o mouse estava localizado. Para mudar a posição do click, modifique cada método (pyautogui.click(x,y)) e mude para o X e Y retornado no seu computador.

**Quantidade de repetições :** Para saber quantas vezes é necessária a repitição do bloco de comando para dar unsubscribe em todos os canais: 
1. Entre no seu youtube 
2. clique nos tracinhos no canto superior esquerdo
3. procure a aba inscrições
4. Haverá um texto (Mostrar mais X)
5. Pegue esse número X e mude no laço (for)

**Tempo de carregamento :** Caso o bot esteja mais rápido que o carregamento do seu browser, aumente a variável (wait) para um número maior que especificará a quantidade de segundos que sera esperado quando o comando (time.sleep(wait)) for chamado.


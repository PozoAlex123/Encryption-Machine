import flet as ft
import pyperclip

def main(page:ft.Page):

    def letras():
        letras_numeros = {'a': 1,'b': 2, 'c': 3, 'd': 4, 'e': 5, 
                'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
                'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 
                'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 
                'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 
                'z': 26}
        return letras_numeros

    def morse():
        letras_morse = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
            'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
            'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
            'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
            'z': '--..', " ":"", "":""}
        outputdemensaje.value = ""
        for letra in dondevaelmensaje.value:
            outputdemensaje.value+=letras_morse[letra] + "/"
        page.update()

    def numeros():
        numeros_letras = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 
                        5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
                        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 
                        16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 
                        21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 
                        26: 'z'}
        return numeros_letras
    
    def crossroads(e):
        match(Porfin.value):
            case "Morse":
                morse()
            case "Letras - Numeros":
                numeros()

    def copiaralclipboard():
        pyperclip.copy(outputdemensaje.value)

    dondevaelmensaje = ft.TextField(label="Mucho Pene", width=400, bgcolor=ft.colors.GREY, color = ft.colors.BLUE)
    outputdemensaje = ft.TextField(label="Encryped text:", read_only=True, bgcolor=ft.colors.GREY, color = ft.colors.BLUE)

    Porfin = ft.Dropdown(
        label="Tamales de Jose",
        bgcolor=ft.colors.GREY,
        color=ft.colors.BLUE,
        options=[
            ft.dropdown.Option("Letras - Numeros"),
            ft.dropdown.Option("Morse"),
            ft.dropdown.Option("Numeros - Letras"),
        ],
    )

    boton1 = ft.ElevatedButton("Encriptar", style=ft.ButtonStyle(bgcolor=ft.colors.GREY,color=ft.colors.WHITE), on_click=crossroads)
    boton2 = ft.ElevatedButton("Copiar al Clipboard" , on_click=copiaralclipboard, style=ft.ButtonStyle(bgcolor=ft.colors.GREY,color=ft.colors.WHITE))
    
    output_text = ft.Text("Selecciona un Encryption")


    page.add(Porfin, output_text ,dondevaelmensaje, outputdemensaje, boton1, boton2)

ft.app(target=main)
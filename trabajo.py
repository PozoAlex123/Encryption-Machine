import flet as ft
import pyperclip

def main(page:ft.Page):

    def letras():
        letras_numeros = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 
                        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 
                        'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 
                        'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 
                        'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 
                        'z': '26', ' ': ''}

        outputdemensaje.value = ""
        for letra in dondevaelmensaje.value.lower():
            outputdemensaje.value+=letras_numeros[letra] + "/"
        page.update()

    def morse():
        letras_morse = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
            'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
            'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
            'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
            'z': '--..', " ":"", "":""}
        outputdemensaje.value = ""
        for letra in dondevaelmensaje.value.lower():
            outputdemensaje.value+=letras_morse[letra] + "/"
        page.update()

    def binaryqueseyo():
        binarydicc = {
            "a": "01100001", "b": "01100010", "c": "01100011", "d": "01100100", "e": "01100101",
            "f": "01100110", "g": "01100111", "h": "01101000", "i": "01101001", "j": "01101010",
            "k": "01101011", "l": "01101100", "m": "01101101", "n": "01101110", "o": "01101111",
            "p": "01110000", "q": "01110001", "r": "01110010", "s": "01110011", "t": "01110100",
            "u": "01110101", "v": "01110110", "w": "01110111", "x": "01111000", "y": "01111001",
            "z": "01111010", " " : ""}
        outputdemensaje.value = ""
        for letra in dondevaelmensaje.value.lower():
            outputdemensaje.value+=binarydicc[letra] + "/"
        page.update()
    
    def crossroads(e):
        match(Porfin.value):
            case "Morse":
                morse()
            case "Letras - Numeros":
                letras()
            case "Binary":
                binaryqueseyo()

    def copiaralclipboard(e):
        Copything = pyperclip.copy(outputdemensaje.value)

    dondevaelmensaje = ft.TextField(label="Mucho no parte privada del hombre", width=400, on_change=crossroads)
    outputdemensaje = ft.TextField(label="Aqui sale el mensaje", read_only=True,)
    Porfin = ft.Dropdown(
        label="Tamales de Jose",
        options=[
            ft.dropdown.Option("Letras - Numeros"),
            ft.dropdown.Option("Morse"),
            ft.dropdown.Option("Binary"),
        ],
    )

    boton2 = ft.ElevatedButton("Copiar al Clipboard" , on_click=copiaralclipboard)
    output_text = ft.Text("Selecciona un Encryption")

    page.add(Porfin, output_text ,dondevaelmensaje, outputdemensaje, boton2)

ft.app(target=main)
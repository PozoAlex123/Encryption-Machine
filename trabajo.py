import flet as ft
import pyperclip

def main(page:ft.Page):

    def letras():
        letras_numeros = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 
                        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 
                        'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 
                        'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 
                        'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 
                        'z': '26'}

        outputdemensaje.value = ""
        for letra in dondevaelmensaje.value:
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
        for letra in dondevaelmensaje.value:
            outputdemensaje.value+=letras_morse[letra] + "/"
        page.update()

    def polarqueseyo():
        polar_cenit_dict = {
            'p': 'l', 'o': 'a', 'l': 'p', 'a': 'o', 'r': 'e', 'e': 'r', 
            'c': 'n', 'n': 'c', 'i': 't', 't': 'i'
        }
        outputdemensaje.value = ""
        for letra in dondevaelmensaje.value:
            outputdemensaje.value+=polar_cenit_dict[letra] + "/"
        page.update()
    
    def crossroads(e):
        match(Porfin.value):
            case "Morse":
                morse()
            case "Letras - Numeros":
                letras()
            case "Polar":
                polarqueseyo()

    def copiaralclipboard():
        pyperclip.copy(outputdemensaje.value)

    dondevaelmensaje = ft.TextField(label="Mucho no parte privada del hombre", width=400, on_change=crossroads)
    outputdemensaje = ft.TextField(label="Encryped text:", read_only=True)

    Porfin = ft.Dropdown(
        label="Tamales de Jose",
        options=[
            ft.dropdown.Option("Letras - Numeros"),
            ft.dropdown.Option("Morse"),
            ft.dropdown.Option("Polar"),
        ],
    )

    boton2 = ft.ElevatedButton("Copiar al Clipboard" , on_click=copiaralclipboard)
    
    output_text = ft.Text("Selecciona un Encryption")

    page.add(Porfin, output_text ,dondevaelmensaje, outputdemensaje, boton2)

ft.app(target=main)
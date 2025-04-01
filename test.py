import flet as ft

def main(page: ft.Page):

    dnaDict = {
        "A" : "T",
        "C" : "G",
        "T" : "A",
        "G" : "C"
    }

    def translateDNA(e):
        dnaResult.value = ""
        dnaText.value = userDna.value
        if dnaText.value[-1] not in dnaDict.keys():
            dnaResult.value = dnaText.value = "Invalid Character, please correct."
        else:
            for letter in dnaText.value:
                dnaResult.value += dnaDict[letter]
        page.update()

    userDna = ft.TextField(label="Write your DNA structure here:", on_change=translateDNA)
    dnaText = ft.Text("Nothing written yet.", size=30)
    dnaResult = ft.Text("Nothing written yet.", size=30)

    page.add(userDna, dnaText, dnaResult)

ft.app(target=main)
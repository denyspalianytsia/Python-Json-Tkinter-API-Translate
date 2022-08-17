import requests
import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox

url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

root = tk.Tk()
root.title("Translator")
root.geometry("300x260")

first_list = [
	"en",
	"uk",
	"ru"
]

first = StringVar()

first.set(first_list[0])

lbl = Label(text="Виберіть мову яку хочете перекласти: ")
lbl.pack()
drop = OptionMenu(root, first,*first_list)
drop.pack()

second_list = [
	"uk",
	"ru",
	"en"
]

second = StringVar()

second.set(second_list[0])

lbl2 = Label(text="Виберіть мову на яку хочете перекласти: ")
lbl2.pack()
drop2 = OptionMenu(root, second,*second_list)
drop2.pack()

translation_lbl = tk.Label( text="Введіть що хочете перекласти:")
translation_lbl.pack()
translation_ent = tk.Entry()
translation_ent.pack()

def translate_text():
	sourcetranslate = first.get()
	targettranslate = second.get()
	translation = translation_ent.get()
	if translation_ent.get() != '':
		payload = {
			"q":"{}".format(translation),
			"source": "{}".format(sourcetranslate),
			"target": "{}".format(targettranslate),
		}

		headers = {
 			"content-type":"application/json",
 			"X-RapidAPI-Key":"f0eda7c17amsha10f3c793fdf668p1ba57fjsn4b46df9be184",
 			"X-RapidAPI-Host":"deep-translate1.p.rapidapi.com"
		}
		response = requests.request("POST", url, json=payload, headers=headers)
		json = response.json()

		text_translate = json['data']['translations']['translatedText']
		translated_text.config(text="Переведений текст: {}".format(text_translate))
	else:
		messagebox.showerror('Error', 'Line is empty')

translate_btn = tk.Button(text = "Перекласти", command = translate_text)
translate_btn.pack()

translated_text = tk.Label(
    text="")
translated_text.pack()


root.mainloop()
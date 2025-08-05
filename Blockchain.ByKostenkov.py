import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def update_b_label(event):
    code = base_combobox.get()
    name = currencies[code]
    b_label.config(text=name)

def update_t_label(event):
    code = target_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

def exchange():
    t_code = target_combobox.get()
    b_code = base_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json()

            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = currencies[t_code]
                b_name = currencies[b_code]
                mb.showinfo("Курс обмена", f"Курс к доллару: {exchange_rate:.2f} {t_name} за 1 {b_name}")

            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")

    else:
        mb.showwarning("Внимание", "Введите код валюты")


currencies = {
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум",
    "USD": "Американский доллар"
}

window = Tk()
window.title("Курс обмена")
window.geometry("360x300")

Label(text="Базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=10)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()

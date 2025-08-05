import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()

            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo("Курс обмена", f"Курс к доллару: {exchange_rate:.2f} {code} за 1 доллар")

            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")

    else:
        mb.showwarning("Внимание", "Введите код валюты")


window = Tk()
window.title("Курс обмена валюты к доллару")
window.geometry("360x180")

Label(text="Выберите код валюты:").pack(padx=10, pady=10)

popular_currencies = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT", "UZS"]
combobox = ttk.Combobox(values=popular_currencies)
combobox.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()

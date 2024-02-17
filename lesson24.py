import tkinter as tk
# tkinter - это библиотека для создания графических пользовательских интерфейсов (GUI) в Python.
# Она предоставляет набор инструментов и виджетов для создания окон, кнопок, полей ввода и других элементов интерфейса.
from parsing import *
# автоматизированный сбор и систематизация информации из открытых источников с помощью скриптов
import webbrowser
# webbrowser - это стандартная библиотека Python, предоставляющая простой интерфейс для открытия веб-браузера и отображения веб-страниц.
# Это может использоваться для автоматизации открытия веб-страниц в браузере, например, при отображении результатов парсинга или открытии веб-сайтов по определенным событиям в программе.
import requests
# requests - это библиотека для отправки HTTP-запросов в Python.
# Она широко используется для взаимодействия с веб-серверами, в том числе для получения данных с веб-страниц.
from bs4 import BeautifulSoup
# BeautifulSoup - это библиотека для парсинга HTML и XML документов в Python.
# Она предоставляет удобные методы для извлечения информации из HTML-кода, таких как поиск тегов, получение атрибутов и текста, облегчая процесс веб-скрапинга.


DOLLAR_TENGE = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%82&aqs=chrome.0.0i131i433i512j69i57j0i457i512j0i402j0i131i433i512j0i512l5.5420j0j7&sourceid=chrome&ie=UTF-8'
RUBLE_TENGE = 'https://www.google.com/search?q=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&sxsrf=AJOqlzXhw_VXNUGJS7RMg0HOPt4hKpZG1w%3A1678784678841&ei=pjgQZKz0Ms-QkwXgrYuoCA&ved=0ahUKEwis376jiNv9AhVPyKQKHeDWAoUQ4dUDCA8&uact=5&oq=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeOgoIABBHENYEELADOg0IABBHENYEEMkDELADOggIABCSAxCwAzoHCAAQDRCABDoNCAAQgAQQDRCxAxCDAToHCAAQgAQQDUoECEEYAFDqB1iRFmDNF2gCcAF4AIABrAGIAb8GkgEDMC41mAEAoAEByAEKwAEB&sclient=gws-wiz-serp'
EURO_TENGE = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&sxsrf=AJOqlzWJ-LT3kK-s15fdJ8wJ19o-GfioFg%3A1678784718588&ei=zjgQZM_DI4W6sAfry4cI&ved=0ahUKEwjP4ri2iNv9AhUFHewKHevlAQEQ4dUDCA8&uact=5&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQsQMQgwEQQzIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDoKCAAQRxDWBBCwAzoNCAAQRxDWBBDJAxCwAzoICAAQkgMQsAM6BwgAELADEEM6BggAEAcQHjoLCAAQBxAeEPEEEAo6CAgAEAcQHhAKOg0IABAFEAcQHhDxBBAKSgQIQRgAUPQEWMMWYIUaaANwAXgAgAHGAYgB6wqSAQMwLjiYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp'

ALMATY_WEATHER = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%B0%D0%BB%D0%BC%D0%B0%D1%82%D0%B5&sxsrf=AJOqlzXQ5M7r-0TZ3qsG4UfPbp-VR0iN8Q%3A1678785769776&ei=6TwQZP70LvyC9u8P-52gmAw&ved=0ahUKEwi-jdirjNv9AhV8gf0HHfsOCMMQ4dUDCA8&uact=5&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%B0%D0%BB%D0%BC%D0%B0%D1%82%D0%B5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzISCAAQgAQQsQMQgwEQChBGEIACMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKOgcIIxDqAhAnOgwIABDqAhC0AhBDGAE6BAgjECc6CwgAEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoICAAQsQMQgwE6CwgAEIAEEAoQARAqOgkIABCABBAKEAE6BQgAEIAEOgoIABCxAxCDARBDOgQIABBDOg8IABCxAxCDARBDEEYQgAI6DQgAELEDEIMBEMkDEEM6DQgAEIAEELEDEIMBEAo6EAgAEIAEELEDEIMBEEYQgAJKBAhBGABQAFi6KWDCKmgIcAF4AIAB0gGIAdEckgEGMC4yMC4xmAEAoAEBsAEUwAEB2gEGCAEQARgB&sclient=gws-wiz-serp'

GITHUB = 'https://github.com/Marlen011'

ATMO_TIKTOK = 'https://www.tiktok.com/@atmosphere.it'
ATMO_INSTAGRAM = 'https://www.instagram.com/atmosphere_it/'
# устанавливает HTTP заголовок "User-Agent" для симуляции запроса от браузера Chrome. В данном случае "User-Agent" указывает на то, что запрос отправляется от браузера Chrome версии 111.0.0.0, работающего под операционной системой Windows 10
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

def get_currency(url):
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('Нет данных')
    return result

def get_weather(url):
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_temperature = soup.findAll("span", {"class": "wob_t q8U8x"})
    convert_wind = soup.findAll("span", {"id": "wob_ws"})
    convert_humidity = soup.findAll("span", {"id": "wob_hm"})
    convert_pressure = soup.findAll("span", {"id": "wob_pp"})
    convert = convert_temperature + convert_wind + convert_humidity + convert_pressure
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('Нет данных')
    return result

def atmosphere_tiktok(url):
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("strong", {"data-e2e": "followers-count"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('Нет данных')
    return result

def count_project(url):
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"data-view-component": "true", "class": "Counter"})
    result = []
    for c in convert:
        result.append(int(c.text))
    if len(result) == 0:
        result.append('Нет данных')
    return [max(result)]

# def main():
#     print(f'Курс доллара: {get_currency(DOLLAR_TENGE)}')
#     print(f'Курс евро: {get_currency(EURO_TENGE)}')
#     print(f'Курс рубля: {get_currency(RUBLE_TENGE)}')
#     print(f'Погода в Алматы: {get_weather(ALMATY_WEATHER)}')
#     print(f'Подписчики на TikTok: {atmosphere_tiktok(ATMO_TIKTOK)}')
#     print(f'Число открытых проектов на GitHub: {count_project(GITHUB)}')

# main()

# lesson 24

root = tk.Tk()
root.title("Atmosphere App")


def App():
    
    def get_data():
        dollar = get_currency(DOLLAR_TENGE)
        euro = get_currency(EURO_TENGE)
        ruble = get_currency(RUBLE_TENGE)
        tiktok = atmosphere_tiktok(ATMO_TIKTOK)
        github = count_project(GITHUB)
        weather = get_weather(ALMATY_WEATHER)
        ALL_DATA = [dollar, euro, ruble, tiktok, github, weather]
        return ALL_DATA
    
    def add_values(ALL_DATA):
        global dollar_value, euro_value, ruble_value, tiktok_value, github_value, weather_value1, weather_value2, weather_value3, weather_value4

        dollar_value = tk.Label(root, text=f"{ALL_DATA[0][0]} тг.", font=("Arial", 15))
        dollar_value.grid(row=1, column=1, padx=10, pady=10)
        euro_value = tk.Label(root, text=f"{ALL_DATA[1][0]} тг.", font=("Arial", 15))
        euro_value.grid(row=2, column=1, padx=10, pady=10)
        ruble_value = tk.Label(root, text=f"{ALL_DATA[2][0]} тг.", font=("Arial", 15))
        ruble_value.grid(row=3, column=1, padx=10, pady=10)
        tiktok_value = tk.Label(root, text=f"{ALL_DATA[3][0]} подписчиков", 
                    font=("Arial", 15))
        tiktok_value.grid(row=4, column=1, padx=10, pady=10)
        github_value = tk.Label(root, text=f"{ALL_DATA[4][0]} проектов", 
                    font=("Arial", 15))
        github_value.grid(row=5, column=1, padx=10, pady=10)

        weather_value1 = tk.Label(root, text=f"{ALL_DATA[5][0]}°C", font=("Arial", 15))
        weather_value1.grid(row=7, column=1, padx=10, pady=5)
        weather_value2 = tk.Label(root, text=f"{ALL_DATA[5][1]}", font=("Arial", 15))
        weather_value2.grid(row=8, column=1, padx=10, pady=5)
        weather_value3 = tk.Label(root, text=f"{ALL_DATA[5][2]}", font=("Arial", 15))
        weather_value3.grid(row=9, column=1, padx=10, pady=5)
        weather_value4 = tk.Label(root, text=f"{ALL_DATA[5][3]}", font=("Arial", 15))
        weather_value4.grid(row=10, column=1, padx=10, pady=5)

    
    def destroy_labels():
        dollar_value.destroy()
        euro_value.destroy()
        ruble_value.destroy()
        tiktok_value.destroy()
        github_value.destroy()
        weather_value1.destroy()
        weather_value2.destroy()
        weather_value3.destroy()
        weather_value4.destroy()
    
    # Методы
    def refresh():
        ALL_DATA = get_data()
        destroy_labels()
        add_values(ALL_DATA=ALL_DATA)
        


    # Заголовок
    label = tk.Label(root, text="Atmosphere Ap", font=("Arial", 20), background="black", foreground="white", border=5)
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Доллар
    dollar_label = tk.Label(root, text="Курс доллара: ", font=("Arial", 15))
    dollar_label.grid(row=1, column=0, padx=10, pady=10)

    # Евро
    euro_label = tk.Label(root, text="Курс евро: ", font=("Arial", 15))
    euro_label.grid(row=2, column=0, padx=10, pady=10)

    # Рубль
    ruble_label = tk.Label(root, text="Курс рубля: ", font=("Arial", 15))
    ruble_label.grid(row=3, column=0, padx=10, pady=10)

    # TikTok
    tiktok_label = tk.Label(root, text="TikTok: ", font=("Arial", 15))
    tiktok_label.grid(row=4, column=0, padx=10, pady=10)

    # GitHub
    github_label = tk.Label(root, text="GitHub: ", font=("Arial", 15))
    github_label.grid(row=5, column=0, padx=10, pady=10)

    # Разделитель
    separator = tk.Label(root, text="----------------------------------------", font=("Arial", 15))
    separator.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Погода
    weather_label1 = tk.Label(root, text="Температура: ", font=("Arial", 15))
    weather_label1.grid(row=7, column=0, padx=10, pady=5)
    weather_label2 = tk.Label(root, text="Скорость ветра: ", font=("Arial", 15))
    weather_label2.grid(row=8, column=0, padx=10, pady=5)
    weather_label3 = tk.Label(root, text="Влажность: ", font=("Arial", 15))
    weather_label3.grid(row=9, column=0, padx=10, pady=5)
    weather_label4 = tk.Label(root, text="Вероятность осадков: ", font=("Arial", 15))
    weather_label4.grid(row=10, column=0, padx=10, pady=5)

    # Значения
    ALL_DATA = get_data()
    add_values(ALL_DATA=ALL_DATA)

    # Обновить
    update_button = tk.Button(root, text="Обновить", font=("Arial", 20), bg="white", 
			fg="black",  command=refresh)
    update_button.grid(row=11, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

    # GitHub кнопка
    github_button = tk.Button(root, width=15, text="Github", command=lambda: webbrowser.open("https://github.com/krivalex"), bg="gray", fg="white")
    github_button.grid(row=12, column=0, columnspan=1, sticky="")

    # Instagram кнопка
    instagram_button = tk.Button(root, width=15, text="Instagram", command=lambda: webbrowser.open("https://www.instagram.com/_krivalex_/"), bg="purple", fg="white")
    instagram_button.grid(row=12, column=1, columnspan=1)

    # YouTube кнопка
    youtube_button = tk.Button(root, width=15, text="YouTube", command=lambda: webbrowser.open("https://www.youtube.com/channel/UCledP-8WCQCAy_1zrj4vukA"), bg="red", fg="white")
    youtube_button.grid(row=13, column=0, columnspan=1)

    # TikTok кнопка
    tiktok_button = tk.Button(root, width=15, text="TikTok",
		  command=lambda: webbrowser.open("https://www.tiktok.com/@atmosphere.it"), 
			bg="black", fg="white")
    tiktok_button.grid(row=13, column=1, columnspan=1)

    # Telegram кнопка
    telegram_button = tk.Button(root, width=15, text="Telegram",
		 command=lambda: webbrowser.open("https://t.me/Krivalex"), bg="blue", fg="white")
    telegram_button.grid(row=14, column=0)

    # Spotify кнопка
    spotify_button = tk.Button(root, text="Spotify", width=15,
		 command=lambda: webbrowser.open("https://open.spotify.com/user/oshhl48dq6dslgqey3vsgxn3p"), bg="green", fg="white")
    spotify_button.grid(row=14, column=1)


if __name__ == "__main__":
    App()
    root.mainloop()


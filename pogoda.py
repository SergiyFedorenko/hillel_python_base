# import pyowm
from tkinter import *
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk

win = Tk()
win.geometry("600x400")
win.title("Погода 1.0")
win.configure(background="#81daff")
lbl1 = Label(win, text ='Яке Місто:', font=('Arial Bold', 25))
lbl1.grid(column=0, row=0)
txt = Entry(win, font=("Times", 14, "bold"), width=10)
txt.grid(column=1, row=0)

answers1 = Listbox(font=("Times", 14, "bold"), width=30, heigh=1)
answers1.grid(column=0, row=1)
answers2 = Listbox(font=("Times", 14, "bold"), width=30, heigh=1)
answers2.grid(column=0, row=2)
answers3 = Listbox(font=("Times", 14, "bold"), width=30, heigh=1)
answers3.grid(column=0, row=3)
answers4 = Listbox(font=("Times", 14, "bold"), width=30, heigh=1)
answers4.grid(column=0, row=4)
def c1():
    owm = OWM('303ade2ed02233c80c2a2166b2073d59')
    mgr = owm.weather_manager()
    config_dict = get_default_config()
    config_dict['language'] = 'ua'  # your language here, eg. Portuguese
    owm.supported_languages
    place = str(txt.get())
    observation = mgr.weather_at_place(place)
    weather = observation.weather
    dump_dict = weather.to_dict() 
    wind_dict_in_meters_per_sec = observation.weather.wind()
    #reg = owm.city_id_registry()
    #kod = reg.ids_for(place)
    #print(kod) 
    #reference_time = observation.weather.wind()['reference_time']
    print(dump_dict)
    speed = wind_dict_in_meters_per_sec['speed']
    print('швидкість м.с.' + str(speed))
    detailed_status = dump_dict['detailed_status']
    print('повітря ' + str(detailed_status))
    weather_icon_name = dump_dict['weather_icon_name']
    print('повітря ' + str(weather_icon_name))
    deg = wind_dict_in_meters_per_sec['deg']
    print('напрямок' + str(deg))
    url = "http://openweathermap.org/img/wn/" + str(weather_icon_name) + "@2x.png"
    #gust = wind_dict_in_meters_per_sec['gust']
    #print('пориви' + str(gust))
    #nebo = w.detailed_status
    #print("небо зараз:" + str(nebo))
    #temp = w.temperature('celsius')['temp']
    #print('теипература зараз' + str(temp))
    #global answers
    #lbl1['text'] = temp
    #place label1['text'] = temp= 'Kyiv'
    #place = input('Яке місто') 
    # observation = mgr.weather_at_place('Kyiv,UA')
    print()
    #print(reference_time)
    print(place)
    temp = weather.temperature('celsius')['temp']
    #one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None)
    #w = observation.weather
    #print(w)
    p = weather.status
    print(p)
    m = weather.detailed_status
    print(m)
    #print('Вітер')
    answers1.insert(0, "Швидкість вітру м.с.  " + str(speed))
    answers2.insert(0, "іконка   " + str(weather_icon_name))
    answers3.insert(0, "Температура, С  " + str(temp))
    answers4.insert(0, "Повітря   " + str(detailed_status))
    #print( 'В Місті' + place + 'зараз' + w.detailed_status())
    #print(w.detailed_status())
    #url = "http://openweathermap.org/img/wn/" + str(weather_icon_name) + "@2x.png"
    label['text'] = 'Погода'
    win.update()
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.Timeout:
        label['text'] = 'Timeout error'
    else:
        if response.status_code != 200:
            label['text'] = 'HTTP error ' + str(response.status_code)
        else:
            pil_image = Image.open(BytesIO(response.content))
            image = ImageTk.PhotoImage(pil_image)
            label.config(image=image, text='')

            # прикрепляем ссылку на изображение к объекту label,
            # чтобы изображение не удалил сборщик мусора
            label.image = image 
btn = Button(win, text='Погода', font=('Arial Bold', 15), command=c1)
btn.grid(column=4, row=0)
label = tk.Label(win)
label.grid(column=0, row=5)
win.mainloop()
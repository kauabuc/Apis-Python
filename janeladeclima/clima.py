# informaçoes
import json
import os.path
import tkinter
from datetime import datetime
from tkinter import *
from tkinter import ttk

import pycountry_convert as pc
import pytz
import requests
from PIL import Image, ImageTk

script_dir = os.path.dirname(os.path.abspath(__file__))
# cores

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"
fundo = fundo_dia

cor = "#444466"
cor1 = "#feffff"
cor2 = "#6f9fbd"

# janela

janela = Tk()
janela.title("Clima")
janela.geometry('320x350')
janela.configure(bg=fundo)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

global imagem


def informacao(evento=None):
    chave = 'e9c73dd5461d0905c6604df5b69bd173'
    cidade = e_local.get()
    api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
        cidade, chave)

    r = requests.get(api_link)
    dados = r.json()

    # dados

    pais_codigo = dados['sys']['country']
    fusopais = pytz.country_timezones[pais_codigo]
    pais = pytz.country_names[pais_codigo]

    zona = pytz.timezone(fusopais[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime('%d/%m/%Y | %H:%M:%S %p')

    tempo = dados['main']['temp']
    pressao = dados['main']['pressure']
    umidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description']

    # mudando informações

    def pais_para_continente(i):
        pais_ap = pc.country_name_to_country_alpha2(i)
        pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_ap)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(
            pais_continente_codigo)

        return pais_continente_nome

    continente = pais_para_continente(pais)

    # passar as informaçoes
    l_cidade['text'] = f'{cidade} - {pais} / {continente}'
    l_data['text'] = zona_horas
    l_umidade['text'] = umidade
    l_pressao['text'] = f'Pressão : {pressao}'
    l_umidadesim['text'] = '% umidade'
    l_vel['text'] = f'Velocidade do vento: {velocidade}'
    l_descricao['text'] = descricao

    # trocar o fundo
    zona_period = datetime.now(zona)
    zona_period = zona_period.strftime('%H')

    global imagem

    zona_period = int(zona_period)

    if zona_period <= 5:
        imagem = Image.open(os.path.join(script_dir, 'images/lua.png'))
        fundo = fundo_noite
    elif zona_period <= 12:
        imagem = Image.open(os.path.join(script_dir, 'images/sol_dia.png'))
        fundo = fundo_dia
    elif zona_period <= 19:
        imagem = Image.open(os.path.join(script_dir, 'images/sol_tarde.png'))
        fundo = fundo_tarde
    elif zona_period <= 23:
        imagem = Image.open(os.path.join(script_dir, 'images/lua.png'))
        fundo = fundo_noite
    else:
        pass

    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_icone = Label(
        frame_corpo,
        image=imagem,
        bg=fundo,
    )
    l_icone.place(x=164, y=50)

    # fundos

    janela.configure(bg=fundo)
    frame_corpo.configure(bg=fundo)
    frame_top.configure(bg=fundo)

    l_cidade['bg'] = fundo
    l_data['bg'] = fundo
    l_umidade['bg'] = fundo
    l_pressao['bg'] = fundo
    l_umidadesim['bg'] = fundo
    l_vel['bg'] = fundo
    l_descricao['bg'] = fundo


# Frames
frame_top = Frame(
    width=320,
    height=50,
    bg=cor1,
    pady=0,
    padx=0
)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(
    width=320,
    height=300,
    bg=fundo,
    pady=12,
    padx=0
)
frame_corpo.grid(row=2, column=0, sticky=NW)

# Configurar o top

e_local = Entry(
    frame_top,
    width=20,
    justify='left',
    font=(None, 14),
    highlightthickness=1,
    relief='solid'
)
e_local.place(x=15, y=10)

b_ver = Button(
    frame_top,
    command=informacao,
    text='Ver clima',
    font=('Ivy 9 bold'),
    bg=cor1,
    fg=cor,
    relief='raised',
    overrelief=RIDGE
)
b_ver.place(x=250, y=10)


# Corpo do frame

l_cidade = Label(
    frame_corpo,
    text='',
    anchor='center',
    bg=fundo,
    fg=cor1,
    font=('Arial 14'),
)
l_cidade.place(x=10, y=4)

l_data = Label(
    frame_corpo,
    text='',
    anchor='center',
    bg=fundo,
    fg=cor1,
    font=('Arial 10'),
)
l_data.place(x=10, y=54)

l_umidade = Label(
    frame_corpo,
    text='',
    anchor='center',
    bg=fundo,
    fg=cor1,
    font=('Arial 45'),
)
l_umidade.place(x=10, y=100)

l_umidadesim = Label(
    frame_corpo,
    text='',
    anchor='center',
    bg=fundo,
    fg=cor1,
    font=('Arial 10 bold'),
)
l_umidadesim.place(x=85, y=110)

l_pressao = Label(
    frame_corpo,
    text='',
    anchor='center',
    bg=fundo,
    fg=cor1,
    font=('Arial 11'),
)
l_pressao.place(x=10, y=184)

l_vel = Label(
    frame_corpo,
    text='',
    anchor='center',
    bg=fundo,
    fg=cor1,
    font=('Arial 11'),
)
l_vel.place(x=10, y=212)


l_descricao = Label(
    frame_corpo,
    text='',
    anchor='center',
    bg=fundo,
    fg=cor1,
    font=('Arial 11'),
)
l_descricao.place(x=170, y=190)


janela.bind('<Return>', informacao)

janela.mainloop()

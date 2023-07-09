import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from IPython.display import display
import io
import folium
from geopy.geocoders import Nominatim
from fpdf import FPDF
import tempfile
from streamlit_drawable_canvas import st_canvas
import PIL.Image as Image
import io
import numpy as np

def save_image(image_data, file_path):
    if image_data is not None:
        img = Image.fromarray(image_data.astype("uint8"))
        img.save(file_path, format="PNG")
    
st.set_page_config(layout="wide")
def main():
    ruta_imagen = "/Users/mac/Desktop/IE/3_TERM/CAPSTONE/parte2.jpg"
    template = pd.read_excel("/Users/mac/Desktop/IE/3_TERM/CAPSTONE/template.xlsx")
    results = pd.read_excel("/Users/mac/Desktop/IE/3_TERM/CAPSTONE/subirfile.xlsx")
    imagen = Image.open(ruta_imagen)
    # Crear menú de navegación en la barra lateral izquierda
    menu = ["Use the template"]
    choice = st.sidebar.selectbox("Select an option", menu)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')
    with col2:
        st.image("data:image/png;base64,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",width=800)
    with col3:
        st.write(' ')
    
    if choice=="Use the template":
        imagen = Image.open(ruta_imagen)
        draw = ImageDraw.Draw(imagen)
        tamano_fuente = 35
        fuente = ImageFont.truetype("Arial.ttf", tamano_fuente)
        w,h=96,17
        imagen_buffer = io.BytesIO()

        st.title('Use the template')
#ENCABEZADOOOOOOOOOOO
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            text1 = st.text_input("Fecha del accidente")
            x,y=100,170
            if len(text1)>0:
                tamanio_primera_letra = draw.textsize(text1[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text1, fill=(0, 0, 0), font=fuente)
                results.at[0, 'text'] = text1
                results.at[0, 'x'] = x
                results.at[0, 'y'] = y

        with col2:
            text2 = st.text_input("Hora")
            x,y=440,170
            if len(text2)>0:
                tamanio_primera_letra = draw.textsize(text2[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text2, fill=(0, 0, 0), font=fuente)
                results.at[1, 'text'] = text2
                results.at[1, 'x'] = x
                results.at[1, 'y'] = y
        with col3:
            text3 = st.text_input("Localización: País")
            x,y=680,170
            if len(text3)>0:
                tamanio_primera_letra = draw.textsize(text3[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text3, fill=(0, 0, 0), font=fuente)
                results.at[2, 'text'] = text3
                results.at[2, 'x'] = x
                results.at[2, 'y'] = y
        with col4:
            text4 = st.text_input("Localización: Lugar")
            x,y=900,170
            if len(text4)>0:
                tamanio_primera_letra = draw.textsize(text4[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text4, fill=(0, 0, 0), font=fuente)
                results.at[7, 'text'] = text4
                results.at[7, 'x'] = x
                results.at[7, 'y'] = y
        with col5:
            option = st.radio("¿Víctimas incluso leves?", ("Sí", "No"), index=1)
            if option == "Sí":
                text="X"
                x,y=1670,170
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[9, 'text'] = text
                results.at[9, 'x'] = x
                results.at[9, 'y'] = y
            else:
                text="X"
                x,y=1490,170
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[8, 'text'] = text
                results.at[8, 'x'] = x
                results.at[8, 'y'] = y
     
        col1, col2, col3 = st.columns(3)
        with col1:
            option = st.radio("Daños materiales vehículos", ("Sí", "No"), index=1)
            if option == "Sí":
                text="X"
                x,y=313,335
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[5, 'text'] = text
                results.at[5, 'x'] = x
                results.at[5, 'y'] = y
            else:
                text="X"
                x,y=135,335
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[6, 'text'] = text
                results.at[6, 'x'] = x
                results.at[6, 'y'] = y
     
        with col2:
            option = st.radio("Daños materiales objetos", ("Sí", "No"), index=1)
            if option == "Sí":
                text="X"
                x,y=710,335
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[3, 'text'] = text
                results.at[3, 'x'] = x
                results.at[3, 'y'] = y
            else:
                text="X"
                x,y=530,335
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[4, 'text'] = text
                results.at[4, 'x'] = x
                results.at[4, 'y'] = y
        with col3:
            text5 = st.text_input("Testigos,nombre,dirección,tel.")
            x,y=860,280
            if len(text5)>0:
                tamanio_primera_letra = draw.textsize(text5[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text5, fill=(0, 0, 0), font=fuente)
                results.at[10, 'text'] = text5
                results.at[10, 'x'] = x
                results.at[10, 'y'] = y

#PARTE DEL MEDIOOOOOOOOOOOOOO 
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h2 style='font-size: 30px;'>Vehículo A</h2>", unsafe_allow_html=True)
            st.write("**Asegurado**")
            text6 = st.text_input("Nombre A")
            x,y=200,550
            if len(text6)>0:
                tamanio_primera_letra = draw.textsize(text6[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text6, fill=(0, 0, 0), font=fuente)
                results.at[11, 'text'] = text6
                results.at[11, 'x'] = x
                results.at[11, 'y'] = y
            text7 = st.text_input("Apellidos A")
            x,y=200,600
            if len(text7)>0:
                tamanio_primera_letra = draw.textsize(text7[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text7, fill=(0, 0, 0), font=fuente)
                results.at[12, 'text'] = text7
                results.at[12, 'x'] = x
                results.at[12, 'y'] = y
            text8 = st.text_input("Dirección A")
            x,y=200,650
            if len(text8)>0:
                tamanio_primera_letra = draw.textsize(text8[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text8, fill=(0, 0, 0), font=fuente)
                results.at[13, 'text'] = text8
                results.at[13, 'x'] = x
                results.at[13, 'y'] = y
            text9 = st.text_input("Código Postal A")
            x,y=250,700
            if len(text9)>0:
                tamanio_primera_letra = draw.textsize(text9[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text9, fill=(0, 0, 0), font=fuente)
                results.at[14, 'text'] = text9
                results.at[14, 'x'] = x
                results.at[14, 'y'] = y
            text10 = st.text_input("País A")
            x,y=500,700
            if len(text10)>0:
                tamanio_primera_letra = draw.textsize(text10[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text10, fill=(0, 0, 0), font=fuente)
                results.at[15, 'text'] = text10
                results.at[15, 'x'] = x
                results.at[15, 'y'] = y
            text11 = st.text_input("Tel. o E-mail A")
            x,y=250,760
            if len(text11)>0:
                tamanio_primera_letra = draw.textsize(text11[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text11, fill=(0, 0, 0), font=fuente)
                results.at[16, 'text'] = text11
                results.at[16, 'x'] = x
                results.at[16, 'y'] = y
                
            st.write("**Vehículo**")
            col5,col6=st.columns(2)
            with col5:
                text12 = st.text_input("Marca, modelo del vehículo motor A")
                x,y=80,960
                if len(text12)>0:
                    tamanio_primera_letra = draw.textsize(text12[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text12, fill=(0, 0, 0), font=fuente)
                    results.at[17, 'text'] = text12
                    results.at[17, 'x'] = x
                    results.at[17, 'y'] = y
                
                text13= st.text_input("Matrícula (o bastidor) del vehículo motor A")
                x,y=80,1060
                if len(text13)>0:
                    tamanio_primera_letra = draw.textsize(text13[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text13, fill=(0, 0, 0), font=fuente)
                    results.at[18, 'text'] = text13
                    results.at[18, 'x'] = x
                    results.at[18, 'y'] = y
                text14= st.text_input("País de matrícula del vehículo motor A")
                x,y=80,1145
                if len(text14)>0:
                    tamanio_primera_letra = draw.textsize(text14[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text14, fill=(0, 0, 0), font=fuente)
                    results.at[19, 'text'] = text14
                    results.at[19, 'x'] = x
                    results.at[19, 'y'] = y
            with col6:
                st.write(" ")
                text15 = st.text_input("Matrícula (o bastidor) del remolque A")
                x,y=480,1060
                if len(text15)>0:
                    tamanio_primera_letra = draw.textsize(text15[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text15, fill=(0, 0, 0), font=fuente)
                    results.at[20, 'text'] = text15
                    results.at[20, 'x'] = x
                    results.at[20, 'y'] = y
                text16= st.text_input("País de matrícula del remolque A")  
                x,y=480,1145
                if len(text16)>0:
                    tamanio_primera_letra = draw.textsize(text16[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text16, fill=(0, 0, 0), font=fuente)
                    results.at[21, 'text'] = text16
                    results.at[21, 'x'] = x
                    results.at[21, 'y'] = y

            st.write("**Aseguradora**")
            text17 = st.text_input("Nombre aseguradora A")
            x,y=200,1260
            if len(text17)>0:
                tamanio_primera_letra = draw.textsize(text17[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text17, fill=(0, 0, 0), font=fuente)
                results.at[22, 'text'] = text17
                results.at[22, 'x'] = x
                results.at[22, 'y'] = y
            text18= st.text_input("Número de póliza A")
            x,y=240,1310
            if len(text18)>0:
                tamanio_primera_letra = draw.textsize(text18[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text18, fill=(0, 0, 0), font=fuente)
                results.at[23, 'text'] = text18
                results.at[23, 'x'] = x
                results.at[23, 'y'] = y
            text19= st.text_input("Número de carta verde A")
            x,y=320,1360
            if len(text19)>0:
                tamanio_primera_letra = draw.textsize(text19[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text19, fill=(0, 0, 0), font=fuente)
                results.at[24, 'text'] = text19
                results.at[24, 'x'] = x
                results.at[24, 'y'] = y

            col5,col6=st.columns(2)
            with col5:
                text20= st.text_input("Válida desde A")
                x,y=480,1440
                if len(text20)>0:
                    tamanio_primera_letra = draw.textsize(text20[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text20, fill=(0, 0, 0), font=fuente)
                    results.at[25, 'text'] = text20
                    results.at[25, 'x'] = x
                    results.at[25, 'y'] = y
            with col6:
                text21 = st.text_input("Válida hasta A")
                x,y=700,1440
                if len(text21)>0:
                    tamanio_primera_letra = draw.textsize(text21[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text21, fill=(0, 0, 0), font=fuente)
                    results.at[26, 'text'] = text21
                    results.at[26, 'x'] = x
                    results.at[26, 'y'] = y
            text22= st.text_input("Agencia (oficina o corredor) A")
            x,y=430,1485
            if len(text22)>0:
                tamanio_primera_letra = draw.textsize(text22[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text22, fill=(0, 0, 0), font=fuente)
                results.at[27, 'text'] = text22
                results.at[27, 'x'] = x
                results.at[27, 'y'] = y
            text23= st.text_input("Nombre Agencia A")
            x,y=180,1530
            if len(text23)>0:
                tamanio_primera_letra = draw.textsize(text23[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text23, fill=(0, 0, 0), font=fuente)
                results.at[28, 'text'] = text23
                results.at[28, 'x'] = x
                results.at[28, 'y'] = y
            text24= st.text_input("Dirección Agencía A")
            x,y=200,1580
            if len(text24)>0:
                tamanio_primera_letra = draw.textsize(text24[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text24, fill=(0, 0, 0), font=fuente)
                results.at[29, 'text'] = text24
                results.at[29, 'x'] = x
                results.at[29, 'y'] = y
            text25= st.text_input("País de la Agencia A")
            x,y=470,1630
            if len(text25)>0:
                tamanio_primera_letra = draw.textsize(text25[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text25, fill=(0, 0, 0), font=fuente)
                results.at[30, 'text'] = text25
                results.at[30, 'x'] = x
                results.at[30, 'y'] = y
            text26= st.text_input("Tel. o E-mail de la Agencia A")
            x,y=250,1690
            if len(text26)>0:
                tamanio_primera_letra = draw.textsize(text26[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text26, fill=(0, 0, 0), font=fuente)
                results.at[31, 'text'] = text26
                results.at[31, 'x'] = x
                results.at[31, 'y'] = y
            option = st.radio("¿Los daños propios del vehículo A están asegurados", ("Sí", "No"), index=1)
            if option == "Sí":
                text="X"
                x,y=515,1800
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[33, 'text'] = text
                results.at[33, 'x'] = x
                results.at[33, 'y'] = y
            else:
                text="X"
                x,y=300,1800
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[32, 'text'] = text
                results.at[32, 'x'] = x
                results.at[32, 'y'] = y

            st.write("**Conductor**")                          
            text27= st.text_input("Nombre del conductor A")
            x,y=200,1922
            if len(text27)>0:
                tamanio_primera_letra = draw.textsize(text27[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text27, fill=(0, 0, 0), font=fuente)
                results.at[34, 'text'] = text27
                results.at[34, 'x'] = x
                results.at[34, 'y'] = y
            text28= st.text_input("Apellidos del conductor A") 
            x,y=200,1972
            if len(text28)>0:
                tamanio_primera_letra = draw.textsize(text28[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text28, fill=(0, 0, 0), font=fuente)
                results.at[35, 'text'] = text28
                results.at[35, 'x'] = x
                results.at[35, 'y'] = y
            text29= st.text_input("Fecha de nacimiento del conductor A")
            x,y=350,2025
            if len(text29)>0:
                tamanio_primera_letra = draw.textsize(text29[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text29, fill=(0, 0, 0), font=fuente)
                results.at[36, 'text'] = text29
                results.at[36, 'x'] = x
                results.at[36, 'y'] = y
            text30= st.text_input("Dirección del conductor A")
            x,y=230,2075
            if len(text30)>0:
                tamanio_primera_letra = draw.textsize(text30[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text30, fill=(0, 0, 0), font=fuente)
                results.at[37, 'text'] = text30
                results.at[37, 'x'] = x
                results.at[37, 'y'] = y
            text31= st.text_input("País del conductor A")   
            x,y=500,2125
            if len(text31)>0:
                tamanio_primera_letra = draw.textsize(text31[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text31, fill=(0, 0, 0), font=fuente)
                results.at[38, 'text'] = text31
                results.at[38, 'x'] = x
                results.at[38, 'y'] = y
            text32= st.text_input("Tel. o E-mail del conductor A")
            x,y=250,2185
            if len(text32)>0:
                tamanio_primera_letra = draw.textsize(text32[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text32, fill=(0, 0, 0), font=fuente)
                results.at[39, 'text'] = text32
                results.at[39, 'x'] = x
                results.at[39, 'y'] = y
            text33= st.text_input("Permiso de conducir A")
            x,y=390,2230
            if len(text33)>0:
                tamanio_primera_letra = draw.textsize(text33[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text33, fill=(0, 0, 0), font=fuente)
                results.at[40, 'text'] = text33
                results.at[40, 'x'] = x
                results.at[40, 'y'] = y
            text34= st.text_input("Categoría del permiso de conducir A")   
            x,y=350,2280
            if len(text34)>0:
                tamanio_primera_letra = draw.textsize(text34[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text34, fill=(0, 0, 0), font=fuente)
                results.at[41, 'text'] = text34
                results.at[41, 'x'] = x
                results.at[41, 'y'] = y
            text35= st.text_input("Permiso del conductor A válido hasta")  
            x,y=350,2330
            if len(text35)>0:
                tamanio_primera_letra = draw.textsize(text35[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text35, fill=(0, 0, 0), font=fuente)
                results.at[42, 'text'] = text35
                results.at[42, 'x'] = x
                results.at[42, 'y'] = y
            text66= st.text_input("Daños apreciado al vehículo A")   
            x,y=70,2940
            if len(text66)>0:
                tamanio_primera_letra = draw.textsize(text66[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text66, fill=(0, 0, 0), font=fuente)
                results.at[43, 'text'] = text66
                results.at[43, 'x'] = x
                results.at[43, 'y'] = y

        with col2:
            st.markdown("<h2 style='font-size: 30px;'>Circunstancias</h2>", unsafe_allow_html=True)
            col7,col8,col9=st.columns(3)

            with col7:
                st.markdown("<h2 style='font-size: 15px;'>Vehículo A</h2>", unsafe_allow_html=True)
                option = st.checkbox("", key=1)
                if option:
                    text="X"
                    x,y=865,615
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[77, 'text'] = text
                    results.at[77, 'x'] = x
                    results.at[77, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=2)
                if option:
                    text="X"
                    x,y=865,660
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[78, 'text'] = text
                    results.at[78, 'x'] = x
                    results.at[78, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=3)
                if option:
                    text="X"
                    x,y=865,760
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[79, 'text'] = text
                    results.at[79, 'x'] = x
                    results.at[79, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=4)
                if option:
                    text="X"
                    x,y=865,825
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[80, 'text'] = text
                    results.at[80, 'x'] = x
                    results.at[80, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=5)
                if option:
                    text="X"
                    x,y=865,925
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[81, 'text'] = text
                    results.at[81, 'x'] = x
                    results.at[81, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=6)
                if option:
                    text="X"
                    x,y=865,1025
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[82, 'text'] = text
                    results.at[82, 'x'] = x
                    results.at[82, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=7)
                if option:
                    text="X"
                    x,y=865,1125
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[83, 'text'] = text
                    results.at[83, 'x'] = x
                    results.at[83, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=8)
                if option:
                    text="X"
                    x,y=865,1230
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[84, 'text'] = text
                    results.at[84, 'x'] = x
                    results.at[84, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=9)
                if option:
                    text="X"
                    x,y=865,1370
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[85, 'text'] = text
                    results.at[85, 'x'] = x
                    results.at[85, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=10)
                if option:
                    text="X"
                    x,y=865,1470
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[86, 'text'] = text
                    results.at[86, 'x'] = x
                    results.at[86, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=11)
                if option:
                    text="X"
                    x,y=865,1530
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[87, 'text'] = text
                    results.at[87, 'x'] = x
                    results.at[87, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=12)
                if option:
                    text="X"
                    x,y=865,1595
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[88, 'text'] = text
                    results.at[88, 'x'] = x
                    results.at[88, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=13)
                if option:
                    text="X"
                    x,y=865,1655
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[89, 'text'] = text
                    results.at[89, 'x'] = x
                    results.at[89, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=14)
                if option:
                    text="X"
                    x,y=865,1720
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[90, 'text'] = text
                    results.at[90, 'x'] = x
                    results.at[90, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=15)
                if option:
                    text="X"
                    x,y=865,1780
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[91, 'text'] = text
                    results.at[91, 'x'] = x
                    results.at[91, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=16)
                if option:
                    text="X"
                    x,y=865,1920
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[92, 'text'] = text
                    results.at[92, 'x'] = x
                    results.at[92, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=17)
                if option:
                    text="X"
                    x,y=865,2020
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[93, 'text'] = text
                    results.at[93, 'x'] = x
                    results.at[93, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)
                text68= st.text_input("",key=50)  
                x,y=860,2120
                if len(text68)>0:
                    tamanio_primera_letra = draw.textsize(text68[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text68, fill=(0, 0, 0), font=fuente)
                    results.at[94, 'text'] = text68
                    results.at[94, 'x'] = x
                    results.at[94, 'y'] = y
            
            with col8:
                st.markdown("<h2 style='font-size: 15px;'>Marcar casilla</h2>", unsafe_allow_html=True)
                st.write("Estaba estacionado/parado")
                st.markdown("<br>" * 1, unsafe_allow_html=True)
                st.write("Salía de un estacionamiento/abriendo puerta")
                st.markdown("<br>" * 1, unsafe_allow_html=True)
                st.write("Iba a estacionar")
                st.markdown("<br>" * 1, unsafe_allow_html=True)
                st.write("Salía de un aparcamiento, de un lugar privado, a un camino de tierra")
                st.write("Entraba a un aparcamiento, a un lugar privado, a un camino de tierra")
                st.write("Entraba a una plaza de sentido giratorio")
                st.markdown("<br>" * 1, unsafe_allow_html=True)
                st.write("Circulaba por una plaza de sentido giratorio")
                st.write("Colisionó en la parte de atrás al otro vehículo que circulaba en el mismo sentido y en el mismo carril")
                st.write("Circulaba en el mismo sentido y en carril diferente")
                st.markdown("<br>" * 1, unsafe_allow_html=True)
                st.write("Cambiaba de carril")
                st.markdown("<br>" * 2, unsafe_allow_html=True)
                st.write("Adelantaba")
                st.markdown("<br>" * 2, unsafe_allow_html=True)
                st.write("Giraba a la derecha")
                st.markdown("<br>" * 2, unsafe_allow_html=True)
                st.write("Giraba a la izquierda")
                st.markdown("<br>" * 2, unsafe_allow_html=True)
                st.write("Daba marcha atrás")
                st.markdown("<br>" * 1, unsafe_allow_html=True)
                st.write("Invadía la parte reservada a la circulación en sentido inverso")
                st.write("Venía a la derecha (en un cruce)")
                st.markdown("<br>" * 1, unsafe_allow_html=True)
                st.write("No respetó la señal de preferencia o semáforo en rojo")
                st.markdown("<br>" * 2, unsafe_allow_html=True)
                st.write("Indicar número de casillas marcadas")
            
            with col9:
                st.markdown("<h2 style='font-size: 15px;'>Vehículo B</h2>", unsafe_allow_html=True)
                option = st.checkbox("", key=18)
                if option:
                    text="X"
                    x,y=1455,615
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[96, 'text'] = text
                    results.at[96, 'x'] = x
                    results.at[96, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=19)
                if option:
                    text="X"
                    x,y=1455,660
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[97, 'text'] = text
                    results.at[97, 'x'] = x
                    results.at[97, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=20)
                if option:
                    text="X"
                    x,y=1455,760
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[98, 'text'] = text
                    results.at[98, 'x'] = x
                    results.at[98, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=21)
                if option:
                    text="X"
                    x,y=1455,825
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[99, 'text'] = text
                    results.at[99, 'x'] = x
                    results.at[99, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=22)
                if option:
                    text="X"
                    x,y=1455,925
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[100, 'text'] = text
                    results.at[100, 'x'] = x
                    results.at[100, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=23)
                if option:
                    text="X"
                    x,y=1455,1025
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[101, 'text'] = text
                    results.at[101, 'x'] = x
                    results.at[101, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=24)
                if option:
                    text="X"
                    x,y=1455,1125
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[102, 'text'] = text
                    results.at[102, 'x'] = x
                    results.at[102, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=25)
                if option:
                    text="X"
                    x,y=1455,1230
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[103, 'text'] = text
                    results.at[103, 'x'] = x
                    results.at[103, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=26)
                if option:
                    text="X"
                    x,y=1455,1370
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[104, 'text'] = text
                    results.at[104, 'x'] = x
                    results.at[104, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=27)
                if option:
                    text="X"
                    x,y=1455,1470
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[105, 'text'] = text
                    results.at[105, 'x'] = x
                    results.at[105, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=28)
                if option:
                    text="X"
                    x,y=1455,1530
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[106, 'text'] = text
                    results.at[106, 'x'] = x
                    results.at[106, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=29)
                if option:
                    text="X"
                    x,y=1455,1595
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[107, 'text'] = text
                    results.at[107, 'x'] = x
                    results.at[107, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=30)
                if option:
                    text="X"
                    x,y=1455,1655
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[108, 'text'] = text
                    results.at[108, 'x'] = x
                    results.at[108, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=31)
                if option:
                    text="X"
                    x,y=1455,1720
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[109, 'text'] = text
                    results.at[109, 'x'] = x
                    results.at[109, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=32)
                if option:
                    text="X"
                    x,y=1455,1780
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[110, 'text'] = text
                    results.at[110, 'x'] = x
                    results.at[110, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=33)
                if option:
                    text="X"
                    x,y=1455,1920
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[111, 'text'] = text
                    results.at[111, 'x'] = x
                    results.at[111, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)

                option = st.checkbox("", key=34)
                if option:
                    text="X"
                    x,y=1455,2020
                    tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                    results.at[112, 'text'] = text
                    results.at[112, 'x'] = x
                    results.at[112, 'y'] = y
                st.markdown("<br>" * 2, unsafe_allow_html=True)
                text69= st.text_input("",key=51)
                x,y=1450,2120
                if len(text69)>0:
                    tamanio_primera_letra = draw.textsize(text69[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text69, fill=(0, 0, 0), font=fuente)
                    results.at[95, 'text'] = text69
                    results.at[95, 'x'] = x
                    results.at[95, 'y'] = y


        with col3:
            st.markdown("<h2 style='font-size: 30px;'>Vehículo B</h2>", unsafe_allow_html=True)
            st.write("**Asegurado**")
            text36 = st.text_input("Nombre B")
            x,y=1650,550
            if len(text36)>0:
                tamanio_primera_letra = draw.textsize(text36[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text36, fill=(0, 0, 0), font=fuente)
                results.at[44, 'text'] = text36
                results.at[44, 'x'] = x
                results.at[44, 'y'] = y
            text37= st.text_input("Apellidos B")
            x,y=1650,600
            if len(text37)>0:
                tamanio_primera_letra = draw.textsize(text37[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text37, fill=(0, 0, 0), font=fuente)
                results.at[45, 'text'] = text37
                results.at[45, 'x'] = x
                results.at[45, 'y'] = y
            text38= st.text_input("Dirección B")
            x,y=1650,650
            if len(text38)>0:
                tamanio_primera_letra = draw.textsize(text38[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text38, fill=(0, 0, 0), font=fuente)
                results.at[46, 'text'] = text38
                results.at[46, 'x'] = x
                results.at[46, 'y'] = y
            text39= st.text_input("Código Postal B")
            x,y=1700,700
            if len(text39)>0:
                tamanio_primera_letra = draw.textsize(text39[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text39, fill=(0, 0, 0), font=fuente)
                results.at[47, 'text'] = text39
                results.at[47, 'x'] = x
                results.at[47, 'y'] = y
            text40 = st.text_input("País B")
            x,y=1950,700
            if len(text40)>0:
                tamanio_primera_letra = draw.textsize(text40[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text40, fill=(0, 0, 0), font=fuente)
                results.at[48, 'text'] = text40
                results.at[48, 'x'] = x
                results.at[48, 'y'] = y
            text41 = st.text_input("Tel. o E-mail B")
            x,y=1700,760
            if len(text41)>0:
                tamanio_primera_letra = draw.textsize(text41[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text41, fill=(0, 0, 0), font=fuente)
                results.at[49, 'text'] = text41
                results.at[49, 'x'] = x
                results.at[49, 'y'] = y

            st.write("**Vehículo**")
            col5,col6=st.columns(2)
            with col5:
                text42 = st.text_input("Marca, modelo del vehículo motor B")
                x,y=1550,960
                if len(text42)>0:
                    tamanio_primera_letra = draw.textsize(text42[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text42, fill=(0, 0, 0), font=fuente)
                    results.at[50, 'text'] = text42
                    results.at[50, 'x'] = x
                    results.at[50, 'y'] = y
                text43= st.text_input("Matrícula (o bastidor) del vehículo motor B")
                x,y=1550,1060
                if len(text43)>0:
                    tamanio_primera_letra = draw.textsize(text43[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text43, fill=(0, 0, 0), font=fuente)
                    results.at[51, 'text'] = text43
                    results.at[51, 'x'] = x
                    results.at[51, 'y'] = y
                text44= st.text_input("País de matrícula del vehículo motor B")
                x,y=1550,1145
                if len(text44)>0:
                    tamanio_primera_letra = draw.textsize(text44[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text44, fill=(0, 0, 0), font=fuente)
                    results.at[52, 'text'] = text44
                    results.at[52, 'x'] = x
                    results.at[52, 'y'] = y
            with col6:
                st.write(" ")
                text45 = st.text_input("Matrícula (o bastidor) del remolque B")
                x,y=1950,1060
                if len(text45)>0:
                    tamanio_primera_letra = draw.textsize(text45[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text45, fill=(0, 0, 0), font=fuente)
                    results.at[53, 'text'] = text45
                    results.at[53, 'x'] = x
                    results.at[53, 'y'] = y
                text46= st.text_input("País de matrícula del remolque B") 
                x,y=1950,1145
                if len(text46)>0:
                    tamanio_primera_letra = draw.textsize(text46[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text46, fill=(0, 0, 0), font=fuente)
                    results.at[54, 'text'] = text46
                    results.at[54, 'x'] = x
                    results.at[54, 'y'] = y

            st.write("**Aseguradora**")
            text47 = st.text_input("Nombre aseguradora B")
            x,y=1650,1260
            if len(text47)>0:
                tamanio_primera_letra = draw.textsize(text47[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text47, fill=(0, 0, 0), font=fuente)
                results.at[55, 'text'] = text47
                results.at[55, 'x'] = x
                results.at[55, 'y'] = y
            text48= st.text_input("Número de póliza B")
            x,y=1700,1310
            if len(text48)>0:
                tamanio_primera_letra = draw.textsize(text48[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text48, fill=(0, 0, 0), font=fuente)
                results.at[56, 'text'] = text48
                results.at[56, 'x'] = x
                results.at[56, 'y'] = y
            text49= st.text_input("Número de carta verde B")
            x,y=1770,1360
            if len(text49)>0:
                tamanio_primera_letra = draw.textsize(text49[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text49, fill=(0, 0, 0), font=fuente)
                results.at[57, 'text'] = text49
                results.at[57, 'x'] = x
                results.at[57, 'y'] = y

            col5,col6=st.columns(2)
            with col5:
                text50= st.text_input("Válida desde B")
                x,y=1960,1440
                if len(text50)>0:
                    tamanio_primera_letra = draw.textsize(text50[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text50, fill=(0, 0, 0), font=fuente)
                    results.at[58, 'text'] = text50
                    results.at[58, 'x'] = x
                    results.at[58, 'y'] = y
                
            with col6:
                text51 = st.text_input("Válida hasta B")
                x,y=2160,1440
                if len(text51)>0:
                    tamanio_primera_letra = draw.textsize(text51[0], font=fuente)
                    x_texto = x + (w - tamanio_primera_letra[0])
                    y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                    draw.text((x_texto, y_texto), text51, fill=(0, 0, 0), font=fuente)
                    results.at[59, 'text'] = text51
                    results.at[59, 'x'] = x
                    results.at[59, 'y'] = y

            text52= st.text_input("Agencia (oficina o corredor) B")
            x,y=1900,1485
            if len(text52)>0:
                tamanio_primera_letra = draw.textsize(text52[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text52, fill=(0, 0, 0), font=fuente)
                results.at[60, 'text'] = text52
                results.at[60, 'x'] = x
                results.at[60, 'y'] = y
            text53= st.text_input("Nombre Agencia B")    
            x,y=1700,1530
            if len(text53)>0:
                tamanio_primera_letra = draw.textsize(text53[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text53, fill=(0, 0, 0), font=fuente)
                results.at[61, 'text'] = text53
                results.at[61, 'x'] = x
                results.at[61, 'y'] = y
            text54= st.text_input("Dirección Agencía B")
            x,y=1700,1580
            if len(text54)>0:
                tamanio_primera_letra = draw.textsize(text54[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text54, fill=(0, 0, 0), font=fuente)
                results.at[62, 'text'] = text54
                results.at[62, 'x'] = x
                results.at[62, 'y'] = y
            text55= st.text_input("País de la Agencia B")
            x,y=1950,1630
            if len(text55)>0:
                tamanio_primera_letra = draw.textsize(text55[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text55, fill=(0, 0, 0), font=fuente)
                results.at[63, 'text'] = text55
                results.at[63, 'x'] = x
                results.at[63, 'y'] = y
            text56= st.text_input("Tel. o E-mail de la Agencia B") 
            x,y=1700,1690
            if len(text56)>0:
                tamanio_primera_letra = draw.textsize(text56[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text56, fill=(0, 0, 0), font=fuente)
                results.at[64, 'text'] = text56
                results.at[64, 'x'] = x
                results.at[64, 'y'] = y
            option = st.radio("¿Los daños propios del vehículo B están asegurados", ("Sí", "No"), index=1)
            if option == "Sí":
                text="X"
                x,y=1977,1800
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[66, 'text'] = text
                results.at[66, 'x'] = x
                results.at[66, 'y'] = y
            else:
                text="X"
                x,y=1760,1800
                tamanio_primera_letra = draw.textsize(text[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text, fill=(0, 0, 0), font=fuente)
                results.at[65, 'text'] = text
                results.at[65, 'x'] = x
                results.at[65, 'y'] = y

            st.write("**Conductor**")                          
            text57= st.text_input("Nombre del conductor B")
            x,y=1650,1922
            if len(text57)>0:
                tamanio_primera_letra = draw.textsize(text57[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text57, fill=(0, 0, 0), font=fuente)
                results.at[67, 'text'] = text57
                results.at[67, 'x'] = x
                results.at[67, 'y'] = y
            text58= st.text_input("Apellidos del conductor B")
            x,y=1650,1977
            if len(text58)>0:
                tamanio_primera_letra = draw.textsize(text58[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text58, fill=(0, 0, 0), font=fuente)
                results.at[68, 'text'] = text58
                results.at[68, 'x'] = x
                results.at[68, 'y'] = y
            text59= st.text_input("Fecha de nacimiento del conductor B")
            x,y=1800,2025
            if len(text59)>0:
                tamanio_primera_letra = draw.textsize(text59[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text59, fill=(0, 0, 0), font=fuente)
                results.at[69, 'text'] = text59
                results.at[69, 'x'] = x
                results.at[69, 'y'] = y
            text60= st.text_input("Dirección del conductor B")
            x,y=1650,2075
            if len(text60)>0:
                tamanio_primera_letra = draw.textsize(text60[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text60, fill=(0, 0, 0), font=fuente)
                results.at[70, 'text'] = text60
                results.at[70, 'x'] = x
                results.at[70, 'y'] = y
            text61= st.text_input("País del conductor B")   
            x,y=1950,2125
            if len(text61)>0:
                tamanio_primera_letra = draw.textsize(text61[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text61, fill=(0, 0, 0), font=fuente)
                results.at[71, 'text'] = text61
                results.at[71, 'x'] = x
                results.at[71, 'y'] = y
            text62= st.text_input("Tel. o E-mail del conductor B")
            x,y=1700,2185
            if len(text62)>0:
                tamanio_primera_letra = draw.textsize(text62[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text62, fill=(0, 0, 0), font=fuente)
                results.at[72, 'text'] = text62
                results.at[72, 'x'] = x
                results.at[72, 'y'] = y
            text63= st.text_input("Permiso de conducir B")
            x,y=1850,2230
            if len(text63)>0:
                tamanio_primera_letra = draw.textsize(text63[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text63, fill=(0, 0, 0), font=fuente)
                results.at[73, 'text'] = text63
                results.at[73, 'x'] = x
                results.at[73, 'y'] = y
            text64= st.text_input("Categoría del permiso de conducir B")   
            x,y=1800,2280
            if len(text64)>0:
                tamanio_primera_letra = draw.textsize(text64[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text64, fill=(0, 0, 0), font=fuente)
                results.at[74, 'text'] = text64
                results.at[74, 'x'] = x
                results.at[74, 'y'] = y
            text65= st.text_input("Permiso del conductor B válido hasta")
            x,y=1800,2330
            if len(text65)>0:
                tamanio_primera_letra = draw.textsize(text65[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text65, fill=(0, 0, 0), font=fuente)
                results.at[75, 'text'] = text65
                results.at[75, 'x'] = x
                results.at[75, 'y'] = y
            text67= st.text_input("Daños apreciado al vehículo B")   
            x,y=1900,2940
            if len(text67)>0:
                tamanio_primera_letra = draw.textsize(text67[0], font=fuente)
                x_texto = x + (w - tamanio_primera_letra[0])
                y_texto = y + (h - tamanio_primera_letra[1]) // 2 
                draw.text((x_texto, y_texto), text67, fill=(0, 0, 0), font=fuente)
                results.at[76, 'text'] = text67
                results.at[76, 'x'] = x
                results.at[76, 'y'] = y

        nombre_calle = st.text_input("Ingresa el nombre de la calle: ")
        nombre_ciudad = st.text_input("Ingresa el nombre de la ciudad: ")

        col1,col2=st.columns(2)
        with col1:
            uploaded_file_vehículo_a = st.file_uploader("Sube una foto del vehículo A", type=["png", "jpg", "jpeg"])
        with col2:
            uploaded_file_vehículo_b = st.file_uploader("Sube una foto del vehículo B", type=["png", "jpg", "jpeg"])
        
        color = st.color_picker("Color", "#000000")
        size = st.slider("Size", 1, 20, 2)

        canvas_result = st_canvas(
                key="canvas",
                width=680,
                height=470,
                drawing_mode="freedraw",
                stroke_width=size,
                stroke_color=color,
                background_color="white",
                update_streamlit=True,
            )
        

        if st.button("Cargar"):
            st.image(imagen, caption='Parte del accidente')

            geolocator = Nominatim(user_agent="my-app")
            ubicacion = geolocator.geocode(nombre_calle + ', ' + nombre_ciudad)

            if ubicacion is not None:
                mapa = folium.Map(location=[ubicacion.latitude, ubicacion.longitude], zoom_start=18, control_scale=True)
                folium.Marker([ubicacion.latitude, ubicacion.longitude], popup=nombre_calle).add_to(mapa)
                maps = mapa._to_png()
                if maps is not None:
                    st.image(maps, caption='Localizacion')

            if uploaded_file_vehículo_a is not None:
                image_a = uploaded_file_vehículo_a.read()
            if uploaded_file_vehículo_b is not None:
                image_b = uploaded_file_vehículo_b.read()
            
            col1,col2=st.columns(2)
            with col1:
                if uploaded_file_vehículo_a is not None:
                    st.image(image_a, caption='Vehículo A',width=600)
            with col2:
                if uploaded_file_vehículo_b is not None:
                    st.image(image_b, caption='Vehículo B',width=600)
        
        if st.button("Save"):
            pdf = FPDF(format='A4')

            with tempfile.NamedTemporaryFile(suffix='.jpg') as tmp:
                imagen.save(tmp.name)
                pdf.add_page()
                pdf.image(tmp.name, x=10, y=10, w=190)

            geolocator = Nominatim(user_agent="my-app")
            ubicacion = geolocator.geocode(nombre_calle + ', ' + nombre_ciudad)

            file_path = "draw.jpg"
            save_image(np.array(canvas_result.image_data), file_path)
            esq=Image.open("draw.jpg")
            if esq is not None:
                with tempfile.NamedTemporaryFile(suffix='.jpg') as tmp:
                    esq = esq.convert("RGB")
                    esq.save(tmp.name)
                    pdf.image(tmp.name, x=52, y=194, w=106.5,h=52)

            if ubicacion is not None:
                mapa = folium.Map(location=[ubicacion.latitude, ubicacion.longitude], zoom_start=18, control_scale=True)
                folium.Marker([ubicacion.latitude, ubicacion.longitude], popup=nombre_calle).add_to(mapa)
                maps = mapa._to_png()
                if maps is not None:
                    mapas = Image.open(io.BytesIO(maps))
                    mapas = mapas.convert("RGB")
                    with tempfile.NamedTemporaryFile(suffix='.jpg') as tmp:
                        mapas.save(tmp.name)
                        pdf.add_page()
                        pdf.image(tmp.name, x=10, y=10, w=190)

            if uploaded_file_vehículo_a is not None:
                image_a = uploaded_file_vehículo_a.read()
                with tempfile.NamedTemporaryFile(suffix='.jpg') as tmp:
                    tmp.write(image_a)
                    pdf.set_font("Arial", size=12)
                    pdf.cell(80, 230, "Vehículo A", ln=True, align="C")
                    pdf.image(tmp.name, x=10, y=130, w=80)

            if uploaded_file_vehículo_b is not None:
                image_b = uploaded_file_vehículo_b.read()
                with tempfile.NamedTemporaryFile(suffix='.jpg') as tmp:
                    tmp.write(image_b)
                    pdf.set_font("Arial", size=12)
                    pdf.cell(300, -230, "Vehículo B", ln=True, align="C")
                    pdf.image(tmp.name, x=120, y=130, w=80)

            pdf.output('final.pdf')
            results.to_csv('final.csv', index=False)
            st.write("El pdf se ha guardado exitósamente")
            
if __name__ == '__main__':
    main()

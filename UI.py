from tkinter import *
from exportdata import *
from datetime import datetime 
import pytz

def run():
    
    # Update time
    dt = datetime.now(pytz.timezone('Asia/Tokyo'))
    timeStamp = dt.strftime("%m-%d-%Y_%H:%M:%S")
    # Create output file name
    clean_data_file = 'clean_data_' + timeStamp + ".csv"
    # Read the file that must be read
    nameInput = n1.get()
    # clean the data
    cleanData(nameInput, clean_data_file)
    # Set the output name
    fileName(clean_data_file)
    
def fileName(name_output_file_label):
    n2_name = name_output_file_label
    n2.set(n2_name)

def borrar():
    n1.set("")
    n2.set("")

# Creamos la raíz
root = Tk()

root.title("Filter Data")   # Título de la ventana 
root.resizable(0, 0)    # Activar redimensión de ventana   
root.geometry("780x160")

root.config(bg="blue")  # color de fondo, background
root.config(bd=15)     # tamaño del borde en píxeles
root.config(relief="sunken")    # relieve del root 

# crea el frame
frame = Frame(root, width=500,height=300) 
# lo empaqueta
frame.pack(fill='both')

# Color de fondo, background
frame.config(bg="lightblue")  
frame.config(bd=25)
frame.config(relief="sunken")

# Variables

n1 = StringVar() # entrada
n2 = StringVar() # salida

# Entradas

# nombre del archivo que queremos analizar
label = Label(frame, text="Raw File name")
label.grid(row=0,column=0, sticky=W, padx=5, pady=5)

entry = Entry(frame, textvariable=n1, width = 80)
entry.grid(row=0,column=1, padx=5, pady=5)

# nombre del generado
label = Label(frame, text="Clean file name")
label.grid(row=1,column=0, sticky=W, padx=5, pady=5)

entry = Entry(frame, textvariable=n2, state="disabled", width = 80)
entry.grid(row=1,column=1, padx=5, pady=5)

# Boton
Button(root, text="Analize", command=run).pack(side="left") 
Button(root, text="Erase", command=borrar).pack(side="left") 
# Comenzamos el bucle de aplicación, es como un while True
root.mainloop()  
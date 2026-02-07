#lab practicefile 
import tkinter as tk
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
#import Lab2_ecg.csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MyGui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SYSC2010")
        self.window.geometry("500x500")
        df = pd.read_csv('Lab2_ecg.csv')
# file name button
        self.label_1 = tk.Label(self.window, text="CSV File Name", font=('Arial', 18))
        self.label_1.pack(padx=20, pady=20)
        self.textbox1 = tk.Entry(self.window, font=('Arial', 16))
        self.textbox1.pack(padx=20)
#x axis button
        self.label_x = tk.Label(self.window, text="X-Axis Column Name", font=('Arial', 18))
        self.label_x.pack(padx=20, pady=20)
        self.textbox2 = tk.Entry(self.window, font=('Arial', 16))
        self.textbox2.pack(padx=20)
#y axis button
        self.label_y = tk.Label(self.window, text="Y-Axis Column Name", font=('Arial', 18))
        self.label_y.pack(padx=20, pady=20)
        self.textbox3 = tk.Entry(self.window, font=('Arial', 16))
        self.textbox3.pack(padx=20)
#load and plot button
        self.button1 = tk.Button(self.window, text="Plot", font=('Arial',10), command=self.plot)
        self.button1.pack(padx=10,pady=10)
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.columnconfigure(0, weight = 1)

    def show_message(self):
        print(self.textbox.get('1.0', tk.END))
    def plot(self):
        file_name = self.textbox1.get()
        x_axis = self.textbox2.get()
        y_axis = self.textbox3.get()
        df = pd.read_csv(file_name)
        self.figure = plt.Figure(figsize=(6, 4))
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(df[x_axis], df[y_axis])
        self.ax.set_xlabel(x_axis)
        self.ax.set_ylabel(y_axis)
            
            # Embed plot in window
        self.canvas = FigureCanvasTkAgg(self.figure, self.window)
        self.canvas.get_tk_widget().pack(padx=10, pady=10)
MyGui()
tk.mainloop()
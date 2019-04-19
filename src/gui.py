#!/usr/bin/env python3 

#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

class GUI:

    def __init__(self):
        self.window = tk.Tk()
        self.create_widgets()

    def create_widgets(self):

        self.window.geometry("1000x520")  # You want the size of the app to be 500x500
        self.window.resizable(0, 0)
        self.window.title("Color Image Processing by Team 9")

        loadimg_button = tk.Button(text="Load image")
        loadimg_button.place(x=20, y=20)

        # Create main frame with tabs ("Notebook")
        note = ttk.Notebook(self.window)
        tab1 = tk.Frame(note, height=400, width=950)
        tab2 = tk.Frame(note, height=400, width=950)
        tab3 = tk.Frame(note, height=400, width=950)
        tab4 = tk.Frame(note, height=400, width=950)

        note.add(tab1, text="Color Image Transformation")
        note.add(tab2, text="Intensity Slicing")
        note.add(tab3, text="Smoothing")
        note.add(tab4, text="Sharpening")

        note.place(x=20, y=70)

        self.create_CIT_tab(tab1)
        self.create_intensityslicing_tab(tab2)
        self.create_smoothing_tab(tab3)
        self.create_sharpening_tab(tab4)

    def create_CIT_tab(self, tab):
        # Tab 1 contents - Color Image Transformation
        lf = ttk.Labelframe(tab, text='Select methods', height=350, width=200)
        lf.place(x=20, y=20)

        cit = tk.IntVar()
        tk.Radiobutton(lf, text="RGB to HSI", variable=cit, value=1).place(x=10, y=10)
        tk.Radiobutton(lf, text="RGB to CMYK", variable=cit, value=2).place(x=10, y=40)

        tk.Frame(lf, height=2, width=170, bd=1, relief="sunken").place(x=10, y=80)

    def create_intensityslicing_tab(self, tab):
        # Tab 2 contents - Intensity slicing
        lf = ttk.Labelframe(tab, text='Select methods', height=350, width=200)
        lf.place(x=20, y=20)

        # Channels
        channel = tk.IntVar()
        tk.Radiobutton(lf, text="RGB", variable=channel, value=1).place(x=10, y=10)
        tk.Radiobutton(lf, text="HSI", variable=channel, value=2).place(x=60, y=10)
        tk.Radiobutton(lf, text="CMYK", variable=channel, value=3).place(x=110, y=10)
        tk.Frame(lf, height=2, width=170, bd=1, relief="sunken").place(x=10, y=50)

        # Color
        color = tk.IntVar()
        tk.Radiobutton(lf, text="Red", variable=color, value=1).place(x=10, y=60)
        tk.Radiobutton(lf, text="Green", variable=color, value=2).place(x=10, y=90)
        tk.Radiobutton(lf, text="Blue", variable=color, value=3).place(x=10, y=120)
        tk.Frame(lf, height=2, width=170, bd=1, relief="sunken").place(x=10, y=160)

        # Minimun intensity found in image
        imin_text = tk.Text(lf, height=2, width=5, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        imin_text.place(x=10, y=180)
        imin_text.insert("end", "Min I:")

        i_min = tk.StringVar()
        imin_entry = tk.Entry(lf, width=5, relief="flat", bg="gray94", textvariable=i_min)
        imin_entry.place(x=60, y=180)
        i_min.set(str(.158))

        # Max intensity found in image
        imax_text = tk.Text(lf, height=2, width=5, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        imax_text.place(x=10, y=200)
        imax_text.insert("end", "Max I:")

        i_max = tk.StringVar()
        imax_entry = tk.Entry(lf, width=5, relief="flat", bg="gray94", textvariable=i_max)
        imax_entry.place(x=60, y=200)
        i_max.set(str(.858))

        # Minimum intensity value for slicing
        smin_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        smin_text.place(x=10, y=230)
        smin_text.insert("end", "Min Slicing:")

        s_min_spinbox = tk.Spinbox(lf, width=5, from_=0, to=1, increment=.001)
        s_min_spinbox.place(x=100, y=230)

        # Max intensity value for slicing
        smax_text = tk.Text(lf, height=2, width=10, font=("TkDefaultFont", 9, "normal"), relief="flat", bg="gray94")
        smax_text.place(x=10, y=250)
        smax_text.insert("end", "Max Slicing:")

        s_max_spinbox = tk.Spinbox(lf, width=5, from_=0, to=1, increment=.001)
        s_max_spinbox.place(x=100, y=250)

        # TODO: prevent max to go below min and viceversa

    def create_sharpening_tab(self, tab):
        # Tab 3 contents - Sharpening
        lf = ttk.Labelframe(tab, text='Select methods', height=350, width=200)
        lf.place(x=20, y=20)

        sharpening = tk.IntVar()
        tk.Radiobutton(lf, text="Sharpening R, G, and B", variable=sharpening, value=1).place(x=10, y=10)
        tk.Radiobutton(lf, text="Sharpening intensity", variable=sharpening, value=2).place(x=10, y=40)
        tk.Radiobutton(lf, text="Difference", variable=sharpening, value=3).place(x=10, y=70)
        tk.Frame(lf, height=2, width=170, bd=1, relief="sunken").place(x=10, y=110)

    def create_smoothing_tab(self, tab):
        # Tab 3 contents - Smoothing
        lf = ttk.Labelframe(tab, text='Select methods', height=370, width=200)
        lf.place(x=20, y=20)

        # Color
        color = tk.IntVar()
        tk.Radiobutton(lf, text="Red", variable=color, value=1).place(x=10, y=10)
        tk.Radiobutton(lf, text="Green", variable=color, value=2).place(x=10, y=40)
        tk.Radiobutton(lf, text="Blue", variable=color, value=3).place(x=10, y=70)
        tk.Frame(lf, height=2, width=170, bd=1, relief="sunken").place(x=10, y=110)

        # HSI
        hsi = tk.IntVar()
        tk.Radiobutton(lf, text="Hue", variable=hsi, value=1).place(x=10, y=130)
        tk.Radiobutton(lf, text="Saturation", variable=hsi, value=2).place(x=10, y=160)
        tk.Radiobutton(lf, text="Intensity", variable=hsi, value=3).place(x=10, y=190)
        tk.Frame(lf, height=2, width=170, bd=1, relief="sunken").place(x=10, y=230)

        # Method
        method = tk.IntVar()
        tk.Radiobutton(lf, text="Average RGB", variable=method, value=1).place(x=10, y=250)
        tk.Radiobutton(lf, text="Intensity", variable=method, value=2).place(x=10, y=280)
        tk.Radiobutton(lf, text="Difference", variable=method, value=3).place(x=10, y=310)


app = GUI()
app.window.mainloop()


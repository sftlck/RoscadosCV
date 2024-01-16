import tkinter as Tk
from tkinter import *
from tkinter import ttk
import cv2

def Ex001(self): #exception in case it detects that images were not selected for img_mtd/parallel_img_mtd 

    def Ex001_close():

        Ex001_wdw.grab_release()
        Ex001_wdw.destroy()

    print("Ex001: No file selected.")
    Ex001_wdw = Tk()
    Ex001_wdw.title('Ex001')
    Ex001_wdw.resizable(False, False)
    Ex001_wdw.attributes('-topmost', 1)
    Ex001_wdw.grab_set_global()
    Ex001_wdw.wait_visibility()
    w = 250
    h = 130
    ws = Ex001_wdw.winfo_screenwidth()
    hs = Ex001_wdw.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    g = Ex001_wdw.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Ex001_text_1 = ttk.Label(Ex001_wdw, text = "Ex001: No file selected.", justify = 'center', anchor = 'center')
    Ex001_text_1.pack()
    Ex001_text_1.grid(row = 0, column = 0, padx = 60, pady = 15, sticky = 'nw')

    rstt_btn = ttk.Button(Ex001_wdw, text = 'Restart', command = lambda: (Ex001_wdw.destroy(), Main.paralel_img_mtd(self)), style = 'TButton')
    rstt_btn.grid(row = 0, column = 0, padx = 85, pady = 60, sticky = 'nw')
    btn_exit_Ex001 = ttk.Button(Ex001_wdw, text = "Close", command = Ex001_close, style = 'TButton')
    btn_exit_Ex001.grid (row = 0, column = 0, padx = 85, pady = 90, sticky='nw')

    Ex001_wdw.mainloop()

def Ex002(self): #exception in case it detects that there is no selected save location

    def Ex002_close():

        Ex002_wdw.grab_release()
        Ex002_wdw.destroy()

    print("Ex002: No savefile directory selected.")
    Ex002_wdw = Tk()
    Ex002_wdw.title('Ex002')
    Ex002_wdw.resizable(False, False)
    Ex002_wdw.attributes('-topmost', 1)
    Ex002_wdw.grab_set_global()
    Ex002_wdw.wait_visibility()
    w = 250
    h = 130
    ws = Ex002_wdw.winfo_screenwidth()
    hs = Ex002_wdw.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    g = Ex002_wdw.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Ex001_text_1 = ttk.Label(Ex002_wdw, text = "Ex002: No savefile directory selected.", justify='center', anchor='center')
    Ex001_text_1.pack()
    Ex001_text_1.grid(row = 0, column = 0, padx = 26, pady = 15, sticky = 'nw')

    rstt_btn = ttk.Button(Ex002_wdw, text = 'Restart', command = lambda: (Ex002_wdw.destroy(), Main.paralel_img_mtd()))
    rstt_btn.grid(row = 0, column = 0, padx = 85, pady = 60, sticky = 'nw')
    btn_exit_Ex003 = ttk.Button(Ex002_wdw, text = "Close", command = Ex002_close)
    btn_exit_Ex003.grid (row = 0, column = 0, padx = 85, pady = 90, sticky='nw')

    Ex002_wdw.mainloop()
    
def Ex003(self): #exception in case it detects that there is no text in input filename box and OS Number box

    def Ex003_close():

        Ex003_wdw.grab_release()
        Ex003_wdw.destroy()

    print("Ex003: Instrument ID and Service Order textboxes are empty.")
    Ex003_wdw = Tk()
    Ex003_wdw.title('Ex003')
    Ex003_wdw.resizable(False, False)
    Ex003_wdw.attributes('-topmost', 1)
    Ex003_wdw.grab_set_global()
    Ex003_wdw.wait_visibility()
    w = 250
    h = 130
    ws = Ex003_wdw.winfo_screenwidth()
    hs = Ex003_wdw.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    g = Ex003_wdw.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Ex003_text_1 = Label(Ex003_wdw, text = "Ex003: Instrument ID and Service Order", justify='center', anchor='center')
    Ex003_text_1.pack()
    Ex003_text_1.grid(row = 0, column = 0, padx = 23, pady = 15, sticky = 'nw')
    Ex003_text_2 = Label(Ex003_wdw, text = "input boxes are empty.", justify = 'center', anchor = 'center')
    Ex003_text_2.grid(row = 0, column = 0, padx = 65, pady = 30, sticky = 'nw')

    #rstt_btn = ttk.Button(Ex003_wdw, text = 'Restart', command = lambda: (Ex003_wdw.destroy()))
    #rstt_btn.grid(row = 0, column = 0, padx = 85, pady = 60, sticky='nw')
    btn_exit_Ex003 = ttk.Button(Ex003_wdw, text = "Close", command = Ex003_close)
    btn_exit_Ex003.grid (row = 0, column = 0, padx = 85, pady = 75, sticky = 'nw')

    Ex003_wdw.mainloop()

def Ex004(self): #exception for case it detects that are not text inserted into filename box

    def Ex004_close():

        Ex004_wdw.grab_release()
        Ex004_wdw.destroy()

    print("Ex004: Instrument ID input box is empty.")
    Ex004_wdw = Tk()
    Ex004_wdw.title('Ex004')
    Ex004_wdw.resizable(False, False)
    Ex004_wdw.attributes('-topmost', 1)
    Ex004_wdw.grab_set_global()
    Ex004_wdw.wait_visibility()
    w = 250
    h = 130
    ws = Ex004_wdw.winfo_screenwidth()
    hs = Ex004_wdw.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    g = Ex004_wdw.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Ex004_text_1 = Label(Ex004_wdw, text = "Ex004: Instrument ID input box is empty.", justify = 'center', anchor = 'center')
    Ex004_text_1.pack()
    Ex004_text_1.grid(row = 0, column = 0, padx = 18, pady = 15, sticky = 'nw')

    #rstt_btn = ttk.Button(Ex004_wdw, text = 'Restart', command = lambda: (Ex004_wdw.destroy(), R()))
    #rstt_btn.grid(row = 0, column = 0, padx = 85, pady = 55, sticky = 'nw')
    btn_exit_Ex003 = ttk.Button(Ex004_wdw, text = "Close", command = Ex004_close)
    btn_exit_Ex003.grid (row = 0, column = 0, padx = 85, pady = 75, sticky='nw')

    Ex004_wdw.mainloop()

def Ex005(self): #exception in case it detects that there is no text only in OS boxx
    def Ex005_close():

        Ex005_wdw.grab_release()
        Ex005_wdw.destroy()

    #exception para caso detectar que não existe texto em SO Number input box
    print("Ex005: Service Order input box is empty.")
    Ex005_wdw = Tk()
    Ex005_wdw.title('Ex005')
    Ex005_wdw.resizable(False, False)
    Ex005_wdw.attributes('-topmost', 1)
    Ex005_wdw.grab_set_global()
    Ex005_wdw.wait_visibility()
    w = 250
    h = 130
    ws = Ex005_wdw.winfo_screenwidth()
    hs = Ex005_wdw.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    g = Ex005_wdw.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Ex005_text_1 = Label(Ex005_wdw, text = "Ex005: Service Order input box is empty.", justify = 'center', anchor = 'center')
    Ex005_text_1.pack()
    Ex005_text_1.grid(row = 0, column = 0, padx = 18, pady = 15, sticky = 'nw')

    #rstt_btn = ttk.Button(Ex005_wdw, text = 'Restart', command = lambda: (Ex005_wdw.destroy(), R()))
    #rstt_btn.grid(row = 0, column = 0, padx = 85, pady = 55, sticky = 'nw')
    btn_exit_Ex003 = ttk.Button(Ex005_wdw, text = "Close", command = Ex005_close)
    btn_exit_Ex003.grid (row = 0, column = 0, padx = 85, pady = 75, sticky='nw')

    Ex005_wdw.mainloop()

"""def Ex006(self): #exception for identifying in-array stored image after switching between methods

    def array_image():
        image_c = np.array(self.cv2image)
        image_c2 = cv2.normalize(image_c, image_c, 0, 255, cv2.NORM_MINMAX)
        image = cv2.cvtColor(image_c2, cv2.COLOR_BGR2RGB)
        Ex006_wdw.grab_release()
        Ex006_wdw.destroy()

    def new_image():

        self.imgtk2 = None
        self.imgtk2  = np.array([])

        Ex006_wdw.grab_release()
        Ex006_wdw.destroy()

    print("Ex006: Image from np array identified, question prompted.")
    Ex006_wdw = Tk()
    Ex006_wdw.title('Ex006')
    Ex006_wdw.resizable(False, False)
    Ex006_wdw.attributes('-topmost', 1)
    Ex006_wdw.grab_set_global()
    Ex006_wdw.wait_visibility()
    w = 250
    h = 130
    ws = Ex006_wdw.winfo_screenwidth()
    hs = Ex006_wdw.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    g = Ex006_wdw.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Ex001_text_1 = ttk.Label(Ex006_wdw, text = "Ex006: use new image or array image?", justify='center', anchor='center')
    Ex001_text_1.pack()
    Ex001_text_1.grid(row = 0, column = 0, padx = 26, pady = 15, sticky = 'nw')

    array_btn = ttk.Button(Ex006_wdw, text = 'Array image', command = array_image)
    array_btn.grid(row = 0, column = 0, padx = 85, pady = 60, sticky = 'nw')

    select_new_Ex006 = ttk.Button(Ex006_wdw, text = "New image", command = new_image)
    select_new_Ex006.grid (row = 0, column = 0, padx = 85, pady = 90, sticky='nw')

    Ex006_wdw.mainloop()
"""
def Ex007(self): #exception for no line segments detected

    def Ex007_close():

        Ex007_wdw.grab_release()
        Ex007_wdw.destroy()

    print("Ex007: No line segments detected")
    Ex007_wdw = Tk()
    Ex007_wdw.title('Ex007')
    Ex007_wdw.resizable(False, False)
    Ex007_wdw.attributes('-topmost', 1)
    Ex007_wdw.grab_set_global()
    Ex007_wdw.wait_visibility()
    w = 250
    h = 130
    ws = Ex007_wdw.winfo_screenwidth()
    hs = Ex007_wdw.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    g = Ex007_wdw.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Ex007_text_1 = ttk.Label(Ex007_wdw, text = "Ex007: No line segments detected.", justify='center', anchor='center')
    Ex007_text_1.grid(row = 0, column = 0, padx = 35, pady = 20, sticky = 'nw')
    
    select_new_Ex006 = ttk.Button(Ex007_wdw, text = "Close", command = Ex007_close)
    select_new_Ex006.grid(row = 0, column = 0, padx = 85, pady = 80, sticky = 'nw')

    Ex007_wdw.mainloop()
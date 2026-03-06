import matplotlib.path as mplPath
import cv2
import numpy as np
import math
import scipy
import PIL.Image
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk
from tkinter import Tk, Label
import os
import shutil
import sys
import scipy.stats
import json
import datetime
import matplotlib.pyplot as plt
import time as t
import Exceptions

def log ():
    log = t.strftime("%D - %H:%M:%S | ")
    return str(log)
    
class TAMS:
    def __init__(self, master):      
        print(log()+'__init__(self, master) initialized')

        self.settings_folder = os.path.join(os.getcwd(), "Settings")

        if not os.path.exists(self.settings_folder):

            print(log()+'settings folder not found, creating settings folder...')
            
            self.int_val = 40
            self.px_val = 60
            print(log()+'settings folder created successfully')

            os.makedirs('Settings')
            print(log()+'initializing settings save...')

            Settings = {
                    "int_val": 40,
                    "px_val": 60
                }
            with open(self.settings_folder + '/' + 'Settings.json', 'w') as outfile:
                json.dump(Settings, outfile)
                
                print(log()+'settings saved succsessfully')

        else:

            print(log()+'settings folder found, loading settings...')

            with open(self.settings_folder + '/' + 'Settings.json', 'r') as f:
                data = json.load(f)
            self.int_val = data['int_val']
            self.px_val = data['px_val']

            print(log()+'settings loaded successfully')

        global text

        self.master = master
        master.title("Software de Medição de Roscados v05-03-26")
        self.master.tkraise()
        logo = PhotoImage(file = 'logo.png')
        self.master.iconphoto(True, logo)

        self.msre_record = os.path.join(os.getcwd(), "Measurements")
                
        if not os.path.exists(self.msre_record):
            os.makedirs(self.msre_record)
        
        w = 600
        h = 300
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.original_dimensions = master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.x_dimension = self.master.winfo_width()
        self.y_dimension = self.master.winfo_height()
        self.master.wm_minsize(600, 300)
        self.master.wm_maxsize(1920, 900)

        w_style = ttk.Style()
        w_style.configure ('TFrame', background = 'black')
        f_style = ttk.Style()
        f_style.configure('TButton', font = ('calibri', 12), background = 'black', width = 14)
        f2_style = ttk.Style()
        f2_style.configure('TButton2', font = ('calibri', 12), background = 'black', width = 25)
        s_style = ttk.Style()
        s_style.configure('TScale', background = 'black', foreground = '#FFFFFF')
        c_style = ttk.Style()
        c_style.configure('Grey.TCheckbutton', sticky = 'W', background = 'black', foreground = '#FFFFFF', highlightcolor = 'blue')

        # create notebook with tabs
        self.notebook = ttk.Notebook(master, width = master.winfo_screenwidth(), height = master.winfo_screenheight())
        self.notebook.grid(row=0, column=0, columnspan=4)

        ####Create Measure frame
        self.Measure = Frame(self.notebook, background = 'black')
        self.Measure.grid(row=0, column=0)
        self.Measure.grid_propagate(False)

        self.settings_folder = os.path.join(os.getcwd(), "Settings")

        ######background universal image
        self.background = ImageTk.PhotoImage(PIL.Image.open('ISI SIM_1 30.png'))
        
        ######background measure set
        image_black_measure_label = Label(self.Measure, image = self.background, bg = 'black')
        image_black_measure_label.place(x = 0, y = 0)

        ######Measure Frame black column
        #black_image = ImageTk.PhotoImage(PIL.Image.open('Black_colour.jpg'))
        black_canvas = Canvas(self.Measure, width = 150, height = 1600, background = 'black', highlightbackground = 'black')
        #black_canvas.create_image (0,0, image = black_image, anchor = 'n')
        #black_canvas.image = black_image
        black_canvas.place(x = 0, y = 0)
        black_canvas.grid_propagate (False)

        ####Create Settings frame
        self.Settings = Frame(self.notebook, background = 'black')
        self.Settings.grid(row=0, column=1)
        self.Settings.grid_propagate(False)

        ######background Settings set
        image_settings_label = Label(self.Settings, image = self.background, bg = 'black')
        image_settings_label.place(x = 0, y = 0)
        list_1 = Label(self.Settings, text = '1', bg = 'black', fg = 'white')
        list_1.grid (row = 0, column = 0, padx = 5)
        
        ######Settings Frame black column
        #black_image = ImageTk.PhotoImage(PIL.Image.open('Black_colour.jpg'))
        black_canvas = Canvas(self.Settings, width = 3000, height = 160, background = 'black', highlightbackground = 'black')
        #black_canvas.create_image (0,0, image = black_image, anchor = 'n')
        #black_canvas.image = black_image
        black_canvas.place(x = 0, y = 0)
        black_canvas.grid_propagate (False)

        ####Create Credits frame
        self.Credits = Frame(self.notebook, background = 'black')
        self.Credits.grid(row=0, column=2)
        self.Credits.grid_propagate(False)

        ######background Credits set
        image_settings_label = Label(self.Credits, image = self.background, bg = 'black')
        image_settings_label.place(x = 0, y = 0)

        ######Credits Frame black column
        #black_image = ImageTk.PhotoImage(PIL.Image.open('Black_colour.jpg'))
        black_canvas = Canvas(self.Credits, width = 3000, height = 80, background = 'black', highlightbackground = 'black')
        #black_canvas.create_image (0,0, image = black_image, anchor = 'n')
        #black_canvas.image = black_image
        black_canvas.place(x = 0, y = 0)
        black_canvas.grid_propagate (False)

        self.notebook.add(self.Measure, text="Medição")
        self.notebook.add(self.Settings, text="Ajustes")
        self.notebook.add(self.Credits, text = "Créditos")

        global mLs

        mLs = 0
        cLs = 0
        sLs = 0

        self.image_label = Label(self.Measure, background = 'grey')
        self.image_label.place (x = 60, y = 15)
        #self.image_label.grid (row = 1, column = 1)
        self.image_label.grid_propagate(False)

        self.btn_strt = ttk.Button(self.Measure, text = 'Iniciar', command = lambda: (self.year_measure(), self.mtd_strt()), style = 'TButton')
        self.btn_strt.grid (row = mLs, column = 0, sticky = 'W', padx = 15, pady = 7)
        btn_exit = ttk.Button(self.Measure, text = 'Sair', command = sys.exit, style = 'TButton')
        btn_exit.grid (row = mLs + 7, column = 0, sticky = 'W', padx = 15, pady = 8)

        #Settings Frame
        lenght_mssg = Label(self.Settings, text = "Threshold for minimum pixels gap length in true edges detection:", fg = '#FFFFFF')
        lenght_mssg.configure (background = 'black')
        lenght_mssg.grid (row = sLs, padx = 15, pady = 15, sticky = 'W')
        
        #self.previous_year_var = BooleanVar(value = False)
        #self.year_chk = ttk.Checkbutton(self.Settings, text = "Previous year Service Order measurement (beta)", variable = self.previous_year_var, style = 'Grey.TCheckbutton')
        #self.year_chk.grid (row = sLs + 1, padx = 15, pady = 15, sticky = 'W')

        #self.sample_var = BooleanVar(value = False)
        #self.sample = ttk.Checkbutton(self.Settings, text = "Non Service Order related measurement (beta)", variable = self.sample_var, style = 'Grey.TCheckbutton')
        #self.sample.grid (row = sLs + 2, padx = 15, pady = 15, sticky = 'W')

        px_mssg = Label(self.Settings, text = "Pixel line extent for true edges detected:", fg = "#FFFFFF")
        px_mssg.configure (background = 'black')
        px_mssg.grid (row = sLs + 3, padx = 15, pady = 15, sticky = 'W')

        def sld_vle_update(val):
            self.int_val = int(float(val))
            self.sld_vle.configure(text=str(int(self.int_val)) + " pixels")
            
        self.sld_vle = Label(self.Settings, text = str(self.int_val), background = 'black', fg = "#000000")
        self.sld_vle.grid (row = sLs, column = sLs + 2, padx = 15, sticky = 'W')
        
        self.length = tk.DoubleVar()
        self.sld = ttk.Scale(self.Settings, from_ = 0, to = 350, variable = self.length, orient = 'horizontal', command = sld_vle_update)
        self.sld.set(str(self.int_val))
        self.sld.grid (row = sLs, column = sLs + 1, padx = 15, sticky = 'W')

        ####################################

        #self.px_val = 60
        def sld_px_update(val_px):
            self.px_val = int(float(val_px))
            self.sld_px.configure(text=str(int(self.px_val)) + " pixels")
            
        self.sld_px = Label(self.Settings, text = str(self.px_val), background = 'black', fg = "#000000")
        self.sld_px.grid (row = sLs + 3, column = sLs + 2, padx = 15, sticky = 'W')
        
        self.px_length = tk.DoubleVar()
        self.sld_px1 = ttk.Scale(self.Settings, from_ = 0, to = 100, variable = self.px_length, orient = 'horizontal', command = sld_px_update)
        self.sld_px1.set(str(self.px_val))
        self.sld_px1.grid (row = sLs + 3, column = sLs + 1 , padx = 15, sticky = 'W')
        self.sld_px1.grid_propagate (False)

        ####################################

        #End of the stuff in Settings Frame
        #Measure Frame
        
        self.inpt_box_flnm_text = Label(self.Measure, text = "ID Instrumento", fg = 'White')
        self.inpt_box_flnm_text.grid (row = mLs + 3, column = 0, sticky = 'W', padx = 15)
        self.inpt_box_flnm_text.configure (bg = 'black')

        self.inpt_box_flnm = ttk.Entry(self.Measure)
        self.inpt_box_flnm.grid (row = mLs + 4, column = 0, sticky = 'W', padx = 16)
        self.inpt_box_flnm.configure (background = 'black', width = 20)
        self.inpt_box_flnm.focus()
        self.inpt_box_flnm.insert(0,'') ##placehlolder, insert

        self.inpt_box_OS_text = Label(self.Measure, text = "Ordem de Serviço", fg = 'White', )
        self.inpt_box_OS_text.grid (row = mLs + 5, column = 0, sticky = 'W', padx = 15)
        self.inpt_box_OS_text.configure (background = 'black')

        self.inpt_box_OS = ttk.Entry(self.Measure)
        self.inpt_box_OS.grid (row = mLs + 6, column = 0, sticky = 'W', padx = 15)
        self.inpt_box_OS.configure (background = 'black', width = 20)
        self.inpt_box_OS.insert(0,'') ##placehlolder, insert
        
        def chk_img_chkbtn():
            if self.img_mtd_chk.instate(['selected']):
                self.cam_mtd_chk.configure(state = 'disabled')
                self.btn_strt.configure (state = 'enabled')
            else:
                self.cam_mtd_chk.configure(state = 'enabled')
                btn_strt_routine()

        self.img_mtd_chk_var = BooleanVar(value = False)
        self.img_mtd_chk = ttk.Checkbutton(self.Measure, text = "Método do Arquivo", variable = self.img_mtd_chk_var, style = 'Grey.TCheckbutton', command = chk_img_chkbtn)
        self.img_mtd_chk.grid (row = mLs + 1, column = mLs, padx = 15, sticky = 'W')

        def chk_cam_chkbtn():
            if self.cam_mtd_chk.instate(['selected']):
                self.img_mtd_chk.configure (state = 'disabled')
                self.btn_strt.configure (state = 'enabled')
            else:
                self.img_mtd_chk.configure (state = 'enabled')
                btn_strt_routine()

        self.cam_mtd_chk_var = BooleanVar(value = False)
        self.cam_mtd_chk = ttk.Checkbutton(self.Measure, text = "Método da Câmera", variable = self.cam_mtd_chk_var, style = 'Grey.TCheckbutton', command = chk_cam_chkbtn)
        self.cam_mtd_chk.grid (row = mLs + 2, column = mLs, padx = 15, sticky = 'W')

        if not self.cam_mtd_chk.instate(['selected']) and not self.img_mtd_chk.instate(['selected']):
                self.btn_strt.configure (state = 'disabled')

        def btn_strt_routine ():
            if not self.cam_mtd_chk.instate(['selected']) and not self.img_mtd_chk.instate(['selected']):
                self.btn_strt.configure (state = 'disabled')

        self.canvas_test = tk.Canvas(self.Measure)

        #end of Measure Frame
        #Credits Frame

        self.crd_mssg = Label(self.Credits, text = "Software de Medição de Roscados, versão 16-03-2025.", fg = 'White', bg = 'black')
        self.crd_mssg.grid (row = cLs, column = 0, padx = 15, pady = 15, sticky = 'W')
        self.crd_mssg.configure (bg = 'black')
        self.crd_mssg2 = Label(self.Credits, text = "Xoko/Castro, 2023.", fg = 'White', bg = 'black')
        self.crd_mssg2.grid (row = cLs + 1, column = 0, sticky = 'W', padx = 15)
        self.crd_mssg2.configure (bg = 'black')
        
        #end of the stuff in Credits Frame
        
    def save_routine_Db(self): #this damn line saves the data from sld_vle into a .json file

        print(log()+'save routine initialized')

        self.settings_folder = os.path.join(os.getcwd(), "Settings")

        if os.path.exists(self.settings_folder):

            #self.sld_str = int(self.sld.get()) .json can't be serializable, so this int line converts to it
            print(log()+'settings folder identified, saving in progress...')
            Settings = {
                        "int_val": int(self.sld.get()), 
                        "px_val": int(self.sld_px1.get())
                }
            with open(self.settings_folder + '/' + 'Settings.json', 'w') as outfile:
                json.dump(Settings, outfile)
                print(log()+'settings saving successful')
    
    def year_measure (self):

        """if self.sample.instate(['selected']):
            
            print(log()+'sample method does not collect OS year')"""

        current_date = datetime.date.today()
        self.year = current_date.year ###extract year

        """if self.year_chk.instate(['selected']): #nunca deveria ser usado
            
            self.year = current_date.year - 1
            self.folder_OS = 'OS ' + str(self.year)
            print(log()+self.folder_OS + ': previous year identified')"""

        self.OS_number_cap = 'OS ' + self.inpt_box_OS.get()
        self.folder_OS = self.OS_number_cap

    def mtd_strt (self):

        print (log()+'mtd_strt initiated')
        print(log()+'threshold for minimum pixel gap in true edges detection: ',int(self.sld.get()),' px')
        print(log()+'pixel line extent for true edges detected: ',int(self.sld_px1.get()),' px')

        self.save_routine_Db()

        self.cv2image = np.array([])
        
        self.msre_date = datetime.date.today()

        if self.img_mtd_chk.instate(['selected']):
            self.paralel_img_mtd()

        if self.cam_mtd_chk.instate(['selected']):
            #self.btn_strt.configure (state = 'disabled')
            self.cam_mtd()
        #if hasattr (self, cap) and self.cap.isOpened():
        #    self.cap.release

    def measurement_path (self):
        self.path_btn = ttk.Button(self.Measure, text = str(self.OS_number_cap) + " folder", command = self.open_measurement_file, width = 25)
        self.path_btn.grid (row = mLs, column = mLs + 2)
        self.path_btn.grid_propagate(False)

    def open_measurement_file (self):
        folder_path = self.msre_record + '/' + str(self.folder_OS)

        if os.path.exists(folder_path):
            os.startfile(folder_path)
    
    def Imgprocessor(self):
        #seleciona a "Region of interest - roi"

        roi=(0,0,0,0)
        n=0

        while roi == (0,0,0,0) or n==0:
            roi = cv2.selectROI(self.image,showCrosshair=True)
            roi_cropped = self.image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
            height = roi_cropped.shape[0]
            width = roi_cropped.shape[1]
            #cv2.imshow("roi_cropped", roi_cropped)
            #cv2.waitKey(0)
            cv2.destroyAllWindows()

        #**************************************************************************************************
        #*******************************     Detecta a aresta    ****************************************** 
        #**************************************************************************************************     

            img_gray = cv2.cvtColor(roi_cropped,cv2.COLOR_BGR2GRAY)
            img_blur = cv2.GaussianBlur(img_gray,(3,3), 0)
            #cv2.imshow("img_blur", img_blur)
            #cv2.waitKey(0)
            #canny_image=cv2.Canny(img_gray, 120,200)
            #edges1 = cv2.Canny(image=img_blur, threshold1=lower, threshold2=upper)

            edges1 = cv2.Canny(image=img_blur, threshold1 = 180, threshold2 = 180)
            
            self.custom_name = f"{text} - Edge.bmp"
            self.cstm_name_measure = f"{text}.bmp"
            
            x_list=[]
            y_list=[]
            
            cv2.imwrite(self.custom_name, edges1)
            #cv2.imwrite('EdgeDetected.bmp',canny_image)
            img2=cv2.imread(self.custom_name)

            #cv2.imshow("img2",img2)
            #cv2.waitKey(0)

            for x in range(0, width):

                for y in range(0, height): #varre cada linha
                    #if (img2[y, x] == [100,100,100]).all():                         
                    if (img2[y, x] == [255,255,255]).all():                         
                        x_list.append(x)
                        y_list.append(y)
                        #print (x_list[x],y_list[x])
                        n=n+1

        #**************************************************************************************************
        #*******************************     Detecta as linhas retas    *********************************** 
        #**************************************************************************************************  

            #img_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
            #Create default parametrization LSD
            lsd = cv2.createLineSegmentDetector(0)

            #cv2.imshow("img_gray",img_gray )
            #cv2.waitKey(0)

            #Detect lines in the image
            lines = lsd.detect(img_gray)[0] #Position 0 of the returned tuple are the detected lines
            
            #mask = np.zeros((img_gray.shape),np.uint8)

            lsd = cv2.createLineSegmentDetector(0)
            lines = lsd.detect(img_gray)[0]
            #or l in lines:
                #x0, y0, x1, y1 = l.flatten()
                #/do whatever and plot using:
                #cv2.line(mask, (x0, y0), (x1,y1), 255, 1, cv2.LINE_AA)
                
            if np.any(lines == None):
                w = 600
                h = 300
                ws = self.master.winfo_screenwidth()
                hs = self.master.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                self.original_dimensions = self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                Exceptions.Ex007(self)
            print("")
            q = 0
            for a in range(len(lines) ):
                xIni = lines[a][0][0]
                yIni = lines[a][0][1]
                xFin = lines[a][0][2]
                yFin = lines[a][0][3]
            
                linha=0

                a=xIni-xFin
                b=yIni-yFin
                #a=(lines[a][0][0])-(lines[a][0][2])
                #b=(lines[a][0][1]-lines[a][0][3])
                    
                center_x=(xIni+xFin)/2
                center_y=(yIni+yFin)/2
                comprimento = math.sqrt((xIni-xFin)*(xIni-xFin)+(yIni-yFin)*(yIni-yFin))
                
                tangente = b/a
                arc_tan=math.atan(tangente)

                rect = ((center_x, center_y), (comprimento-20, 20), arc_tan*180/math.pi)
                box = cv2.boxPoints(rect) 
                box = np.intp(box)

                if comprimento > self.sld.get():
                    cv2.drawContours(img2,[box],-1,(100,100,100),1)

        #**************************************************************************************************
        #******************     COLOCA NA LISTA OS PONTOS DOS FLANCOS    ********************************** 
        #**************************************************************************************************     
            
                if comprimento > self.sld.get():
                    x_list2=[]
                    y_list2=[]
                    poly_path = mplPath.Path(np.array([box[0],box[1],box[2],box[3]]))
                    g = 0
                    fPx = None
                    lPx = None
                    for h in range (n):
                        point=(x_list[h],y_list[h])
                        if poly_path.contains_point(point) == True:
                            x_list2.append(x_list[h])
                            y_list2.append(y_list[h])
                            #print(point[0], point[1])
                            img2[point[1],point[0]]=(0,255,255)
                            if fPx is None:
                                fPx = point
                            lPx = point
                            
                    """print(f"fP2: ({fPx[0]}, {fPx[1]})")
                    print(f"lP2: ({lPx[0]}, {lPx[1]})")"""

            #**************************************************************************************************
            #*************************    ÂNGULO E DESVIO PADRÃO     ******************************************
            #**************************************************************************************************
                    
                    center_x=int(center_x)
                    center_y= int(center_y)

                    if (x_list2 == []) or (y_list2 == []):
                        Exceptions.Ex007(self)
                    
                    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_list2, y_list2)

                    #print(r_value**2)
                    tangente2=slope
                    desviopadrao=std_err
                    
                    arc_tan2=math.atan(tangente2)

                    ##### CASTRO 05/03/2026 - NÃO VAI TER QUEBRALINHA NESSE BGL
                    #print(" ")
                    Angulo = (90-abs (arc_tan2*180/math.pi))

                    ##### CASTRO 05/03/2026 - AGORA DÁ PRINT BONITINHO NA ORDEM QUE APARECE NA TELA
                    Angulo = str(round(Angulo, 6)).replace(".",",")
                    
                    ##### CASTRO 06/03/2026 - ADICIONEI O ÍNDICE Q PARA SABER A QUAL LINHA CADA COISA PERTENCE
                    print(f"{q} - {Angulo}")
                
                    global points_list
                    points_list = []

                    if slope >0:
                        
                        ang = (90 - abs(arc_tan2 * 180 / math.pi))
                        ##### CASTRO 05/03/2026 - OCULTEI PARA PODER SELECIONAR E COLAR NO EXCEL
                        #print("Ângulo do flanco esquerdo do vão ________ ", round(Angulo, 6))
                        
                        slope_a = (lPx[1] - fPx[1]) / (lPx[0] - fPx[0])

                        nfP = (int(fPx[0] - self.sld_px1.get() / math.sqrt(1 + slope_a ** 2)), int(fPx[1] - slope_a * self.sld_px1.get() / math.sqrt(1 + slope_a ** 2)))
                        nlP = (int(lPx[0] + self.sld_px1.get() / math.sqrt(1 + slope_a ** 2)), int(lPx[1] + slope_a * self.sld_px1.get() / math.sqrt(1 + slope_a ** 2)))

                        points_list.append((nfP[0], nfP[1], nlP[0], nlP[1]))

                        cv2.line(img2, nfP, nlP, (0, 255, 0), thickness=1)

                        X1 = nfP[0]
                        Y1 = nfP[1]
                        X2 = nlP[0]
                        Y2 = nlP[1]

                    else:
                        #Angulo = str(round(Angulo, 6)).replace(".",",")
                        #print(Angulo)
                        slope_b = (lPx[1] - fPx[1]) / (lPx[0] - fPx[0])
                        nfP2 = (int(fPx[0] - self.sld_px1.get() / math.sqrt(1 + slope_b ** 2)), int(fPx[1] - slope_b * self.sld_px1.get() / math.sqrt(1 + slope_b ** 2)))
                        nlP2 = (int(lPx[0] + self.sld_px1.get() / math.sqrt(1 + slope_b ** 2)), int(lPx[1] + slope_b * self.sld_px1.get() / math.sqrt(1 + slope_b ** 2)))
                        points_list.append((nfP2[0], nfP2[1], nlP2[0], nlP2[1]))
                        cv2.line(img2, nfP2, nlP2, (0, 255, 0), thickness=1)

                        #update X3, Y3, X4, Y4
                        X3 = nfP2[0]
                        Y3 = nfP2[1]
                        X4 = nlP2[0]
                        Y4 = nlP2[1]

                    #print ("Desvio Padrão___________________________ ",round(desviopadrao,6))
                    #print ("slope___________________________________ ",round(tangente2,6))
                
        #**************************************************************************************************
        #************************    IMPRIME OS VALORES NA IMAGEM     *************************************
        #**************************************************************************************************
        #                     
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    valor = str("%.6f" %((90-abs (arc_tan2*180/math.pi))))
                    #print(len(valor))
                    center_x=center_x-(len(valor)*5)

                    ##### CASTRO 05/03/2026 - DE TANTA LINHA IMPRESSA, VOU ADICIONAR UM ÍNDICE A ELAS PARA PODER SABER QUAL É QUAL
                    cv2.putText(img2, str(q), (center_x,center_y), font,0.3,(0,0,255),1,cv2.LINE_AA)
                    q+=1
                
                    ##########################################################################################

                    self.instrument_ID_img2 =   str(self.inpt_box_flnm.get())
                    self.OS_number_img2 =       self.OS_number_cap

                    text_size_instrument =      cv2.getTextSize(self.instrument_ID_img2, cv2.FONT_HERSHEY_SIMPLEX, 0.3, 1)[0]
                    text_x_instrument =         img2.shape[1] - text_size_instrument[0] - 10
                    text_y_instrument =         img2.shape[0] - 15

                    text_size_OS_number =       cv2.getTextSize(self.OS_number_img2, cv2.FONT_HERSHEY_SIMPLEX, 0.3, 1)[0]
                    text_x_OS_number =          img2.shape[1] - text_size_OS_number[0] - 10
                    text_y_OS_number =          img2.shape[0] - 27

                    cv2.putText(img2, self.instrument_ID_img2, (text_x_instrument, text_y_instrument), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.putText(img2, self.OS_number_img2, (text_x_OS_number, text_y_OS_number), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1, cv2.LINE_AA)

                    cv2.destroyAllWindows()
                    linha=linha+1
            print("")
            
            if not os.path.exists(self.msre_record + '/' + self.folder_OS):
                os.makedirs(self.msre_record + '/' + self.folder_OS)
                print(log()+'OS Folder name created.')

            #cv2.imread(str(img2))
            self.s_flnm = filedialog.asksaveasfilename(defaultextension = ".bmp", initialdir = self.msre_record + '/' + self.folder_OS, initialfile = self.inpt_box_flnm.get())
            
            if self.s_flnm:

                cv2.imwrite(self.s_flnm, img2)

                if os.path.isfile(self.msre_record + '/' + self.folder_OS + '/'):
                    img = cv2.imread(self.msre_record + '/' + self.folder_OS + '/' + self.custom_name)

                    if img is not None:
                        cv2.imread(str(img2))
                        cv2.imwrite(str(self.s_flnm), img2)
                        print(log()+'img2 saved in OS folder.')

                else:
                    shutil.move(os.path.join(os.getcwd(), self.custom_name), os.path.join(self.msre_record, self.folder_OS, self.custom_name))
                
                if hasattr(self, 'roi_label'):
                    self.roi_label.destroy()
                    
                if hasattr(self, 'cam_label'):
                    self.cam_label.destroy()

                if hasattr(self, 'path_btn'):
                    self.path_btn.destroy()

                if hasattr(self, 'save_btn'):
                    self.save_btn.destroy()
                    
                img_roi = PIL.Image.fromarray(edges1)
                self.roi_image_tk = ImageTk.PhotoImage(img_roi)

                width, height = img_roi.size
                self.canvas = tk.Canvas(self.Measure, width = width, height = height, background = 'black')
                self.canvas.place(x = 33 + self.inpt_box_OS.winfo_width(), y = 40)
                self.canvas.grid_propagate(False)
                self.canvas.configure (background = 'black')

                img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
                measure_show = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(img3))
                self.canvas.create_image(0, 0, image = measure_show, anchor=NW)
                
                self.image_label = Label(self.Measure, image=measure_show, background = 'black')

                self.image_label.image = measure_show
                self.image_label.configure (background = 'black')
                
                w_i = img2.shape[1]
                h_i = img2.shape[0]

                if int(w_i) + 30 + int(self.x_dimension) > int(self.x_dimension):  
                    self.master.geometry('{}x{}'.format(w_i + 60 + self.inpt_box_OS.winfo_width(), h_i + 100))

            else:
                Exceptions.Ex002(self)

            self.measurement_path ()

    def paralel_img_mtd(self):

        print(log()+'paralel_img_mtd initiated')

        global text

        if len(self.inpt_box_flnm.get()) == 0 and len(self.inpt_box_OS.get()) == 0:
            Exceptions.Ex003(self)
        else:
            text = self.inpt_box_flnm.get()

        if len(self.inpt_box_flnm.get()) == 0:
            Exceptions.Ex004(self)
        else:
            text = self.inpt_box_flnm.get()

        if len(self.inpt_box_OS.get()) == 0:
            Exceptions.Ex005(self)
        else:
            text = self.inpt_box_flnm.get()

        if hasattr(self, 'cam_label'):
            self.cam_label.destroy()

        if hasattr(self, 'roi_label'):
            self.roi_label.destroy()

        if hasattr(self, 'path_btn'):
            self.path_btn.destroy()

        if hasattr(self, 'canvas'):
            self.canvas.destroy()
            
        if hasattr(self, 'save_btn'):
            self.save_btn.destroy()
        
        print(log()+"cam mtd intiated Imgprocessor")
        for k in range(1):#k é o número de medições

            #print(" ")
            #print("****************************************************************")
            #print("                        MEDIÇÃO ",k+1)
            #print("****************************************************************")

            def nothing(x):
                pass

            if hasattr(self, 'imgtk2') and hasattr(self, 'cam_label') and self.img_mtd_chk.instate(['selected']): #case to switch from cam mtd to img mtd
                self.imgtk2 = None
                self.imgtk2  = np.array([])
                self.cv2image = None
                self.root = os.getcwd()
                #self.l_flnm = filedialog.askopenfilename(initialdir = root) ## devkitoriginal
                self.l_flnm = filedialog.askopenfilename(initialdir = 'C:\\Users\\Castro\\Desktop') ## devkitmod
                #self.image = os.chdir(path=root)
                
                if self.l_flnm != "":
                    #self.image = os.chdir(self.l_flnm)
                    self.image = cv2.imread(self.l_flnm)
                    self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                    self.Imgprocessor()
                
                else:
                    Exceptions.Ex001(self)

            if hasattr(self, 'imgtk2') and hasattr(self, 'cam_label') and self.cam_mtd_chk.instate(['selected']): #case to process image obtained in cam mtd
                print(log()+"cam mtd intiated Imageprocessor")
                root = os.getcwd()
                self.image = cv2.imread(self.s_flnm_cap)
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                self.Imgprocessor()
                #self.s_flnm = filedialog.asksaveasfilename(initialdir=root)

            else:

            #if (self.imgtk2 == None) and (self.cam_label == None) and self.img_mtd_chk.instate(['selected']):
                root = os.getcwd()
                print(log()+"Imageprocessor initiated while none conditions true")
                self.imgtk2 = None
                self.imgtk2  = np.array([])
                self.cv2image = None
                root = os.getcwd()
                self.l_flnm = filedialog.askopenfilename(initialdir = root) ## devkitoriginal
                #self.l_flnm = filedialog.askopenfilename(initialdir = 'C:\\Users\\Castro\\Desktop') ## devkitmod
                
                if self.l_flnm != "":
                    self.image = cv2.imread(self.l_flnm)
                    self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                    self.Imgprocessor()
    
                else:
                    Exceptions.Ex001(self)

    def cam_mtd(self):
        print (log()+'cam_mtd intiated')
        
        if hasattr(self, 'image_label'):
            self.image_label.destroy()
        
        """if hasattr(self, 'cam_label'):
            Main.cam_label.destroy(self)"""
        
        if hasattr(self, 'roi_label'):    
            self.roi_label.destroy()
            print(log()+'roi_label label destroyed')

        if hasattr(self, 'path_btn'):
            self.path_btn.destroy()
            print(log()+'path_btn label destroyed')

        if hasattr (self, 'self.canvas'):
            self.canvas.destroy()
            print(log()+'self.canvas label destroyed')
        
        print(log()+'camera connection check running...')

        self.cam_label = Label(self.Measure)
        self.cam_label.place(x = 33 + self.inpt_box_OS.winfo_width(), y = 40)
        self.cam_label.grid_propagate (True)

        def testdevice(source):
            captest = cv2.VideoCapture(source) 
            if captest is None or not captest.isOpened():
                print(log()+'unable to connect to video source: ', source)
                Exceptions.Ex008(self)

        testdevice(0)

        cap = cv2.VideoCapture(0)
        if cap != None:
            print(log()+'camera connection requested')

        w_c, h_c = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.master.geometry("{}x{}".format(w_c + 60 + self.inpt_box_OS.winfo_width(), h_c))

        self.show_marker = True
        
        def show_frames():
            ret, frame = cap.read()
            if ret:
                self.cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if self.show_marker:
                    cv2.drawMarker(self.cv2image, (int(round((w_c/2),0)), int(round((h_c/2),0))), (255, 0, ), cv2.MARKER_CROSS, 1900, 1)

                img = PIL.Image.fromarray(self.cv2image)
                self.imgtk2 = ImageTk.PhotoImage(image=img)
                self.cam_label.configure(image=self.imgtk2)
            self.cam_label.after(20, show_frames)
            
        show_frames()

        def save_cam_img ():
            
            self.show_marker = False

            print(log()+'save_cam_img initiated')

            global text

            if len(self.inpt_box_flnm.get()) == 0 and len(self.inpt_box_OS.get()) == 0:
                Exceptions.Ex003(self)
            else:
                text = self.inpt_box_flnm.get()

            if len(self.inpt_box_flnm.get()) == 0:
                Exceptions.Ex004(self)
            else:
                text = self.inpt_box_flnm.get()

            if len(self.inpt_box_OS.get()) == 0:
                Exceptions.Ex005(self)
            else:
                text = self.inpt_box_flnm.get()

            if not os.path.exists(self.msre_record + '/' + self.folder_OS):
                os.makedirs(self.msre_record + '/' + self.folder_OS)
                print(log()+'OS Folder name created.')

            save_directory = os.path.join(self.msre_record, self.folder_OS) 
            file_extension = ".bmp"
            file_name = self.inpt_box_flnm.get() + " - Capture" 
            self.s_flnm_cap = os.path.join(save_directory, file_name + file_extension)
            
            try:
                pil_image = ImageTk.getimage(self.imgtk2)
                pil_image.save(self.s_flnm_cap)
                self.paralel_img_mtd()
            except Exception as e:
                Exceptions.Ex002(self)
                
        self.save_btn = ttk.Button(self.Measure, text = "Capture", command = save_cam_img, style = 'TButton')
        self.save_btn.grid (row = 0, column = 2)

open_wdw = Tk()
software = TAMS(open_wdw)
open_wdw.mainloop()

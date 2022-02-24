import tkinter as tk
from tkinter import *
from tkinter import ttk
from registers import *
from memory import *
from Instruction import *
import sys, os


class Window:
    def __init__(self, master, gpr0, gpr1, gpr2, gpr3, ixr1, ixr2, ixr3, pc, mar, mbr, ir, mfr, mem, ins):
        self.master = master
        self.registers = [gpr0, gpr1, gpr2, gpr3, ixr1, ixr2, ixr3, pc, mar, mbr, ir, mfr]
        self.ixrs = [ixr1, ixr2, ixr3]
        self.gprs = [gpr0, gpr1, gpr2, gpr3]
        self.mem = mem
        self.ins_object = ins

        # parameters to update the label widget
        self.txt_value_GPR0 = StringVar()
        self.txt_value_GPR1 = StringVar()
        self.txt_value_GPR2 = StringVar()
        self.txt_value_GPR3 = StringVar()
        self.txt_value_IXR1 = StringVar()
        self.txt_value_IXR2 = StringVar()
        self.txt_value_IXR3 = StringVar()
        self.txt_value_PC = StringVar()
        self.txt_value_MAR = StringVar()
        self.txt_value_MBR = StringVar()
        self.txt_value_IR = StringVar()
        self.txt_value_MFR = StringVar()
        self.txt_value_registers = [self.txt_value_GPR0, self.txt_value_GPR1, self.txt_value_GPR2, self.txt_value_GPR3,
                                    self.txt_value_IXR1, self.txt_value_IXR2, self.txt_value_IXR3,
                                    self.txt_value_PC, self.txt_value_MAR, self.txt_value_MBR, self.txt_value_IR, self.txt_value_MFR]

        self.txt_value_Opcode = StringVar()
        self.txt_value_GPR_index = StringVar()
        self.txt_value_IXR_index = StringVar()
        self.txt_value_Indirect = StringVar()
        self.txt_value_Address = StringVar()


        # set layout
        self.set_window(gpr0, gpr1, gpr2, gpr3, ixr1, ixr2, ixr3, pc, mar, mbr, ir, mfr, mem)

    def set_window(self, gpr0, gpr1, gpr2, gpr3, ixr1, ixr2, ixr3, pc, mar, mbr, ir, mfr, mem):
        """This function sets the layout of the window"""
        # GUI setting para
        win_title = 'Computer Simulator'
        win_size = '1600x900'
        window_width = 1200
        window_height = 800
        win_color = '#0096c7'
        instruction_btn_width = 5
        interact_btn_width = 10

        # centers window on screen
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # GUI setting
        self.master.title(win_title)
        self.master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.master.minsize(window_width, window_height)
        self.master["bg"] = win_color
        self.master.resizable(False, False)

        # -----------------------------START: TOP PANEL --------------------------------#
        self.op_panel = tk.Frame(self.master, height=600, width=1200, bg='#0096c7')
        self.op_panel.pack(expand=True, side='top', fill='both', padx=5, pady=5)

        # ------------------------------START: GPR PANEL ---------------------------#

        self.gpr_panel = ttk.Frame(self.op_panel, height=50, width=33)
        self.gpr_panel.config(style='new.TFrame')

        self.gpr_panel.grid(column=0, row=0, padx=35, pady=[50, 25])

        self.gpr_panel.rowconfigure(0, weight=1)
        self.gpr_panel.rowconfigure(1, weight=1)
        self.gpr_panel.rowconfigure(2, weight=1)
        self.gpr_panel.rowconfigure(3, weight=1)

        self.gpr_panel.columnconfigure(0, weight=2)
        self.gpr_panel.columnconfigure(1, weight=1)
        self.gpr_panel.columnconfigure(2, weight=1)
        self.gpr_panel.columnconfigure(3, weight=1)
        self.gpr_panel.columnconfigure(4, weight=1)
        self.gpr_panel.columnconfigure(5, weight=1)
        self.gpr_panel.columnconfigure(6, weight=1)
        self.gpr_panel.columnconfigure(7, weight=1)
        self.gpr_panel.columnconfigure(8, weight=1)
        self.gpr_panel.columnconfigure(9, weight=1)
        self.gpr_panel.columnconfigure(10, weight=1)
        self.gpr_panel.columnconfigure(11, weight=1)
        self.gpr_panel.columnconfigure(12, weight=1)
        self.gpr_panel.columnconfigure(13, weight=1)
        self.gpr_panel.columnconfigure(14, weight=1)
        self.gpr_panel.columnconfigure(15, weight=1)
        self.gpr_panel.columnconfigure(16, weight=1)
        self.gpr_panel.columnconfigure(17, weight=2)
        # -----------------------START: GPR LABELS ----------------------#
        self.gpr0_label = ttk.Label(self.gpr_panel, text="GPR 0", anchor='c', width=5)
        self.gpr0_label.grid(column=0, row=0, padx=5, pady=5, ipadx=2)
        self.gpr1_label = ttk.Label(self.gpr_panel, text="GPR 1", anchor='c', width=5)
        self.gpr1_label.grid(column=0, row=1, padx=5, pady=5, ipadx=2)
        self.gpr2_label = ttk.Label(self.gpr_panel, text="GPR 2", anchor='c', width=5)
        self.gpr2_label.grid(column=0, row=2, padx=5, pady=5, ipadx=2)
        self.gpr3_label = ttk.Label(self.gpr_panel, text="GPR 3", anchor='c', width=5)
        self.gpr3_label.grid(column=0, row=3, padx=5, pady=5, ipadx=2)
        # -----------------------END: GPR LABELS ------------------------#

        # -----------------------START: GPR LABELS (LIGHTS) ------------------------#
        self.gpr0_label1 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label1.grid(column=1, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label2 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label2.grid(column=2, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label3 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label3.grid(column=3, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label4 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label4.grid(column=4, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label5 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label5.grid(column=5, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label6 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label6.grid(column=6, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label7 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label7.grid(column=7, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label8 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label8.grid(column=8, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label9 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label9.grid(column=9, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label10 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label10.grid(column=10, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label11 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label11.grid(column=11, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label12 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label12.grid(column=12, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label13 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label13.grid(column=13, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label14 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label14.grid(column=14, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label15 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label15.grid(column=15, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_label16 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr0_label16.grid(column=16, row=0, sticky=tk.E, padx=2, pady=5)
        self.gpr0_GUI = [self.gpr0_label1, self.gpr0_label2, self.gpr0_label3, self.gpr0_label4,
                        self.gpr0_label5, self.gpr0_label6, self.gpr0_label7, self.gpr0_label8,
                        self.gpr0_label9, self.gpr0_label10, self.gpr0_label11, self.gpr0_label12,
                        self.gpr0_label13, self.gpr0_label14, self.gpr0_label15, self.gpr0_label16]

        self.gpr1_label1 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label1.grid(column=1, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label2 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label2.grid(column=2, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label3 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label3.grid(column=3, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label4 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label4.grid(column=4, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label5 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label5.grid(column=5, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label6 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label6.grid(column=6, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label7 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label7.grid(column=7, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label8 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label8.grid(column=8, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label9 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label9.grid(column=9, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label10 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label10.grid(column=10, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label11 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label11.grid(column=11, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label12 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label12.grid(column=12, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label13 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label13.grid(column=13, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label14 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label14.grid(column=14, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label15 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label15.grid(column=15, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_label16 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr1_label16.grid(column=16, row=1, sticky=tk.E, padx=2, pady=5)
        self.gpr1_GUI = [self.gpr1_label1, self.gpr1_label2, self.gpr1_label3, self.gpr1_label4,
                        self.gpr1_label5, self.gpr1_label6, self.gpr1_label7, self.gpr1_label8,
                        self.gpr1_label9, self.gpr1_label10, self.gpr1_label11, self.gpr1_label12,
                        self.gpr1_label13, self.gpr1_label14, self.gpr1_label15, self.gpr1_label16]

        self.gpr2_label1 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label1.grid(column=1, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label2 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label2.grid(column=2, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label3 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label3.grid(column=3, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label4 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label4.grid(column=4, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label5 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label5.grid(column=5, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label6 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label6.grid(column=6, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label7 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label7.grid(column=7, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label8 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label8.grid(column=8, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label9 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label9.grid(column=9, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label10 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label10.grid(column=10, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label11 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label11.grid(column=11, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label12 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label12.grid(column=12, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label13 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label13.grid(column=13, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label14 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label14.grid(column=14, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label15 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label15.grid(column=15, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_label16 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr2_label16.grid(column=16, row=2, sticky=tk.E, padx=2, pady=5)
        self.gpr2_GUI = [self.gpr2_label1, self.gpr2_label2, self.gpr2_label3, self.gpr2_label4,
                        self.gpr2_label5, self.gpr2_label6, self.gpr2_label7, self.gpr2_label8,
                        self.gpr2_label9, self.gpr2_label10, self.gpr2_label11, self.gpr2_label12,
                        self.gpr2_label13, self.gpr2_label14, self.gpr2_label15, self.gpr2_label16]

        self.gpr3_label1 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label1.grid(column=1, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label2 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label2.grid(column=2, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label3 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label3.grid(column=3, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label4 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label4.grid(column=4, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label5 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label5.grid(column=5, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label6 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label6.grid(column=6, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label7 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label7.grid(column=7, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label8 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label8.grid(column=8, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label9 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label9.grid(column=9, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label10 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label10.grid(column=10, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label11 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label11.grid(column=11, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label12 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label12.grid(column=12, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label13 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label13.grid(column=13, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label14 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label14.grid(column=14, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label15 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label15.grid(column=15, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_label16 = tk.Label(self.gpr_panel, text='  ', width=2, bg='black')
        self.gpr3_label16.grid(column=16, row=3, sticky=tk.E, padx=2, pady=5)
        self.gpr3_GUI = [self.gpr3_label1, self.gpr3_label2, self.gpr3_label3, self.gpr3_label4,
                        self.gpr3_label5, self.gpr3_label6, self.gpr3_label7, self.gpr3_label8,
                        self.gpr3_label9, self.gpr3_label10, self.gpr3_label11, self.gpr3_label12,
                        self.gpr3_label13, self.gpr3_label14, self.gpr3_label15, self.gpr3_label16]

        # -----------------------END: GPR LABELS (LIGHTS) ------------------------#
        # -----------------------START: GPR LOAD BUTTONS------------------------#
        def gpr0_load_callback():
            print("gpr0 load button clicked")
            self.func_reg_load(self.gpr0_GUI, self.registers[0])

        gpr0_btn = ttk.Button(self.gpr_panel, text='LD', command=gpr0_load_callback, width=6)
        gpr0_btn.grid(column=17, row=0, padx=5, pady=5)

        def gpr1_load_callback():
            print("gpr1 load button clicked")
            self.func_reg_load(self.gpr1_GUI, self.registers[1])

        gpr1_btn = ttk.Button(self.gpr_panel, text='LD', command=gpr1_load_callback, width=6)
        gpr1_btn.grid(column=17, row=1, padx=5, pady=5)

        def gpr2_load_callback():
            print("gpr2 load button clicked")
            self.func_reg_load(self.gpr2_GUI, self.registers[2])

        gpr2_btn = ttk.Button(self.gpr_panel, text='LD', command=gpr2_load_callback, width=6)
        gpr2_btn.grid(column=17, row=2, padx=5, pady=5)

        def gpr3_load_callback():
            print("gpr3 load button clicked")
            self.func_reg_load(self.gpr3_GUI, self.registers[3])

        gpr3_btn = ttk.Button(self.gpr_panel, text='LD', command=gpr3_load_callback, width=6)
        gpr3_btn.grid(column=17, row=3, padx=5, pady=5)

        # -----------------------END: GPR LOAD BUTTONS--------------------------#

        # -----------------------END: GPR PANEL-------------------------------------#
        # ------------------------------START: IXR PANEL ---------------------------#

        self.ixr_panel = ttk.Frame(self.op_panel, height=50, width=33)
        self.ixr_panel.config(style='new.TFrame')

        self.ixr_panel.grid(column=0, row=1, padx=35)

        self.ixr_panel.rowconfigure(0, weight=1)
        self.ixr_panel.rowconfigure(1, weight=1)
        self.ixr_panel.rowconfigure(2, weight=1)

        self.ixr_panel.columnconfigure(0, weight=2)
        self.ixr_panel.columnconfigure(1, weight=1)
        self.ixr_panel.columnconfigure(2, weight=1)
        self.ixr_panel.columnconfigure(3, weight=1)
        self.ixr_panel.columnconfigure(4, weight=1)
        self.ixr_panel.columnconfigure(5, weight=1)
        self.ixr_panel.columnconfigure(6, weight=1)
        self.ixr_panel.columnconfigure(7, weight=1)
        self.ixr_panel.columnconfigure(8, weight=1)
        self.ixr_panel.columnconfigure(9, weight=1)
        self.ixr_panel.columnconfigure(10, weight=1)
        self.ixr_panel.columnconfigure(11, weight=1)
        self.ixr_panel.columnconfigure(12, weight=1)
        self.ixr_panel.columnconfigure(13, weight=1)
        self.ixr_panel.columnconfigure(14, weight=1)
        self.ixr_panel.columnconfigure(15, weight=1)
        self.ixr_panel.columnconfigure(16, weight=1)
        self.ixr_panel.columnconfigure(17, weight=2)
        # -----------------------START: IXR LABELS ----------------------#
        self.ixr1_label = ttk.Label(self.ixr_panel, text="IXR 1", anchor='c', width=5)
        self.ixr1_label.grid(column=0, row=0, padx=5, pady=5, ipadx=2)
        self.ixr2_label = ttk.Label(self.ixr_panel, text="IXR 2", anchor='c', width=5)
        self.ixr2_label.grid(column=0, row=1, padx=5, pady=5, ipadx=2)
        self.ixr3_label = ttk.Label(self.ixr_panel, text="IXR 3", anchor='c', width=5)
        self.ixr3_label.grid(column=0, row=2, padx=5, pady=5, ipadx=2)
        # -----------------------END: IXR LABELS ------------------------#

        # -----------------------START: IXR LABELS (LIGHTS) ------------------------#
        self.ixr1_label1 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label1.grid(column=1, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label2 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label2.grid(column=2, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label3 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label3.grid(column=3, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label4 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label4.grid(column=4, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label5 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label5.grid(column=5, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label6 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label6.grid(column=6, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label7 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label7.grid(column=7, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label8 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label8.grid(column=8, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label9 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label9.grid(column=9, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label10 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label10.grid(column=10, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label11 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label11.grid(column=11, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label12 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label12.grid(column=12, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label13 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label13.grid(column=13, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label14 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label14.grid(column=14, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label15 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label15.grid(column=15, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_label16 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr1_label16.grid(column=16, row=0, sticky=tk.E, padx=2, pady=5)
        self.ixr1_GUI = [self.ixr1_label1, self.ixr1_label2, self.ixr1_label3, self.ixr1_label4,
                        self.ixr1_label5, self.ixr1_label6, self.ixr1_label7, self.ixr1_label8,
                        self.ixr1_label9, self.ixr1_label10, self.ixr1_label11, self.ixr1_label12,
                        self.ixr1_label13, self.ixr1_label14, self.ixr1_label15, self.ixr1_label16]

        self.ixr2_label1 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label1.grid(column=1, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label2 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label2.grid(column=2, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label3 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label3.grid(column=3, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label4 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label4.grid(column=4, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label5 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label5.grid(column=5, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label6 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label6.grid(column=6, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label7 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label7.grid(column=7, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label8 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label8.grid(column=8, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label9 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label9.grid(column=9, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label10 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label10.grid(column=10, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label11 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label11.grid(column=11, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label12 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label12.grid(column=12, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label13 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label13.grid(column=13, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label14 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label14.grid(column=14, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label15 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label15.grid(column=15, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_label16 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr2_label16.grid(column=16, row=1, sticky=tk.E, padx=2, pady=5)
        self.ixr2_GUI = [self.ixr2_label1, self.ixr2_label2, self.ixr2_label3, self.ixr2_label4,
                        self.ixr2_label5, self.ixr2_label6, self.ixr2_label7, self.ixr2_label8,
                        self.ixr2_label9, self.ixr2_label10, self.ixr2_label11, self.ixr2_label12,
                        self.ixr2_label13, self.ixr2_label14, self.ixr2_label15, self.ixr2_label16]

        self.ixr3_label1 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label1.grid(column=1, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label2 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label2.grid(column=2, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label3 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label3.grid(column=3, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label4 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label4.grid(column=4, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label5 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label5.grid(column=5, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label6 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label6.grid(column=6, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label7 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label7.grid(column=7, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label8 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label8.grid(column=8, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label9 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label9.grid(column=9, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label10 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label10.grid(column=10, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label11 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label11.grid(column=11, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label12 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label12.grid(column=12, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label13 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label13.grid(column=13, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label14 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label14.grid(column=14, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label15 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label15.grid(column=15, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_label16 = tk.Label(self.ixr_panel, text='  ', width=2, bg='black')
        self.ixr3_label16.grid(column=16, row=2, sticky=tk.E, padx=2, pady=5)
        self.ixr3_GUI = [self.ixr3_label1, self.ixr3_label2, self.ixr3_label3, self.ixr3_label4,
                        self.ixr3_label5, self.ixr3_label6, self.ixr3_label7, self.ixr3_label8,
                        self.ixr3_label9, self.ixr3_label10, self.ixr3_label11, self.ixr3_label12,
                        self.ixr3_label13, self.ixr3_label14, self.ixr3_label15, self.ixr3_label16]

        # -----------------------END: IXR LABELS (LIGHTS) ----------------------#

        # -----------------------START: IXR LOAD BUTTONS------------------------#

        def ixr1_load_callback():
            print("ixr1 load button clicked")
            self.func_reg_load(self.ixr1_GUI, self.registers[4])

        ixr1_btn = ttk.Button(self.ixr_panel, text='LD', command=ixr1_load_callback, width=6)
        ixr1_btn.grid(column=17, row=0, padx=5, pady=5)

        def ixr2_load_callback():
            print("ixr2 load button clicked")
            self.func_reg_load(self.ixr2_GUI, self.registers[5])

        ixr2_btn = ttk.Button(self.ixr_panel, text='LD', command=ixr2_load_callback, width=6)
        ixr2_btn.grid(column=17, row=1, padx=5, pady=5)

        def ixr3_load_callback():
            print("ixr3 load button clicked")
            self.func_reg_load(self.ixr3_GUI, self.registers[6])

        ixr3_btn = ttk.Button(self.ixr_panel, text='LD', command=ixr3_load_callback, width=6)
        ixr3_btn.grid(column=17, row=2, padx=5, pady=5)

        # -----------------------END: IXR LOAD BUTTONS--------------------------#

        # ------------------------------END: IXR PANEL -----------------------------#

        # ------------------------------START: RIGHT PANEL ---------------------------#

        self.right_panel = ttk.Frame(self.op_panel, height=50, width=33)
        self.right_panel.config(style='new.TFrame')

        self.right_panel.grid(column=1, row=0, padx=[100, 20], pady=[77, 20], sticky=tk.E)

        self.right_panel.rowconfigure(0, weight=1)
        self.right_panel.rowconfigure(1, weight=1)
        self.right_panel.rowconfigure(2, weight=1)
        self.right_panel.rowconfigure(3, weight=1)
        self.right_panel.rowconfigure(4, weight=1)
        self.right_panel.rowconfigure(5, weight=1)

        self.right_panel.columnconfigure(0, weight=2)
        self.right_panel.columnconfigure(1, weight=1)
        self.right_panel.columnconfigure(2, weight=1)
        self.right_panel.columnconfigure(3, weight=1)
        self.right_panel.columnconfigure(4, weight=1)
        self.right_panel.columnconfigure(5, weight=1)
        self.right_panel.columnconfigure(6, weight=1)
        self.right_panel.columnconfigure(7, weight=1)
        self.right_panel.columnconfigure(8, weight=1)
        self.right_panel.columnconfigure(9, weight=1)
        self.right_panel.columnconfigure(10, weight=1)
        self.right_panel.columnconfigure(11, weight=1)
        self.right_panel.columnconfigure(12, weight=1)
        self.right_panel.columnconfigure(13, weight=1)
        self.right_panel.columnconfigure(14, weight=1)
        self.right_panel.columnconfigure(15, weight=1)
        self.right_panel.columnconfigure(16, weight=1)
        self.right_panel.columnconfigure(17, weight=2)
        # -----------------------START: RIGHT LABELS ----------------------#
        self.pc_label = ttk.Label(self.right_panel, text="PC", anchor='c', width=5)
        self.pc_label.grid(column=3, row=0, padx=5, pady=5, ipadx=2, columnspan=2)
        self.mar_label = ttk.Label(self.right_panel, text="MAR", anchor='c', width=5)
        self.mar_label.grid(column=3, row=1, padx=5, pady=5, ipadx=2, columnspan=2)
        self.mbr_label = ttk.Label(self.right_panel, text="MBR", anchor='c', width=5)
        self.mbr_label.grid(column=0, row=2, padx=5, pady=5, ipadx=2)
        self.ir_label = ttk.Label(self.right_panel, text="IR", anchor='c', width=5)
        self.ir_label.grid(column=0, row=3, padx=5, pady=5, ipadx=2)
        self.mfr_label = ttk.Label(self.right_panel, text="MFR", anchor='c', width=5)
        self.mfr_label.grid(column=11, row=4, padx=5, pady=5, ipadx=2, columnspan=2)
        # self.privileged_label = ttk.Label(self.right_panel, text="PRIVILEGED", anchor='c')
        # self.privileged_label.grid(column=13, row=5, padx=5, pady=5, ipadx=2, columnspan=3)
        # -----------------------END: RIGHT LABELS ------------------------#

        # -----------------------START: RIGHT LABELS (LIGHTS) ------------------------#
        self.pc_label1 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label1.grid(column=5, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label2 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label2.grid(column=6, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label3 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label3.grid(column=7, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label4 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label4.grid(column=8, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label5 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label5.grid(column=9, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label6 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label6.grid(column=10, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label7 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label7.grid(column=11, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label8 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label8.grid(column=12, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label9 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label9.grid(column=13, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label10 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label10.grid(column=14, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label11 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label11.grid(column=15, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_label12 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.pc_label12.grid(column=16, row=0, sticky=tk.E, padx=2, pady=5)
        self.pc_GUI = [self.pc_label1, self.pc_label2, self.pc_label3, self.pc_label4,
                        self.pc_label5, self.pc_label6, self.pc_label7, self.pc_label8,
                        self.pc_label9, self.pc_label10, self.pc_label11, self.pc_label12]


        self.mar_label1 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label1.grid(column=5, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label2 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label2.grid(column=6, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label3 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label3.grid(column=7, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label4 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label4.grid(column=8, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label5 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label5.grid(column=9, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label6 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label6.grid(column=10, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label7 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label7.grid(column=11, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label8 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label8.grid(column=12, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label9 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label9.grid(column=13, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label10 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label10.grid(column=14, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label11 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label11.grid(column=15, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_label12 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mar_label12.grid(column=16, row=1, sticky=tk.E, padx=2, pady=5)
        self.mar_GUI = [self.mar_label1, self.mar_label2, self.mar_label3, self.mar_label4,
                        self.mar_label5, self.mar_label6, self.mar_label7, self.mar_label8,
                        self.mar_label9, self.mar_label10, self.mar_label11, self.mar_label12]


        self.mbr_label1 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label1.grid(column=1, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label2 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label2.grid(column=2, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label3 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label3.grid(column=3, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label4 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label4.grid(column=4, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label5 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label5.grid(column=5, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label6 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label6.grid(column=6, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label7 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label7.grid(column=7, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label8 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label8.grid(column=8, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label9 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label9.grid(column=9, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label10 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label10.grid(column=10, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label11 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label11.grid(column=11, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label12 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label12.grid(column=12, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label13 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label13.grid(column=13, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label14 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label14.grid(column=14, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label15 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label15.grid(column=15, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_label16 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mbr_label16.grid(column=16, row=2, sticky=tk.E, padx=2, pady=5)
        self.mbr_GUI = [self.mbr_label1, self.mbr_label2, self.mbr_label3, self.mbr_label4,
                        self.mbr_label5, self.mbr_label6, self.mbr_label7, self.mbr_label8,
                        self.mbr_label9, self.mbr_label10, self.mbr_label11, self.mbr_label12,
                        self.mbr_label13, self.mbr_label14, self.mbr_label15, self.mbr_label16]

        self.ir_label1 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label1.grid(column=1, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label2 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label2.grid(column=2, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label3 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label3.grid(column=3, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label4 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label4.grid(column=4, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label5 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label5.grid(column=5, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label6 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label6.grid(column=6, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label7 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label7.grid(column=7, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label8 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label8.grid(column=8, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label9 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label9.grid(column=9, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label10 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label10.grid(column=10, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label11 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label11.grid(column=11, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label12 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label12.grid(column=12, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label13 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label13.grid(column=13, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label14 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label14.grid(column=14, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label15 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label15.grid(column=15, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_label16 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.ir_label16.grid(column=16, row=3, sticky=tk.E, padx=2, pady=5)
        self.ir_GUI = [self.ir_label1, self.ir_label2, self.ir_label3, self.ir_label4,
                        self.ir_label5, self.ir_label6, self.ir_label7, self.ir_label8,
                        self.ir_label9, self.ir_label10, self.ir_label11, self.ir_label12,
                        self.ir_label13, self.ir_label14, self.ir_label15, self.ir_label16]

        self.mfr_label1 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mfr_label1.grid(column=13, row=4, sticky=tk.E, padx=2, pady=5)
        self.mfr_label2 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mfr_label2.grid(column=14, row=4, sticky=tk.E, padx=2, pady=5)
        self.mfr_label3 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mfr_label3.grid(column=15, row=4, sticky=tk.E, padx=2, pady=5)
        self.mfr_label4 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        self.mfr_label4.grid(column=16, row=4, sticky=tk.E, padx=2, pady=5)
        self.mfr_GUI = [self.mfr_label1, self.mfr_label2, self.mfr_label3, self.mfr_label4]

        # self.privileged_label1 = tk.Label(self.right_panel, text='  ', width=2, bg='black')
        # self.privileged_label1.grid(column=16, row=5, sticky=tk.E, padx=2, pady=5)

        # -----------------------END: RIGHT LABELS (LIGHTS) ------------------------#

        # -----------------------START: RIGHT LOAD BUTTONS------------------------#
        def pc_load_callback():
            print("pc load button clicked")
            self.func_reg_load(self.pc_GUI, self.registers[7])

        pc_btn = ttk.Button(self.right_panel, text='LD', command=pc_load_callback, width=6)
        pc_btn.grid(column=17, row=0, padx=5, pady=5)

        def mar_load_callback():
            print("mar load button clicked")
            self.func_reg_load(self.mar_GUI, self.registers[8])

        mar_btn = ttk.Button(self.right_panel, text='LD', command=mar_load_callback, width=6)
        mar_btn.grid(column=17, row=1, padx=5, pady=5)

        def mbr_load_callback():
            print("mbr load button clicked")
            self.func_reg_load(self.mbr_GUI, self.registers[9])

        mbr_btn = ttk.Button(self.right_panel, text='LD', command=mbr_load_callback, width=6)
        mbr_btn.grid(column=17, row=2, padx=5, pady=5)

        # -----------------------END: RIGHT LOAD BUTTONS--------------------------#

        # -----------------------END: RIGHT PANEL-------------------------------------#

        # -----------------------------END TOP PANEL -----------------------------------#

        # -----------------------------START: BOTTOM PANEL -----------------------------#
        bottom_panel = tk.Frame(self.master, height=200, width=1200)
        bottom_panel.config(bg='#0096c7')
        bottom_panel.pack(expand=True, side='bottom', fill='both', padx=60, pady=5)

        # ----------------------------START: OPERATION PANEL--------------------------- #
        # Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
        s = ttk.Style()
        s.configure('new.TFrame', background='#48cae4')

        self.op_panel = ttk.Frame(bottom_panel, height=50, width=100)
        self.op_panel.config(style='new.TFrame')

        self.op_panel.grid(column=0, row=0, padx=10)

        self.op_panel.rowconfigure(0, weight=1)
        self.op_panel.rowconfigure(1, weight=2)

        self.op_panel.columnconfigure(0, weight=1)
        self.op_panel.columnconfigure(1, weight=1)
        self.op_panel.columnconfigure(2, weight=1)
        self.op_panel.columnconfigure(3, weight=1)
        self.op_panel.columnconfigure(4, weight=1)
        self.op_panel.columnconfigure(5, weight=1)

        op_text1 = tk.StringVar()
        self.op_entry1 = ttk.Entry(self.op_panel, textvariable=op_text1, width=3)
        self.op_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        op_text2 = tk.StringVar()
        self.op_entry2 = ttk.Entry(self.op_panel, textvariable=op_text2, width=3)
        self.op_entry2.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        op_text3 = tk.StringVar()
        self.op_entry3 = ttk.Entry(self.op_panel, textvariable=op_text3, width=3)
        self.op_entry3.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)

        op_text4 = tk.StringVar()
        self.op_entry4 = ttk.Entry(self.op_panel, textvariable=op_text4, width=3)
        self.op_entry4.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)

        op_text5 = tk.StringVar()
        self.op_entry5 = ttk.Entry(self.op_panel, textvariable=op_text5, width=3)
        self.op_entry5.grid(column=4, row=0, sticky=tk.E, padx=5, pady=5)

        op_text6 = tk.StringVar()
        self.op_entry6 = ttk.Entry(self.op_panel, textvariable=op_text6, width=3)
        self.op_entry6.grid(column=5, row=0, sticky=tk.E, padx=5, pady=5)

        op_label = ttk.Label(self.op_panel, text="Operation", anchor='s')
        op_label.grid(column=1, row=1, sticky=tk.S, padx=5, pady=5, ipadx=5, columnspan=4)

        # op_entry1.get()
        # op_entry1.focus()

        # ----------------------------END: OPERATION PANEL--------------------------- #

        # ----------------------------START: GPR ADDRESS PANEL--------------------------- #
        # Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
        s = ttk.Style()
        s.configure('new.TFrame', background='#48cae4')

        self.gpr_add_panel = ttk.Frame(bottom_panel, height=50, width=33)
        self.gpr_add_panel.config(style='new.TFrame')

        self.gpr_add_panel.grid(column=1, row=0, padx=10)

        self.gpr_add_panel.rowconfigure(0, weight=1)
        self.gpr_add_panel.rowconfigure(1, weight=2)

        self.gpr_add_panel.columnconfigure(0, weight=1)
        self.gpr_add_panel.columnconfigure(1, weight=1)

        gpr_add_text1 = tk.StringVar()
        self.gpr_add_entry1 = ttk.Entry(self.gpr_add_panel, textvariable=gpr_add_text1, width=3)
        self.gpr_add_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        gpr_add_text2 = tk.StringVar()
        self.gpr_add_entry2 = ttk.Entry(self.gpr_add_panel, textvariable=gpr_add_text2, width=3)
        self.gpr_add_entry2.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        gpr_add_label = ttk.Label(self.gpr_add_panel, text="GPR", anchor='s')
        gpr_add_label.grid(column=0, row=1, sticky=tk.S, padx=5, pady=5, ipadx=5, columnspan=2)

        # ----------------------------END: GPR ADDRESS PANEL--------------------------- #

        # ----------------------------START: IXR ADDRESS PANEL--------------------------- #
        # Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
        s = ttk.Style()
        s.configure('new.TFrame', background='#48cae4')

        self.ixr_add_panel = ttk.Frame(bottom_panel, height=50, width=33)
        self.ixr_add_panel.config(style='new.TFrame')

        self.ixr_add_panel.grid(column=2, row=0, padx=10)

        self.ixr_add_panel.rowconfigure(0, weight=1)
        self.ixr_add_panel.rowconfigure(1, weight=2)

        self.ixr_add_panel.columnconfigure(0, weight=1)
        self.ixr_add_panel.columnconfigure(1, weight=1)

        ixr_add_text1 = tk.StringVar()
        self.ixr_add_entry1 = ttk.Entry(self.ixr_add_panel, textvariable=ixr_add_text1, width=3)
        self.ixr_add_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        ixr_add_text2 = tk.StringVar()
        self.ixr_add_entry2 = ttk.Entry(self.ixr_add_panel, textvariable=ixr_add_text2, width=3)
        self.ixr_add_entry2.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        ixr_add_label = ttk.Label(self.ixr_add_panel, text="IXR", anchor='s')
        ixr_add_label.grid(column=0, row=1, sticky=tk.S, padx=5, pady=5, ipadx=5, columnspan=2)

        # ----------------------------END: IXR ADDRESS PANEL--------------------------- #

        # ----------------------------START: I PANEL--------------------------- #
        # Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
        s = ttk.Style()
        s.configure('new.TFrame', background='#48cae4')

        self.i_panel = ttk.Frame(bottom_panel, height=50, width=33)
        self.i_panel.config(style='new.TFrame')

        self.i_panel.grid(column=3, row=0, padx=10)

        self.i_panel.rowconfigure(0, weight=1)
        self.i_panel.rowconfigure(1, weight=2)

        self.i_panel.columnconfigure(0, weight=1)

        i_text1 = tk.StringVar()
        self.i_entry1 = ttk.Entry(self.i_panel, textvariable=i_text1, width=3)
        self.i_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        i_label = ttk.Label(self.i_panel, text="I", anchor='s')
        i_label.grid(column=0, row=1, sticky=tk.S, padx=5, pady=5, ipadx=5, columnspan=2)

        # ----------------------------END: I PANEL--------------------------- #

        # ----------------------------START: ADDRESS PANEL--------------------------- #
        # Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
        s = ttk.Style()
        s.configure('new.TFrame', background='#48cae4')

        self.add_panel = ttk.Frame(bottom_panel, height=50, width=100)
        self.add_panel.config(style='new.TFrame')

        self.add_panel.grid(column=4, row=0, padx=10)

        self.add_panel.rowconfigure(0, weight=1)
        self.add_panel.rowconfigure(1, weight=2)

        self.add_panel.columnconfigure(0, weight=1)
        self.add_panel.columnconfigure(1, weight=1)
        self.add_panel.columnconfigure(2, weight=1)
        self.add_panel.columnconfigure(3, weight=1)
        self.add_panel.columnconfigure(4, weight=1)
        self.add_panel.columnconfigure(5, weight=1)

        add_text1 = tk.StringVar()
        self.add_entry1 = ttk.Entry(self.add_panel, textvariable=add_text1, width=3)
        self.add_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        add_text2 = tk.StringVar()
        self.add_entry2 = ttk.Entry(self.add_panel, textvariable=add_text2, width=3)
        self.add_entry2.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        add_text3 = tk.StringVar()
        self.add_entry3 = ttk.Entry(self.add_panel, textvariable=add_text3, width=3)
        self.add_entry3.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)

        add_text4 = tk.StringVar()
        self.add_entry4 = ttk.Entry(self.add_panel, textvariable=add_text4, width=3)
        self.add_entry4.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)

        add_text5 = tk.StringVar()
        self.add_entry5 = ttk.Entry(self.add_panel, textvariable=add_text5, width=3)
        self.add_entry5.grid(column=4, row=0, sticky=tk.E, padx=5, pady=5)

        add_label = ttk.Label(self.add_panel, text="Address", anchor='s')
        add_label.grid(column=1, row=1, sticky=tk.S, padx=5, pady=5, ipadx=5, columnspan=3)

        # ----------------------------END: ADDRESS PANEL--------------------------- #

        # ----------------------------START: BOTTOM BTN PANEL------------------------  #
        s = ttk.Style()
        s.configure('new.TFrame', background='#48cae4')

        bottom_btn_panel = ttk.Frame(bottom_panel, height=50, width=100)
        bottom_btn_panel.config(style='new.TFrame')

        bottom_btn_panel.grid(column=5, row=0, padx=50)

        bottom_btn_panel.rowconfigure(0, weight=1)
        bottom_btn_panel.rowconfigure(1, weight=1)

        bottom_btn_panel.columnconfigure(0, weight=1)
        bottom_btn_panel.columnconfigure(1, weight=1)
        bottom_btn_panel.columnconfigure(2, weight=1)
        bottom_btn_panel.columnconfigure(3, weight=1)

        # Store Button and Callback
        def store_callback():
            print("Store button clicked")
            self.func_store(mar, mbr, mem)
            # do something

        store_btn = ttk.Button(bottom_btn_panel, text='Store', command=store_callback, width=6)
        store_btn.grid(column=0, row=1, padx=5, pady=10)

        # St+ Button and Callback
        def stPlus_callback():
            print("St+ button clicked")
            self.func_st_plus(mar, mbr, mem)

        stPlus_btn = ttk.Button(bottom_btn_panel, text='St+', command=stPlus_callback, width=6)
        stPlus_btn.grid(column=1, row=1, padx=5, pady=10)

        # Load Button and Callback
        def load_callback():
            print("load button clicked")
            self.func_load(mar, mbr, mem)
\

        load_btn = ttk.Button(bottom_btn_panel, text='Load', command=load_callback, width=6)
        load_btn.grid(column=2, row=1, padx=5, pady=10)

        # ipl Button and Callback
        def ipl_callback():
            print("ipl button clicked")
            self.func_ipl(pc, mem)

        ipl_btn = tk.Button(bottom_btn_panel, text='IPL', command=ipl_callback, width=6, bg='red')
        ipl_btn.grid(column=3, row=1, padx=5, pady=10)

        # SS (Single Step) button and Callback
        def ss_callback():
            print("SS button clicked")
            self.func_ss(mem, pc, mar, mbr, ir, True)

        ss_btn = ttk.Button(bottom_btn_panel, text='SS', command=ss_callback, width=6)
        ss_btn.grid(column=0, row=2, columnspan=1, padx=5, pady=20, sticky=tk.W)

        # Run light
        run_label = ttk.Label(bottom_btn_panel, text='Run', width=4)
        run_label.grid(column=2, row=3, columnspan=1, padx=5, pady=10, sticky=tk.E)

        self.run_light_label = tk.Label(bottom_btn_panel, text='  ', width=2, bg="black")
        self.run_light_label.grid(column=3, row=3, columnspan=1, padx=2, pady=10, sticky=tk.W)

        # Halt
        halt_label = ttk.Label(bottom_btn_panel, text='Halt', width=4)
        halt_label.grid(column=0, row=3, columnspan=1, padx=5, pady=10, sticky=tk.E)

        self.halt_light_label = tk.Label(bottom_btn_panel, text='  ', width=2, bg="black")
        self.halt_light_label.grid(column=1, row=3, columnspan=1, padx=2, pady=10, sticky=tk.W)

        # Run Button and Callback
        def run_callback():
            print("run button clicked")
            self.run_light_label.config(bg='green')
            self.halt_light_label.config(bg='black')
            self.func_run(mem, pc, mar, mbr, ir)

        run_btn = ttk.Button(bottom_btn_panel, text='Run', command=run_callback, width=6)
        run_btn.grid(column=1, row=2, columnspan=1, padx=5, pady=20, sticky=tk.S)


        def reset_callback():
            print("reset button clicked")
            self.reset()

        reset_btn = ttk.Button(bottom_btn_panel, text='Reset', command=reset_callback, width=6)
        reset_btn.grid(column=2, row=2, columnspan=1, padx=5, pady=20, sticky=tk.E)

        # ----------------------------END: BOTTOM BTN PANEL---------------------------- #

        # -----------------------------END: BOTTOM PANEL -------------------------------#

    def reset(self):
        """This function resets all of the system"""
        self.mem.reset_memory()
        for i in self.registers:
             i.reset()
        self.ins_object.reset()

        self.refresh_reg_info()
        self.refresh_instruction_info()
        self.refresh_mem_info()

        self.run_light_label.config(bg="black")
        self.halt_light_label.config(bg="black")
        print('System Is Ready')

    def refresh_mem_info(self):
        """This function refreshes the mem_info"""
        content = ''
        for i in self.registers:
            content += i.label + ':\t' + i.value.zfill(i.size) +'\n'
        for i in range(len(self.mem.memory)):
            content += str(i) + ':\t' + str(int(self.mem.memory[i])) + '\n'

        print("MEMORY: \n" + content)
    # END: refresh_mem_info

    def refresh_instruction_info(self):
        # This function refreshes the text of instruction
        self.refresh_OpCode()
        self.refresh_GPR_address()
        self.refresh_IXR_address()
        self.refresh_I_instruction()
        self.refresh_ADD()



#   END: refresh_instruction_info

    def refresh_reg_info(self):
        """This function refreshes the text of registers"""

        length = len(self.registers)
        """        for i in range(length-1):
        print(f"{type(self.registers[i])}: {self.registers[i].value.zfill(self.registers[i].size)}")"""

        gpr0_val = self.registers[0].get_value()
        for i in range(0, 16):
            if gpr0_val[i] == '0':
                self.gpr0_GUI[i].config(bg="black")
                self.gpr0_GUI[i].update()
            elif gpr0_val[i] == '1':
                self.gpr0_GUI[i].config(bg="yellow")
                self.gpr0_GUI[i].update()

        gpr1_val = self.registers[1].get_value()
        for i in range(0, 16):
            if gpr1_val[i] == '0':
                self.gpr1_GUI[i].config(bg="black")
                self.gpr1_GUI[i].update()
            elif gpr1_val[i] == '1':
                self.gpr1_GUI[i].config(bg="yellow")
                self.gpr1_GUI[i].update()

        gpr2_val = self.registers[2].get_value()
        for i in range(0, 16):
            if gpr2_val[i] == '0':
                self.gpr2_GUI[i].config(bg="black")
                self.gpr2_GUI[i].update()
            elif gpr2_val[i] == '1':
                self.gpr2_GUI[i].config(bg="yellow")
                self.gpr2_GUI[i].update()

        gpr3_val = self.registers[3].get_value()
        for i in range(0, 16):
            if gpr3_val[i] == '0':
                self.gpr3_GUI[i].config(bg="black")
                self.gpr3_GUI[i].update()
            elif gpr3_val[i] == '1':
                self.gpr3_GUI[i].config(bg="yellow")
                self.gpr3_GUI[i].update()

        ixr1_val = self.registers[4].get_value()
        for i in range(0, 16):
            if ixr1_val[i] == '0':
                self.ixr1_GUI[i].config(bg="black")
                self.ixr1_GUI[i].update()
            elif ixr1_val[i] == '1':
                self.ixr1_GUI[i].config(bg="yellow")
                self.ixr1_GUI[i].update()

        ixr2_val = self.registers[5].get_value()
        for i in range(0, 16):
            if ixr2_val[i] == '0':
                self.ixr2_GUI[i].config(bg="black")
                self.ixr2_GUI[i].update()
            elif ixr2_val[i] == '1':
                self.ixr2_GUI[i].config(bg="yellow")
                self.ixr2_GUI[i].update()

        ixr3_val = self.registers[6].get_value()
        for i in range(0, 16):
            if ixr3_val[i] == '0':
                self.ixr3_GUI[i].config(bg="black")
                self.ixr3_GUI[i].update()
            elif ixr3_val[i] == '1':
                self.ixr3_GUI[i].config(bg="yellow")
                self.ixr3_GUI[i].update()

        pc_val = self.registers[7].get_value()
        for i in range(0, 12):
            if pc_val[i] == '0':
                self.pc_GUI[i].config(bg="black")
                self.pc_GUI[i].update()
            elif pc_val[i] == '1':
                self.pc_GUI[i].config(bg="yellow")
                self.pc_GUI[i].update()

        mar_val = self.registers[8].get_value()
        for i in range(0, 12):
            if mar_val[i] == '0':
                self.mar_GUI[i].config(bg="black")
                self.mar_GUI[i].update()
            elif mar_val[i] == '1':
                self.mar_GUI[i].config(bg="yellow")
                self.mar_GUI[i].update()

        mbr_val = self.registers[9].get_value()
        for i in range(15, (15-len(mbr_val)), -1):
            if mbr_val[i] == '0':
                self.mbr_GUI[i].config(bg="black")
                self.mbr_GUI[i].update()
            elif mbr_val[i] == '1':
                self.mbr_GUI[i].config(bg="yellow")
                self.mbr_GUI[i].update()
        mbr_val = self.registers[9].get_value()

        for i in range(0, (16-len(mbr_val))):
                self.mbr_GUI[i].config(bg="black")
                self.mbr_GUI[i].update()


        ir_val = self.registers[10].get_value()
        for i in range(0,16):
            if ir_val[i] == '0':
                self.ir_GUI[i].config(bg="black")
                self.ir_GUI[i].update()
            elif ir_val[i] == '1':
                self.ir_GUI[i].config(bg="yellow")
                self.ir_GUI[i].update()

        mfr_val = self.registers[11].get_value()
        for i in range(0,4):
            if mfr_val[i] == '0':
                self.mfr_GUI[i].config(bg="black")
                self.mfr_GUI[i].update()
            elif mfr_val[i] == '1':
                self.mfr_GUI[i].config(bg="yellow")
                self.mfr_GUI[i].update()

        """priv_val = self.registers[12].get_value()
        if priv_val == '0':
            self.privileged_label1.config(bg="black")
            self.privileged_label1.update()
        elif priv_val == '1':
            self.privileged_label1.config(bg="yellow")
            self.privileged_label1.update()"""

#   END: refresh_reg_info

    def refresh_OpCode(self):
        op_text1 = tk.StringVar()
        op_text2 = tk.StringVar()
        op_text3 = tk.StringVar()
        op_text4 = tk.StringVar()
        op_text5 = tk.StringVar()
        op_text6 = tk.StringVar()
        op_texts = [op_text1, op_text2, op_text3, op_text4, op_text5, op_text6]

        for i in range(0,6):
            op_texts[i].set(self.ins_object.opcode[i])


        self.op_entry1.config(textvariable=op_text1)
        self.op_entry2.config(textvariable=op_text2)
        self.op_entry3.config(textvariable=op_text3)
        self.op_entry4.config(textvariable=op_text4)
        self.op_entry5.config(textvariable=op_text5)
        self.op_entry6.config(textvariable=op_text6)

#   END: refresh_OpCode

    def refresh_GPR_address(self):
        gpr_add_text1 = tk.StringVar()
        gpr_add_text2 = tk.StringVar()
        self.gpr_add_entry1.config(textvariable=gpr_add_text1)
        self.gpr_add_entry2.config(textvariable=gpr_add_text2)

#   END: refresh_GPR_address

    def refresh_IXR_address(self):
        ixr_add_text1 = tk.StringVar()
        ixr_add_text2 = tk.StringVar()
        self.ixr_add_entry1.config(textvariable=ixr_add_text1)
        self.ixr_add_entry2.config(textvariable=ixr_add_text2)

#   END: refresh_IXR_address

    def refresh_I_instruction(self):
        i_text = tk.StringVar()
        self.i_entry1.config(textvariable=i_text)

#   END: refresh_I_instruction

    def refresh_ADD(self):
        add_text1 = tk.StringVar()
        add_text2 = tk.StringVar()
        add_text3 = tk.StringVar()
        add_text4 = tk.StringVar()
        add_text5 = tk.StringVar()
        self.add_entry1.config(textvariable=add_text1)
        self.add_entry2.config(textvariable=add_text2)
        self.add_entry3.config(textvariable=add_text3)
        self.add_entry4.config(textvariable=add_text4)
        self.add_entry5.config(textvariable=add_text5)
#   END: refresh_ADD

    def func_load(self, mar : MAR, mbr : MBR, mem : Memory):
        """This function loads the value of MEM[MAR] into MBR"""
        print('button Load is pressed')
        print("Load from Memory:")
        print("MBR <- MEM[MAR]:")

        self.func_instruction()
        mbr.load_from_mem(mar, mem)
        self.refresh_reg_info()
        self.refresh_mem_info()


        print("MBR = MEM[" + str(int(mar.get_value(), 2)) + "] = " + str(int(mbr.get_value())))
#   END: func_load

    def func_store(self, mar : MAR, mbr : MBR, mem : Memory):
        """This function stores the value of MBR into MEM[MAR]"""
        print('button Store is pressed')
        print("Store into Memory:")
        print("MEM[MAR] <- MBR:")
        self.func_instruction()
        mbr.store_to_mem(mar,mem)
        self.refresh_mem_info()

        print('MEM['+ str(int(mar.get_value(),2)) + '] = ' + str(int(mem.memory[int(mar.get_value(),2)])))
#   END: func_store

    def func_instruction(self):
        """This function sets the bit of the instruction into 1 or 0"""
        opcode_GUI = "".join([str(self.op_entry1.get()),str(self.op_entry2.get()), str(self.op_entry3.get()),
                              str(self.op_entry4.get()), str(self.op_entry5.get()), str(self.op_entry6.get())])
        gpr_add_GUI = "".join([str(self.gpr_add_entry1.get()), str(self.gpr_add_entry2.get())])
        ixr_add_GUI = "".join([str(self.ixr_add_entry1.get()), str(self.ixr_add_entry2.get())])
        i_GUI = str(self.i_entry1.get())
        add_GUI = "".join([str(self.add_entry1.get()), str(self.add_entry2.get()), str(self.add_entry3.get()),
                              str(self.add_entry4.get()), str(self.add_entry5.get())])
        self.ins_object.value = "".join([opcode_GUI, gpr_add_GUI, ixr_add_GUI, i_GUI, add_GUI])

        """        print(f"OPCODE: {opcode_GUI}")
        print(f"GPR ADD: {gpr_add_GUI}")
        print(f"IXR ADD: {ixr_add_GUI}")
        print(f"I: {i_GUI}")
        print(f"ADD: {add_GUI}")
        print(f"INSTRUCTION: {self.ins_object.value}")"""

        self.ins_object.update()
        self.refresh_instruction_info()
#   END: func_instruction

    def func_reg_load(self, reg_GUI,  reg: Register):
        """This function loads the value of instruction into a register"""
        print("button Load " + reg.label + " was pressed")

        self.func_instruction()
        reg.set_value(self.ins_object.value[16 - reg.size:16])
        print(f'Load value of {reg.get_value()} to {reg.label}')
        self.refresh_reg_info()
        self.refresh_mem_info()
        print(reg.label + ' <- ' + str(int(reg.get_value())))
#   END: func_reg_load

    def func_ipl(self, pc : PC, mem = Memory):
        """This function reset the system and pre-load the ipl.txt"""
        self.reset()
        file_dir = './ipl.txt'
        try:
            with open(resource_path(file_dir), 'r') as f:
                lines = f.readlines()
            f.close()
        except FileNotFoundError:
             self.txt_ipl_info.insert( file_dir + ' does not exist')
             return

        print("IPL Executing")
        for i in lines:
            # mem[add] <- value
            temp = i.split(' ')
            add, value = int(temp[0],16),bin(int(temp[1][0:4],16))[2:]
            mem.set_to_memory(add,value)
            # step_info update
            print('MEM[' + str(add) + '] = ' + value)

        # set pc (9 by default)
        pc.set_value("1010")
        print('PC has been set to ' + pc.get_value())
        # mem_info refresh
        self.refresh_mem_info()
        self.refresh_reg_info()
#   END: func_ipl


    def func_run(self, mem : Memory, pc : PC, mar : MAR, mbr : MBR, ir : IR):
        """This function implements RUN"""
        if_run = True

        while if_run:
            if_run = self.func_ss(mem,pc,mar,mbr,ir,False)

#   END: func_run

    def func_ss(self, mem: Memory, pc: PC, mar: MAR, mbr: MBR, ir: IR, if_clean: bool):
        """This function implements single step"""

        self.run_light_label.config(bg='green')
        self.halt_light_label.config(bg='black')

        print('button ss is pressed')
        print('-------------------------------------------------')
        print('Step: PC = ' + pc.get_value() + '\n')

        # Fetch Instruction
        print('Fetch Instruction')
        # MAR <- PC
        mar.get_from_PC(pc)
        print('MAR <- PC :\t\t\tMAR = ' + mar.get_value() + '\n')
        # MBR <- mem[MAR]
        mbr.load_from_mem(mar, mem)
        print('MBR <- MEM[' + str(int(mar.get_value(), 2)) + '] :\t\t\tMBR = ' + mbr.get_value() + '\n')
        # IR <- MBR
        ir.get_from_MBR(mbr)
        print('IR <- MBR :\t\t\tIR = ' + ir.get_value() + '\n\n')

        # Decode
        print( 'Decode Instruction \n')
        word = Instruction(ir.get_value())
        op = int(word.opcode, 2)
        gpr = self.gprs[int(word.gpr_index, 2)]

        # Halt
        if op == 0:
            print( 'Program is done\n\n')
            self.halt_light_label.config(bg="red")
            self.run_light_label.config(bg="black")
            return False
        print( 'Instruction :\t\t\t' + word.print_out() + '\n\n')

        # Locate
        print( 'Locate EA \n')
        # IAR <- ADD
        iar = Register(12, 'IAR')
        iar.set_value(str(int(word.address)))
        print('IAR <- Add :\t\t\tIAR = ' + iar.get_value() + '\n')
        # IAR += X[IXR] if IXR = 1 or 2 or 3
        ixr_id = int(word.ixr_index, 2)
        if ixr_id != 0:
            ixr = self.ixrs[ixr_id - 1]
            iar.add_2(ixr.get_value())
            print('IAR += ' + ixr.label + ' :\t\t\tIAR = ' + iar.get_value() + '\n')
        # IAR <- MEM[IAR] if I = 1
        if int(word.indirect, 2) == 1:
            add = int(iar.get_value(), 2)
            iar.set_value(mem.get_from_memory(add))
            print('IAR <- MEM[' + str(add) + '] :\t\t\tIAR = ' + iar.get_value() + '\n')
        # MAR <- IAR
        mar.set_value(iar.get_value())
        print('MAR <- IAR :\t\t\tMAR = ' + mar.get_value() + '\n\n')

        # Excute and Deposit
        print('Excute and Deposit Result \n')

        irr = Register(16, 'IRR')
        # LDR
        if op == 1:
            # MBR <- MEM[MAR]
            mbr.load_from_mem(mar, mem)
            print('MBR <- MEM[' + str(int(mar.get_value(), 2)) + '] :\t\t\tMBR = ' + mbr.get_value() + '\n')
            # IRR <- MBR
            irr.set_value(mbr.get_value())
            print('IRR <- MBR :\t\t\tIRR = ' + irr.get_value() + '\n')
            # R[GPR] <- IRR
            gpr.set_value(irr.get_value())
            print(gpr.label + ' <- IRR :\t\t\t' + gpr.label + ' = ' + gpr.get_value() + '\n')
        # STR
        elif op == 2:
            # IRR <- R[GPR]
            irr.set_value(gpr.get_value())
            print('IRR <- ' + gpr.label + ' :\t\t\tIRR = ' + irr.get_value() + '\n')
            # MBR <- IRR
            mbr.set_value(irr.get_value())
            print('MBR <- IRR :\t\t\tMBR = ' + mbr.get_value() + '\n')
            # MEM[MAR] <- MBR
            mbr.store_to_mem(mar, mem)
            print('MEM[' + str(int(mar.get_value(), 2)) + '] <- MBR :\t\t\tMEM[' + str(
                int(mar.get_value(), 2)) + '] = ' + mem.memory[int(mar.get_value(), 2)] + '\n')
        # LDA
        elif op == 3:
            # MBR <- MAR
            mbr.set_value(mar.get_value())
            print('MBR <- MAR : \t\t\tMBR = ' + mbr.get_value() + '\n')
            # IRR <- MBR
            irr.set_value(mbr.get_value())
            print('IRR <- MBR :\t\t\tIRR = ' + irr.get_value() + '\n')
            # R[GPR] <- IRR
            gpr.set_value(irr.get_value())
            print(gpr.label + ' <- IRR :\t\t\t' + gpr.label + ' = ' + gpr.get_value() + '\n')
        # LDX
        elif op == 33:
            # MBR <- MEM[MAR]
            mbr.load_from_mem(mar, mem)
            print('MBR <- MEM[' + str(int(mar.get_value(), 2)) + '] :\t\t\tMBR = ' + mbr.get_value() + '\n')
            # IRR <- MBR
            irr.set_value(mbr.get_value())
            print('IRR <- MBR :\t\t\tIRR = ' + irr.get_value() + '\n')
            # X[IXR] <- IRR
            ixr = self.ixrs[ixr_id - 1]
            ixr.set_value(irr.get_value())
            print(ixr.label + ' <- IRR :\t\t\t' + ixr.label + ' = ' + ixr.get_value() + '\n')
            # STX
        elif op == 34:
            # IRR <- X[IXR]
            ixr = self.ixrs[ixr_id - 1]
            irr.set_value(ixr.get_value())
            print('IRR <- ' + ixr.label + ' :\t\t\tIRR = ' + irr.get_value() + '\n')
            # MBR <- IRR
            mbr.set_value(irr.get_value())
            print('MBR <- IRR :\t\t\tMBR = ' + mbr.get_value() + '\n')
            # MEM[MAR] <- MBR
            mbr.store_to_mem(mar, mem)
            print('MEM[' + str(int(mar.get_value(), 2)) + '] <- MBR :\t\t\tMEM[' +
                  str(int(mar.get_value(), 2)) + '] = ' + mem.memory[int(mar.get_value(), 2)] + '\n')

        # PC++
        pc.next()
        print( '\nPC++ :\t\t\tPC = ' + pc.get_value() + '\n')
        self.refresh_reg_info()
        self.refresh_mem_info()
        return True
#   END func_ss

    def func_st_plus(self, mar : MAR, mbr : MBR, mem : Memory):
            """This function stores the value of MBR into MEM[MAR] and MAR++"""
            self.run_light_label.config(bg='green')
            self.halt_light_label.config(bg='black')
            print('button St+ is pressed')
            print('St+:\n\n')
            print('MEM[MAR] <- MBR:\n')
            mbr.store_to_mem(mar, mem)
            print('MEM['+ str(int(mar.get_value(),2)) + '] = ' + str(int(mem.memory[int(mar.get_value(),2)])) + '\n\n')

            print('MAR++:\n')
            mar.add_10(1)
            self.refresh_reg_info()
            self.refresh_mem_info()
            print('MAR = ' + str(mar.get_value()) + '\n')
    #   END: func_st_plus

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#   END: resource_path
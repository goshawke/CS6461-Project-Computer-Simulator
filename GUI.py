import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.config(bg='#0096c7')

# configure the root window
window_width = 1200
window_height = 800

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set position of window to center of screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# makes window a fixed size
root.resizable(False, False)

# Sets text on window header
root.title('Computer System Architecture Project')

# -----------------------------START: TOP PANEL --------------------------------#
top_panel = tk.Frame(root, height=600, width=1200)
top_panel.config(bg='#0096c7')
top_panel.pack(expand=True, side='top', fill='both', padx=5, pady=5)

# ------------------------------START: GPR PANEL ---------------------------#

gpr_panel = ttk.Frame(top_panel, height=50, width=33)
gpr_panel.config(style='new.TFrame')

gpr_panel.grid(column=0, row=0, padx=35, pady=[50, 25])

gpr_panel.rowconfigure(0, weight=1)
gpr_panel.rowconfigure(1, weight=1)
gpr_panel.rowconfigure(2, weight=1)
gpr_panel.rowconfigure(3, weight=1)

gpr_panel.columnconfigure(0, weight=2)
gpr_panel.columnconfigure(1, weight=1)
gpr_panel.columnconfigure(2, weight=1)
gpr_panel.columnconfigure(3, weight=1)
gpr_panel.columnconfigure(4, weight=1)
gpr_panel.columnconfigure(5, weight=1)
gpr_panel.columnconfigure(6, weight=1)
gpr_panel.columnconfigure(7, weight=1)
gpr_panel.columnconfigure(8, weight=1)
gpr_panel.columnconfigure(9, weight=1)
gpr_panel.columnconfigure(10, weight=1)
gpr_panel.columnconfigure(11, weight=1)
gpr_panel.columnconfigure(12, weight=1)
gpr_panel.columnconfigure(13, weight=1)
gpr_panel.columnconfigure(14, weight=1)
gpr_panel.columnconfigure(15, weight=1)
gpr_panel.columnconfigure(16, weight=1)
gpr_panel.columnconfigure(17, weight=2)
# -----------------------START: GPR LABELS ----------------------#
gpr0_label = ttk.Label(gpr_panel, text="GPR 0", anchor='c', width=5)
gpr0_label.grid(column=0, row=0, padx=5, pady=5, ipadx=2)
gpr1_label = ttk.Label(gpr_panel, text="GPR 1", anchor='c', width=5)
gpr1_label.grid(column=0, row=1, padx=5, pady=5, ipadx=2)
gpr2_label = ttk.Label(gpr_panel, text="GPR 2", anchor='c', width=5)
gpr2_label.grid(column=0, row=2, padx=5, pady=5, ipadx=2)
gpr3_label = ttk.Label(gpr_panel, text="GPR 3", anchor='c', width=5)
gpr3_label.grid(column=0, row=3, padx=5, pady=5, ipadx=2)
# -----------------------END: GPR LABELS ------------------------#

# -----------------------START: GPR LABELS (LIGHTS) ------------------------#
gpr0_label1 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label1.grid(column=1, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label2 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label2.grid(column=2, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label3 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label3.grid(column=3, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label4 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label4.grid(column=4, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label5 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label5.grid(column=5, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label6 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label6.grid(column=6, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label7 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label7.grid(column=7, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label8 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label8.grid(column=8, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label9 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label9.grid(column=9, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label10 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label10.grid(column=10, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label11 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label11.grid(column=11, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label12 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label12.grid(column=12, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label13 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label13.grid(column=13, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label14 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label14.grid(column=14, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label15 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label15.grid(column=15, row=0, sticky=tk.E, padx=2, pady=5)
gpr0_label16 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr0_label16.grid(column=16, row=0, sticky=tk.E, padx=2, pady=5)

gpr1_label1 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label1.grid(column=1, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label2 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label2.grid(column=2, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label3 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label3.grid(column=3, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label4 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label4.grid(column=4, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label5 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label5.grid(column=5, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label6 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label6.grid(column=6, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label7 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label7.grid(column=7, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label8 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label8.grid(column=8, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label9 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label9.grid(column=9, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label10 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label10.grid(column=10, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label11 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label11.grid(column=11, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label12 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label12.grid(column=12, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label13 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label13.grid(column=13, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label14 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label14.grid(column=14, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label15 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label15.grid(column=15, row=1, sticky=tk.E, padx=2, pady=5)
gpr1_label16 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr1_label16.grid(column=16, row=1, sticky=tk.E, padx=2, pady=5)

gpr2_label1 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label1.grid(column=1, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label2 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label2.grid(column=2, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label3 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label3.grid(column=3, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label4 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label4.grid(column=4, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label5 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label5.grid(column=5, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label6 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label6.grid(column=6, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label7 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label7.grid(column=7, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label8 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label8.grid(column=8, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label9 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label9.grid(column=9, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label10 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label10.grid(column=10, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label11 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label11.grid(column=11, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label12 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label12.grid(column=12, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label13 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label13.grid(column=13, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label14 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label14.grid(column=14, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label15 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label15.grid(column=15, row=2, sticky=tk.E, padx=2, pady=5)
gpr2_label16 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr2_label16.grid(column=16, row=2, sticky=tk.E, padx=2, pady=5)

gpr3_label1 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label1.grid(column=1, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label2 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label2.grid(column=2, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label3 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label3.grid(column=3, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label4 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label4.grid(column=4, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label5 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label5.grid(column=5, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label6 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label6.grid(column=6, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label7 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label7.grid(column=7, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label8 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label8.grid(column=8, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label9 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label9.grid(column=9, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label10 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label10.grid(column=10, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label11 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label11.grid(column=11, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label12 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label12.grid(column=12, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label13 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label13.grid(column=13, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label14 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label14.grid(column=14, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label15 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label15.grid(column=15, row=3, sticky=tk.E, padx=2, pady=5)
gpr3_label16 = tk.Label(gpr_panel, text='  ', width=2, bg='black')
gpr3_label16.grid(column=16, row=3, sticky=tk.E, padx=2, pady=5)


# -----------------------END: GPR LABELS (LIGHTS) ------------------------#
# -----------------------START: GPR LOAD BUTTONS------------------------#
def gpr0_load_callback():
    print("gpr0 load button clicked")
    # do something


gpr0_btn = ttk.Button(gpr_panel, text='LD', command=gpr0_load_callback, width=6)
gpr0_btn.grid(column=17, row=0, padx=5, pady=5)


def gpr1_load_callback():
    print("gpr1 load button clicked")
    # do something


gpr1_btn = ttk.Button(gpr_panel, text='LD', command=gpr1_load_callback, width=6)
gpr1_btn.grid(column=17, row=1, padx=5, pady=5)


def gpr2_load_callback():
    print("gpr2 load button clicked")
    # do something


gpr2_btn = ttk.Button(gpr_panel, text='LD', command=gpr2_load_callback, width=6)
gpr2_btn.grid(column=17, row=2, padx=5, pady=5)


def gpr3_load_callback():
    print("gpr3 load button clicked")
    # do something


gpr3_btn = ttk.Button(gpr_panel, text='LD', command=gpr3_load_callback, width=6)
gpr3_btn.grid(column=17, row=3, padx=5, pady=5)

# -----------------------END: GPR LOAD BUTTONS--------------------------#

# -----------------------END: GPR PANEL-------------------------------------#

# ------------------------------START: IXR PANEL ---------------------------#

ixr_panel = ttk.Frame(top_panel, height=50, width=33)
ixr_panel.config(style='new.TFrame')

ixr_panel.grid(column=0, row=1, padx=35)

ixr_panel.rowconfigure(0, weight=1)
ixr_panel.rowconfigure(1, weight=1)
ixr_panel.rowconfigure(2, weight=1)

ixr_panel.columnconfigure(0, weight=2)
ixr_panel.columnconfigure(1, weight=1)
ixr_panel.columnconfigure(2, weight=1)
ixr_panel.columnconfigure(3, weight=1)
ixr_panel.columnconfigure(4, weight=1)
ixr_panel.columnconfigure(5, weight=1)
ixr_panel.columnconfigure(6, weight=1)
ixr_panel.columnconfigure(7, weight=1)
ixr_panel.columnconfigure(8, weight=1)
ixr_panel.columnconfigure(9, weight=1)
ixr_panel.columnconfigure(10, weight=1)
ixr_panel.columnconfigure(11, weight=1)
ixr_panel.columnconfigure(12, weight=1)
ixr_panel.columnconfigure(13, weight=1)
ixr_panel.columnconfigure(14, weight=1)
ixr_panel.columnconfigure(15, weight=1)
ixr_panel.columnconfigure(16, weight=1)
ixr_panel.columnconfigure(17, weight=2)
# -----------------------START: IXR LABELS ----------------------#
ixr1_label = ttk.Label(ixr_panel, text="IXR 0", anchor='c', width=5)
ixr1_label.grid(column=0, row=0, padx=5, pady=5, ipadx=2)
ixr2_label = ttk.Label(ixr_panel, text="IXR 1", anchor='c', width=5)
ixr2_label.grid(column=0, row=1, padx=5, pady=5, ipadx=2)
ixr3_label = ttk.Label(ixr_panel, text="IXR 2", anchor='c', width=5)
ixr3_label.grid(column=0, row=2, padx=5, pady=5, ipadx=2)
# -----------------------END: IXR LABELS ------------------------#

# -----------------------START: IXR LABELS (LIGHTS) ------------------------#
ixr1_label1 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label1.grid(column=1, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label2 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label2.grid(column=2, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label3 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label3.grid(column=3, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label4 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label4.grid(column=4, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label5 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label5.grid(column=5, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label6 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label6.grid(column=6, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label7 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label7.grid(column=7, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label8 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label8.grid(column=8, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label9 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label9.grid(column=9, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label10 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label10.grid(column=10, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label11 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label11.grid(column=11, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label12 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label12.grid(column=12, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label13 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label13.grid(column=13, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label14 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label14.grid(column=14, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label15 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label15.grid(column=15, row=0, sticky=tk.E, padx=2, pady=5)
ixr1_label16 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr1_label16.grid(column=16, row=0, sticky=tk.E, padx=2, pady=5)

ixr2_label1 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label1.grid(column=1, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label2 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label2.grid(column=2, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label3 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label3.grid(column=3, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label4 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label4.grid(column=4, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label5 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label5.grid(column=5, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label6 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label6.grid(column=6, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label7 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label7.grid(column=7, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label8 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label8.grid(column=8, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label9 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label9.grid(column=9, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label10 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label10.grid(column=10, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label11 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label11.grid(column=11, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label12 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label12.grid(column=12, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label13 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label13.grid(column=13, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label14 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label14.grid(column=14, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label15 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label15.grid(column=15, row=1, sticky=tk.E, padx=2, pady=5)
ixr2_label16 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr2_label16.grid(column=16, row=1, sticky=tk.E, padx=2, pady=5)

ixr3_label1 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label1.grid(column=1, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label2 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label2.grid(column=2, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label3 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label3.grid(column=3, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label4 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label4.grid(column=4, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label5 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label5.grid(column=5, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label6 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label6.grid(column=6, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label7 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label7.grid(column=7, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label8 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label8.grid(column=8, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label9 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label9.grid(column=9, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label10 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label10.grid(column=10, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label11 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label11.grid(column=11, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label12 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label12.grid(column=12, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label13 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label13.grid(column=13, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label14 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label14.grid(column=14, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label15 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label15.grid(column=15, row=2, sticky=tk.E, padx=2, pady=5)
ixr3_label16 = tk.Label(ixr_panel, text='  ', width=2, bg='black')
ixr3_label16.grid(column=16, row=2, sticky=tk.E, padx=2, pady=5)


# -----------------------END: IXR LABELS (LIGHTS) ----------------------#

# -----------------------START: IXR LOAD BUTTONS------------------------#

def ixr1_load_callback():
    print("ixr1 load button clicked")
    # do something


ixr1_btn = ttk.Button(ixr_panel, text='LD', command=ixr1_load_callback, width=6)
ixr1_btn.grid(column=17, row=0, padx=5, pady=5)


def ixr2_load_callback():
    print("ixr2 load button clicked")
    # do something


ixr2_btn = ttk.Button(ixr_panel, text='LD', command=ixr2_load_callback, width=6)
ixr2_btn.grid(column=17, row=1, padx=5, pady=5)


def ixr3_load_callback():
    print("ixr3 load button clicked")
    # do something


ixr3_btn = ttk.Button(ixr_panel, text='LD', command=ixr3_load_callback, width=6)
ixr3_btn.grid(column=17, row=2, padx=5, pady=5)

# -----------------------END: IXR LOAD BUTTONS--------------------------#


# ------------------------------END: IXR PANEL -----------------------------#


# ------------------------------START: RIGHT PANEL ---------------------------#

right_panel = ttk.Frame(top_panel, height=50, width=33)
right_panel.config(style='new.TFrame')

right_panel.grid(column=1, row=0, padx=[100, 20], pady=[77, 20], sticky=tk.E)

right_panel.rowconfigure(0, weight=1)
right_panel.rowconfigure(1, weight=1)
right_panel.rowconfigure(2, weight=1)
right_panel.rowconfigure(3, weight=1)
right_panel.rowconfigure(4, weight=1)
right_panel.rowconfigure(5, weight=1)

right_panel.columnconfigure(0, weight=2)
right_panel.columnconfigure(1, weight=1)
right_panel.columnconfigure(2, weight=1)
right_panel.columnconfigure(3, weight=1)
right_panel.columnconfigure(4, weight=1)
right_panel.columnconfigure(5, weight=1)
right_panel.columnconfigure(6, weight=1)
right_panel.columnconfigure(7, weight=1)
right_panel.columnconfigure(8, weight=1)
right_panel.columnconfigure(9, weight=1)
right_panel.columnconfigure(10, weight=1)
right_panel.columnconfigure(11, weight=1)
right_panel.columnconfigure(12, weight=1)
right_panel.columnconfigure(13, weight=1)
right_panel.columnconfigure(14, weight=1)
right_panel.columnconfigure(15, weight=1)
right_panel.columnconfigure(16, weight=1)
right_panel.columnconfigure(17, weight=2)
# -----------------------START: RIGHT LABELS ----------------------#
pc_label = ttk.Label(right_panel, text="PC", anchor='c', width=5)
pc_label.grid(column=3, row=0, padx=5, pady=5, ipadx=2, columnspan=2)
mar_label = ttk.Label(right_panel, text="MAR", anchor='c', width=5)
mar_label.grid(column=3, row=1, padx=5, pady=5, ipadx=2, columnspan=2)
mbr_label = ttk.Label(right_panel, text="MBR", anchor='c', width=5)
mbr_label.grid(column=0, row=2, padx=5, pady=5, ipadx=2)
ir_label = ttk.Label(right_panel, text="IR", anchor='c', width=5)
ir_label.grid(column=0, row=3, padx=5, pady=5, ipadx=2)
mfr_label = ttk.Label(right_panel, text="MFR", anchor='c', width=5)
mfr_label.grid(column=11, row=4, padx=5, pady=5, ipadx=2, columnspan=2)
privileged_label = ttk.Label(right_panel, text="PRIVILEGED", anchor='c')
privileged_label.grid(column=13, row=5, padx=5, pady=5, ipadx=2, columnspan=3)
# -----------------------END: RIGHT LABELS ------------------------#

# -----------------------START: RIGHT LABELS (LIGHTS) ------------------------#
pc_label1 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label1.grid(column=5, row=0, sticky=tk.E, padx=2, pady=5)
pc_label2 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label2.grid(column=6, row=0, sticky=tk.E, padx=2, pady=5)
pc_label3 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label3.grid(column=7, row=0, sticky=tk.E, padx=2, pady=5)
pc_label4 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label4.grid(column=8, row=0, sticky=tk.E, padx=2, pady=5)
pc_label5 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label5.grid(column=9, row=0, sticky=tk.E, padx=2, pady=5)
pc_label6 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label6.grid(column=10, row=0, sticky=tk.E, padx=2, pady=5)
pc_label7 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label7.grid(column=11, row=0, sticky=tk.E, padx=2, pady=5)
pc_label8 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label8.grid(column=12, row=0, sticky=tk.E, padx=2, pady=5)
pc_label9 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label9.grid(column=13, row=0, sticky=tk.E, padx=2, pady=5)
pc_label10 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label10.grid(column=14, row=0, sticky=tk.E, padx=2, pady=5)
pc_label11 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label11.grid(column=15, row=0, sticky=tk.E, padx=2, pady=5)
pc_label12 = tk.Label(right_panel, text='  ', width=2, bg='black')
pc_label12.grid(column=16, row=0, sticky=tk.E, padx=2, pady=5)

mar_label1 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label1.grid(column=5, row=1, sticky=tk.E, padx=2, pady=5)
mar_label2 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label2.grid(column=6, row=1, sticky=tk.E, padx=2, pady=5)
mar_label3 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label3.grid(column=7, row=1, sticky=tk.E, padx=2, pady=5)
mar_label4 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label4.grid(column=8, row=1, sticky=tk.E, padx=2, pady=5)
mar_label5 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label5.grid(column=9, row=1, sticky=tk.E, padx=2, pady=5)
mar_label6 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label6.grid(column=10, row=1, sticky=tk.E, padx=2, pady=5)
mar_label7 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label7.grid(column=11, row=1, sticky=tk.E, padx=2, pady=5)
mar_label8 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label8.grid(column=12, row=1, sticky=tk.E, padx=2, pady=5)
mar_label9 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label9.grid(column=13, row=1, sticky=tk.E, padx=2, pady=5)
mar_label10 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label10.grid(column=14, row=1, sticky=tk.E, padx=2, pady=5)
mar_label11 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label11.grid(column=15, row=1, sticky=tk.E, padx=2, pady=5)
mar_label12 = tk.Label(right_panel, text='  ', width=2, bg='black')
mar_label12.grid(column=16, row=1, sticky=tk.E, padx=2, pady=5)

mbr_label1 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label1.grid(column=1, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label2 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label2.grid(column=2, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label3 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label3.grid(column=3, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label4 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label4.grid(column=4, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label5 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label5.grid(column=5, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label6 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label6.grid(column=6, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label7 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label7.grid(column=7, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label8 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label8.grid(column=8, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label9 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label9.grid(column=9, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label10 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label10.grid(column=10, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label11 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label11.grid(column=11, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label12 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label12.grid(column=12, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label13 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label13.grid(column=13, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label14 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label14.grid(column=14, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label15 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label15.grid(column=15, row=2, sticky=tk.E, padx=2, pady=5)
mbr_label16 = tk.Label(right_panel, text='  ', width=2, bg='black')
mbr_label16.grid(column=16, row=2, sticky=tk.E, padx=2, pady=5)

ir_label1 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label1.grid(column=1, row=3, sticky=tk.E, padx=2, pady=5)
ir_label2 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label2.grid(column=2, row=3, sticky=tk.E, padx=2, pady=5)
ir_label3 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label3.grid(column=3, row=3, sticky=tk.E, padx=2, pady=5)
ir_label4 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label4.grid(column=4, row=3, sticky=tk.E, padx=2, pady=5)
ir_label5 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label5.grid(column=5, row=3, sticky=tk.E, padx=2, pady=5)
ir_label6 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label6.grid(column=6, row=3, sticky=tk.E, padx=2, pady=5)
ir_label7 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label7.grid(column=7, row=3, sticky=tk.E, padx=2, pady=5)
ir_label8 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label8.grid(column=8, row=3, sticky=tk.E, padx=2, pady=5)
ir_label9 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label9.grid(column=9, row=3, sticky=tk.E, padx=2, pady=5)
ir_label10 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label10.grid(column=10, row=3, sticky=tk.E, padx=2, pady=5)
ir_label11 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label11.grid(column=11, row=3, sticky=tk.E, padx=2, pady=5)
ir_label12 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label12.grid(column=12, row=3, sticky=tk.E, padx=2, pady=5)
ir_label13 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label13.grid(column=13, row=3, sticky=tk.E, padx=2, pady=5)
ir_label14 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label14.grid(column=14, row=3, sticky=tk.E, padx=2, pady=5)
ir_label15 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label15.grid(column=15, row=3, sticky=tk.E, padx=2, pady=5)
ir_label16 = tk.Label(right_panel, text='  ', width=2, bg='black')
ir_label16.grid(column=16, row=3, sticky=tk.E, padx=2, pady=5)

mfr_label1 = tk.Label(right_panel, text='  ', width=2, bg='black')
mfr_label1.grid(column=13, row=4, sticky=tk.E, padx=2, pady=5)
mfr_label2 = tk.Label(right_panel, text='  ', width=2, bg='black')
mfr_label2.grid(column=14, row=4, sticky=tk.E, padx=2, pady=5)
mfr_label3 = tk.Label(right_panel, text='  ', width=2, bg='black')
mfr_label3.grid(column=15, row=4, sticky=tk.E, padx=2, pady=5)
mfr_label4 = tk.Label(right_panel, text='  ', width=2, bg='black')
mfr_label4.grid(column=16, row=4, sticky=tk.E, padx=2, pady=5)

privileged_label1 = tk.Label(right_panel, text='  ', width=2, bg='black')
privileged_label1.grid(column=16, row=5, sticky=tk.E, padx=2, pady=5)


# -----------------------END: RIGHT LABELS (LIGHTS) ------------------------#

# -----------------------START: RIGHT LOAD BUTTONS------------------------#
def pc_load_callback():
    print("pc load button clicked")
    # do something


pc_btn = ttk.Button(right_panel, text='LD', command=pc_load_callback, width=6)
pc_btn.grid(column=17, row=0, padx=5, pady=5)


def mar_load_callback():
    print("mar load button clicked")
    # do something


mar_btn = ttk.Button(right_panel, text='LD', command=mar_load_callback, width=6)
mar_btn.grid(column=17, row=1, padx=5, pady=5)


def mbr_load_callback():
    print("mbr load button clicked")
    # do something


mbr_btn = ttk.Button(right_panel, text='LD', command=mbr_load_callback, width=6)
mbr_btn.grid(column=17, row=2, padx=5, pady=5)

# -----------------------END: RIGHT LOAD BUTTONS--------------------------#

# -----------------------END: RIGHT PANEL-------------------------------------#

# -----------------------------END TOP PANEL -----------------------------------#


# -----------------------------START: BOTTOM PANEL -----------------------------#
bottom_panel = tk.Frame(root, height=200, width=1200)
bottom_panel.config(bg='#0096c7')
bottom_panel.pack(expand=True, side='bottom', fill='both', padx=60, pady=5)

# ----------------------------START: OPERATION PANEL--------------------------- #
# Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
s = ttk.Style()
s.configure('new.TFrame', background='#48cae4')

op_panel = ttk.Frame(bottom_panel, height=50, width=100)
op_panel.config(style='new.TFrame')

op_panel.grid(column=0, row=0, padx=10)

op_panel.rowconfigure(0, weight=1)
op_panel.rowconfigure(1, weight=2)

op_panel.columnconfigure(0, weight=1)
op_panel.columnconfigure(1, weight=1)
op_panel.columnconfigure(2, weight=1)
op_panel.columnconfigure(3, weight=1)
op_panel.columnconfigure(4, weight=1)
op_panel.columnconfigure(5, weight=1)

op_text1 = tk.StringVar()
op_entry1 = ttk.Entry(op_panel, textvariable=op_text1, width=3)
op_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

op_text2 = tk.StringVar()
op_entry2 = ttk.Entry(op_panel, textvariable=op_text2, width=3)
op_entry2.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

op_text3 = tk.StringVar()
op_entry3 = ttk.Entry(op_panel, textvariable=op_text3, width=3)
op_entry3.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)

op_text4 = tk.StringVar()
op_entry4 = ttk.Entry(op_panel, textvariable=op_text4, width=3)
op_entry4.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)

op_text5 = tk.StringVar()
op_entry5 = ttk.Entry(op_panel, textvariable=op_text5, width=3)
op_entry5.grid(column=4, row=0, sticky=tk.E, padx=5, pady=5)

op_text6 = tk.StringVar()
op_entry6 = ttk.Entry(op_panel, textvariable=op_text6, width=3)
op_entry6.grid(column=5, row=0, sticky=tk.E, padx=5, pady=5)

op_label = ttk.Label(op_panel, text="Operation", anchor='s')
op_label.grid(column=1, row=1, sticky=tk.S, padx=5, pady=5, ipadx=5, columnspan=4)

# op_entry1.get()
# op_entry1.focus()

# ----------------------------END: OPERATION PANEL--------------------------- #


# ----------------------------START: GPR ADDRESS PANEL--------------------------- #
# Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
s = ttk.Style()
s.configure('new.TFrame', background='#48cae4')

gpr_add_panel = ttk.Frame(bottom_panel, height=50, width=33)
gpr_add_panel.config(style='new.TFrame')

gpr_add_panel.grid(column=1, row=0, padx=10)

gpr_add_panel.rowconfigure(0, weight=1)
gpr_add_panel.rowconfigure(1, weight=2)

gpr_add_panel.columnconfigure(0, weight=1)
gpr_add_panel.columnconfigure(1, weight=1)

gpr_add_text1 = tk.StringVar()
gpr_add_entry1 = ttk.Entry(gpr_add_panel, textvariable=gpr_add_text1, width=3)
gpr_add_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

gpr_add_text2 = tk.StringVar()
gpr_add_entry2 = ttk.Entry(gpr_add_panel, textvariable=gpr_add_text2, width=3)
gpr_add_entry2.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

gpr_add_label = ttk.Label(gpr_add_panel, text="GPR", anchor='s')
gpr_add_label.grid(column=0, row=1, sticky=tk.S, padx=5, pady=5, ipadx=5, columnspan=2)

# ----------------------------END: GPR ADDRESS PANEL--------------------------- #


# ----------------------------START: IXR ADDRESS PANEL--------------------------- #
# Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
s = ttk.Style()
s.configure('new.TFrame', background='#48cae4')

ixr_add_panel = ttk.Frame(bottom_panel, height=50, width=33)
ixr_add_panel.config(style='new.TFrame')

ixr_add_panel.grid(column=2, row=0, padx=10)

ixr_add_panel.rowconfigure(0, weight=1)
ixr_add_panel.rowconfigure(1, weight=2)

ixr_add_panel.columnconfigure(0, weight=1)
ixr_add_panel.columnconfigure(1, weight=1)

ixr_add_text1 = tk.StringVar()
ixr_add_entry1 = ttk.Entry(ixr_add_panel, textvariable=ixr_add_text1, width=3)
ixr_add_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

ixr_add_text2 = tk.StringVar()
ixr_add_entry2 = ttk.Entry(ixr_add_panel, textvariable=ixr_add_text2, width=3)
ixr_add_entry2.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

ixr_add_label = ttk.Label(ixr_add_panel, text="IXR", anchor='s')
ixr_add_label.grid(column=0, row=1, sticky=tk.S, padx=5, pady=5, ipadx=5, columnspan=2)

# ----------------------------END: IXR ADDRESS PANEL--------------------------- #

# ----------------------------START: I PANEL--------------------------- #
# Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
s = ttk.Style()
s.configure('new.TFrame', background='#48cae4')

i_panel = ttk.Frame(bottom_panel, height=50, width=33)
i_panel.config(style='new.TFrame')

i_panel.grid(column=3, row=0, padx=10)

i_panel.rowconfigure(0, weight=1)
i_panel.rowconfigure(1, weight=2)

i_panel.columnconfigure(0, weight=1)

i_text1 = tk.StringVar()
i_entry1 = ttk.Entry(i_panel, textvariable=i_text1, width=3)
i_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

i_label = ttk.Label(i_panel, text="I", anchor='s')
i_label.grid(column=0, row=1, sticky=tk.S, padx=5, pady=5, ipadx=5, columnspan=2)

# ----------------------------END: I PANEL--------------------------- #

# ----------------------------START: ADDRESS PANEL--------------------------- #
# Since the frame is tkk.Frame NOT tk.Frame, we have to use tkk.Style to change the background color
s = ttk.Style()
s.configure('new.TFrame', background='#48cae4')

add_panel = ttk.Frame(bottom_panel, height=50, width=100)
add_panel.config(style='new.TFrame')

add_panel.grid(column=4, row=0, padx=10)

add_panel.rowconfigure(0, weight=1)
add_panel.rowconfigure(1, weight=2)

add_panel.columnconfigure(0, weight=1)
add_panel.columnconfigure(1, weight=1)
add_panel.columnconfigure(2, weight=1)
add_panel.columnconfigure(3, weight=1)
add_panel.columnconfigure(4, weight=1)
add_panel.columnconfigure(5, weight=1)

add_text1 = tk.StringVar()
add_entry1 = ttk.Entry(add_panel, textvariable=add_text1, width=3)
add_entry1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

add_text2 = tk.StringVar()
add_entry2 = ttk.Entry(add_panel, textvariable=add_text2, width=3)
add_entry2.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

add_text3 = tk.StringVar()
add_entry3 = ttk.Entry(add_panel, textvariable=add_text3, width=3)
add_entry3.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)

add_text4 = tk.StringVar()
add_entry4 = ttk.Entry(add_panel, textvariable=add_text4, width=3)
add_entry4.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)

add_text5 = tk.StringVar()
add_entry5 = ttk.Entry(add_panel, textvariable=add_text5, width=3)
add_entry5.grid(column=4, row=0, sticky=tk.E, padx=5, pady=5)

add_label = ttk.Label(add_panel, text="Address", anchor='s')
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
    # do something


store_btn = ttk.Button(bottom_btn_panel, text='Store', command=store_callback, width=6)
store_btn.grid(column=0, row=1, padx=5, pady=10)


# St+ Button and Callback
def stPlus_callback():
    print("St+ button clicked")
    # do something


stPlus_btn = ttk.Button(bottom_btn_panel, text='St+', command=stPlus_callback, width=6)
stPlus_btn.grid(column=1, row=1, padx=5, pady=10)


# Load Button and Callback
def load_callback():
    print("load button clicked")
    # do something
    opcode=op_entry1.get()+op_entry2.get()+op_entry3.get()+op_entry4.get()+op_entry5.get()+op_entry6.get()
    gpr=gpr_add_entry1.get()+gpr_add_entry2.get()
    ixr=ixr_add_text1.get()+ixr_add_text2.get()
    i=i_text1.get()
    address=add_text1.get()+add_text2.get()+add_text3.get()+add_text4.get()+add_text5.get()
    instruction=opcode+gpr+ixr+i+address
    print(instruction)

    if ixr == "00":
        # Get the value stored in address
        ea = instruction
    elif ixr != "00":
        sumb = int(ixr, 2) + int(instruction, 2)
        ea = (bin(sumb)[2:]).zfill(16)
    print(ea)

    #ldr instruction

    if opcode=="000001":
        if gpr=="00":
            gpr0_label6.config(bg="yellow")
            if(ea[8]=="1"):
                gpr0_label9.config(bg="yellow")
            if(ea[9]=="1"):
                gpr0_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr0_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr0_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr0_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr0_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr0_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr0_label16.config(bg="yellow")
        if gpr=="01":
            gpr1_label6.config(bg="yellow")
            if(ea[8]=="1"):
                gpr1_label9.config(bg="yellow")
            if(ea[9]=="1"):
                gpr1_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr1_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr1_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr1_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr1_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr1_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr1_label16.config(bg="yellow")
        if gpr=="10":
            gpr2_label6.config(bg="yellow")
            if(ea[8]=="1"):
                gpr2_label9.config(bg="yellow")
            if(ea[9]=="1"):
                gpr2_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr2_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr2_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr2_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr2_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr2_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr2_label16.config(bg="yellow")

        if gpr=="11":
            gpr3_label6.config(bg="yellow")
            if(ea[8]=="1"):
                gpr3_label9.config(bg="yellow")
            if(ea[9]=="1"):
                gpr3_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr3_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr3_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr3_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr3_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr3_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr3_label16.config(bg="yellow")

        # str instruction

    elif opcode == "000010":
        if gpr == "00":
            gpr0_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr0_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr0_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr0_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr0_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr0_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr0_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr0_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr0_label16.config(bg="yellow")
        if gpr == "01":
            gpr1_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr1_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr1_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr1_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr1_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr1_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr1_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr1_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr1_label16.config(bg="yellow")
        if gpr == "10":
            gpr2_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr2_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr2_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr2_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr2_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr2_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr2_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr2_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr2_label16.config(bg="yellow")

        if gpr == "11":
            gpr3_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr3_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr3_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr3_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr3_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr3_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr3_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr3_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr3_label16.config(bg="yellow")

        # lda instruction

    if opcode == "000011":
        if gpr == "00":
            gpr0_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr0_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr0_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr0_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr0_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr0_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr0_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr0_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr0_label16.config(bg="yellow")
        if gpr == "01":
            gpr1_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr1_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr1_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr1_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr1_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr1_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr1_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr1_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr1_label16.config(bg="yellow")
        if gpr == "10":
            gpr2_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr2_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr2_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr2_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr2_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr2_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr2_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr2_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr2_label16.config(bg="yellow")

        if gpr == "11":
            gpr3_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr3_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr3_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr3_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr3_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr3_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr3_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr3_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr3_label16.config(bg="yellow")

        # ldx instruction

    if opcode == "101001":
        if gpr == "00":
            gpr0_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr0_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr0_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr0_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr0_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr0_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr0_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr0_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr0_label16.config(bg="yellow")
        if gpr == "01":
            gpr1_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr1_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr1_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr1_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr1_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr1_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr1_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr1_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr1_label16.config(bg="yellow")
        if gpr == "10":
            gpr2_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr2_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr2_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr2_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr2_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr2_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr2_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr2_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr2_label16.config(bg="yellow")

        if gpr == "11":
            gpr3_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr3_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr3_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr3_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr3_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr3_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr3_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr3_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr3_label16.config(bg="yellow")

        # stx instruction

    if opcode == "101010":
        if gpr == "00":
            gpr0_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr0_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr0_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr0_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr0_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr0_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr0_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr0_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr0_label16.config(bg="yellow")
        if gpr == "01":
            gpr1_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr1_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr1_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr1_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr1_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr1_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr1_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr1_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr1_label16.config(bg="yellow")
        if gpr == "10":
            gpr2_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr2_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr2_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr2_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr2_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr2_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr2_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr2_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr2_label16.config(bg="yellow")

        if gpr == "11":
            gpr3_label6.config(bg="yellow")
            if (ea[8] == "1"):
                gpr3_label9.config(bg="yellow")
            if (ea[9] == "1"):
                gpr3_label10.config(bg="yellow")
            if (ea[10] == "1"):
                gpr3_label11.config(bg="yellow")
            if (ea[11] == "1"):
                gpr3_label12.config(bg="yellow")
            if (ea[12] == "1"):
                gpr3_label13.config(bg="yellow")
            if (ea[13] == "1"):
                gpr3_label14.config(bg="yellow")
            if (ea[14] == "1"):
                gpr3_label15.config(bg="yellow")
            if (ea[15] == "1"):
                gpr3_label16.config(bg="yellow")

    else:
        print("Wrong instruction")






load_btn = ttk.Button(bottom_btn_panel, text='Load', command=load_callback, width=6)
load_btn.grid(column=2, row=1, padx=5, pady=10)


# Init Button and Callback
def init_callback():
    with open("ipl.txt", "r") as f:
        data = f.read()
        lst = data.split()
        addr = []
        inst = []
        print(lst)

        addr= [int(x,16) for x in lst]
        print(addr)
        addr = [(bin(y)[2:]).zfill(16) for y in addr]
        print(addr)




        #Display PC with address
        if(addr[0][15]=="1"):
            pc_label12.config(bg="yellow")
        if (addr[0][14] == "1"):
            pc_label11.config(bg="yellow")
        if (addr[0][13] == "1"):
            pc_label10.config(bg="yellow")
        if (addr[0][12] == "1"):
            pc_label9.config(bg="yellow")
        if (addr[0][11] == "1"):
            pc_label8.config(bg="yellow")
        if (addr[0][10] == "1"):
            pc_label7.config(bg="yellow")
        if (addr[0][9] == "1"):
            pc_label6.config(bg="yellow")
        if (addr[0][8] == "1"):
            pc_label5.config(bg="yellow")
        if (addr[0][7] == "1"):
            pc_label4.config(bg="yellow")
        if (addr[0][6] == "1"):
            pc_label3.config(bg="yellow")
        if (addr[0][5] == "1"):
            pc_label2.config(bg="yellow")
        if (addr[0][4] == "1"):
            pc_label1.config(bg="yellow")

        #Display MAR

        if (addr[0][15] == "1"):
            mar_label12.config(bg="yellow")
        if (addr[0][14] == "1"):
            mar_label11.config(bg="yellow")
        if (addr[0][13] == "1"):
            mar_label10.config(bg="yellow")
        if (addr[0][12] == "1"):
            mar_label9.config(bg="yellow")
        if (addr[0][11] == "1"):
            mar_label8.config(bg="yellow")
        if (addr[0][10] == "1"):
            mar_label7.config(bg="yellow")
        if (addr[0][9] == "1"):
            mar_label6.config(bg="yellow")
        if (addr[0][8] == "1"):
            mar_label5.config(bg="yellow")
        if (addr[0][7] == "1"):
            mar_label4.config(bg="yellow")
        if (addr[0][6] == "1"):
            mar_label3.config(bg="yellow")
        if (addr[0][5] == "1"):
            mar_label2.config(bg="yellow")
        if (addr[0][4] == "1"):
            mar_label1.config(bg="yellow")

        #MBR is what is inside MAR so next location of addr
        if (addr[1][15] == "1"):
            mbr_label16.config(bg="yellow")
        if (addr[1][14] == "1"):
            mbr_label15.config(bg="yellow")
        if (addr[1][13] == "1"):
            mbr_label14.config(bg="yellow")
        if (addr[1][12] == "1"):
            mbr_label13.config(bg="yellow")
        if (addr[1][11] == "1"):
            mbr_label12.config(bg="yellow")
        if (addr[1][10] == "1"):
            mbr_label11.config(bg="yellow")
        if (addr[1][9] == "1"):
            mbr_label10.config(bg="yellow")
        if (addr[1][8] == "1"):
            mbr_label9.config(bg="yellow")
        if (addr[1][7] == "1"):
            mbr_label8.config(bg="yellow")
        if (addr[1][6] == "1"):
            mbr_label7.config(bg="yellow")
        if (addr[1][5] == "1"):
            mbr_label6.config(bg="yellow")
        if (addr[1][4] == "1"):
            mbr_label5.config(bg="yellow")
        if (addr[1][3] == "1"):
            mbr_label4.config(bg="yellow")
        if (addr[1][2] == "1"):
            mbr_label3.config(bg="yellow")
        if (addr[1][1] == "1"):
            mbr_label2.config(bg="yellow")
        if (addr[1][0] == "1"):
            mbr_label1.config(bg="yellow")

        #IR takes what is in MBR

        if (addr[1][15] == "1"):
            ir_label16.config(bg="yellow")
        if (addr[1][14] == "1"):
            ir_label15.config(bg="yellow")
        if (addr[1][13] == "1"):
            ir_label14.config(bg="yellow")
        if (addr[1][12] == "1"):
            ir_label13.config(bg="yellow")
        if (addr[1][11] == "1"):
            ir_label12.config(bg="yellow")
        if (addr[1][10] == "1"):
            ir_label11.config(bg="yellow")
        if (addr[1][9] == "1"):
            ir_label10.config(bg="yellow")
        if (addr[1][8] == "1"):
            ir_label9.config(bg="yellow")
        if (addr[1][7] == "1"):
            ir_label8.config(bg="yellow")
        if (addr[1][6] == "1"):
            ir_label7.config(bg="yellow")
        if (addr[1][5] == "1"):
            ir_label6.config(bg="yellow")
        if (addr[1][4] == "1"):
            ir_label5.config(bg="yellow")
        if (addr[1][3] == "1"):
            ir_label4.config(bg="yellow")
        if (addr[1][2] == "1"):
            ir_label3.config(bg="yellow")
        if (addr[1][1] == "1"):
            ir_label2.config(bg="yellow")
        if (addr[1][0] == "1"):
            ir_label1.config(bg="yellow")

        opcode=addr[1][0]+addr[1][1]+addr[1][2]+addr[1][3]+addr[1][4]+addr[1][5]
        gpr=addr[1][6]+addr[1][7]
        ixr=addr[1][8]+addr[1][9]
        i=addr[1][10]
        addresse=addr[1][11]+addr[1][12]+addr[1][13]+addr[1][14]+addr[1][15]
        #print (opcode)
        if ixr == "00":
            # Get the value stored in address
            ea = addresse
        elif ixr != "00":
            sumb = int(ixr, 2) + int(addresse, 2)
            ea = bin(sumb)[2:]
            print(ea)
            print(gpr)
            #if i=="1":
           # ea=[ea]
        print(opcode)
        if opcode=="000001":
            #ldr instruction:
            if gpr=="00":
                #load content at address
                gpr0_label1.config(bg="yellow")
            elif gpr=="01":
                #load content at address
                gpr1_label1.config(bg="yellow")
            elif gpr=="10":
                #load content at address
                gpr2_label1.config(bg="yellow")
            elif gpr=="11":
                #load content at address
                gpr3_label1.config(bg="yellow")

            elif opcode == "000010":
                # str instruction:
                pass

            elif opcode == "000011":
                # lda instruction:
                pass
            elif opcode == "101001":
                # ldx instruction:
                pass
            elif opcode == "101010":
                # stx instruction:
                pass








        #for i in lst:
           # i = int(i,16)
       # print(i)
        #for j in addr:
         #
          #  print (inst)

       # print(addr)
          ##  addr.append(i)
    #  else:
    #     inst[i]=lst[i]
    # print("address list", addr)
    # print("instruction list", inst)

    print("init button clicked")
    # do something


init_btn = tk.Button(bottom_btn_panel, text='Init', command=init_callback, width=6, bg='red')
init_btn.grid(column=3, row=1, padx=5, pady=10)


# SS (Single Step) button and Callback
def ss_callback():
    print("SS button clicked")
    # do something


ss_btn = ttk.Button(bottom_btn_panel, text='SS', command=ss_callback, width=4)
ss_btn.grid(column=1, row=2, columnspan=1, padx=5, pady=20, sticky=tk.W)

# Run light
run_label = ttk.Label(bottom_btn_panel, text='Run', width=4)
run_label.grid(column=2, row=3, columnspan=1, padx=5, pady=10, sticky=tk.E)

run_light_label = tk.Label(bottom_btn_panel, text='  ', width=2)
run_light_label.grid(column=3, row=3, columnspan=1, padx=2, pady=10, sticky=tk.W)

# Halt
halt_label = ttk.Label(bottom_btn_panel, text='Halt', width=4)
halt_label.grid(column=0, row=3, columnspan=1, padx=5, pady=10, sticky=tk.E)

halt_light_label = tk.Label(bottom_btn_panel, text='  ', width=2, bg="red")
halt_light_label.grid(column=1, row=3, columnspan=1, padx=2, pady=10, sticky=tk.W)


def halt():
    if halt_light_label.cget('bg') == "red":
        run_light_label.config(bg='red')

    '''
    TODO
    Halt functionality
    '''


# Run Button and Callback
def run_callback():
    print("run button clicked")
    run_light_label.config(bg="green")
    halt_light_label.config(bg="yellow")
    # do something


run_btn = ttk.Button(bottom_btn_panel, text='Run', command=run_callback, width=4)
run_btn.grid(column=2, row=2, columnspan=1, padx=5, pady=20, sticky=tk.E)

# ----------------------------END: BOTTOM BTN PANEL---------------------------- #

# -----------------------------END: BOTTOM PANEL -------------------------------#

# runs the GUI
root.mainloop()

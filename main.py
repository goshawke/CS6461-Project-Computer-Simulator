import tkinter
from GUI import *
from system import System


if __name__ == '__main__':
    file_dir = 'program1.txt'
    pc_default = 6

    # file_dir = "program2.txt"
    text_dir = "text.txt"
    # pc_default = 6

    # file_dir = './Programs/program1.txt.txt'
    # pc_default = int('100',16)

    # file_dir = 'ipl.txt'
    # pc_default = int('1010', 2)

    # initialize the system
    sys = System(file_dir, pc_default, text_dir)


    # initialize a tkinter window
    window = tkinter.Tk()
    app = Window(window, sys)

    # show window
    window.mainloop()


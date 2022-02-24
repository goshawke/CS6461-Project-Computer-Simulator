import tkinter
from GUI import *

from registers import *
from memory import *
from Instruction import *
# import tools

if __name__ == '__main__':
    ins = Instruction()
    mem = Memory()
    pc = PC()
    mar = MAR()
    mbr = MBR()
    ir = IR()
    mfr = MFR()
    gpr0 = GPR(label='GPR0')
    gpr1 = GPR(label='GPR1')
    gpr2 = GPR(label='GPR2')
    gpr3 = GPR(label='GPR3')
    ixr1 = IXR(label='IXR1')
    ixr2 = IXR(label='IXR2')
    ixr3 = IXR(label='IXR3')
    # tools.sample()


    window = Tk()
    app = Window(window, gpr0, gpr1, gpr2, gpr3, ixr1, ixr2, ixr3, pc, mar, mbr, ir, mfr, mem, ins)
    # Runs the GUI
    window.mainloop()

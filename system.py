
import time
from GUI import *
from CPU.registers import *
from CPU.Instruction import *
from CPU.ALU import *
from Memory.cache import *
from ioDevice import *
import sys, os

class System:
    def __init__(self, file_dir, pc_default):
        # initialize cache
        self.cache = Cache()
        # initialize an instruction object
        self.ins = Instruction()
        # initialize registers
        self.pc = PC()
        self.mar = MAR()
        self.mbr = MBR()
        self.ir = IR()
        self.mfr = MFR()
        self.cc = CC()
        self.gpr0 = GPR(label='GPR0')
        self.gpr1 = GPR(label='GPR1')
        self.gpr2 = GPR(label='GPR2')
        self.gpr3 = GPR(label='GPR3')
        self.ixr1 = IXR(label='IXR1')
        self.ixr2 = IXR(label='IXR2')
        self.ixr3 = IXR(label='IXR3')
        # initialize ALU
        self.alu = ALU(self.cc)
        # initialize io devices
        self.keyboard = Keyboard()
        self.printer = Printer()

        # for refreshing
        self.registers = [self.gpr0, self.gpr1, self.gpr2, self.gpr3, self.ixr1, self.ixr2, self.ixr3,
                            self.pc, self.mar, self.mbr, self.ir, self.mfr, self.cc]
        self.gprs = [self.gpr0, self.gpr1, self.gpr2, self.gpr3]
        self.ixrs = [self.ixr1, self.ixr2, self.ixr3]


        self.file_dir = file_dir
        self.pc_default = pc_default

    def reset(self):
        """This function resets the system
        It's called in GUI.resets
        """
        self.cache.reset()
        for reg in self.registers:
            reg.reset()
        self.ins.reset()
        self.alu.reset()
        self.keyboard.reset()
        self.printer.reset()

        # TODO - can we delete this? Only has one usage and we have a work-around, GUI line 1274ish
    '''    def set_instruction(self, index):
        """This function sets the bit of instruction into 1 or 0
        It's called in GUI.func_instruction
        """
        temp = list(self.ins.value)
        if temp[index] == '1':
            temp[index] = '0'
        else:
            temp[index] = '1'
        self.ins.value = ''.join(temp)
        self.ins.update()
    '''
    def reg_load_ins(self, reg: Register):
        """This function loads register with the value of the instruction
        It's called in GUI.func_reg_load
        """
        reg.set_value(ins.value[16-reg.size:16])
        print('reg.label' + '<-' + str(int(reg.value)))

    def load(self):
        """MBR <- MEM[MAR]
        It's called in GUI.func_reg_load
        """
        print('MBR <- MEM[MAR]:')
        self.mbr.set_value(self.cache.get(int(self.mar.value,2)))
        print(f'MBR <- {self.cache.msg}')

    def store(self):
        """MEM[MAR] <- MBR
        It's called in GUI.func_store
        """
        print('MEM[MAR] <- MBR:\n')
        self.cache.set(int(self.mar.value,2), self.mbr.value)
        print(self.cache.msg)

    def st_plus(self):
        """MEM[MAR] <- MBR; MAR++
        It's called in GUI.fun_st_plus
        """
        print('MEM[MAR] <- MBR:\n')
        self.cache.set(int(self.mar.value,2), self.mbr.value)
        print(self.cache.msg)
        print('MAR++:\n')
        self.mar.add_10(1)
        print(f'MAR = {str(int(self.mar.value))}')




    def load_file(self):
        """Pre-load the file
        It's called in GUI.func_ipl
        """
        # test
        # file_dir = './ipl.txt'
        def resource_path(relative_path):
            """ Get the absolute path to the resource, works for dev and for PyInstaller """
            try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        #   END: resource_path

        try:
            with open(resource_path(self.file_dir), 'r') as f:
                lines = f.readlines()
            f.close()
        except FileNotFoundError:
            print(self.file_dir + ' does not exist')
            return

        for i in lines:
            i = i.replace('\n','')
            if i == '':
                continue
            # ipl_info update
            print(i + '\n')
            # mem[add] <- value
            temp = i.split(' ')
            if temp[0] == '#':
                continue
            add, value = int(temp[0], 16), bin(int(temp[1][0:4], 16))[2:]
            self.cache.mem.set_to_memory(add, value)
            # step_info update
            print('MEM[' + str(add) + '] = ' + value)

        # set pc by default
        self.pc.set_value(bin(self.pc_default)[2:])
        print('PC has been set to ' + self.pc.value)

    def __fetch(self):
        """Fetching of instruciton"""
        print('Fetch Instruction')
        # MAR <- PC
        self.mar.get_from_PC(self.pc)
        print('MAR <- PC :\t\t\t' + self.mar.value)
        # MBR <- mem[MAR]
        self.mbr.set_value(self.cache.get(int(self.mar.value,2)))
        print('MBR <- ' + self.cache.msg)
        # IR <- MBR
        self.ir.get_from_MBR(self.mbr)
        print('IR <- MBR :\t\t\t' + self.ir.value + '')

    def __decode(self):
        """Decoding of instruction"""
        print('Decode Instruction')
        word = Instruction(self.ir.value)
        print('Instruction :\t\t\t' + word.print_out())
        return word

    def __locate(self, word):
        """Computation of EA"""
        print('Locate EA')
        # IAR <- ADD
        iar = Register(12, 'IAR')
        iar.set_value(str(int(word.address)))
        print('IAR <- Add :\t\t\t' + iar.value)
        # IAR += X[IXR] if IXR = 1 or 2 or 3
        ixr_id = int(word.ixr_index,2)
        if ixr_id != 0:
            ixr = self.ixrs[ixr_id-1]
            iar.set_value(bin(int(iar.value,2) + int(ixr.value,2))[2:])
            print('IAR += ' + ixr.label + ' :\t\t\t' + iar.value)
        # IAR <- MEM[IAR] if I = 1
        if int(word.indirect,2) == 1:
            add = int(iar.value,2)
            iar.set_value(self.cache.get(add))
            print('IAR <- ' + self.cache.msg)
        # MAR <- IAR
        self.mar.set_value(iar.value)
        print('MAR <- IAR :\t\t\t' + self.mar.value)

    def __execute_deposit(self, word, input, output):
        """The execution and deposit"""
        print('Execute and Deposit Result')
        irr = Register(16,'IRR')
        ea = self.mar.value
        op = int(word.opcode, 2)
        if op in [16, 17, 18, 19, 20, 21]:
            rx = self.gprs[int(word.rx,2)]
            if op != 21:
                ry = self.gprs[int(word.ry,2)]
        elif op in [25, 26]:
            a_l = int(word.a_l)
            l_r = int(word.l_r)
            count = int(word.count,2)
            gpr = self.gprs[int(word.gpr_index, 2)]
        else:
            gpr = self.gprs[int(word.gpr_index, 2)]
            ixr = self.ixrs[int(word.ixr_index,2)-1]
            immed = word.address
            devid = word.address
        # LDR
        if op == 1:
            # MBR <- MEM[MAR]
            self.mbr.set_value(self.cache.get(int(self.mar.value,2)))
            print('MBR <- '+ self.cache.msg)
            # IRR <- MBR
            irr.set_value(self.mbr.value)
            print('IRR <- MBR :\t\t\t' + irr.value)
            # R[GPR] <- IRR
            gpr.set_value(irr.value)
            print(gpr.label + ' <- IRR :\t\t\t' + gpr.value)
        # STR
        elif op == 2:
            # IRR <- R[GPR]
            irr.set_value(gpr.value)
            print('IRR <- ' + gpr.label + ' :\t\t\t' + irr.value)
            # MBR <- IRR
            self.mbr.set_value(irr.value)
            print('MBR <- IRR :\t\t\t' + self.mbr.value)
            # MEM[MAR] <- MBR
            self.cache.set(int(self.mar.value,2), self.mbr.value)
            print(self.cache.msg)
        # LDA
        elif op == 3:
            # MBR <- MAR
            self.mbr.set_value(self.mar.value)
            print('MBR <- MAR : \t\t\t' + self.mbr.value)
            # IRR <- MBR
            irr.set_value(self.mbr.value)
            print('IRR <- MBR :\t\t\t' + irr.value)
            # R[GPR] <- IRR
            gpr.set_value(irr.value)
            print(gpr.label + ' <- IRR :\t\t\t' + gpr.value)
        # AMR: R=c(R)+c(EA)
        elif op == 4:
            # MBR <- MEM[MAR]
            self.mbr.set_value(self.cache.get(int(self.mar.value,2)))
            print('MBR <- '+ self.cache.msg)
            # IRR <- R[GPR] + MBR
            irr.set_value(self.alu.arithmetic_cal('+', gpr.value, self.mbr.value))
            print('IRR <- ' + gpr.label + ' + MBR:\t\t\t' + irr.value)
            # R[GPR] <- IRR
            gpr.set_value(irr.value)
            print(gpr.label + ' <- IRR :\t\t\t' + gpr.value)
        # SMR: R=c(R)-c(EA)
        elif op == 5:
            # MBR <- MEM[MAR]
            self.mbr.set_value(self.cache.get(int(self.mar.value,2)))
            print('MBR <- '+ self.cache.msg)
            # IRR <- R[GPR] - MBR
            irr.set_value(self.alu.arithmetic_cal('-', gpr.value, self.mbr.value))
            print('IRR <- ' + gpr.label + ' - MBR:\t\t\t' + irr.value + '\n')
            # R[GPR] <- IRR
            gpr.set_value(irr.value)
            print(gpr.label + ' <- IRR :\t\t\t' + gpr.value + '\n')
        # AIR: R=c(R)+Immed
        elif op == 6:
            # IRR <- R[GPR] + Immed
            irr.set_value(self.alu.arithmetic_cal('+', gpr.value, immed))
            print('IRR <- ' + gpr.label + ' + Immed:\t\t\t' + irr.value + '\n')
            # R[GPR] <- IRR
            gpr.set_value(irr.value)
            print(gpr.label + ' <- IRR :\t\t\t' + gpr.value + '\n')
        # SIR: R=c(R)-Immed
        elif op == 7:
            # IRR <- R[GPR] - Immed
            irr.set_value(self.alu.arithmetic_cal('-', gpr.value, immed))
            print('IRR <- ' + gpr.label + ' - Immed:\t\t\t' + irr.value + '\n')
            # R[GPR] <- IRR
            gpr.set_value(irr.value)
            print(gpr.label + ' <- IRR :\t\t\t' + gpr.value + '\n')
        # JZ: PC=EA if c(R)=0 else PC++
        elif op == 8:
            print(gpr.label +  ' = ' + str(int(gpr.value)) + '\t\t\t')
            if int(gpr.value,2) == 0:
                print('== 0\n')
                self.pc.set_value(ea)
                print('PC <- EA :\t\t\t' + self.pc.value + '\n\n')
            else:
                print('!= 0\n')
                self.pc.next()
                print('PC ++ :\t\t\t' + self.pc.value + '\n\n')
        # JNE: PC=EA if c(R)!=0 else PC++
        elif op == 9:
            print(gpr.label +  ' = ' + str(int(gpr.value)) + '\t\t\t')
            if int(gpr.value,2) != 0:
                print('!= 0\n')
                self.pc.set_value(ea)
                print('PC <- EA :\t\t\t' + self.pc.value + '\n\n')
            else:
                print('== 0\n')
                self.pc.next()
                print('PC++ :\t\t\t' + self.pc.value + '\n\n')
        # JCC: PC=EA if CC[r]=1 else PC++
        elif op == 10:
            index = int(word.gpr_index,2)
            print('CC[' + str(index) +'] = ' + self.cc.value[index] + '\t\t\t')
            if self.cc.value[index] == '1':
                print('== 1\n')
                self.pc.set_value(ea)
                print('PC <- EA :\t\t\t' + self.pc.value + '\n\n')
            else:
                print('!= 1\n')
                self.pc.next()
                print('PC++ :\t\t\t' + self.pc.value + '\n\n')
        # JMA:
        elif op == 11:
            # PC <- EA
            self.pc.set_value(ea)
            print('PC <- EA :\t\t\t' + self.pc.value + '\n\n')
        # JSR:
        elif op == 12:
            # PC ++
            self.pc.next()
            print('PC++ :\t\t\t' + self.pc.value + '\n')
            # R[3] <- PC
            self.gpr3.set_value(self.pc.value)
            print('GPR3 <- PC :\t\t\t' + self.gpr3.value + '\n')
            # PC <- EA
            self.pc.set_value(ea)
            print('PC <- EA :\t\t\t' + self.pc.value + '\n\n')
        # RFS:
        elif op == 13:
            # R[0] <- Immed
            self.gpr0.set_value(immed)
            print('GPR0 <- Immed :\t\t\t' + self.gpr0.value + '\n')
            # PC <- R[3]
            # if R[3].len > pc.size: pc=c(r3)[-pc.size:]
            self.pc.set_value(str(int(self.gpr3.value[-self.pc.size:])))
            print('PC <- GPR3 :\t\t\t' + self.pc.value + '\n\n')
        # SOB: c(R)=c(R)-1; PC=EA if C(R)>0 else PC++
        elif op == 14:
            # R[GPR] --
            gpr.set_value(self.alu.arithmetic_cal('-', gpr.value, '1'))
            # the real decimal result of subtraction
            gpr_value = self.alu.value
            print(gpr.label + '-- = ' + str(gpr_value) + '\t\t\t')
            if gpr_value > 0:
                print('> 0\n')
                self.pc.set_value(ea)
                print('PC <- EA : \t\t\t' + self.pc.value + '\n\n')
            else:
                print('<= 0\n')
                self.pc.next()
                print('PC++ : \t\t\t' + self.pc.value + '\n\n')
        # JGE: PC=EA if c(R)>=0 else PC++
        elif op == 15:
            print(gpr.label +  ' = ' + str(int(gpr.value)) + '\t\t\t')
            if int(gpr.value,2) >= 0:
                print('>= 0\n')
                self.pc.set_value(ea)
                print('PC <- EA : \t\t\t' + self.pc.value + '\n\n')
            else:
                print('< 0\n')
                self.pc.next()
                print('PC++ : \t\t\t' + self.pc.value + '\n\n')
        # MLT: Rx, Rx+1=c(Rx)*(Ry)
        elif op == 16:
            if int(word.rx,2) not in [0,2] or int(word.ry,2) not in [0,2]:
                print("Rx, Ry must be 0 or 2\n")
            else:
                print(rx.label + ' * ' + ry.label + ' :\t\t\t' + rx.get_value() + ' * ' + ry.get_value() + '\n')
                res = self.alu.arithmetic_cal('*', rx.value, ry.value).zfill(32)
                # IRR = Highter bits of Rx * Ry
                irr.set_value(res[:16])
                print("IRR <- High(Rx * Ry)\t\t\t" + irr.value + '\n')
                # Rx = IRR
                rx.set_value(irr.value)
                print(rx.label + ' <- IRR\t\t\t' + rx.value + '\n\n')
                # IRR = Lower bits of Rx * Ry
                irr.set_value(res[16:])
                print("IRR <- Low(Rx * Ry)\t\t\t" + irr.value + '\n')
                # Rx+1 = IRR
                rxx = self.gprs[int(word.rx,2)+1]
                rxx.set_value(irr.value)
                print(rxx.label + ' <- IRR\t\t\t' + rxx.value + '\n\n')
                # CC state
                print('CC State:\t\t\t' + self.cc.state + '\n')
        # DVD: Rx, Rx+1=c(Rx)/(Ry)
        elif op == 17:
            if int(word.rx,2) not in [0,2] or int(word.ry,2) not in [0,2]:
                print("Rx, Ry must be 0 or 2\n")
            else:
                print(rx.label + ' / ' + ry.label + ' :\t\t\t' + rx.get_value() + ' / ' + ry.get_value() + '\n')
                # Ry = 0 -> cc = DIVZERO
                if int(ry.value,2) == 0:
                    self.cc.set_state('DIVZERO')
                    # CC state
                    print('CC State:\t\t\t' + self.cc.state + '\n')
                else:
                    # Rx+1 <- Rx % Ry
                    irr.set_value(self.alu.arithmetic_cal('%', rx.value, ry.value))
                    print("IRR <- Rx % Ry\t\t\t" + irr.value + '\n')
                    # Rxx = IRR
                    rxx = self.gprs[int(word.rx,2)+1]
                    rxx.set_value(irr.value)
                    print(rxx.label + ' <- IRR\t\t\t' + rxx.value + '\n\n')
                    # IRR = Rx / Ry
                    irr.set_value(self.alu.arithmetic_cal('/', rx.value, ry.value))
                    print("IRR <- Rx / Ry\t\t\t" + irr.value + '\n')
                    # Rx = IRR
                    rx.set_value(irr.value)
                    print(rx.label + ' <- IRR\t\t\t' + rx.value + '\n\n')

        # TRR: cc(4)=1 if c(Rx)=c(Ry) else cc(r)=0
        elif op == 18:
            if int(rx.value,2) == int(ry.value,2):
                print(rx.label + ' = ' + ry.label + ' :\t\t\t' + rx.get_value() + ' = ' + ry.get_value() + '\n')
                self.cc.set_state('EQUALORNOT')
                print('CC State:\t\t\t' + self.cc.state + '\n')
            else:
                print(rx.label + ' != ' + ry.label + ' :\t\t\t' + rx.get_value() + ' != ' + ry.get_value() + '\n')
                self.cc.reset()
                print('CC State:\t\t\t' + self.cc.state + '\n')
        # AND: c(Rx)=c(Rx) AND c(Ry)
        elif op == 19:
            print(rx.label + ' :\t\t\t' + rx.value + '\n')
            print(ry.label + ' :\t\t\t' + ry.value + '\n')
            # IRR = Rx & Ry
            irr.set_value(self.alu.logic_cal('&', rx.value, ry.value))
            txt.insert(INSERT,'IRR = Rx & Ry :\t\t\t' + irr.value.zfill(irr.size) + '\n')
            # Rx = IRR
            rx.set_value(irr.value)
            print(rx.label + ' <- IRR\t\t\t' + rx.value + '\n\n')
        # ORR: c(Rx)=c(Rx) OR c(Ry)
        elif op == 20:
            print(rx.label + ' :\t\t\t' + rx.value + '\n')
            print(ry.label + ' :\t\t\t' + ry.value + '\n')
            # IRR = Rx | Ry
            irr.set_value(self.alu.logic_cal('|', rx.value, ry.value))
            txt.insert(INSERT,'IRR = Rx | Ry :\t\t\t' + irr.value.zfill(irr.size) + '\n')
            # Rx = IRR
            rx.set_value(irr.value)
            print(rx.label + ' <- IRR\t\t\t' + rx.value + '\n\n')
        # NOT: c(Rx)=NOT c(Rx)
        elif op == 21:
            print(rx.label + ' :\t\t\t' + rx.value + '\n')
            # IRR = ~ Rx
            irr.set_value(self.alu.logic_cal('~', rx.value))
            txt.insert(INSERT,'IRR = NOT Rx  :\t\t\t' + irr.value.zfill(irr.size) + '\n')
            # Rx = IRR
            rx.set_value(irr.value)
            print(rx.label + ' <- IRR\t\t\t' + rx.value + '\n\n')
        # SRC: c(R) is shifted left(L/R=1) or right(L/R=0) either logically(A/L=1) or arithmetically(A/L=0)
        elif op == 25:
            lr = 'left' if l_r == 1 else 'right'
            al = 'logically' if a_l == 1 else 'arithmetically'
            print(gpr.label + ' is shifted ' + lr + ' ' + al + '\n')
            gpr.set_value(self.alu.shift(gpr.value.zfill(gpr.size), count, l_r, a_l))
            print(gpr.label + ' :\t\t\t' + gpr.value + '\n')
            print('CC State:\t\t\t' + self.cc.state + '\n')
        # RRC: c(R) is Rotated left(L/R=1) or right(L/R=0) either logically(A/L=1)
        elif op == 26:
            al = 'logically' if a_l == 1 else 'arithmetically'
            lr = 'left' if l_r == 1 else 'right'
            print(gpr.label + ' is rotated ' + lr + ' ' + al + '\n')
            gpr.set_value(self.alu.rotate(gpr.value.zfill(gpr.size), count, l_r, a_l))
            print(gpr.label + ' :\t\t\t' + gpr.value + '\n')
            print('CC State:\t\t\t' + self.cc.state + '\n')
        # LDX
        elif op == 33:
            # MBR <- MEM[MAR]
            self.mbr.set_value(self.cache.get(int(self.mar.value,2)))
            print('MBR <- ' + self.cache.msg)
            # IRR <- MBR
            irr.set_value(self.mbr.value)
            print('IRR <- MBR :\t\t\t' + irr.value + '\n')
            # X[IXR] <- IRR
            ixr.set_value(irr.value)
            print(ixr.label + ' <- IRR :\t\t\t' + ixr.value + '\n')
        # STX
        elif op == 34:
            # IRR <- X[IXR]
            irr.set_value(ixr.value)
            print('IRR <- ' + ixr.label + ' :\t\t\t' + irr.value + '\n')
            # MBR <- IRR
            self.mbr.set_value(irr.value)
            print('MBR <- IRR :\t\t\t' + self.mbr.value + '\n')
            # MEM[MAR] <- MBR
            self.cache.set(int(self.mar.value,2), self.mbr.value)
            print(self.cache.msg)
        # IN: R[GPR] <- In
        elif op == 49:
            print('Please input a number')
            if self.keyboard.write(input):
                gpr.reset()
                gpr.add_10(self.keyboard.read())
                print(gpr.label + ' <- Input :\t\t\t' + gpr.label + ' = ' + gpr.get_value() + '\n')
            else:
                print('Invalid Input\n')
                gpr.reset()
        # OUT: Out <- R[GPR]
        elif op == 50:
            self.printer.write_line(gpr.get_value())
            output.configure(state='normal')
            output.delete(1.0, END)
            output.insert(INSERT, self.printer.read_content())
            output.yview_moveto('1.0')
            output.configure(state='disabled')
            print('Output <- '+ gpr.label + ' :\t\t\tOutput ' + self.printer.read_line() +  '\n')

    def single_step(self, input, output):
        """This function implements the single step
        It's called in GUI.func_ss
        """
        # Fetch
        self.__fetch()
        # Decode
        word = self.__decode()
        op = int(word.opcode, 2)
        # Halt if op = 0
        if op == 0:
            print('Program is done\n\n')
            return 'DONE'
        # EA Compute: for some operation x, i are ignored, which means no EA needed
        if op not in [6, 7, 13, 16, 17, 18, 19, 20, 21, 25, 26, 49, 50]:
            self.__locate(word)
        # Excute and Deposit
        self.__execute_deposit(word, input, output)
        # PC++: for some operation, pc++ is not needed
        if op not in [8,9,10,11,12,14,15]:
            self.pc.next()
            print('PC++')


    def test_ins(self, ins, input, output):
        """This function implements testing of input instrucitons
        It's called in GUI.func_test
        """
        i = Instruction()
        msg = i.decode_test(ins)
        print(msg)
        if msg == 'Decoding Complete\n\n':
            # for some operation x, i are ignored, which means no EA needed
            if int(i.opcode,2) not in [6, 7, 13, 16, 17, 18, 19, 20, 21, 25, 26, 49, 50]:
                self.__locate(i)
            self.__execute_deposit(i, input, output)


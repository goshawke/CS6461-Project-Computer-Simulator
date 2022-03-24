class Instruction:

    def __init__(self, value = '0' * 16):
        if len(value) < 16:
            value = value.zfill(16)
        self.value = value

# new
        self.opcode = []
        self.dict_opcode = {0: 'HLT', 1: 'LDR', 2: 'STR', 3: 'LDA',
                            4: 'AMR', 5: 'SMR', 6: 'AIR', 7: 'SIR',
                            8: 'JZ', 9: 'JNE', 10: 'JCC', 11: 'JMA',
                            12: 'JSR', 13: 'RFS', 14: 'SOB', 15: 'JGE',
                            16: 'MLT', 17: 'DVD', 18: 'TRR', 19: 'AND',
                            20: 'ORR', 21: 'NOT', 24: 'TRAP', 25: 'SRC',
                            26: 'RRC', 33: 'LDX', 34: 'STX', 49: 'IN',
                            50: 'OUT'}
        self.dict_opcode.setdefault(0, 'HLT')
        self.gpr_index = []
        self.ixr_index = []
        self.indirect = []
        self.address = []

        self.rx = []
        self.ry = []

        self.a_l = []
        self.l_r = []
        self.count = []
# end new

        self.update()

    def update(self):
        self.opcode = self.value[:6]

        opcode_value = int(self.opcode, 2)
        # Arithmetic and Logical Instructions (Register to Register)
        if opcode_value in [16, 17, 18, 19, 20, 21]:
            self.rx = self.value[6:8]
            self.ry = self.value[8:10]
        # Shift/Rotate Instructions
        elif opcode_value in [25, 26]:
            self.gpr_index = self.value[6:8]
            self.a_l = self.value[8]
            self.l_r = self.value[9]
            self.count = self.value[12:]


        self.gpr_index = self.value[6:8]
        self.ixr_index = self.value[8:10]
        self.indirect = self.value[10:11]
        self.address = self.value[11:]

    def reset(self):
        self.value = '0' * 16
        self.update()

    def print_out(self):
        """This function translates the instruction and prints it out at the Step_info
                """
        opcode_value = int(self.opcode, 2)
        word = self.dict_opcode[int(self.opcode, 2)] + ' '
        # Halt
        if opcode_value == 0:
            word += '0'
        # Arithmetic and Logical Instructions (Register to Register)
        elif opcode_value in [16, 17, 18, 19, 20, 21]:
            word += str(int(self.rx, 2)) + ' '
            if opcode_value != 21:
                word += str(int(self.ry, 2)) + ' '
        # Shift/Rotate Instructions
        elif opcode_value in [25, 26]:
            word += str(int(self.gpr_index, 2)) + ' '
            word += self.a_l + ' '
            word += self.l_r + ' '
        # IO
        elif opcode_value in [49, 50]:
            word += str(int(self.gpr_index, 2)) + ' '
            word += str(int(self.address, 2))
        else:
            word += str(int(self.gpr_index, 2)) + ' '
            word += str(int(self.ixr_index, 2)) + ' '
            word += self.indirect + ' '
            word += str(int(self.address, 2))
        return word


    def decode_test(self, ins_test):
        dict = {str:num for num, str in self.dict_opcode.items()}
        print(dict)
        ins_test = ins_test.split(' ')
        opcode = ins_test[0]
        num = len(ins_test)
        if opcode not in dict.keys():
            return("Unknown Operation")
        else:
            self.opcode = dict[opcode]

        # Arithmetic and Logical Instructions (Register to Register)
        if self.opcode in [16, 17, 18, 19, 20]:
            if num != 3:
                return(opcode + ' needs two params: ' + opcode + ' rx ry\n')
            else:
                rx = int(ins_test[1])
                ry = int(ins_test[2])
                if rx not in [0,1,2,3]:
                    return("Rx should be 0, 1, 2 or 3\n")
                elif ry not in [0,1,2,3]:
                    return("Ry should be 0, 1, 2 or 3\n")
                else:
                    self.opcode = bin(self.opcode)[2:]
                    self.rx = bin(rx)[2:]
                    self.ry = bin(ry)[2:]
        elif self.opcode == 21:
            if num != 2:
                return(opcode + ' needs one param: ' + opcode + ' rx\n')
            else:
                rx = int(ins_test[1])
                if rx not in [0,1,2,3]:
                    return("Rx should be 0, 1, 2 or 3\n")
                else:
                    self.opcode = bin(self.opcode)[2:]
                    self.rx = bin(rx)[2:]
        # Shift/Rotate Instructions
        elif self.opcode in [25, 26]:
            if num != 5:
                return(opcode + ' needs 4 params: ' + opcode + ' R Count L/R A/L\n')
            else:
                r, count, l_r, a_l = ins_test[1:]
                if int(r) not in [0,1,2,3]:
                    return("gpr should be 0, 1, 2 or 3\n")
                elif int(count) > 15 or int(count) < 0:
                    return("Count should be in range of 0:15")
                elif int(l_r) not in [0,1]:
                    return("L/R should be 0 or 1\n")
                elif int(a_l) not in [0,1]:
                    return("A/L should be 0 or 1\n")
                else:
                    self.opcode = bin(self.opcode)[2:]
                    self.gpr_index = bin(int(r))[2:]
                    self.count = bin(int(count))[2:]
                    self.l_r = bin(int(l_r))[2:]
                    self.a_l = bin(int(a_l))[2:]
        # IO
        elif self.opcode in[49, 50]:
            if num != 3:
                return(opcode + ' needs 2 params: ' + opcode + ' R DevID\n')
            else:
                r, id = ins_test[1:]
                if int(r) not in [0,1,2,3]:
                    return("GPR should be 0, 1, 2 or 3\n")
                else:
                    self.opcode = bin(self.opcode)[2:]
                    self.gpr_index = bin(int(r))[2:]
                    self.address = bin(int(id))[2:]
        else:
            if num != 5:
                msg = opcode + ' needs 4 params: r  x  i  add\n'
                msg += 'Set 0 if a param is ignored\n'
                return(msg)
            else:
                r, x, i, add = ins_test[1:]
                if int(r) not in [0,1,2,3]:
                    return 'GPR should be 0, 1, 2 or 3\n'
                elif int(x) not in [0,1,2,3]:
                    return 'IXR should be 0, 1, 2 or 3\n'
                elif int(i) not in [0,1]:
                    return("Indirect bit should be 0 or 1\n")
                else:
                    self.opcode = bin(self.opcode)[2:]
                    self.gpr_index = bin(int(r))[2:]
                    self.ixr_index = bin(int(x))[2:]
                    self.indirect = bin(int(i))[2:]
                    self.address = bin(int(add))[2:]
        return 'Decoding Complete\n\n'



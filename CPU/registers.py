
class Register:
    """This class is the super class of all of registers
    Parameters:
    --------------
    size : int type; the size of the register
    value: str type; the value of the register
    label: str type; the kind of the register
    """

    def __init__(self, size=4, label='register'):
        self.size = size
        self.value = '0' * self.size
        self.label = label

    def check_state(self, input_value):
        """This function checks if the value cause fault"""
        max_value = int('1' * self.size, 2)
        min_value = int('0' * self.size, 2)
        if input_value > max_value:
            return 'OVERFLOW'
        elif input_value < min_value:
            return 'UNDERFLOW'
        else:
            return '0000'

    def add_10(self, adder: int):
        """This function adds value and return the state of the register
        Parameters:
        ------------
        adder: the decimal number that going to be added to
        """
        value = int(self.value, 2) + adder
        if value >= 0:
            temp = bin(value)[2:].zfill(self.size)
        else:
            temp = bin(value)[3:].zfill(self.size)
        state = self.check_state(value)
        self.set_value(str(int(temp[-self.size:])))
        return state

    def get_value(self):
        """Return str type of decimal value"""
        return self.value

    def set_value(self, val: str):
        while len(val) < self.size:
            val = '0' + val

        self.value = val

    def reset(self):
        """This function resets the register"""
        self.value = '0' * self.size


class PC(Register):
    """This is the class of Program Counter
    PC has 12 bits
    """

    def __init__(self, size=12, label='PC'):
        super().__init__(size=size, label=label)

    def next(self):
        """This function defines how pc find the next instruction"""
        self.add_10(1)


class MAR(Register):
    """This is the class of Memory Address Register
    MAR has 12 bits

    Function:
    ------------
    get_from_PC
    """

    def __init__(self, size=12, label='MAR'):
        super().__init__(size=size, label=label)

    def get_from_PC(self, pc: PC):
        """The function for MAR <- PC
        """
        self.value = pc.value


class MBR(Register):
    """This is the class of Memory Buffer Register
    MBR has 16 bits
    """

    def __init__(self, size=16, label='MBR'):
        super().__init__(size=size, label=label)


class IR(Register):
    """This is the class of Instruction Register
    IR has 16 bits
    """

    def __init__(self, size=16, label='IR'):
        super().__init__(size=size, label=label)

    def get_from_MBR(self, mbr: MBR):
        """The function for IR <- MBR
        """
        self.value = mbr.value


class CC(Register):
    """This is the class of Condition Code
    CC has 4 bits
    """

    def __init__(self, size=4, label='CC'):
        super().__init__(size=size, label=label)
        self.state = '0000'

    def reset(self):
        self.value = '0' * self.size
        self.state = '0000'

    def set_state(self, state: str):
        self.reset()
        self.state = state
        value = list(self.value)
        if state == 'OVERFLOW':
            value[0] = '1'
        elif state == 'UNDERFLOW':
            value[1] = '1'
        elif state == 'DIVZERO':
            value[2] = '1'
        elif state == 'EQUALORNOT':
            value[3] = '1'
        self.value = ''.join(value)


class MFR(Register):
    """This is the class of Memory Fault Register
    MFR has 4 bits
    """

    def __init__(self, size=4, label='MFR'):
        super().__init__(size=size, label=label)


class GPR(Register):
    """This is the class of General Purpose Register
    GPR has 16 bits
    """

    def __init__(self, size=16, label='GPR'):
        super().__init__(size=size, label=label)


class IXR(Register):
    """This is the class of Index Register
    IXR has 16 bits
    """

    def __init__(self, size=16, label='IXR'):
        super().__init__(size=size, label=label)

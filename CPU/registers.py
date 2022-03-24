from Memory.memory import *
from Memory.cache import *

class Register:

    def __init__(self, size=0, label=''):
        self.size = size
        self.value = '0' * self.size
        self.label = label

    def check_state(self, input_value):
        """This function checks if the value cause fault"""
        max = int('1'*self.size, 2)
        min = int('0'*self.size, 2)
        if input_value > max:
            return 'OVERFLOW'
        elif input_value < min:
            return 'UNDERFLOW'
        else:
            return '0000'


    def check_overflow(self, input_value) -> bool:

        return True if len(input_value) > self.size else False

    def get_value(self):
        return self.value

    def set_value(self, val: str):
        while len(val) < self.size:
            val = '0' + val

        self.value = val

    # TODO - delete?
    def add_2(self, adder: str):

        temp = bin(int(self.value, 2) + int(adder, 2))[2:]
        if self.check_overflow(temp) != True:
            self.set_value(temp)
        else:
            print(self.label + ' overflow error')

    # TODO
    def add_10(self, adder: int):
        """This function adds value and return the state of the register
        Parameters:
        ------------
        adder: the decimal number that going to be added to
        """
        value = int(self.value,2) + adder
        if value >= 0:
            temp = bin(value)[2:].zfill(self.size)
        else:
             temp = bin(value)[3:].zfill(self.size)
        state = self.check_state(value)
        self.set_value(str(int(temp[-self.size:])))

        return state


    def reset(self):
        self.value = '0' * self.size


class PC(Register):

    def __init__(self, size=12, label='PC'):
        super().__init__(size=size, label=label)

    def next(self):
        self.add_10(1)


class MAR(Register):

    def __init__(self, size=12, label='MAR'):
        super().__init__(size=size, label=label)

    def get_from_PC(self, pc: PC):
        self.value = pc.get_value()


class MBR(Register):

    def __init__(self, size=16, label='MBR'):
        super().__init__(size=size, label=label)

    # TODO - delete?
    '''
    def load_from_mem(self, mar: MAR, mem: Memory):
        address = int(''.join(mar.value), 2)
        self.value = mem.get_from_memory(address)

        while len(self.value) < self.size:
            self.value = '0' + self.value
    '''
    # TODO - delete?
    '''
    def store_to_mem(self, mar: MAR, mem: Memory):
        address = int(''.join(mar.value), 2)

        while len(self.value) < 16:
            self.value = '0' + self.value

        mem.set_to_memory(address, self.value)
    '''

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

    def set_state(self, state : str):
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


class IR(Register):

    def __init__(self, size=16, label='IR'):
        super().__init__(size=size, label=label)

    def get_from_MBR(self, mbr: MBR):
        self.value = mbr.value


class MFR(Register):

    def __init__(self, size=4, label='MFR'):
        super().__init__(size=size, label=label)


class GPR(Register):

    def __init__(self, size=16, label='GPR'):
        super().__init__(size=size, label=label)


class IXR(Register):

    def __init__(self, size=16, label='IXR'):
        super().__init__(size=size, label=label)

class PRIV(Register):

    def __init__(self, size=1, label='PRIV'):
        super().__init__(size=size, label=label)
from memory import *


class Register:

    def __init__(self, size=0, label=''):
        self.size = size
        self.value = '0' * self.size
        self.label = label

    def check_overflow(self, input_value) -> bool:

        return True if len(input_value) > self.size else False

    def get_value(self):
        return self.value

    def set_value(self, val: str):
        while len(val) < self.size:
            val = '0' + val

        self.value = val


    def add_2(self, adder: str):

        temp = bin(int(self.value, 2) + int(adder, 2))[2:]
        if self.check_overflow(temp) != True:
            self.set_value(temp)
        else:
            print(self.label + ' overflow error')


    def add_10(self, adder: int):

        temp = bin(int(self.value, 2) + adder)[2:]
        if self.check_overflow(temp) != True:
            self.set_value(temp)
        else:
            print(self.label + ' overflow error')


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

    def load_from_mem(self, mar: MAR, mem: Memory):
        address = int(''.join(mar.value), 2)
        self.value = mem.get_from_memory(address)

        while len(self.value) < self.size:
            self.value = '0' + self.value


    def store_to_mem(self, mar: MAR, mem: Memory):
        address = int(''.join(mar.value), 2)

        while len(self.value) < 16:
            self.value = '0' + self.value

        mem.set_to_memory(address, self.value)


class IR(Register):

    def __init__(self, size=16, label='IR'):
        super().__init__(size=size, label=label)

    def get_from_MBR(self, mbr: MBR):
        self.value = mbr.value


class CC(Register):

    def __init__(self, size=4, label='CC'):
        super().__init__(size=size, label=label)


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
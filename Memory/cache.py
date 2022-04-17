
class Memory:
    """This is the class for Memory"""

    def __init__(self):
        self.size = 2048
        self.memory = ['0'] * self.size

    def reset(self):
        self.memory = ['0'] * self.size

    def memory_expansion(self):
        """Expand memory size to 4096"""
        self.size = 4096
        self.memory = ['0'] * self.size

    def get_from_memory(self, address):
        return self.memory[address]

    def set_to_memory(self, address, value):
        self.memory[address] = value

    def get_value(self, address):
        """This function is for Step_info
        :param address: the address to request data
        :return: string type of decimal values
        """
        address = int(address, 2)
        return str(int(self.memory[address], 2))

    def print_out(self):
        word = '\n-------------MEMORY--------------\n'
        for i, line in enumerate(self.memory):
            word += str(i) + ':\t' + str(int(line)) + '\n'
        return word

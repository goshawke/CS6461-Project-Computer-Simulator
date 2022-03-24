class Memory:

    def __init__(self):
        self.size = 2048
        self.memory = ['0'] * self.size

    def get_from_memory(self, address):
        return self.memory[address]

    def set_to_memory(self, address, value):
        self.memory[address] = value

    # called reset() in other code
    # Memory is reset when cache.reset() is called in system.reset() method
    # TODO - change this to reset or not?
    def reset_memory(self):
        self.memory = ['0'] * self.size

    def memory_expansion(self):
        """If it is needed, memory size can be expanded to 4096
        """
        self.size = 4096
        self.memory = ['0'] * self.size

    def print_out(self):
        word = '\n-------------MEMORY--------------\n'
        for i, line in enumerate(self.memory):
            word += str(i) + ':\t' + str(int(line)) + '\n'
        return word

    # TODO - decide if needed
    '''    def get_value(self, address):
        """This function is for Step_info
        it returns string type of decimal values
        """
        address = int(address,2)
        return str(int(self.memory[address],2))'''

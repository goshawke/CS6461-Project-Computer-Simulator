class Memory:

    def __init__(self):
        self.size = 32
        self.memory = ['0'] * self.size

    def get_from_memory(self, address):
        return self.memory[address]

    def set_to_memory(self, address, value):
        self.memory[address] = value

    def reset_memory(self):
        self.memory = ['0'] * self.size
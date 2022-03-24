
class IO:
    def __init__(self, id):
        self.id = id
        self.content = ''

    def reset(self):
        self.content = ''

class Keyboard(IO):
    def __init__(self, id=0):
        super().__init__(id=id)

    def write(self, input):
        entry, content, btn, trigger = input[0], input[1], input[2], input[3]
        entry.configure(state='normal')
        btn.wait_variable(trigger)
        # get number
        number = content.get()
        # reset the box
        trigger.set(0)
        content.set('')
        entry.configure(state='disabled')
        # pre-process number
        number = number.strip()
        if len(number) == 0:
            return False
        else:
            self.content = int(number)
            return True

    def read(self):
        return self.content

class Printer(IO):
    def __init__(self, id=1):
        super().__init__(id=id)
        self.content_line = ''
        self.line_id = 1

    def write_line(self, new_line):
        self.content_line = new_line
        self.content += 'line ' + str(self.line_id) + ':\t' + self.content_line + '\n'
        self.line_id += 1

    def read_content(self):
        return self.content

    def read_line(self):
        return self.content_line

    def reset(self):
        self.content_line = ''
        self.content = ''
        self.line_id = 1

import os
import sys


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
            self.content = number
            return True

    def read(self):
        return self.content


class Printer(IO):
    def __init__(self, id=1):
        super().__init__(id=id)
        self.content_line = ''
        self.line_id = 1

    def write_line(self, new_line):

        # For Program 2
        # if int(new_line) > 10:
        #     new_line = chr(int(new_line))

        self.content_line = new_line
        self.content += 'line ' + str(self.line_id) + ':\t' + self.content_line + '\n'
        self.line_id += 1

    # new - not sure if correct
    def write_paragraph(self, new_paragraph):
        self.content_line = new_paragraph
        self.content += 'line ' + str(self.line_id) + ':\t' + self.content_line + '\n'
        self.line_id += 1
    # new

    def read_content(self):
        return self.content

    def read_line(self):
        return self.content_line

    def reset(self):
        self.content_line = ''
        self.content = ''
        self.line_id = 1

# new - not sure if correct
class Reader(IO):
    def __init__(self, id=2):
        super().__init__(id=id)
        self.flag = None
        self.msg = None
        self.content = None

    def reset(self):
        self.content = None
        self.flag = None
        self.msg = None


    def read_file(self, text_dir):

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
                with open(resource_path(text_dir), 'r') as f:
                    self.content = f.readlines()
                    self.flag = '1'
                    self.msg = "Text File Opened Successfully"
                f.close()
            except FileNotFoundError:
                print(text_dir + ' does not exist')
                self.flag = '0'
                return

            # for i in lines:
                # self.content += i






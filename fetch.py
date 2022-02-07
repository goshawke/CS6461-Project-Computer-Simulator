
class Fetch:

    def __init__(self, opcode, gpr, ixr, i, address):
        self.opcode = opcode
        self.pr = gpr
        self.ixr = ixr
        self.i = i
        self.address = address
        self.instruction = opcode + gpr + ixr + i + address

    def calculate_ea(self):

        if self.ixr == "00":

            # Get the value stored in address
            ea = self.address
            print(ea)

        elif self.ixr != "00":
            sumb = int(self.ixr, 2) + int(self.address, 2)
            ea = bin(sumb)[2:]
            print(ea)

        if self.i !="0":

            # ea=content_in_memory_at_ea
            print(f" Go to location {ea} and  ea= what is inside that location")




    def load_pc(self):
        print(self.instruction)

    def what_instruction(self):

        #Check if it is a load or store instruction and what type
        if self.opcode =="000001":
            print:("do ldr")

        elif self.opcode =="000010":
            print: ("do str")

        elif self.opcode == "000011":

            print: ("do lda")

        elif self.opcode =="101001":
            print: ("do ldx")

        elif self.opcode =="101010":
            print: ("do stx")

    def ldr(self):

        addresse=self.calculate_ea()



        if(self.gpr =="00"):
            #go to location EA and put what is in EA to register 0
            print ("put in gpr 0")
        elif(self.gpr =="01"):
            # go to location EA and put what is in EA to register 1
            print("put in gpr 1")

        elif (self.gpr == "10"):
            # go to location EA and put what is in EA to register 2
            print("put in gpr 2")

        elif (self.gpr == "11"):
            # go to location EA and put what is in EA to register 3
            print("put in gpr 3")



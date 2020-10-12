"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.running = True
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.SP = 7
        self.fl = 5
        self.l = 0
        self.g = 0
        self.e = 0
        self.instruction = {
            0b00000001: self.hlt,
            0b10000010: self.ldi,
            0b01000111: self.prn,
            0b10100010: self.mul,
            0b01000101: self.push,
            0b01000110: self.pop,
            0b10100000: self.add,
            0b01010000: self.call,
            0b00010001: self.ret,
            0b10100111: self.cmp,
            0b01010100: self.jmp,
            0b01010101: self.jeq,
            0b01010110: self.jne
        }

    def load(self, program):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:
        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0, 8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]
        
        with open(program) as f: 
            for line in f:
                possible_num = line[:line.find("#")]
                if possible_num == "":
                    continue # skil to next iteration of loop

                try:
                    self.ram_write(int(possible_num, 2), address)
                    address += 1

                except FileNotFoundError:
                    print(f'Error: {program} not found')


        for instruction in program:
            self.ram[address] = instruction
            address += 1
    
    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value

    def hlt(self, operand_a, operand_b):
        return(1, False)

    def ldi(self, operand_a, operand_b):
        self.reg[operand_a] = operand_b
        return(3, True)
    
    def prn(self, operand_a, operand_b):
        print(self.reg[operand_a])
        return(2, True)

    def mul(self, operand_a, operand_b):
        self.alu("MUL", operand_a, operand_b)
        return(3, True)

    def add(self, operand_a, operand_b):
        self.alu('ADD', operand_a, operand_b)
        return (3, True)

    def divide(self, operand_a, operand_b):
        self.alu('DIV', operand_a, operand_b)
        return (3, True)

    def subtract(self, operand_a, operand_b):
        self.alu('SUB', operand_a, operand_b)
        return (3, True)
    
    def push(self, operand_a, operand_b):
        self.reg[self.SP] -= 1
        self.ram[self.reg[self.SP]] = self.reg[operand_a]
        return (2, True)

    def pop(self, operand_a, operand_b):
        self.reg[operand_a] = self.ram[self.reg[self.SP]]
        self.reg[self.SP] += 1
        return (2, True)

    def call(self, operand_a, operand_b):
        self.SP -= 1
        self.ram[self.SP] = self.pc + 2
        self.pc = self.reg[operand_a]
        return (0, True)

    def ret(self, operand_a, operand_b):
        self.pc = self.ram[self.SP]
        return (0, True)
    
    def jmp(self, operand_a, operand_b):
        self.pc = self.reg[operand_a]
        return (0, True)

    def jeq(self, operand_a, operand_b):
        if self.e == 1:
            self.pc = self.reg[operand_a]
            return (0, True)
        else:
            return (2, True)

    def jne(self, operand_a, operand_b):
        if self.e == 0:
            self.pc = self.reg[operand_a]
            return (0, True)
        else:
            return(2, True)

    def cmp(self, operand_a, operand_b):
        self.alu("CMP", operand_a, operand_b)
        return (3, True)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == "DIV":
            self.reg[reg_a] /= self.reg[reg_b]
        elif op == "CMP":
            if self.reg[reg_a] == self.reg[reg_b]:
                self.e = 1
                self.l = 0
                self.g = 0
            elif self.reg[reg_a] <= self.reg[reg_b]:
                self.e = 0
                self.l = 1
                self.g = 0
            else:
                self.e = 0
                self.l = 0
                self.g = 1
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        
        while self.running:
            IR = self.ram[self.pc]

            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            try:
                operation = self.instruction[IR](operand_a, operand_b)
                self.running = operation[1]
                self.pc += operation[0]

            except:
                print(f"Unknown command: {IR}")
                sys.exit()


# // need load
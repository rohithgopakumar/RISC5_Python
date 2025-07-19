from Src.ALU_Control import *
from Src.Main_Control import * 
from Src.Instruction_Mem import *
from Src.PC import PC
from Src.ALU import *

# print(bin(ALU_Control(ALU_Main_Control(0b0110011),0b0000000,0b000)), "Add")
# print(bin(ALU_Control(ALU_Main_Control(0b0110011),0b0100000,0b000)), "Sub")
# print(bin(ALU_Control(ALU_Main_Control(0b0110011),0b0000000,0b110)), "OR")
# print(bin(ALU_Control(ALU_Main_Control(0b0110011),0b0000000,0b111)), "AND")


out = Instruction_Fetch(PC(0))

#print(out)

opcode = out[-1]
func7 = out[0]
func3 = out[3]

#print(func7,func3,opcode)
Alu_src = Main_control(opcode)[-1]

Alu_opr = ALU_Control(Alu_src,func7,func3)

Alu_out = ALU("0001","0001",Alu_opr)

print(Alu_out)

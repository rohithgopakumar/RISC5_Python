# This is a test for PC and inst mem

from Src.PC import PC
from Src.Instruction_Mem import *



# print(Instruction_Decoder(Instruction_Mem(PC(0))))

print(Instruction_Fetch(PC(0)))
print(Instruction_Fetch(PC(4)))
print(Instruction_Fetch(PC(8)))
print(Instruction_Fetch(PC(0 + 4)))     
print(Instruction_Fetch(PC(8 + 4)))
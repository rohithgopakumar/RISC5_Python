from Main_Control import *
from Instruction_Mem import *




#out = Instruction_Fetch(4)

print(Main_control(Instruction_Fetch(4)[-1]))
print(Main_control(Instruction_Fetch(8)[-1]))
print(Main_control(Instruction_Fetch(12)[-1]))
print(Main_control(Instruction_Fetch(16)[-1]))



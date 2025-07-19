from Src.Instruction_Mem import *



print(Instruction_Mem(0b0001))
print(Instruction_Mem(0b0001))
a = Instruction_Mem(0b0000)


print(a)

print("opcode", a[-7:])
print("rd", a[-12:-7])
print("func3", a[-15:-12])
print("rs1", a[-20:-15])
print("rs2", a[-25:-20])
print("func7",a[-32:-25])


# out = (Instruction_Decoder(Instruction_Mem(0)))

# print(out[0],out[1],out[2],out[3],out[4],out[5])

print(Instruction_Fetch(16))

# Idea is to return a list that is of the form [opcode,func3,func7,rd,rs2,rs1]
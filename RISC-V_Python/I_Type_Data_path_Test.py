# This is the data path for I Type instructions
from PC import *
from Instruction_Mem import *
from Register_file import *
from Main_Control import *
from ALU_Control import *
from Sign_Ext import *
from ALU_mux import *
from ALU import *
from Data_Memory import *
from WB import *
from Reg_mem_init import *
from Data_mem_init import *

# Init the reg mem

register = Reg_mem_init()
data_mem = Data_mem_init()

# Initialize the program counter
pc = PC(28)

# Instruction Decode stage
decode = Instruction_Fetch(pc)

opcode = decode[-1]
rd = decode[-2]
func3 = decode[-3]
rs1 = decode[-4]
imm12 = decode[0]

print(decode)
# print(imm12,rs1,func3,rd,opcode)

# Main Control Unit 

m_cont = Main_control(opcode)
alu_src = m_cont[0]
mem2reg = m_cont[1]
regwrite = m_cont[2]
memread = m_cont[3]
memwrite = m_cont[4]
alu_op = m_cont[-1]

#print(m_cont)

# ALU Control Unit
alu_opr = ALU_Control(alu_op, 0, func3)

#print(alu_opr)

# Register memory Reading

reg = Register_File(0,None,rs1,0,0,register)

Reg1 = reg
#print(reg)

# Get the address from the ALU
Alu_out = ALU(Reg1,ALU_mux(None,imm12,alu_src),alu_opr) 
print(Alu_out)

# Use the Data Memory

Data_out = Data_Memory(Alu_out, 0, memwrite, memread, data_mem)

print(Data_out)

# Write back stage 

Wb = WB(Alu_out, Data_out,mem2reg)

print(Wb)

# Write back into the register 

print(Register_File(rd,None,rs1,Wb,regwrite,register))

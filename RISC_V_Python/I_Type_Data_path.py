# This is the data path for I Type instructions
from Test.Src.PC import PC
from Test.Src.Instruction_Mem import *
from Test.Src.Register_file import *
from Test.Src.Main_Control import *
from Test.Src.ALU_Control import *
from Test.Src.Sign_Ext import *
from Test.Src.ALU_mux import *
from Test.Src.ALU import *
from Test.Src.Data_Memory import *
from Test.Src.WB import *
from Test.Src.Reg_mem_init import *
from Test.Src.Data_mem_init import *


def I_type(pc, register, data_mem):
 
# Initialize the register
 register_mem = register

# Initialize the program counter
 pc = PC(pc)

# Instruction Decode stage
 decode = Instruction_Fetch(pc)

 opcode = decode[-1]
 rd = decode[-2]
 func3 = decode[-3]
 rs1 = decode[-4]
 imm12 = decode[0]

# Main Control Unit 

 m_cont = Main_control(opcode)
 alu_src = m_cont[0]
 mem2reg = m_cont[1]
 regwrite = m_cont[2]
 memread = m_cont[3]
 memwrite = m_cont[4]
 alu_op = m_cont[-1]

# ALU Control Unit
 alu_opr = ALU_Control(alu_op, 0, func3)

# Register memory Reading

 reg = Register_File(0,None,rs1,0,0,register_mem)

# Get the address from the ALU
 Alu_out = ALU(reg,ALU_mux(None,imm12,alu_src),alu_opr) 
 
# Use the Data Memory

 Data_out = Data_Memory(Alu_out, 0, memwrite, memread, data_mem)

# Write back stage 

 Wb = WB(Alu_out, Data_out,mem2reg)

# Write back into the register 

 register_mem = Register_File(rd,None,rs1,Wb,regwrite,register)

 pc = pc + 4

 return register_mem , data_mem , pc

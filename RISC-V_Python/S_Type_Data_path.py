# This is the data path for the store instruction 
from PC import *
from Instruction_Mem import *
from Main_Control import *
from Register_file import *
from ALU_Control import *
from ALU_mux import *
from ALU import *
from Data_Memory import *
from WB import *
from Reg_mem_init import *
from Data_mem_init import *
from Sign_Ext import *


def S_type(pc, register, data_mem):

# Decode the instruction 

 decode = Instruction_Fetch(pc)

 #print(decode)
 opcode = decode[-1]
 func3 = decode[-3]
 rs1 = decode[2]
 rs2 = decode[1]
 imm12 = decode[0] + decode[-2]

 #print(imm12, rs2, rs1, func3, opcode)

# Main control unit 

 m_cont = Main_control(opcode)

 alu_src = m_cont[0]
 mem2reg = m_cont[1]
 regwrite = m_cont[2]
 memread = m_cont[3]
 memwrite = m_cont[4]
 alu_op = m_cont[-1]

 #print(m_cont)

# ALU Control unit 

 alu_opr = ALU_Control(alu_op, 0, func3)

 #print(alu_opr)

# Read from the Register mem

 register_mem = Register_File(0,rs2,rs1,0,regwrite,register)

 Reg1 = register_mem[0]
 Reg2 = register_mem[1]

 #print(Reg1,Reg2)

# Alu Processing 

 Alu_out = ALU(Reg1, ALU_mux(Reg2,Sign_Ext(imm12),alu_src), alu_opr)

 #print(Alu_out)

# Memory access (Write operation)

 Data_mem = Data_Memory(Alu_out, Reg2, memwrite, memread, data_mem)

 #print(Data_mem)
 pc = pc+4

 return register , Data_mem , pc
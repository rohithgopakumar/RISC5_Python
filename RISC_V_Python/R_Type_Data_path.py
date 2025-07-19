from Test.Src.PC import PC
from Test.Src.Instruction_Mem import *
from Test.Src.Register_file import *
from Test.Src.Main_Control import *
from Test.Src.ALU_Control import *
from Test.Src.ALU import *
from Test.Src.ALU_mux import *
from Test.Src.WB import *
from Test.Src.Reg_mem_init import *


# Start the program counter

def R_Type(pc, register, data_mem):
 
 register_mem = register
## Pc 
 pc = PC(pc)

## Intruction Fetch and Decode

 decode = Instruction_Fetch(pc)

 opcode = decode[-1]
 rd = decode[-2]
 func3 = decode[-3]
 rs1 = decode[-4]
 rs2 = decode[-5]
 func7 = decode[-6]
 #print(decode)

# Main Control unit

 m_cont = Main_control(opcode)
 alu_op = m_cont[-1]
 regwrite = m_cont[2]
 alu_src = m_cont[0]
 mem2reg = m_cont[1]

 #print(m_cont)

# AlU Control
 alu_opr = ALU_Control(alu_op,func7,func3)

# Register Reading File 

 reg = Register_File(rd,rs2,rs1,0,0,register_mem)

 #print(reg)
 reg1 = reg[0]
 reg2 = reg[1]

# Using the ALU 

 ALU_out = ALU(reg1,ALU_mux(reg2,0,alu_src),alu_opr)

 #print(ALU_out)

# Write back into the reg

 register_mem = Register_File(rd,rs2,rs1,WB(ALU_out,35,mem2reg),regwrite,register_mem)
 
 pc = pc + 4

 return register_mem , data_mem, pc
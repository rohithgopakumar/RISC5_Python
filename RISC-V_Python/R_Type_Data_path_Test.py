from PC import *
from Instruction_Mem import *
from Register_file import *
from Main_Control import *
from ALU_Control import *
from ALU import *
from ALU_mux import *
from WB import *
from Reg_mem_init import *

#Initialize the register mem

register_mem = Reg_mem_init()

# Start the program counter

pc = 0
while pc < 21:

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
 print("--------------------------------------------------------------------------------------------")
 print(register_mem)
 print("--------------------------------------------------------------------------------------------")
 
 pc = pc + 4

 #print(PC(pc))
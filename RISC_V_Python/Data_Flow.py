# This is a test to Show the proof of concept of the processor to achieve R-Type, I-Type and S-Type instructions
from I_Type_Data_path import *
from R_Type_Data_path import *
from S_Type_Data_path import *
from Test.Src.Reg_mem_init import *
from Test.Src.Data_mem_init import *
from Test.Src.PC import PC
import copy
# Initialize the reg and data mem

register_init = Reg_mem_init()
data_mem_init = Data_mem_init()

# Copying the lists to preserve the initialized one
register = copy.deepcopy(register_init)
data_mem = copy.deepcopy(data_mem_init)

# Init the pc
pc = PC(0)

# out = [reg_mem, data_mem, pc_next]

out0 = R_Type(pc, register, data_mem)
out1 = R_Type(out0[2], out0[0], out0[1])         # I0 = add r10,r2,r3  
out2 = R_Type(out1[2], out1[0], out1[1])         # I1 = add r15,r5,r6
out3 = R_Type(out2[2], out2[0], out2[1])         # I2 = add r20,r10,r15
out3 = R_Type(out2[2], out2[0], out2[1])         # I3 = and r30,r20,r0
out4 = R_Type(out3[2], out3[0], out3[1])         # I4 = or r18,r15,r15
out5 = R_Type(out4[2], out4[0], out4[1])         # I5 = sub r21,r30,r18
out6 = I_type(out5[2], out5[0], out5[1])         # I6 = lw r10, 4(r0)
out7 = I_type(out6[2], out6[0], out6[1])         # I7 = lw r30, 8(r4)
out8 = S_type(out7[2], out7[0], out7[1])         # I8 = sw r30, 8(r12)
out9 = S_type(out8[2], out8[0], out8[1])         # I9 = sw r12, 12(r12)



print(" The initial reg mem is", register_init)
print("------------------------------------------------------------------------------------------------------------------------")
print(" The reg mem is", out9[0])
print("------------------------------------------------------------------------------------------------------------------------")
print(" The iniial data mem is", data_mem_init)
print("------------------------------------------------------------------------------------------------------------------------")
print(" The data mem is", out9[1])



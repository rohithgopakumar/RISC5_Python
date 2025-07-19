# This is the mux that chooses between Reg2 and imm32



def ALU_mux(reg2,imm32,alu_src):

    if alu_src == 1:
        return imm32
    elif alu_src == 0:
        return reg2


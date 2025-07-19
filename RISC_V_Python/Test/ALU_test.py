from Src.ALU import ALU

opr1 = 0b0001
opr2 = 0b0010


print(ALU(opr1,opr2,0b0010), "sum case")
print(ALU(opr1,opr2,0b0110), "sub case")
print(ALU(opr1,opr2,0b0001), "OR case")
print(ALU(opr1,opr2,0b0000), "AND case")

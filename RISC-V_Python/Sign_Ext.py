# This is to sign extend the Imm12 bit to 32


def Sign_Ext(imm12):
 imm12 = int(imm12,2)
 return (format(imm12,'032b'))
 




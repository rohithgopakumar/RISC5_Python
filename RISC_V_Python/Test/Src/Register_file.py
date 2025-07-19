# This is the register file where the registers sit


def Register_File(ws,rs2,rs1,wd,Regwrite,register_mem):

    for i in range(len(register_mem)):
        if register_mem[i][0] == rs1:
            Reg1 = register_mem[i][1]
        
        if register_mem[i][0] == rs2:
            Reg2 = register_mem[i][1]
        
        if Regwrite == 1 and register_mem[i][0] == ws: 
            register_mem[i][1] = int(wd,2)
            
            break

 
    if Regwrite != 1 and rs2 != None:
      return ([format(Reg1, '032b'),format(Reg2, '032b')])     
    elif Regwrite == 1:
      return register_mem
    elif Regwrite != 1 and rs2 == None:
       return (format(Reg1, '032b')) 

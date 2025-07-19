# This is the main control unit 



def Main_control(opcode):

    if opcode == '0110011':
        return [0,0,1,0,0,0,"{:02b}".format(2)]                         #|alusrc|mem2reg|regwrite|memread|memwrite|branch|aluop|
                                                                        #|0     |0      |1       |0      |0       |0     |10   |   R-Type
    elif opcode == '0000011':                                           #|1     |1      |1       |1      |0       |0     |00   |   I-Type
        return [1,1,1,1,0,0,"{:02b}".format(00)]                        #|1     |0      |0       |0      |1       |0     |00   |   S-Type
    
    elif opcode == '0100011':
        return [1,0,0,0,1,0,"{:02b}".format(00)]
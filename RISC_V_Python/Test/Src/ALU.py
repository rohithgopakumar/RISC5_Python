# This is the ALU Function

def ALU(operand1,operand2,ALUoper):
    opr1 = operand1
    opr2 = operand2

    match ALUoper:
        case '0000':
            return (bin(int(opr1, 2) & int(opr2, 2)))   # This is for AND 
        case '0001':
            return (bin(int(opr1, 2) | int(opr2, 2)))   # This is for OR
        case '0010':
            return (bin(int(opr1, 2) + int(opr2, 2)))   # This is for ADD
        case '0110':
            return (bin(int(opr1, 2) - int(opr2, 2)))  # This is for SUB
        
    return None
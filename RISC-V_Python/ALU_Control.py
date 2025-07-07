# This is to generate the ALU oper


def ALU_Control(ALUop,func7,func3):

    if ALUop == '10':
        if func7 == '0000000' and func3 == '111':
            return '0000'                                           #   0000 --> AND
        elif func7 == '0000000' and func3 == '110':                 #   0001 --> OR
            return '0001'                                           #   0010 --> ADD
        elif func7 == '0000000' and func3 == '000':                 #   0110 --> SUB
            return '0010'
        elif func7 == '0100000' and func3 == '000':
            return '0110'
    if ALUop == '00':
        return '0010' 


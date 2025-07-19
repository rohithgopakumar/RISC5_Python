# This is the instruction memory 



def Instruction_Mem(PC):                                         # This is the inst memory. it stores the information data

    Inst = {            
           0 : 0b00000000001000011000010100110011,               # I0 = add r10,r2,r3  
           4 : 0b00000000010100110000011110110011,               # I1 = add r15,r5,r6
           8 : 0b00000000101001111000101000110011,               # I2 = add r20,r10,r15
          12 : 0b00000001010000000111111100110011,               # I3 = and r30,r20,r0
          16 : 0b00000000111101111110100100110011,               # I4 = or r18,r15,r15
          20 : 0b01000001001011110000101010110011,               # I5 = sub r21,r30,r18
          24 : 0b00000000010000000010010100000011,               # I6 = lw r10, 4(r0) 
          28 : 0b00000000100000100010111100000011,               # I7 = lw r30, 8(r4)
          32 : 0b00000001111001100010010000100011,               # I8 = sw r30, 8(r12)
          36 : 0b00000000110001100010011000100011                # I9 = sw r12, 12(r12)
    }

    for pc,inst in Inst.items():
        if pc == PC:
         
         return ("{:032b}".format(inst))
    

def Instruction_Decoder(Inst):
   
   opcode = Inst[-7:]

   if opcode == '0110011':                                  # R-Type instruction
                                                            # [func7][rs2][rs1][func3][rd][opcode]
    rd = Inst[-12:-7]
    func3 = Inst[-15:-12]
    rs1 = Inst[-20:-15]
    rs2 = Inst[-25:-20]
    func7 = Inst[-32:-25]
    return [func7,rs2,rs1,func3,rd,opcode]
   
   if opcode == '0000011':                                  # I-Type instruction
                                                            # [imm12][rs1][func3][rd][opcode]
      imm12 = Inst[-32:-20]
      rs1 = Inst[-20:-15]
      func3 = Inst[-15:-12]
      rd = Inst[-12:-7]

      return [imm12,rs1,func3,rd,opcode]
 
   if opcode == '0100011':                                  # S-Type instruction
                                                            # [imm7][rs2][rs1][func3][imm5][opcode]
      imm7 = Inst[-32:-25]
      rs2 = Inst[-25:-20]
      rs1 = Inst[-20:-15]
      func3 = Inst[-15:-12]
      imm5 = Inst[-12:-7]

      return ([imm7,rs2,rs1,func3,imm5,opcode])

def Instruction_Fetch(PC):                                  # Made into one function for easier look
   
   return (Instruction_Decoder(Instruction_Mem(PC)))
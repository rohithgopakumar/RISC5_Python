# This is the write back stage ( it is a simple 2:1 mux)

def WB(ALUout,DataOut,MemtoReg):
  
  if MemtoReg == 1:
    return DataOut
  elif MemtoReg == 0: 
    return ALUout
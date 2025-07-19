# This is the Data memory of the processor



def Data_Memory(Addr, Datain, Memwrite, Memread, Data_mem):


 for i in range(len(Data_mem)):

     if Data_mem[i][0] == int(Addr,2) and Memread == 1:
          #print("-----------------------s")
          #print(Data_mem[i][0], Addr)
          return Data_mem[i][1]
     
     #print( Data_mem[i][0] , int(Addr,2))
     if Memwrite == 1 and Data_mem[i][0] == int(Addr,2): 
        Data_mem[i][1] = Datain
        return Data_mem

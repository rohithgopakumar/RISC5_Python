from Src.Data_Memory import *
from Src.Data_mem_init import *


datamem = Data_mem_init()



Out = Data_Memory('00000000000000000000000000000000',0,0,1, datamem)

print(type(Out))

Out1 = Data_Memory('00000000000000000000000000000000','00000000000000000000000000000001',1,0, datamem)

print(Out1)
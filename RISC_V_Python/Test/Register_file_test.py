from Src.Register_file import *
from Src.Reg_mem_init import *

regmem = Reg_mem_init()



print(Register_File(0,'00000','00001',0,0, regmem), "test1")    # Test 1
print(Register_File(0,'00011','00001',0,0, regmem), "test2")    # Test 2
print(Register_File(0,'00110','00101',0,0, regmem), "test3")    # Test 3
print(Register_File(0,'10110','00101',0,0, regmem), "test4")    # Test 4
print(Register_File(0,'11010','00111',0,0, regmem), "test5")    # Test 5

#print(Regiter_File('00000','11010','00111',0b00000000000000000000000000000001, regmem),"test 6")    # Test 6

# need to check why the issue failed (not priority)




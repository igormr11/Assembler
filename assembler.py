import math
inst_set = ["ADD","SUB","ADDi","SUBi","MUL2","DIV2","CLR","RST","MOV","JMP","JZ","INC","DEC","LOAD","STORE","PRN"]
registers = ['A','B','C','D']
G1 = ["MUL2","DIV2","CLR","INC","DEC"]
G2 = ["ADD","SUB","MOV"]
G3 = ["ADDi","SUBi","LOAD"]
G4 = ["JMP","JZ"]


input = open("assembly.txt",'r')
output = open("machine.txt",'w')
for elemento in input:
     elemento = elemento.replace("\n","")
     elemento = elemento.split(" ")
     elemento = ', '.join(elemento)
     elemento = elemento.replace(" ","")
     elemento = elemento.split(",")
     print(elemento)

     l = len(elemento)
     comando = elemento[0]
     indexI = inst_set.index(comando)

     if (comando == "PRN"):
         indexA = registers.index(elemento[1])
         output.write("{0:04b}".format(indexI))
         output.write("{0:04b}".format(0))
         output.write("{0:02b}".format(indexA))
     if (comando == "RST"):
         output.write("{0:04b}".format(indexI))
         output.write("{0:06b}".format(0))
     elif (comando == "STORE"):
         indexA = registers.index(elemento[1])
         output.write("{0:04b}".format(indexI))
         output.write("{0:04b}".format(int(elemento[2])))
         output.write("{0:02b}".format(indexA))
     elif (comando in G1):
          indexA = registers.index(elemento[1]) #index for register 1
          output.write("{0:04b}".format(indexI))
          output.write("{0:02b}".format(indexA))
          output.write("{0:02b}".format(indexA))
          output.write("{0:02b}".format(0))
     elif (comando in G2):
          indexA = registers.index(elemento[1])
          indexB = registers.index(elemento[2])  # index for register 1
          output.write("{0:04b}".format(indexI))
          output.write("{0:02b}".format(indexA))
          output.write("{0:02b}".format(indexA))
          output.write("{0:02b}".format(indexB))
     elif (comando in G3):
          indexA = registers.index(elemento[1])  # index for register 1
          output.write("{0:04b}".format(indexI))
          output.write("{0:02b}".format(indexA))
          output.write("{0:04b}".format(int(elemento[2])))
     elif (comando in G4):
          output.write(("{0:04b}".format(indexI)))
          output.write("{0:06b}".format(int(elemento[1])))

     output.write("\n")

input.close()
output.close()

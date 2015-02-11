'''
This is a converter for depth profiles created using RUMP the genplot based Rutherford Backscattering Spectrometry Analysis tool.
The discrete layers are treated as steps with a width defined by dx.
This program doubles the number of lines of code for a depth profile created using the WRITEPRO command in the SIM Enviroment
and allows convienient plotting with the Graphics Layout Engine GLE or any other plotting tool that will look at a comma separated table.
'''
from os import listdir
print "This is the depth profile converter for XRUMP.\n  It was created by Robert Balsano in February 2015. \n It is designed to be used with xrump and the Graphics Layout Engine GLE."

filepath1= raw_input("Please enter the full location of the RUMP profile you would like to convert")
filepath3= raw_input("Please enter the full location of the CSV file you would like to create")
file1 = open(filepath1,"r")
file3 = open(filepath3,"w")
linesave = file1.read()
theory = []
line = ""
for char in linesave:
    if char !="\n":
        line += char
    if char == "\n":
        theory.append(line)
        line = ""

file1.close

#file1.close()

file3.write("!"+ theory[0]+ "\n")
for i in range(1, len(theory)-1):
    #file3.write(theory[i]+ "\n")
    spacecounter = 0
    collum = []
    element = ""
    for char in theory[i]:
        if spacecounter == 0 and (char == " " or char == "\t"):
                collum.append(element)
                element = ""
                #file3.write(", ")
        if char != " " and char!= "\t":
            spacecounter = 0
            #capture the cell
            element += char
        else:
            spacecounter += 1
    collum.append(element)
    element = ""            
    for elt in collum:
        file3.write(elt + ", ")
    file3.write("\n")
    for i in range(0, len(collum)):
        if i < 1 or i>1:
            file3.write(collum[i] + ", ")
        if i == 1:
            file3.write(str(float(collum[1])+float(collum[3])) + ", ")
    file3.write("\n")
#print len(theory)
file3.close()
input("conversion has completed press enter to exit")

from os import listdir
print "This is a simple utility designed to combine RBS theory spectrum and RBS data spectrum into a single file \n It takes files generated using the command WRASCII in XRUMP/RUMP. /n It finds the energy conversion factor from the theory file and uses that for bothe spectrum. \n make sure the calibration is the same for both files \n \n"
filepath1=raw_input("Please enter the full file path of the theory spectrum file:")
filepath2=raw_input("Please enter the full file path of the data spectrum file:")
filepath3=raw_input("Please enter the full file path of the destination spectrum file:")
file1 = open(filepath1,"r")
file2 = open(filepath2,"r")
file3 = open(filepath3,"w")
#read all the lines until you get to the conversion
#then save the conversion factors
# add a commented key an ! would work fine
#then write the channel umbers in collum 1 and the energies in collum 2
#while writing the theory numbers in collum three and the experimental in 4
#for line in file1:
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
linesave = file2.read()
data = []
line = ""
for char in linesave:
    if char !="\n":
        line += char
    if char == "\n":
        data.append(line)
        line = ""

slope = float(theory[5][11:19])
intercept = float(theory[5][20:29])
#file1.close()
file2.close()
file3.write("!channel no, energy kev, theory counts, experiment counts \n")
chan = 0
for i in range(12, len(theory)-1):
    file3.write(str(chan) + ", " + str(slope*chan + intercept) + ", " + theory[i] + ", " + data[i] + "\n")
    chan+=1
#print len(theory)
file3.close()

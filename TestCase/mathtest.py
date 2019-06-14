import os,sys
sys.path.insert(0,"C:\Users\saursing\Documents\Sample_framework\Libs")

from mathoperation import airthmatic as at
import ConfigParser
#print at.add(7,8) #if you want to run directly.


##########################################3
#Using config file use config parser in input folder

config = ConfigParser.ConfigParser()
config.read("C:\\Users\\saursing\\Documents\\Sample_framework\\Input\\input.ini")
#to see how many section is availble
config.sections()
#to get value from section
x = config.get("Others","x")
y = config.get("Others","y")
obj = at()

print obj.add(int(x),int(y))




#to use result folder write the same output to some file:

with open("C:\\Users\\saursing\\Documents\\Sample_framework\\Result\\output.txt",'w') as wr:
    wr.write("output is: "+str(obj.add(int(x),int(y))))
    

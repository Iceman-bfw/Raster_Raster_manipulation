import numpy as np
import os


def read_header(filein):
    f = open(filein,'r')
    #Header =[]
    Header = ''
    for i in range(6):
        header = f.readline()
        Header=Header + header 
        #Header.append(header)
    nodata = int(header.split(' ')[-1])
    #Header[-1]= "NODATA_value -9999"
    #header.append( str(f.readlines(i)[0:6]))  #header + (str(f.readlines(i))[2:-4]) + '\n'
    f.close()
    print(header)
    
    
if __name__ == "__main__":
    filein = "/home/damboise/Documents/text_replace/init.asc"
    nodata = int(header.split(' ')[-1])
    #header = "ncols         620\nnrows         412\nxllcenter     61520\nyllcenter     254585\ncellsize      5\nNODATA_value  -9999"
    raster = np.loadtxt(filein, dtype= 'int' ,skiprows=6)
    raster[raster==nodata]=-9999
    #raster[raster>1]= int(0)
    raster[raster==int(2)]= int(0)
    raster[raster==int(3)]= int(0)
    #for r in (("2", "0"), ("3", "0"), (nan_value_string[1], "-9999")):
    #newraster1 = raster[raster>1]=0  
    #save_path = "/home/simulation/avalanche_simulation/01_simulation/{}-Lawine/psamUH/qgis/".format(Lawine)
    np.savetxt('class_1.txt', raster, fmt="%d", header=Header, comments='')
       
"""
f = open(filein,'r')
filedata = f.readlines()
f.close()

header = ("ncols", "nrows", "xllcorner", "yllcorner", "cellsize")

f1 = open("release_class_1.asc",'a')
f2 = open("release_class_2.asc",'a')
f3 = open("release_class_3.asc",'a')

for line in filedata:
    if any(meta_string in line for meta_string in header):
        f1.write(line)
        f2.write(line)
        f3.write(line)
        continue
    elif "NODATA_value" in line:
        f1.write("NODATA_value -9999")
        f2.write("NODATA_value -9999")
        f3.write("NODATA_value -9999")
        nan_value_string = line.split(" ")
        #nan_value = float(nan_value_string[1])
        continue
    else:
        for r in (("2", "0"), ("3", "0"), (nan_value_string[1], "-9999")):
            line_1 = line.replace(*r)
            f1.write(line_1)
        for r in (("1", "0"), ("3", "0"), (nan_value_string[1], "0")):
            line_2 = line.replace(*r)
            f2.write(line_2)
        for r in (("1", "0"), ("2", "0"), (nan_value_string[1], "0")):
            line_3 = line.replace(*r)
            f3.write(line_3)


f1.close()
f2.close()
f3.close()
"""
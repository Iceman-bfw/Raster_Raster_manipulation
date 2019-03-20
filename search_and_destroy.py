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
    return  Header


if __name__ == "__main__":
    filein = "/home/damboise/Documents/text_replace/init.asc"
    header = read_header(filein)
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

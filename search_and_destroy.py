import numpy as np
import os


def read_header(filein):
    f = open(filein, 'r')
    Header = ''
    for i in range(6):
        header = f.readline()
        Header = Header + header

    nodata = int(header.split(' ')[-1])
    f.close()
    return Header


if __name__ == "__main__":
    filein = "/home/damboise/Documents/text_replace/init.asc"
    header = read_header(filein)
    nodata = int(header.split(' ')[-1])
    raster = np.loadtxt(filein, dtype='int', skiprows=6)
    # change the raster
    raster[raster == nodata] = -9999
    raster[raster == int(2)] = int(0)
    raster[raster == int(3)] = int(0)
    # save file
    np.savetxt('class_1.txt', raster, fmt="%d", header=header, comments='')

import numpy as np
import sys

def read_header(filein):
    with open(filein, 'r') as f:
        Header = ''
        for i in range(6):
            header = f.readline()
            Header = Header + header

    # nodata = int(header.split(' ')[-1])
    return Header

def class_builder(raster_changed, size_class):
    #raster_changed[raster > size_class] = int(0)
    #raster_changed[raster < size_class] = int(0)
    raster_changed[raster_changed != size_class] = int(0)
    return raster_changed

if __name__ == "__main__":
    filein = sys.argv[1]
    header = read_header(filein)
    raster = np.loadtxt(filein, skiprows=6)

    # make release classes
    for i in range(1,14,1):
        raster = np.loadtxt(filein, skiprows=6)
        ras = class_builder(raster, i)
        np.savetxt('release_class_%s.asc' %(str(i),), ras, fmt="%d", header=header, comments='')

    

# This python code will open up a dhm raster file read and copy the header and
# make an new empty raster file of the same shape
# This is useful for empty infrastructure layers for Gravipro model
import numpy as np
from search_and_destroy import read_header

if __name__ == "__main__":
    filein = "/home/damboise/Documents/text_replace/init.asc"
    header = read_header(filein)
    nodata = int(header.split(' ')[-1])
    raster = np.loadtxt(filein, dtype='int', skiprows=6)
    raster[raster != 0] = int(0)
    np.savetxt('empty_infra.txt', raster, fmt="%d", header=header, comments='')

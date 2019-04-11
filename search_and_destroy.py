import numpy as np


def read_header(filein):
    with open(filein, 'r') as f:
        Header = ''
        for i in range(6):
            header = f.readline()
            Header = Header + header

    # nodata = int(header.split(' ')[-1])
    return Header


if __name__ == "__main__":
    #filein = "/home/damboise/Documents/text_replace/test_dhm_release_s_.asc"
    filein = "/home/damboise/Documents/text_replace/40m_slope_45obs_hemi_rel.asc"
    header = read_header(filein)
    # nodata = float(int(header.split(' ')[-1]))
    raster = np.loadtxt(filein,  skiprows=6)
    # change the raster
    # raster[raster == nodata] = -9999
    raster[raster >= 1] = int(1)
    raster[raster < 1] = int(0)
    # save file
    np.savetxt('class_1.asc', raster, fmt="%d", header=header, comments='')

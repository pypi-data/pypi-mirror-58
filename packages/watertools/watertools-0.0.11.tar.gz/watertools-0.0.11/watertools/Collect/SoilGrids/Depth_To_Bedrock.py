# -*- coding: utf-8 -*-
"""
Authors: Tim Hessels
Module: Collect/SoilGrids
"""
import os
from watertools.Collect.SoilGrids.DataAccess import DownloadData
import sys


def main(Dir, latlim, lonlim, Waitbar = 1):
    """
    Downloads SoilGrids data from ftp://ftp.soilgrids.org/data/recent/

    The following keyword arguments are needed:
    Dir -- 'C:/file/to/path/'
    latlim -- [ymin, ymax]
    lonlim -- [xmin, xmax] 
    Waitbar -- '1' if you want a waitbar (Default = 1)
    """

    # Create directory if not exists for the output
    output_folder = os.path.join(Dir, 'SoilGrids', 'Depth_To_Bedrock')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the output map and create this if not exists
    nameEnd = os.path.join(output_folder, 'DepthToBedrock_SoilGridsc_cm.tif')  

    if not os.path.exists(nameEnd):

        # Create Waitbar
        if Waitbar == 1:
            print('\nDownload Depth to bedrock soil map from SoilGrids.org')
            import watertools.Functions.Random.WaitbarConsole as WaitbarConsole
            total_amount = 1
            amount = 0
            WaitbarConsole.printWaitBar(amount, total_amount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # Download and process the data
        DownloadData(output_folder, latlim, lonlim, "BDRICM")

        if Waitbar == 1:
            amount = 1
            WaitbarConsole.printWaitBar(amount, total_amount, prefix = 'Progress:', suffix = 'Complete', length = 50)

    else:
        if Waitbar == 1:
            print("\nDepth to Bedrock soil map from SoilGrids.org already exists in output folder")

if __name__ == '__main__':
    main(sys.argv)


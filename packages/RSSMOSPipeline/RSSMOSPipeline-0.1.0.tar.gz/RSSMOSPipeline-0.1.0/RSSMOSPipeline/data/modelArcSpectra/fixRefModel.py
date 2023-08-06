#!/usr/bin/env python

"""

Plots a given arc reference model, labelling the identified features.

"""

import os
import sys
import pyfits
import atpy
#from astLib import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy import interpolate
from scipy import optimize
import argparse
import pickle
import IPython
#plt.matplotlib.interactive(True)

#-------------------------------------------------------------------------------------------------------------
def parseApproxArcCoordsFile(fileName):
    """Returns a dictionary indexed by x coord of line wavelengths in Angstroms.
    
    """
    
    inFile=open(fileName, "r")
    lines=inFile.readlines()
    inFile.close()
    
    coordsDict={}
    for line in lines:
        if len(line) > 3 and line[0] != "#":
            bits=line.split()
            coordsDict[int(bits[1])]=float(bits[0])
    
    return coordsDict

#-------------------------------------------------------------------------------------------------------------
def detectLines(data, sigmaCut = 3.0, thresholdSigma = 2.0, featureMinPix = 5):
    """Detect lines in a 2d (or 1d) arc spectrum. If 2d, uses the central row of the 2d spectrum only.
    
    Returns: featureTable, segmentationMap
    
    NOTE: this should match that in rss_mos_reducer.py - we should make a module
    
    """
    
    # Detect arc lines
    mean=0
    sigma=1e6
    for i in range(20):
        nonZeroMask=np.not_equal(data, 0)
        mask=np.less(abs(data-mean), sigmaCut*sigma)
        mask=np.logical_and(nonZeroMask, mask)
        mean=np.mean(data[mask])
        sigma=np.std(data[mask])
    detectionThreshold=thresholdSigma*sigma
    mask=np.greater(data-mean, detectionThreshold)

    # Get feature positions, number of pixels etc.
    # Find features in 2d, match to wavelength coord in centre row
    segmentationMap, numObjects=ndimage.label(mask)
    sigPixMask=np.equal(mask, 1)
    objIDs=np.unique(segmentationMap)
    objNumPix=ndimage.sum(sigPixMask, labels = segmentationMap, index = objIDs)
    if data.ndim == 2:
        objPositions_centreRow=ndimage.center_of_mass(data[data.shape[0]/2], labels = segmentationMap, index = objIDs)
    elif data.ndim == 1:
        # ndmage.centre_of_mass can be led astray... just use local maximum
        #objPositions_centreRow=ndimage.center_of_mass(data, labels = segmentationMap, index = objIDs)
        objPositions_centreRow=ndimage.maximum_position(data, labels = segmentationMap, index = objIDs)
        objAmplitudes_centreRow=ndimage.maximum(data, labels = segmentationMap, index = objIDs)

    objPositions_centreRow=np.array(objPositions_centreRow).flatten()
    objAmplitudes_centreRow=np.array(objAmplitudes_centreRow).flatten()
    minPixMask=np.greater(objNumPix, featureMinPix)
    featureTable=atpy.Table()
    featureTable.add_column('id', objIDs[minPixMask])
    featureTable.add_column('x_centreRow', objPositions_centreRow[minPixMask])
    if data.ndim == 2:
        featureTable.add_column('y_centreRow', [data.shape[0]/2]*len(featureTable))
        featureTable.add_column('amplitude', data[data.shape[0]/2, np.array(np.round(featureTable['x_centreRow']), dtype = int)])
    elif data.ndim == 1:
        featureTable.add_column('amplitude', objAmplitudes_centreRow[minPixMask])

    # Sanity check plot
    #plt.matplotlib.interactive(True)
    #plt.figure(figsize=(12, 8))
    #plt.plot(data, 'k-')
    #plt.plot(featureTable['x_centreRow'], featureTable['amplitude'], 'bo')
    #for row in featureTable:
        #plt.text(row['x_centreRow'], row['amplitude'], "line")
    #plt.xlabel("x")
    #plt.ylabel("Relative Flux")
    
    return featureTable, segmentationMap

#-------------------------------------------------------------------------------------------------------------
def tagWavelengthFeatures(featureTable, approxCoordsDict, maxDiffPix = 10):
    """This adds a wavelength column to featureTable, tagging features which are nearest in x-coord to the 
    contents of features in approxCoordsDict. This will only work on the reference arc spectrum.
    
    approxCoordsDict needs to be accurate at the level of 5 pixels
    
    Removes features from featureTable which are not tagged with wavelengths.
    
    Returns featureTable
    
    """

    # If we don't use maxDiffPix constraint, sometimes we can overwrite a correct line id with a wrong one
    # (this would happen if an undetected line had an entry for a wavelength)
    featureTable.add_column('wavelength', np.zeros(len(featureTable)))
    for x in approxCoordsDict.keys():
        wavelength=approxCoordsDict[x]
        diff=abs(x-featureTable['x_centreRow'])
        if diff.min() < maxDiffPix:
            rowNumber=np.argmin(diff)
            featureTable['wavelength'][rowNumber]=wavelength
    
    featureTable=featureTable.where(featureTable['wavelength'] != 0)
    
    return featureTable

#-------------------------------------------------------------------------------------------------------------
def makeModelArcSpectrum(data, approxCoordsDict, outFileName, yRow, sigmaCut = 3.0, thresholdSigma = 5.0, 
                         featureMinPix = 30):
    """Make reference model arc spectrum. This has wavelengths of features identified in a table. We also
    save the middle row of the spectrum.
    
    """
    
    # Detect and tag features with known wavelengths in reference spectrum
    featureTable, segMap=detectLines(data)
    featureTable=tagWavelengthFeatures(featureTable, approxCoordsDict)
    data_centreRow=data[yRow]
    
    # Save reference model as a pickled dictionary
    refModelDict={'featureTable': featureTable, 'arc_centreRow': data_centreRow}
    pickleFile=file(outFileName, "wb")
    pickler=pickle.Pickler(pickleFile)
    pickler.dump(refModelDict)
    pickleFile.close()
    
#-------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    parser = argparse.ArgumentParser("inspectRefModel.py")
    parser.add_argument("refModelFileName", help="The name of the RefModel_*.pickle file to inspect.")

    args = parser.parse_args()

    modelFileName=args.refModelFileName
    
    # Load reference model
    pickleFile=file(modelFileName, "rb")
    unpickler=pickle.Unpickler(pickleFile)
    refModelDict=unpickler.load()
    pickleFile.close()
    
    # Refit it
    arcData=refModelDict['arc_centreRow']
    coordsFileName=modelFileName.replace("RefModel_", "").replace(".pickle", ".txt")
    approxCoordsDict=parseApproxArcCoordsFile(coordsFileName)
    featureTable, segMap=detectLines(arcData)
    featureTable=tagWavelengthFeatures(featureTable, approxCoordsDict)
    data_centreRow=arcData#data[yRow]    
    refModelDict={'featureTable': featureTable, 'arc_centreRow': data_centreRow}

    # Test refitted model...
    print("Inspect plot windows - close all when done. You will then be asked if you want to update %s." % (modelFileName))
    arcData=refModelDict['arc_centreRow']
    xs=refModelDict['featureTable']['x_centreRow']
    wavelengths=refModelDict['featureTable']['wavelength']
    arcFeatureTable=refModelDict['featureTable']

    # Pixel space - is it tagged correctly?
    #plt.matplotlib.interactive(True)
    plt.figure(figsize=(12, 8))
    plt.plot(arcData, 'k-')
    plt.plot(arcFeatureTable['x_centreRow'], arcFeatureTable['amplitude'], 'bo')
    for row in arcFeatureTable:
        plt.text(row['x_centreRow'], row['amplitude'], row['wavelength'])
    plt.xlabel("x (pixels)")
    plt.ylabel("Relative Flux")
    plt.title("Features tagged")
    
    # Fit the wavelength calibration as in rss_mos_reducer.py
    # Really we should make a module to put all these routines in
    order=2
    fitCoeffs=np.polyfit(xs, wavelengths, order)
    wavelengthCalibPoly=np.poly1d(fitCoeffs)
    wavelengths=wavelengthCalibPoly(np.arange(arcData.shape[0]))
    
    # Check of wavelength calibration fit
    plt.figure(figsize=(12,8))
    plt.title("Wavelength calibration model fit")
    plt.plot(np.arange(arcData.shape[0]), wavelengths, 'k--')
    plt.plot(arcFeatureTable['x_centreRow'], arcFeatureTable['wavelength'], 'r.')
    plt.xlabel("x (pixels)")
    plt.ylabel("Wavelength (Angstroms)")
    
    # Sanity check of transformation
    #plt.matplotlib.interactive(True)
    plt.figure(figsize=(12, 8))
    plt.title("Wavelength calibration check")
    plt.plot(wavelengths, arcData, 'k-')
    plt.plot(arcFeatureTable['wavelength'], arcFeatureTable['amplitude'], 'bo')
    for row in arcFeatureTable:
        plt.text(row['wavelength'], row['amplitude'], row['wavelength'])
    plt.xlabel("Wavelength (Angstroms)")
    plt.ylabel("Relative Flux")
    plt.show()
    
    # Overwrite the old reference model, if all appears well
    choice=raw_input("Overwrite reference model %s? [y/n]" % (modelFileName))
    if choice == 'y':
        pickleFile=file(modelFileName, "wb")
        pickler=pickle.Pickler(pickleFile)
        pickler.dump(refModelDict)
        pickleFile.close()
    

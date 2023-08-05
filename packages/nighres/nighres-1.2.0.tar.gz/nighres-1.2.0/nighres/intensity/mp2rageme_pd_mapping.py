import numpy as np
import nibabel as nb
import os
import sys
import nighresjava
from ..io import load_volume, save_volume
from ..utils import _output_dir_4saving, _fname_4saving, \
                    _check_topology_lut_dir, _check_available_memory


def mp2rageme_pd_mapping(first_inversion, second_inversion, 
                      t1map, r2smap, echo_times,
                      inversion_times, flip_angles, inversion_TR,
                      excitation_TR, N_excitations, efficiency=0.96,
                      b1map=None, s0img=None,
                      save_data=False, overwrite=False, output_dir=None,
                      file_name=None):
    """ MP2RAGEME PD mapping

    Estimate PD maps from MP2RAGEME data, combining T1 and R2* estimates
    with the MPRAGE model of _[1].

    Parameters
    ----------
    first_inversion: [niimg]
        List of {magnitude, phase} images for the first inversion
    second_inversion: [niimg]
        List of {magnitude, phase} images for the second inversion
    t1map: niimg
        Quantitative T1 map image, in milliseconds
    r2smap: niimg
        Quantitative R2* map image, in kHz
    echo_times: [float]
        List of {te1, te2, te3, te4, te5} echo times, in seconds
    inversion_times: [float]
        List of {first, second} inversion times, in seconds
    flip_angles: [float]
        List of {first, second} flip angles, in degrees
    inversion_TR: float
        Inversion repetition time, in seconds
    excitation_TR: [float]
        List of {first,second} repetition times,in seconds
    N_excitations: int
        Number of excitations
    efficiency: float
        Inversion efficiency (default is 0.96)
    correct_B1: bool
        Whether to correct for B1 inhomogeneities (default is False)
    b1map: niimg
        Computed B1 map (optional)
    s0map: niimg
        Computed S0 map (optional)
    scale_phase: bool
        Whether to rescale the phase image in [0,2PI] or to assume it is 
        already in radians
    save_data: bool
        Save output data to file (default is False)
    overwrite: bool
        Overwrite existing results (default is False)
    output_dir: str, optional
        Path to desired output directory, will be created if it doesn't exist
    file_name: str, optional
        Desired base name for output files with file extension
        (suffixes will be added)

    Returns
    ----------
    dict
        Dictionary collecting outputs under the following keys
        (suffix of output files in brackets)

        * pd1 (niimg): Map of estimated proton density from inv1 (_qpd-inv1)
        * pd2 (niimg): Map of estimated proton density from inv2 (_qpd-inv2)
        * pd (niimg):  Map of estimated proton density average (_qpd-avg)
        
    Notes
    ----------
    Original Java module by Pierre-Louis Bazin.
    
    References
    ----------
    .. [1] Marques, Kober, Krueger, van der Zwaag, Van de Moortele, Gruetter (2010)
        MP2RAGE, a self bias-field corrected sequence for improved segmentation 
        and T1-mapping at high field. doi: 10.1016/j.neuroimage.2009.10.002.
    """

    print('\nPD Mapping')

    # make sure that saving related parameters are correct
    if save_data:
        output_dir = _output_dir_4saving(output_dir, first_inversion[0])

        pd1_file = os.path.join(output_dir, 
                        _fname_4saving(module=__name__,file_name=file_name,
                                   rootfile=first_inversion[0],
                                   suffix='qpd-inv1'))

        pd2_file = os.path.join(output_dir, 
                        _fname_4saving(module=__name__,file_name=file_name,
                                   rootfile=first_inversion[0],
                                   suffix='qpd-inv2'))

        pd_file = os.path.join(output_dir, 
                        _fname_4saving(module=__name__,file_name=file_name,
                                   rootfile=first_inversion[0],
                                   suffix='qpd-avg'))

        if overwrite is False \
            and os.path.isfile(pd1_file) \
            and os.path.isfile(pd2_file) \
            and os.path.isfile(pd_file) :
                output = {'pd1': pd1_file,
                          'pd2': pd2_file, 
                          'pd': pd_file}
                return output

    # start virtual machine, if not already running
    try:
        mem = _check_available_memory()
        nighresjava.initVM(initialheap=mem['init'], maxheap=mem['max'])
    except ValueError:
        pass
    # create algorithm instance
    qpdmap = nighresjava.IntensityMp2ragemePDmapping()

    # set algorithm parameters
    qpdmap.setFirstEchoTime(echo_times[0])
    qpdmap.setFirstInversionTime(inversion_times[0])
    qpdmap.setSecondInversionTime(inversion_times[1])
    qpdmap.setFirstFlipAngle(flip_angles[0])
    qpdmap.setSecondFlipAngle(flip_angles[1])
    qpdmap.setInversionRepetitionTime(inversion_TR)
    qpdmap.setFirstExcitationRepetitionTime(excitation_TR[0])
    qpdmap.setSecondExcitationRepetitionTime(excitation_TR[1])
    qpdmap.setNumberExcitations(N_excitations)
    qpdmap.setInversionEfficiency(efficiency)
    qpdmap.setCorrectB1inhomogeneities(b1map!=None)
     
    # load first image and use it to set dimensions and resolution
    img = load_volume(first_inversion[0])
    data = img.get_data()
    #data = data[0:10,0:10,0:10]
    affine = img.affine
    header = img.header
    resolution = [x.item() for x in header.get_zooms()]
    dimensions = data.shape

    qpdmap.setDimensions(dimensions[0], dimensions[1], dimensions[2])
    qpdmap.setResolutions(resolution[0], resolution[1], resolution[2])

    # input images
    qpdmap.setFirstInversionMagnitude(nighresjava.JArray('float')(
                                    (data.flatten('F')).astype(float)))
    
    data = load_volume(first_inversion[1]).get_data()
    qpdmap.setFirstInversionPhase(nighresjava.JArray('float')(
                                    (data.flatten('F')).astype(float)))
    
    data = load_volume(second_inversion[0]).get_data()
    qpdmap.setSecondInversionMagnitude(nighresjava.JArray('float')(
                                    (data.flatten('F')).astype(float)))
    
    data = load_volume(second_inversion[1]).get_data()
    qpdmap.setSecondInversionPhase(nighresjava.JArray('float')(
                                    (data.flatten('F')).astype(float)))
 
    data = load_volume(t1map).get_data()
    qpdmap.setT1mapImage(nighresjava.JArray('float')(
                                    (data.flatten('F')).astype(float)))
    
    data = load_volume(r2smap).get_data()
    qpdmap.setR2smapImage(nighresjava.JArray('float')(
                                    (data.flatten('F')).astype(float)))
    
    if (s0img!=None):
        data = load_volume(s0img).get_data()
        qpdmap.setS0Image(nighresjava.JArray('float')(
                                    (data.flatten('F')).astype(float)))
 
    if (b1map!=None):
        data = load_volume(b1map).get_data()
        qpdmap.setB1mapImage(nighresjava.JArray('float')(
                                    (data.flatten('F')).astype(float)))
 
    # execute the algorithm
    try:
        qpdmap.execute()

    except:
        # if the Java module fails, reraise the error it throws
        print("\n The underlying Java code did not execute cleanly: ")
        print(sys.exc_info()[0])
        raise
        return

    # reshape output to what nibabel likes
    pd1_data = np.reshape(np.array(qpdmap.getProtonDensityImage1(),
                                    dtype=np.float32), dimensions, 'F')

    pd2_data = np.reshape(np.array(qpdmap.getProtonDensityImage2(),
                                    dtype=np.float32), dimensions, 'F')

    pd_data = np.reshape(np.array(qpdmap.getProtonDensityImage(),
                                    dtype=np.float32), dimensions, 'F')

    # adapt header max for each image so that correct max is displayed
    # and create nifiti objects
    header['cal_min'] = np.nanmin(pd1_data)
    header['cal_max'] = np.nanmax(pd1_data)
    pd1 = nb.Nifti1Image(pd1_data, affine, header)

    header['cal_min'] = np.nanmin(pd2_data)
    header['cal_max'] = np.nanmax(pd2_data)
    pd2 = nb.Nifti1Image(pd2_data, affine, header)

    header['cal_min'] = np.nanmin(pd_data)
    header['cal_max'] = np.nanmax(pd_data)
    pd = nb.Nifti1Image(pd_data, affine, header)

    if save_data:
        save_volume(pd1_file, pd1)
        save_volume(pd2_file, pd2)
        save_volume(pd_file, pd)
        return {'pd1': pd1_file, 'pd2': pd2_file, 'pd': pd_file}
    else:
        return {'pd1': pd1, 'pd2': pd2, 'pd': pd}

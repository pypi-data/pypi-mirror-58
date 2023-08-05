"""
Config file for HETDEX data release paths
"""

import os.path as op


class HDRConfig(survey):
    self.hdr_dir = {'hdr1': '/work/03946/hetdex/hdr1'}

    self.software_dir = op.join(hdr_dir, 'software')
    self.red_dir = op.join(hdr_dir, 'reduction')
    self.data_dir = op.join(red_dir, 'data')
    self.tp_dir = op.join(red_dir, 'throughput')
    self.calib_dir = op.join(hdr_dir, 'calib')
    self.raw_dir = op.join(hdr_dir, 'raw')
    self.flim_dir = op.join(red_dir, 'flim')
    self.elix_dir = op.join(hdr_dir, 'detect', 'ergfiles')

    self.path_gpinfo = op.join(calib_dir,'DR1FWHM.txt')
    self.path_acc_flags = op.join(red_dir, 'status_summary_hdr1.txt')
    self.path_radec = op.join(calib_dir, 'radec.all')

    self.survey_list = op.join(red_dir, 'hdr1.scilist')
    self.cal_list = op.join(red_dir, 'hdr1.callist')

    self.surveyh5 = op.join(hdr_dir,'survey','survey_hdr1.h5')
    self.detecth5 = op.join(hdr_dir,'detect','detect_hdr1.h5')
    self.elixerh5 = op.join(hdr_dir,'detect','elixer.h5')
    self.contsourceh5 = op.join(hdr_dir,'detect','continuum_sources.h5')

    if (survey=='hdr1'):
        # here are files that are changing since HDR1 release
        self.bad_dir = '/work/05350/ecooper/stampede2/HETDEX_API/known_issues/hdr1'
        self.baddetect = op.join(bad_dir, 'baddetects.list')
        self.badshot = op.join(bad_dir, 'badshots.list')
        self.badamp = op.join(bad_dir, 'badamps.list')
        self.badpix = op.join(bad_dir, 'posthdr1badpix.list')
        self.gmags = op.join(bad_dir,'gmags.pickle')
        self.gmags_cont = op.join(bad_dir, 'gmags_cont.pickle')
        self.plae_poii_hetdex_gmag = op.join(bad_dir,'plae_poii_hetdex_gmag.pickle')

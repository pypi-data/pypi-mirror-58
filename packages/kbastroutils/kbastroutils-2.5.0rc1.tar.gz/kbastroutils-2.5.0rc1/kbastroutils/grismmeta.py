import copy
from astropy.io import fits
import numpy as np
import re
import sys
from acstools import utils_calib

class GrismMeta:
    def __init__(self,files):
        self.files = copy.deepcopy(files)
        self.meta = {}
        for i,ii in enumerate(files):
            self.meta[i] = {}
            self.meta[i]['ID'] = i
            self.meta[i]['FILE'] = ii
        self.make_meta()
        self.make_fullframe()
    def make_meta(self):
        keys1 = {'PRIMARY': ['TELESCOP','INSTRUME','DETECTOR'
                             ,'TARGNAME','RA_TARG','DEC_TARG'
                             ,'EXPSTART','EXPTIME','POSTARG1','POSTARG2'
                             ,'SUBARRAY'
                            ]
                }        
        keys2 = {
            ('HST','ACS','WFC'): {
                'NCHIP': 2,
                'PRIMARY': ['FILTER1','APERTURE'],
                'EXT': 'Assign conditioning on SUBARRAY and APERTURE',
                'SCI': ['CCDCHIP','IDCSCALE','BUNIT']
            },
            ('HST','WFC3','IR'): {
                'NCHIP': 1,
                'PRIMARY': ['FILTER'],
                'EXT': ('SCI',1),
                'SCI': ['IDCSCALE','BUNIT']
            }
        }                 
        for i in self.meta:
            x = fits.open(self.files[i])
            #### keys1 ####
            for j in keys1:
                for k in keys1[j]:
                    self.meta[i][k] = x[j].header[k]
            #### keys2 ####
            keyforkeys2 = (self.meta[i]['TELESCOP'],self.meta[i]['INSTRUME'],self.meta[i]['DETECTOR'])
            if keyforkeys2 not in keys2.keys():
                print('Error: {0} is not available. Remove {1} before running the program. Terminate'.format(keyforkeys2,self.files[i]))
                sys.exit()
            if keyforkeys2==('HST','WFC3','IR'):
                for j in keys2[keyforkeys2]:
                    if j in {'NCHIP','EXT'}:
                        self.meta[i][j] = copy.deepcopy(keys2[keyforkeys2][j])
                    else:
                        for k in keys2[keyforkeys2][j]:
                            self.meta[i][k] = x[j].header[k]
            elif keyforkeys2==('HST','ACS','WFC'):
                for j in keys2[keyforkeys2]:
                    if j=='NCHIP':
                        self.meta[i][j] = copy.deepcopy(keys2[keyforkeys2][j])
                    elif j=='PRIMARY':
                        for k in keys2[keyforkeys2][j]:
                            self.meta[i][k] = x[j].header[k]
                    elif j=='EXT':
                        ext = None
                        if self.meta[i]['SUBARRAY']:
                            ext = ('SCI',1)
                        else:
                            if re.search('WFC2',self.meta[i]['APERTURE']):
                                ext = ('SCI',1)
                            elif re.search('WFC1',self.meta[i]['APERTURE']):
                                ext = ('SCI',2)
                        if not ext:
                            print('Error: cannot assign ext. Terminate')
                            sys.exit()
                        else:
                            self.meta[i][j] = copy.deepcopy(ext)
                    elif j=='SCI':
                        try:
                            ext = self.meta[i]['EXT']
                        except:
                            print('Error: cannot read ext. Terminate')
                            sys.exit()
                        for k in keys2[keyforkeys2][j]:
                            self.meta[i][k] = x[ext].header[k]
    def make_fullframe(self):
        for i,ii in enumerate(self.files):
            self.meta[i]['SUBARRAY_PARAMS'] = None
            issub = self.meta[i]['SUBARRAY']
            if not issub:
                pass
            elif issub:
                x = fits.open(ii)
                hdr = x[self.meta[i]['EXT']].header
                binsize,corner = utils_calib.get_corner(hdr,rsize=1)
                self.meta[i]['SUBARRAY_PARAMS'] = {'binsize': binsize, 'corner': corner}
           
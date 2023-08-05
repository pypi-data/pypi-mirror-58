import pandas as pd
from scipy.interpolate import interp1d
from astropy.io import fits
class GrismSens:
    def __init__(self,sens,meta):
        DETERMINANT = {('HST','ACS','WFC'): 'CCDCHIP',
                       ('HST','WFC3','IR'): 'FILTER'
                      }
        instrument = (meta['TELESCOP'],meta['INSTRUME'],meta['DETECTOR'])
        det = DETERMINANT[instrument]
        val = meta[det]
        file = sens[val]
        self.file = file
        x = fits.open(self.file)
        xdata = pd.DataFrame(x[1].data.tolist())
        ww,ss,ee = xdata[0].values,xdata[1].values,xdata[2].values
        self.model = interp1d(ww,ss
                              ,kind='linear'
                              ,bounds_error=False,fill_value=None)
        self.emodel = interp1d(ww,ee
                              ,kind='nearest'
                              ,bounds_error=False,fill_value=None)
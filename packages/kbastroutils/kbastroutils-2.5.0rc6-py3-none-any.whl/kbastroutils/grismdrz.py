import sys,shutil,os,glob
from drizzlepac import astrodrizzle
class GrismDRZ:
    def __init__(self,pairs,group,params,run,outpath,meta):
        if group:
            self.group = group
        else:
            self.group = self.make_group(pairs)
        if params:
            self.params = params
        else:
            self.params = self.make_params(meta)
        if run:
            if not outpath:
                self.outpath = os.getcwd() + '/drz/'
            if len(glob.glob(self.outpath))==0:
                os.mkdir(self.outpath)
            self.meta = self.run(meta)
    #####
    #####
    #####
    def run(self,meta):
        for i in self.group:
            inputlist = []
            outmeta = {}
            for j in i:
                source = meta[j]['FILE']
                destination = self.outpath + source.split('/')[-1]
                shutil.copyfile(source,destination)                 
                inputlist.append(destination) 
            if not self.params['final_refimage']:
                self.params['final_refimage'] = inputlist[0]
            if not self.params['output']:
                self.params['output'] = inputlist[0].split('flt')[0]
            astrodrizzle.AstroDrizzle(input=inputlist, **self.params)
            for j,jj in enumerate(i):
                source = inputlist[j]
                os.remove(source)
            outfile = self.params['output'] + '_drz.fits'
            outmeta[i[0]] = copy.deepcopy(meta[i[0]])
            outmeta[i[0]]['FILE'] = outfile
        return outmeta                      
    #####
    #####
    #####
    def make_params(self,meta):
        PARAMS = {'driz_sep_bits': 11775,
                  'driz_sep_scale': 0.128254,
                  'combine_type': 'median',
                  'blot': 'Yes',
                  'blot_addsky': 'No',
                  'final_bits': 11775,
                  'final_wcs': 'Yes',
                  'final_refimage': None,
                  'final_scale': 0.128254,
                  'build': 'Yes',
                  'clean': 'Yes',
                  'output': None
                 }
        return PARAMS
    #####
    #####
    #####
    def make_group(self,pairs):
        gr = []
        for i in pairs:
            if len(pairs[i]) > 1:
                gr.append(pairs[i])
        return gr
        
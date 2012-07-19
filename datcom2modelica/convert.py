# Copyright 2012 Shiwen Zhang, Lenna X. Peterson, James Goppert
# All rights reserved
# License: GPL v3
# This program comes with ABSOLUTELY NO WARRANTY. This is free software
# and you are welcome to distribute it under certain conditions.
# For details, see license.txt

import argparse
import logging
import os
import sys

class Convert(object):
    '''
    classdocs
    '''

    def __init__(self, filename_in, filename_out, interface):
        '''
        Constructor
        '''
        self.filename_in = filename_in
        self.filename_out = filename_out
        self.modelica_name = os.path.splitext(os.path.basename(filename_out))[0]
        self.names = []
        self.coefs = []
        self._convert()
        if interface:
            self.interface = interface
            self._generate_interface()
        
    def _convert(self):
        
        with open(self.filename_in, 'r') as datcom:
            lines = datcom.readlines()

        data = []
        for n in range(len(lines)):
            if lines[n].find('CASEID')!=-1:
                start = lines[n].find('CASEID')+7
                end = lines[n].find(':')
                name = lines[n][start:end]
                self.names.append(name)
            if lines[n].find('0 ALPHA')!=-1 or lines[n].find('0   ALPHA')!=-1:
                coef = lines[n].split()
                self.coefs.append(coef)
                for k in range(1,len(coef)-1):
                    if data==[]:
                        data.append('\t\t'+coef[k+1]+'_'+name+'.tableOnFile=false,\n')
                    else:
                        data.append(',\n\t\t'+coef[k+1]+'_'+name+'.tableOnFile=false,\n')
                    data.append('\t\t'+coef[k+1]+'_'+name+'.table=\n\t\t{\n')
                    a = n+2
        ##            data.append('\n\t{'+lines[a-1].split()[0]+',\t\t'+lines[a-1].split()[k]+'},\n')
                    pos = lines[a].find(lines[a].split()[k])
                    while lines[a][0]!='0':
                        if lines[a].split()[0][0]=='.':
                            lines[a].split()[0] = lines[a].split()[0].replace('.','0.')
                        if lines[a][pos:(pos+len(lines[n+2].split()[k]))]==' '*len(lines[n+2].split()[k]):
                            lines[a]=lines[a].replace(' '*(len(lines[n+2].split()[k])+4),'\t'+lines[n+2].split()[k],1)
                        if lines[a].split()[k]=='NDM':
                            if lines[a].split()[0][0]=='.':
                                data.append('\t\t\t{0'+lines[a].split()[0]+',\t0.000}')
                            else:
                                data.append('\t\t\t{'+lines[a].split()[0]+',\t0.000}')
                        elif lines[a].split()[k][0] == '.':
                            if lines[a].split()[0][0]=='.':
                                data.append('\t\t\t{0'+lines[a].split()[0]+',\t0'+lines[a].split()[k]+'}')
                            else:
                                data.append('\t\t\t{'+lines[a].split()[0]+',\t0'+lines[a].split()[k]+'}')
                        elif lines[a].split()[k][0] == '-' and lines[a].split()[k][1] == '.':
                            if lines[a].split()[0][0]=='.':
                                data.append('\t\t\t{0'+lines[a].split()[0]+',\t-0'+lines[a].split()[k][1:len(lines[a].split()[k])-1]+'}')
                            else:
                                data.append('\t\t\t{'+lines[a].split()[0]+',\t-0'+lines[a].split()[k][1:len(lines[a].split()[k])-1]+'}')
                        else:
                            if lines[a].split()[0][0]=='.':
                                data.append('\t\t\t{0'+lines[a].split()[0]+',\t'+lines[a].split()[k]+'}')
                            else:
                                data.append('\t\t\t{'+lines[a].split()[0]+',\t'+lines[a].split()[k]+'}')
        ##                if k == 9 or k == 10:
        ##                    data.append('\t{'+lines[a].split()[0]+',\t'+lines[n+2].split()[k]+'}')
        ##                elif k == 11:
        ##                    data.append('\t{'+lines[a].split()[0]+',\t'+lines[a].split()[k-2]+'}')
        ##                else:
        ##                    data.append('\t{'+lines[a].split()[0]+',\t'+lines[a].split()[k-1]+'}')
                        a = a+1
                        if lines[a][0]=='0' or lines[a].split()[k]=='NA':
                            data.append('\n\t\t}')                            
                            break
                        else:
                            data.append(',\n')            
            
        with open(self.filename_out, 'w') as table:
            table.write('model DatcomTable_'+self.modelica_name+'\n\textends DatcomTable(\n')
            for line in data:
                table.write(line)
            table.write(');\nend DatcomTable_'+self.modelica_name+';')

    def _generate_interface(self):

        with open(self.interface,'w') as table:
            for i in xrange(len(self.names)):
                table.write('%s : %s\n' % (self.names[i], self.coefs[i]) )
            
    @classmethod
    def from_argv(cls,argv):
        '''
        Constructor from command line arguments
        '''
        sys.argv = argv
        parser = argparse.ArgumentParser()
        parser.add_argument("infile",
                          help="DATCOM file to convert")
        parser.add_argument("outfile",
                            help="Path to write converted file")
        parser.add_argument("-f", "--format",
                            choices=['table', 'model'], default='model',
                            help="Format to write (table not implemented)")
        parser.add_argument("-i", "--interface",
                           help="Generate the modelica interface")
        noise = parser.add_mutually_exclusive_group()
        noise.add_argument("-q", "--quiet", action="store_true",
                           help="Less output")
        noise.add_argument("-v", "--verbose", action="store_true",
                           help="More output")
    
        args = parser.parse_args()
    
        if args.quiet:
            log_level = logging.WARNING
        elif args.verbose:
            log_level = logging.DEBUG
        else:
            log_level = logging.INFO
    
        logging.basicConfig(format="%(message)s", level=log_level)

        return cls(args.infile, args.outfile,args.interface)
         
if __name__ == '__main__':
    Convert.from_argv(sys.argv)
# vim:expandtab:ts=4:sw=4:

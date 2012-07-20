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
        self.coefname = []
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
            if lines[n].find('0 ALPHA')!=-1 or lines[n].find('0   ALPHA')!=-1:
                coef = lines[n].split()
                for c in range(2,len(coef)):
                    coef[c] = coef[c]+'_'+name
                self.coefname.append(coef)
                for k in range(1,len(coef)-1):
                    if data==[]:
                        data.append('    %s.tableOnFile=false,\n' % coef[k+1])
                    else:
                        data.append(',\n    %s.tableOnFile=false,\n' % coef[k+1])
                    data.append('    '+coef[k+1]+'.table=\n    {\n')
                    a = n+2
                    pos = lines[a].find(lines[a].split()[k])
                    while lines[a][0]!='0': # while not end of table
                        data.append('      {%7.3f' % float(lines[a].split()[0])) # write beginning of row
                        # handle columns correctly
                        if lines[a][pos:(pos+len(lines[n+2].split()[k]))]==' '*len(lines[n+2].split()[k]):
                            lines[a]=lines[a].replace(' '*(len(lines[n+2].split()[k])+4),'  '+lines[n+2].split()[k],1)
                        # write within row
                        if lines[a].split()[k]=='NDM': # write zero for NDM
                            data.append(', %7.3f}' % 0)
                        else:
                            data.append(', %7.3f}' % float(lines[a].split()[k]))
                        a = a+1
                        if lines[a][0]=='0' or lines[a].split()[k]=='NA': # end of table
                            data.append('\n    }')                            
                            break
                        else:
                            data.append(',\n')            
            
        with open(self.filename_out, 'w') as table:
            table.write('model DatcomTable_'+self.modelica_name+'\n  extends DatcomTable(\n')
            for line in data:
                table.write(line)
            table.write(');\nend DatcomTable_'+self.modelica_name+';')

    def _generate_interface(self):
        datcom_table_file = os.path.join(self.interface,'DatcomTable.mo')
        aero_connector_file = os.path.join(self.interface,'AeroConnector.mo')
        
        with open(datcom_table_file,'w') as table:
            table.write('model DatcomTable\n  import Modelica.Blocks.Tables.*;\n  input AircraftState state;\n  output AeroConnector coef;\n  parameter Boolean tableOnFile = false;\n')
            for i in xrange(len(self.coefname)):
                for k in xrange(len(self.coefname[i])-2):
                    table.write('  CombiTable1D '+self.coefname[i][k+2]+';\n')
            table.write('equation\n')
            for i in xrange(len(self.coefname)):
                for k in xrange(len(self.coefname[i])-2):
                    table.write('  connect('+self.coefname[i][k+2]+'.u[1],state.alpha);\n')
                    table.write('  connect('+self.coefname[i][k+2]+'.y[1],coef.'+self.coefname[i][k+2]+');\n')
            table.write('end DatcomTable;')
            
        with open(aero_connector_file,'w') as connector:
            connector.write("test")

            
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
                           help="Generate the modelica interface (takes directory to write to)")
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

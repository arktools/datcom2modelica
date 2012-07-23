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
        extra = []
        chrdfi = []
        chrdfo = []
        spanfi = []
        spanfo = []
        for n in range(len(lines)):
            if lines[n].find('CASEID')!=-1:
                start = lines[n].find('CASEID')+7
                end = lines[n].find(':')
                name = lines[n][start:end]
            if lines[n].find('$WGPLNF')!=-1:
                lines[n] = lines[n].replace('$',',')
                print lines[n]
                a = n
                while lines[a].find('$')==-1:
                    if lines[a].find('CHRDR')!=-1:
                        chrdr = float(lines[a][lines[a].find('CHRDR')+6:lines[a].find(',',lines[a].find('CHRDR'))])
                    if lines[a].find('CHRDTP')!=-1:
                        chrdtp = float(lines[a][lines[a].find('CHRDTP')+7:lines[a].find(',',lines[a].find('CHRDTP'))])
                    a = a+1
                if lines[a].find('CHRDR')!=-1:
                    chrdr = float(lines[a][lines[a].find('CHRDR')+6:lines[a].find(',',lines[a].find('CHRDR'))])
                if lines[a].find('CHRDTP')!=-1:
                    chrdtp = float(lines[a][lines[a].find('CHRDTP')+7:lines[a].find(',',lines[a].find('CHRDTP'))])
                cbar = (chrdr+chrdtp)/2
                span = float(lines[n+1][lines[n+1].find('SSPN')+5:lines[n+1].find(',')])*2
                area = cbar*span
            if lines[n].find('$SYMFLP')!=-1 or lines[n].find('$ASYFLP')!=-1:
                lines[n] = lines[n].replace('$',',')
                a = n
                while lines[a].find('$')==-1:
                    if lines[a].find('CHRDFI')!=-1:
                        chrdfi.append(float(lines[a][lines[a].find('CHRDFI')+7:lines[a].find(',',lines[a].find('CHRDFI'))]))
                    if lines[a].find('CHRDFO')!=-1:
                        chrdfo.append(float(lines[a][lines[a].find('CHRDFO')+7:lines[a].find(',',lines[a].find('CHRDFO'))]))
                    if lines[a].find('SPANFO')!=-1:
                        spanfo.append(float(lines[a][lines[a].find('SPANFO')+7:lines[a].find(',',lines[a].find('SPANFO'))]))
                    if lines[a].find('SPANFI')!=-1:
                        spanfi.append(float(lines[a][lines[a].find('SPANFI')+7:lines[a].find(',',lines[a].find('SPANFI'))]))
                    a = a+1
                if lines[a].find('CHRDFI')!=-1:
                    chrdfi.append(float(lines[a][lines[a].find('CHRDFI')+7:lines[a].find(',',lines[a].find('CHRDFI'))]))
                if lines[a].find('CHRDFO')!=-1:
                    chrdfo.append(float(lines[a][lines[a].find('CHRDFO')+7:lines[a].find(',',lines[a].find('CHRDFO'))]))
                if lines[a].find('SPANFO')!=-1:
                    spanfo.append(float(lines[a][lines[a].find('SPANFO')+7:lines[a].find(',',lines[a].find('SPANFO'))]))
                if lines[a].find('SPANFI')!=-1:
                    spanfi.append(float(lines[a][lines[a].find('SPANFI')+7:lines[a].find(',',lines[a].find('SPANFI'))]))
#            if lines[n].find('SPANFI')!=-1:
#                spanfi.append(float(lines[n][lines[n].find('SPANFI')+7:lines[n].find(',',lines[n].find('SPANFI'))]))
#                spanfo.append(float(lines[n][lines[n].find('SPANFO')+1:lines[n].rfind(',',lines[n].find('SPANFO'))]))
            if lines[n].find('0 ALPHA')!=-1 or lines[n].find('0   ALPHA')!=-1 or lines[n].find('0     DELTA')!=-1 or lines[n].find('0                                            DELTAL')!=-1:
                for e in range(len(lines[n])):
                    if e>=len(lines[n])-1:
                        break
                    elif lines[n][e] == '(':
                        space = lines[n].find(' ',e)
                        bracket = lines[n].find(')',e)
                        if bracket > space and space!=-1:
                            lines[n] = lines[n][0:space]+'_'+lines[n][space+1:len(lines[n])]
                lines[n] = lines[n].replace(' (','')
                lines[n] = lines[n].replace(') ','')
                lines[n] = lines[n].replace('(','_')
                lines[n] = lines[n].replace(')','_')
                coef = lines[n].split()
                for c in range(2,len(coef)):
                    coef[c] = coef[c]+'_'+name
                self.coefname.append(coef)
                pos = 0
                for k in range(1,len(coef)-1):
                    if coef[k+1] == 'D_CL_FLAPS' or coef[k+1] == 'D_CL_TOTAL' or coef[k+1] == 'D_CM_FLAPS' or coef[k+1] == 'D_CM_TOTAL' or coef[k-1] == 'DELTAL':
                        extra.append('    '+coef[k+1]+'.data=\n    {\n')
#                    elif coef[k+1]=='CLQ_TOTAL' or coef[k+1]=='CLAD_TOTAL' or coef[k+1]=='D_CL_TOTAL' or coef[k+1]=='CD_TOTAL' or coef[k+1]=='CYB_TOTAL' or coef[k+1]=='CYP_TOTAL' or coef[k+1]=='CLB_TOTAL' or coef[k+1]=='CLP_TOTAL' or coef[k+1]=='CLR_TOTAL' or coef[k+1]=='CNB_TOTAL' or coef[k+1]=='CNP_TOTAL' or coef[k+1]=='CNR_TOTAL' or coef[k+1]=='CMQ_TOTAL' or coef[k+1]=='CMAD_TOTAL' or coef[k+1]=='D_CM_TOTAL':
#                        extra.append('    '+coef[k+1]+'.data=\n    {\n')
                    data.append('    '+coef[k+1]+'.data=\n    {\n')
                    if lines[n].find('0     DELTA')!=-1:
                        a = n+3
                    else:
                        a = n+2
                    beg = a
                    pos = lines[a].find(lines[a].split()[k],pos+1)
                    while lines[a][0]!='0' or lines[a][0]!='1': # while not end of table
                        data.append('      {%6.2f' % float(lines[a].split()[0])) # write beginning of row
                        if coef[k+1] == 'D_CL_FLAPS' or coef[k+1] == 'D_CL_TOTAL' or coef[k+1] == 'D_CM_FLAPS' or coef[k+1] == 'D_CM_TOTAL':
                            extra.append('      {%6.2f' % float(lines[a].split()[0]))
                        elif coef[k-1] == 'DELTAL':
                            f = float(lines[a].split()[0])*2
                            extra.append('      {%6.2f' % f)
#                        elif coef[k+1]=='CLQ_TOTAL' or coef[k+1]=='CLAD_TOTAL' or coef[k+1]=='D_CL_TOTAL' or coef[k+1]=='CD_TOTAL' or coef[k+1]=='CYB_TOTAL' or coef[k+1]=='CYP_TOTAL' or coef[k+1]=='CLB_TOTAL' or coef[k+1]=='CLP_TOTAL' or coef[k+1]=='CLR_TOTAL' or coef[k+1]=='CNB_TOTAL' or coef[k+1]=='CNP_TOTAL' or coef[k+1]=='CNR_TOTAL' or coef[k+1]=='CMQ_TOTAL' or coef[k+1]=='CMAD_TOTAL' or coef[k+1]=='D_CM_TOTAL':
#                            extra.append('      {%6.2f' % float(lines[a].split()[0]))
                        # handle columns correctly
                        if lines[a][pos:(pos+len(lines[beg].split()[k]))]==' '*len(lines[beg].split()[k]):
                            lines[a] = lines[a][0:pos-1]+' '+lines[beg].split()[k]+' '+lines[a][(pos+len(lines[beg].split()[k])+1):len(lines[a])]
                        # write within row
                        if lines[a].split()[k]=='NDM': # write zero for NDM
                            lines[a] = lines[a].replace('NDM','0.000',1)
                        data.append(', %10.3e}' % float(lines[a].split()[k]))
                        if coef[k+1] == 'D_CL_FLAPS' or coef[k+1] == 'D_CL_TOTAL' or coef[k+1] == 'D_CM_FLAPS' or coef[k+1] == 'D_CM_TOTAL':
                            f = float(lines[a].split()[k])/2
                            extra.append(', %10.3e}' % f)
                        elif coef[k-1] == 'DELTAL':
                            extra.append(', %10.3e}' % float(lines[a].split()[k]))
#                        elif coef[k+1]=='CLQ_TOTAL' or coef[k+1]=='CLAD_TOTAL' or coef[k+1]=='D_CL_TOTAL' or coef[k+1]=='CD_TOTAL' or coef[k+1]=='CYB_TOTAL' or coef[k+1]=='CYP_TOTAL' or coef[k+1]=='CLB_TOTAL' or coef[k+1]=='CLP_TOTAL' or coef[k+1]=='CLR_TOTAL' or coef[k+1]=='CNB_TOTAL' or coef[k+1]=='CNP_TOTAL' or coef[k+1]=='CNR_TOTAL' or coef[k+1]=='CMQ_TOTAL' or coef[k+1]=='CMAD_TOTAL' or coef[k+1]=='D_CM_TOTAL':
#                            extra.append(', %10.3e}' % float(lines[a].split()[k]))
                        a = a+1
                        if lines[a][0]=='0' or lines[a][0]=='1' or lines[a].split()[k]=='NA': # end of table
                            data.append('\n    },\n')
                            if coef[k+1] == 'D_CL_FLAPS' or coef[k+1] == 'D_CL_TOTAL' or coef[k+1] == 'D_CM_FLAPS' or coef[k+1] == 'D_CM_TOTAL' or coef[k-1] == 'DELTAL':
                                extra.append('\n    },\n')
#                            elif coef[k+1]=='CLQ_TOTAL' or coef[k+1]=='CLAD_TOTAL' or coef[k+1]=='D_CL_TOTAL' or coef[k+1]=='CD_TOTAL' or coef[k+1]=='CYB_TOTAL' or coef[k+1]=='CYP_TOTAL' or coef[k+1]=='CLB_TOTAL' or coef[k+1]=='CLP_TOTAL' or coef[k+1]=='CLR_TOTAL' or coef[k+1]=='CNB_TOTAL' or coef[k+1]=='CNP_TOTAL' or coef[k+1]=='CNR_TOTAL' or coef[k+1]=='CMQ_TOTAL' or coef[k+1]=='CMAD_TOTAL' or coef[k+1]=='D_CM_TOTAL':
#                                extra.append('\n    },\n')
                            break
                        else:
                            data.append(',\n')
                            if coef[k+1] == 'D_CL_FLAPS' or coef[k+1] == 'D_CL_TOTAL' or coef[k+1] == 'D_CM_FLAPS' or coef[k+1] == 'D_CM_TOTAL' or coef[k-1] == 'DELTAL':
                                extra.append(',\n')
#                            elif coef[k+1]=='CLQ_TOTAL' or coef[k+1]=='CLAD_TOTAL' or coef[k+1]=='D_CL_TOTAL' or coef[k+1]=='CD_TOTAL' or coef[k+1]=='CYB_TOTAL' or coef[k+1]=='CYP_TOTAL' or coef[k+1]=='CLB_TOTAL' or coef[k+1]=='CLP_TOTAL' or coef[k+1]=='CLR_TOTAL' or coef[k+1]=='CNB_TOTAL' or coef[k+1]=='CNP_TOTAL' or coef[k+1]=='CNR_TOTAL' or coef[k+1]=='CMQ_TOTAL' or coef[k+1]=='CMAD_TOTAL' or coef[k+1]=='D_CM_TOTAL':
#                                extra.append(',\n')
            # read 2D tables
            elif lines[n].find('0(DELTAL-DELTAR)')!=-1 or lines[n].find('0       DELTA =')!=-1:
                start = lines[n-1].find(',')
                end = lines[n-1].rfind(',')
                coef = lines[n-1][start+1:end]
#                coef = u1+' '+u2+' '+lines[n-1][start+1:end]
                coef = coef.replace(' (','')
                coef = coef.replace(') ','')
                coef = coef.replace('(','_')
                coef = coef.replace(')','_')
#                coef = coef.split()
                coef = coef.replace(' ','')
                coef = coef+'2D_'+name
#                for c in range(2,len(coef)):
#                    coef[c] = coef[c]+'_'+name
                self.coefname.append([coef])
#                data.append(',\n    %s.tableOnFile=false,\n' % coef)
                data.append('    '+coef+'.data = transpose(\n    {\n')
                lines[n] = lines[n].replace(lines[n][0:(lines[n].find('=')+1)],'0 ')
                data.append('      {')
                if coef == 'D_CDI2D_TOTAL' or coef == 'D_CDI2D_FLAPS':
                    extra.append('    '+coef+'.data = transpose(\n    {\n')
                    extra.append('      {')
#                elif coef == 'D_CDI2D_TOTAL' or coef == 'CN_AILERONS':
#                    extra.append('    '+coef+'.data = transpose(\n    {\n')
#                    extra.append('      {')
                for i in lines[n].split():
                    if coef == 'D_CDI2D_TOTAL' or coef == 'D_CDI2D_FLAPS':
                        extra.append('%10.2f, ' % float(i))
#                    elif coef == 'D_CDI_TOTAL' or coef == 'CN_AILERONS':
#                        extra.append('%10.2f, ' % float(i))
                    data.append('%10.2f, ' % float(i))
                if coef == 'D_CDI2D_TOTAL' or coef == 'D_CDI2D_FLAPS':
                    extra[len(extra)-1] = extra[len(extra)-1].replace(', ','},\n')
#                elif coef == 'D_CDI_TOTAL' or coef == 'CN_AILERONS':
#                    extra[len(extra)-1] = extra[len(extra)-1].replace(', ','},\n')
                data[len(data)-1] = data[len(data)-1].replace(', ','},\n')
                a = n+3
                while lines[a][0]!='0':
                    if coef == 'D_CDI2D_TOTAL' or coef == 'D_CDI2D_FLAPS':
                        extra.append('      {')
#                    elif coef == 'D_CDI_TOTAL' or coef == 'CN_AILERONS':
#                        extra.append('      {')
                    data.append('      {')
                    for i in lines[a].split():
                        if i > 0 and (coef == 'D_CDI2D_TOTAL' or coef == 'D_CDI2D_FLAPS'):
                            f = float(i)/2
                            extra.append('%10.3e, ' % f)
                        elif i==0:
                            extra.append('%10.3e, ' % float(i))
#                        elif coef == 'D_CDI_TOTAL' or coef == 'CN_AILERONS':
#                            extra.append('%10.3e, ' % float(i))
                        data.append('%10.3e, ' % float(i))
                    if coef == 'D_CDI2D_TOTAL' or coef == 'D_CDI2D_FLAPS':
                        extra[len(extra)-1] = extra[len(extra)-1].replace(', ','},\n')
                    data[len(data)-1] = data[len(data)-1].replace(', ','},\n')
                    a = a+1
                if coef == 'D_CDI2D_TOTAL' or coef == 'D_CDI2D_FLAPS':
                    extra[len(extra)-1] = extra[len(extra)-1].replace('\n','') 
                    extra[len(extra)-1] = extra[len(extra)-1].replace(',','\n    }),\n')
                data[len(data)-1] = data[len(data)-1].replace('\n','') 
                data[len(data)-1] = data[len(data)-1].replace(',','\n    }),\n')
        dist = []
        print chrdfi
        print chrdfo
        print spanfi
        print spanfo
        for i in range(len(chrdfi)/2):
            dist.append((chrdfi[i]+2*chrdfo[i])/3/(chrdfi[i]+chrdfo[i])*(spanfo[i]-spanfi[i]))
        with open(self.filename_out, 'w') as table:
            table.write('model AerodynamicsDatcom_'+self.modelica_name+'\n  extends AerodynamicsDatcom(\n')
            table.write('    cBar = %4.2f,\n' % cbar)
            table.write('    b = %4.2f,\n' % span)
            table.write('    s = %4.2f,\n' % area)
            for l in range(len(data)):
                if data[l].find('CLQ_TOTAL')!=-1:
                    data[l] = data[l].replace('CLQ_TOTAL','CLq')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CLAD_TOTAL')!=-1:
                    data[l] = data[l].replace('CLAD_TOTAL','CLad')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('D_CL_TOTAL')!=-1:
                    data[l] = data[l].replace('D_CL_TOTAL','CLDe')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CD_TOTAL')!=-1:
                    data[l] = data[l].replace('CD_TOTAL','CD')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('D_CDI2D_TOTAL')!=-1:
                    data[l] = data[l].replace('D_CDI2D_TOTAL','CdDe')
                    a = l
                    while data[a].find('\n    }),\n')==-1:
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CYB_TOTAL')!=-1:
                    data[l] = data[l].replace('CYB_TOTAL','Cyb')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CYP_TOTAL')!=-1:
                    data[l] = data[l].replace('CYP_TOTAL','Cyp')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CLB_TOTAL')!=-1:
                    data[l] = data[l].replace('CLB_TOTAL','Clb')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CLP_TOTAL')!=-1:
                    data[l] = data[l].replace('CLP_TOTAL','Clp')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CLR_TOTAL')!=-1:
                    data[l] = data[l].replace('CLR_TOTAL','Clr')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CNB_TOTAL')!=-1:
                    data[l] = data[l].replace('CNB_TOTAL','Cnb')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CNP_TOTAL')!=-1:
                    data[l] = data[l].replace('CNP_TOTAL','Cnp')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CNR_TOTAL')!=-1:
                    data[l] = data[l].replace('CNR_TOTAL','Cnr')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CN2D_AILERONS')!=-1:
                    data[l] = data[l].replace('CN2D_AILERONS','CnDa')
                    a = l
                    while data[a].find('\n    }),\n')==-1:
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CMQ_TOTAL')!=-1:
                    data[l] = data[l].replace('CMQ_TOTAL','Cmq')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CMAD_TOTAL')!=-1:
                    data[l] = data[l].replace('CMAD_TOTAL','Cmad')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('D_CM_TOTAL')!=-1:
                    data[l] = data[l].replace('D_CM_TOTAL','CmDe')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
            for line in extra:
                line = line.replace('D_CL_TOTAL','CLdF1L')
                line = line.replace('D_CL_FLAPS','CLdF2L')
                line = line.replace('D_CM_TOTAL','CmdF1L')
                line = line.replace('D_CM_FLAPS','CmdF2L')
                line = line.replace('D_CDI2D_TOTAL','CdDf1L')
                line = line.replace('D_CDI2D_FLAPS','CdDf2L')
                line = line.replace('CL_ROLL_AILERONS','ClDs4')
                table.write(line)
            table.write('    CLdF1R.data = CLdF1L.data,\n    CLdF2R.data = CLdF2L.data,\n    CdDf1R.data = CdDf1L.data,\n    CdDf2R.data = CdDf2L.data,\n')
            table.write('    CmDf1R.data = CmDf1L.data,\n    CmDf2R.data = CmDf2L.data,\n')

            table.write('    CldF1 = %4.3f, //Guess Value\n' % dist[0])
#            table.write('    CldF2 = %4.3f, //Guess Value\n' % dist[1])
            table.write('    CnDf1 = %4.3f, //Guess Value\n' % dist[0])
#            table.write('    CnDf2 = %4.3f, //Guess Value\n' % dist[1])
            table.write('    CLge.data = {{0,0},{1,0}}, //Not in .out file\n    CLwbh.data = {{0,0},{1,0}}, //Not in .out file\n    CDge.data = {{0,0},{1,0}}, //Not in .out file\n')
            table.write('    ClDr = 0, //Not calculated in Datcom\n    Cm_basic.data = {{0,0},{1,0}},//Not in .out file\n    CnDr = 0 //Not in .out file\n')
            table.write('  );\nend AerodynamicsDatcom_'+self.modelica_name+';')
            

    def _generate_interface(self):
        datcom_table_file = os.path.join(self.interface,'Table.mo')
        aero_connector_file = os.path.join(self.interface,'Derivatives.mo')
        
        with open(datcom_table_file,'w') as table:
            table.write('partial model Table\n  import Modelica.Blocks.Tables.*;\n  input AircraftState state;\n  output Derivatives coef;\n')
            for i in xrange(len(self.coefname)):
                if len(self.coefname[i]) == 1:
                    table.write('  CombiTable2D '+self.coefname[i][0]+';\n')
                else:
                    for k in xrange(len(self.coefname[i])-2):
                        table.write('  CombiTable1D '+self.coefname[i][k+2]+';\n')
            table.write('equation\n')
            for i in xrange(len(self.coefname)):
                if len(self.coefname[i]) == 1:
                    table.write('  connect('+self.coefname[i][0]+'.u[1],state.alpha);\n')
                    table.write('  connect('+self.coefname[i][0]+'.u[2],state.delta);\n')
                    table.write('  connect('+self.coefname[i][0]+'.y[1],coef.'+self.coefname[i][0]+');\n')
                else:
                    for k in xrange(len(self.coefname[i])-2):
                        table.write('  connect('+self.coefname[i][k+2]+'.u[1],state.alpha);\n')
                        table.write('  connect('+self.coefname[i][k+2]+'.y[1],coef.'+self.coefname[i][k+2]+');\n')
            table.write('end Table;')
            
        with open(aero_connector_file,'w') as connector:
            connector.write("expandable connector Derivatives\n")
            for i in xrange(len(self.coefname)):
                if len(self.coefname[i]) == 1:
                    connector.write('  Real '+self.coefname[i][0]+';\n')
                else:
                    for k in xrange(len(self.coefname[i])-2):
                        connector.write('  Real '+self.coefname[i][k+2]+';\n')
                    
            connector.write('end Derivatives;')

            
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

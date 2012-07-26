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
#            if lines[n].find('CASEID')!=-1:
#                start = lines[n].find('CASEID')+7
#                end = lines[n].find(':')
#                name = lines[n][start:end]
            if lines[n].find('NACA W')!=-1 or lines[n].find('NACA H')!=-1:
                name = lines[n][lines[n].find('NACA ')+5]
                b = n
                while  lines[b][0]!='1' and lines[b].find('NEXT CASE')==-1:
                    if lines[b].find('$SYMFLP')!=-1 or lines[b].find('$ASYFLP')!=-1:
                        control = lines[b][lines[b].find('$')+1:lines[b].find('$')+7]
                        lines[b] = lines[b].replace('$',',')
                        a = b
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
                        lines[a] = lines[a].replace('$',',')
                        if lines[a].find('CHRDFI')!=-1:
                            chrdfi.append(float(lines[a][lines[a].find('CHRDFI')+7:lines[a].find(',',lines[a].find('CHRDFI'))]))
                        if lines[a].find('CHRDFO')!=-1:
                            chrdfo.append(float(lines[a][lines[a].find('CHRDFO')+7:lines[a].find(',',lines[a].find('CHRDFO'))]))
                        if lines[a].find('SPANFO')!=-1:
                            spanfo.append(float(lines[a][lines[a].find('SPANFO')+7:lines[a].find(',',lines[a].find('SPANFO'))]))
                        if lines[a].find('SPANFI')!=-1:
                            spanfi.append(float(lines[a][lines[a].find('SPANFI')+7:lines[a].find(',',lines[a].find('SPANFI'))]))
                    b = b+1
            if lines[n].find('$WGPLNF')!=-1:
                lines[n] = lines[n].replace('$',',')
                a = n
                while lines[a].find('$')==-1:
                    if lines[a].find('CHRDR')!=-1:
                        chrdr = float(lines[a][lines[a].find('CHRDR')+6:lines[a].find(',',lines[a].find('CHRDR'))])
                    if lines[a].find('CHRDTP')!=-1:
                        chrdtp = float(lines[a][lines[a].find('CHRDTP')+7:lines[a].find(',',lines[a].find('CHRDTP'))])
                    if lines[a].find('SSPN=')!=-1:
                        span = float(lines[a][lines[a].find('SSPN=')+5:lines[a].find(',',lines[a].find('SSPN='))])*2
                    a = a+1
                if lines[a].find('CHRDR')!=-1:
                    chrdr = float(lines[a][lines[a].find('CHRDR')+6:lines[a].find(',',lines[a].find('CHRDR'))])
                if lines[a].find('CHRDTP')!=-1:
                    chrdtp = float(lines[a][lines[a].find('CHRDTP')+7:lines[a].find(',',lines[a].find('CHRDTP'))])
                if lines[a].find('SSPN=')!=-1:
                    span = float(lines[a][lines[a].find('SSPN=')+5:lines[a].find(',',lines[a].find('SSPN='))])*2
                cbar = (chrdr+chrdtp)/2
                area = cbar*span
            
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
#                print name
#                print control
                for c in range(2,len(coef)):
                    coef[c] = coef[c]+'_'+name+'_'+control
#                print coef
                self.coefname.append(coef)
                pos = 0
                for k in range(1,len(coef)-1):
                    if coef[k+1] == 'D_CL_W_SYMFLP' or coef[k+1] == 'D_CL_H_SYMFLP' or coef[k+1] == 'D_CM_W_SYMFLP' or coef[k+1] == 'D_CM_H_SYMFLP' or coef[k-1] == 'DELTAL':
                        extra.append('    '+coef[k+1]+'.data=\n    {\n')
#                        print coef[k+1]
#                    elif coef[k+1]=='CLQ_H_SYMFLP' or coef[k+1]=='CLAD_H_SYMFLP' or coef[k+1]=='D_CL_H_SYMFLP' or coef[k+1]=='CD_H_SYMFLP' or coef[k+1]=='CYB_H_SYMFLP' or coef[k+1]=='CYP_H_SYMFLP' or coef[k+1]=='CLB_H_SYMFLP' or coef[k+1]=='CLP_H_SYMFLP' or coef[k+1]=='CLR_H_SYMFLP' or coef[k+1]=='CNB_H_SYMFLP' or coef[k+1]=='CNP_H_SYMFLP' or coef[k+1]=='CNR_H_SYMFLP' or coef[k+1]=='CMQ_H_SYMFLP' or coef[k+1]=='CMAD_H_SYMFLP' or coef[k+1]=='D_CM_H_SYMFLP':
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
                        if coef[k+1] == 'D_CL_W_SYMFLP' or coef[k+1] == 'D_CL_H_SYMFLP' or coef[k+1] == 'D_CM_W_SYMFLP' or coef[k+1] == 'D_CM_H_SYMFLP':
                            extra.append('      {%6.2f' % float(lines[a].split()[0]))
                        elif coef[k-1] == 'DELTAL':
                            f = float(lines[a].split()[0])*2
                            extra.append('      {%6.2f' % f)
#                        elif coef[k+1]=='CLQ_H_SYMFLP' or coef[k+1]=='CLAD_H_SYMFLP' or coef[k+1]=='D_CL_H_SYMFLP' or coef[k+1]=='CD_H_SYMFLP' or coef[k+1]=='CYB_H_SYMFLP' or coef[k+1]=='CYP_H_SYMFLP' or coef[k+1]=='CLB_H_SYMFLP' or coef[k+1]=='CLP_H_SYMFLP' or coef[k+1]=='CLR_H_SYMFLP' or coef[k+1]=='CNB_H_SYMFLP' or coef[k+1]=='CNP_H_SYMFLP' or coef[k+1]=='CNR_H_SYMFLP' or coef[k+1]=='CMQ_H_SYMFLP' or coef[k+1]=='CMAD_H_SYMFLP' or coef[k+1]=='D_CM_H_SYMFLP':
#                            extra.append('      {%6.2f' % float(lines[a].split()[0]))
                        # handle columns correctly
                        if lines[a][pos:(pos+len(lines[beg].split()[k]))]==' '*len(lines[beg].split()[k]):
                            lines[a] = lines[a][0:pos-1]+' '+lines[beg].split()[k]+' '+lines[a][(pos+len(lines[beg].split()[k])+1):len(lines[a])]
                        # write within row
                        if lines[a].split()[k]=='NDM': # write zero for NDM
                            lines[a] = lines[a].replace('NDM','0.000',1)
                        data.append(', %10.3e}' % float(lines[a].split()[k]))
                        if coef[k+1] == 'D_CL_W_SYMFLP' or coef[k+1] == 'D_CL_H_SYMFLP' or coef[k+1] == 'D_CM_W_SYMFLP' or coef[k+1] == 'D_CM_H_SYMFLP':
                            f = float(lines[a].split()[k])/2
                            extra.append(', %10.3e}' % f)
                        elif coef[k-1] == 'DELTAL':
                            extra.append(', %10.3e}' % float(lines[a].split()[k]))
#                        elif coef[k+1]=='CLQ_H_SYMFLP' or coef[k+1]=='CLAD_H_SYMFLP' or coef[k+1]=='D_CL_H_SYMFLP' or coef[k+1]=='CD_H_SYMFLP' or coef[k+1]=='CYB_H_SYMFLP' or coef[k+1]=='CYP_H_SYMFLP' or coef[k+1]=='CLB_H_SYMFLP' or coef[k+1]=='CLP_H_SYMFLP' or coef[k+1]=='CLR_H_SYMFLP' or coef[k+1]=='CNB_H_SYMFLP' or coef[k+1]=='CNP_H_SYMFLP' or coef[k+1]=='CNR_H_SYMFLP' or coef[k+1]=='CMQ_H_SYMFLP' or coef[k+1]=='CMAD_H_SYMFLP' or coef[k+1]=='D_CM_H_SYMFLP':
#                            extra.append(', %10.3e}' % float(lines[a].split()[k]))
                        a = a+1
                        if lines[a][0]=='0' or lines[a][0]=='1' or lines[a].split()[k]=='NA': # end of table
                            data.append('\n    },\n')
                            if coef[k+1] == 'D_CL_W_SYMFLP' or coef[k+1] == 'D_CL_H_SYMFLP' or coef[k+1] == 'D_CM_W_SYMFLP' or coef[k+1] == 'D_CM_H_SYMFLP' or coef[k-1] == 'DELTAL':
                                extra.append('\n    },\n')
#                            elif coef[k+1]=='CLQ_H_SYMFLP' or coef[k+1]=='CLAD_H_SYMFLP' or coef[k+1]=='D_CL_H_SYMFLP' or coef[k+1]=='CD_H_SYMFLP' or coef[k+1]=='CYB_H_SYMFLP' or coef[k+1]=='CYP_H_SYMFLP' or coef[k+1]=='CLB_H_SYMFLP' or coef[k+1]=='CLP_H_SYMFLP' or coef[k+1]=='CLR_H_SYMFLP' or coef[k+1]=='CNB_H_SYMFLP' or coef[k+1]=='CNP_H_SYMFLP' or coef[k+1]=='CNR_H_SYMFLP' or coef[k+1]=='CMQ_H_SYMFLP' or coef[k+1]=='CMAD_H_SYMFLP' or coef[k+1]=='D_CM_H_SYMFLP':
#                                extra.append('\n    },\n')
                            break
                        else:
                            data.append(',\n')
                            if coef[k+1] == 'D_CL_W_SYMFLP' or coef[k+1] == 'D_CL_H_SYMFLP' or coef[k+1] == 'D_CM_W_SYMFLP' or coef[k+1] == 'D_CM_H_SYMFLP' or coef[k-1] == 'DELTAL':
                                extra.append(',\n')
#                            elif coef[k+1]=='CLQ_H_SYMFLP' or coef[k+1]=='CLAD_H_SYMFLP' or coef[k+1]=='D_CL_H_SYMFLP' or coef[k+1]=='CD_H_SYMFLP' or coef[k+1]=='CYB_H_SYMFLP' or coef[k+1]=='CYP_H_SYMFLP' or coef[k+1]=='CLB_H_SYMFLP' or coef[k+1]=='CLP_H_SYMFLP' or coef[k+1]=='CLR_H_SYMFLP' or coef[k+1]=='CNB_H_SYMFLP' or coef[k+1]=='CNP_H_SYMFLP' or coef[k+1]=='CNR_H_SYMFLP' or coef[k+1]=='CMQ_H_SYMFLP' or coef[k+1]=='CMAD_H_SYMFLP' or coef[k+1]=='D_CM_H_SYMFLP':
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
                coef = coef+'2D_'+name+'_'+control
#                for c in range(2,len(coef)):
#                    coef[c] = coef[c]+'_'+name
                self.coefname.append([coef])
#                data.append(',\n    %s.tableOnFile=false,\n' % coef)
                data.append('    '+coef+'.data = transpose(\n    {\n')
                lines[n] = lines[n].replace(lines[n][0:(lines[n].find('=')+1)],'0 ')
                data.append('      {')
                if coef == 'D_CDI2D_H_SYMFLP' or coef == 'D_CDI2D_W_SYMFLP':
                    extra.append('    '+coef+'.data = transpose(\n    {\n')
                    extra.append('      {')
#                elif coef == 'D_CDI2D_H_SYMFLP' or coef == 'CN_W_ASYFLP':
#                    extra.append('    '+coef+'.data = transpose(\n    {\n')
#                    extra.append('      {')
                for i in lines[n].split():
                    if coef == 'D_CDI2D_H_SYMFLP' or coef == 'D_CDI2D_W_SYMFLP':
                        extra.append('%10.2f, ' % float(i))
#                    elif coef == 'D_CDI_H_SYMFLP' or coef == 'CN_W_ASYFLP':
#                        extra.append('%10.2f, ' % float(i))
                    data.append('%10.2f, ' % float(i))
                if coef == 'D_CDI2D_H_SYMFLP' or coef == 'D_CDI2D_W_SYMFLP':
                    extra[len(extra)-1] = extra[len(extra)-1].replace(', ','},\n')
#                elif coef == 'D_CDI_H_SYMFLP' or coef == 'CN_W_ASYFLP':
#                    extra[len(extra)-1] = extra[len(extra)-1].replace(', ','},\n')
                data[len(data)-1] = data[len(data)-1].replace(', ','},\n')
                a = n+3
                while lines[a][0]!='0':
                    if coef == 'D_CDI2D_H_SYMFLP' or coef == 'D_CDI2D_W_SYMFLP':
                        extra.append('      {')
#                    elif coef == 'D_CDI_H_SYMFLP' or coef == 'CN_W_ASYFLP':
#                        extra.append('      {')
                    data.append('      {')
                    for i in lines[a].split():
                        if i > 0 and (coef == 'D_CDI2D_H_SYMFLP' or coef == 'D_CDI2D_W_SYMFLP'):
                            f = float(i)/2
                            extra.append('%10.3e, ' % f)
                        elif i==0:
                            extra.append('%10.3e, ' % float(i))
#                        elif coef == 'D_CDI_H_SYMFLP' or coef == 'CN_W_ASYFLP':
#                            extra.append('%10.3e, ' % float(i))
                        data.append('%10.3e, ' % float(i))
                    if coef == 'D_CDI2D_H_SYMFLP' or coef == 'D_CDI2D_W_SYMFLP':
                        extra[len(extra)-1] = extra[len(extra)-1].replace(', ','},\n')
                    data[len(data)-1] = data[len(data)-1].replace(', ','},\n')
                    a = a+1
                if coef == 'D_CDI2D_H_SYMFLP' or coef == 'D_CDI2D_W_SYMFLP':
                    extra[len(extra)-1] = extra[len(extra)-1].replace('\n','') 
                    extra[len(extra)-1] = extra[len(extra)-1].replace(',','\n    }),\n')
                data[len(data)-1] = data[len(data)-1].replace('\n','') 
                data[len(data)-1] = data[len(data)-1].replace(',','\n    }),\n')
        total = '_'+name+'_'+control
#        dist = []
##        print chrdfi
##        print chrdfo
##        print spanfi
##        print spanfo
#        for i in range(len(chrdfi)/2):
#            dist.append((chrdfi[i]+2*chrdfo[i])/3/(chrdfi[i]+chrdfo[i])*(spanfo[i]-spanfi[i]))
        with open(self.filename_out, 'w') as table:
            table.write('model AerodynamicsDatcom_'+self.modelica_name+'\n  extends AerodynamicsDatcom(\n')
            table.write('    cBar = %4.2f,\n' % cbar)
            table.write('    b = %4.2f,\n' % span)
            table.write('    s = %4.2f,\n' % area)
            table.write('    CL.data = {{0,0},{1,0}},\n')
            table.write('    CLa.data = {{0,0},{1,0}},\n')
            table.write('    CLq.data = {{0,0},{1,0}},\n')
            table.write('    CLad.data = {{0,0},{1,0}},\n')
            table.write('    CLdF1L.data = {{0,0},{1,0}},\n')
            table.write('    CLdF2L.data = {{0,0},{1,0}},\n')
            table.write('    CLDe.data = {{0,0},{1,0}},\n')
            table.write('    CD.data = {{0,0},{1,0}},\n')
            table.write('    CdDf1L.data = {{0,0},{1,0}},\n')
            table.write('    CdDf2L.data = {{0,0},{1,0}},\n')
            table.write('    CdDe.data = {{0,0},{1,0}},\n')
            table.write('    Cyb.data = {{0,0},{1,0}},\n')
            table.write('    Cyp.data = {{0,0},{1,0}},\n')
            table.write('    Clb.data = {{0,0},{1,0}},\n')
            table.write('    Clp.data = {{0,0},{1,0}},\n')
            table.write('    Clr.data = {{0,0},{1,0}},\n')
            table.write('    ClDs4.data = {{0,0},{1,0}},\n')
            table.write('    Cnb.data = {{0,0},{1,0}},\n')
            table.write('    Cnp.data = {{0,0},{1,0}},\n')
            table.write('    Cnr.data = {{0,0},{1,0}},\n')
            table.write('    CnDa.data = {{0,0},{1,0}},\n')
            table.write('    Cm.data = {{0,0},{1,0}},\n')
            table.write('    Cma.data = {{0,0},{1,0}},\n')
            table.write('    Cmq.data = {{0,0},{1,0}},\n')
            table.write('    Cmadot.data = {{0,0},{1,0}},\n')
            table.write('    CmDe.data = {{0,0},{1,0}},\n')
            table.write('    CmDf1L.data = {{0,0},{1,0}},\n')
            table.write('    CmDf2L.data = {{0,0},{1,0}},\n')

            for l in range(len(data)):
                if data[l].find('CLQ'+total)!=-1:
                    data[l] = data[l].replace('CLQ'+total,'CLq')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('D_CL_H_SYMFLP')!=-1:
                    data[l] = data[l].replace('D_CL_H_SYMFLP','CLDe')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('D_CM_H_SYMFLP')!=-1:
                    data[l] = data[l].replace('D_CM_H_SYMFLP','CmDe')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find(' CL'+total)!=-1:
                    data[l] = data[l].replace('CL'+total,'CL')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CLA'+total)!=-1:
                    data[l] = data[l].replace('CLA'+total,'CLa')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find(' CM'+total)!=-1:
                    data[l] = data[l].replace('CM'+total,'Cm')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CMA'+total)!=-1:
                    data[l] = data[l].replace('CMA'+total,'Cma')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CLAD'+total)!=-1:
                    data[l] = data[l].replace('CLAD'+total,'CLad')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CD'+total)!=-1:
                    data[l] = data[l].replace('CD'+total,'CD')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('D_CDI2D_H_SYMFLP')!=-1:
                    data[l] = data[l].replace('D_CDI2D_H_SYMFLP','CdDe')
                    a = l
                    while data[a].find('\n    }),\n')==-1:
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CYB'+total)!=-1:
                    data[l] = data[l].replace('CYB'+total,'Cyb')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CYP'+total)!=-1:
                    data[l] = data[l].replace('CYP'+total,'Cyp')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CLB'+total)!=-1:
                    data[l] = data[l].replace('CLB'+total,'Clb')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CLP'+total)!=-1:
                    data[l] = data[l].replace('CLP'+total,'Clp')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CLR'+total)!=-1:
                    data[l] = data[l].replace('CLR'+total,'Clr')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CNB'+total)!=-1:
                    data[l] = data[l].replace('CNB'+total,'Cnb')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CNP'+total)!=-1:
                    data[l] = data[l].replace('CNP'+total,'Cnp')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CNR'+total)!=-1:
                    data[l] = data[l].replace('CNR'+total,'Cnr')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CN2D_W_ASYFLP')!=-1:
                    data[l] = data[l].replace('CN2D_W_ASYFLP','CnDa')
                    a = l
                    while data[a].find('\n    }),\n')==-1:
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CMQ'+total)!=-1:
                    data[l] = data[l].replace('CMQ'+total,'Cmq')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])
                elif data[l].find('CMAD'+total)!=-1:
                    data[l] = data[l].replace('CMAD'+total,'Cmad')
                    a = l
                    while data[a]!='\n    },\n':
                        table.write(data[a])
                        a = a+1
                    table.write(data[a])

            for line in extra:
                line = line.replace('D_CL_H_SYMFLP','CLdF1L')
                line = line.replace('D_CL_W_SYMFLP','CLdF2L')
                line = line.replace('D_CM_H_SYMFLP','CmdF1L')
                line = line.replace('D_CM_W_SYMFLP','CmdF2L')
                line = line.replace('D_CDI2D_H_SYMFLP','CdDf1L')
                line = line.replace('D_CDI2D_W_SYMFLP','CdDf2L')
                line = line.replace('CL_ROLL_W_ASYFLP','ClDs4')
                table.write(line)
            table.write('    CLdF1R.data = CLdF1L.data,\n    CLdF2R.data = CLdF2L.data,\n    CdDf1R.data = CdDf1L.data,\n    CdDf2R.data = CdDf2L.data,\n')
            table.write('    CmDf1R.data = CmDf1L.data,\n    CmDf2R.data = CmDf2L.data,\n')
#            table.write('    CldF1 = %4.3f, //Guess Value\n' % dist[0])
#            table.write('    CldF2 = %4.3f, //Guess Value\n' % dist[1])
#            table.write('    CnDf1 = %4.3f, //Guess Value\n' % dist[0])
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

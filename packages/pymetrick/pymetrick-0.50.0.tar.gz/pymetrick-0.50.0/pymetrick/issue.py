#!/usr/bin/env python3.6
# -*- coding: iso-8859-1 -*-

# This file is part of Pymetrick.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

"""Modulo para emitir documentos"""
from __future__ import division, with_statement
from pymetrick import version
__author__ = version.__author__
__copyright__ = version.__copyright__
__license__ = version.__license__
__version__ = version.__version__
__date__ = '2019-09-08'
__modify__ = '2019-09-08'
__credits__ = ''
__text__ = 'Issue documents'
__file__ = 'issue.py'

#--- CHANGES ------------------------------------------------------------------
# 2019-09-08 v0.50.0 PL: - First version




import os, sys, zlib, struct, re, tempfile, struct
from datetime import datetime
from functools import wraps
import math
import errno

from pymetrick.fpdf import FPDF

from pymetrick.ttfonts import TTFontFile
from pymetrick.fonts import fpdf_charwidths
from pymetrick.php import substr, sprintf, print_r, UTF8ToUTF16BE, UTF8StringToArray
from pymetrick.py3k import PY3K, pickle, urlopen, Image, basestring, unicode, exception, b, hashpath

class Order(FPDF):

    def config(self,*args,**kwargs):
        ''' * logo          text  imagen logotipo
            * letterhead    list  membrete
            * client        list  datos de cliente
            * title         text  tipo de documento
            * title_head    list  titulo columnas
            * title_line    list  datos de documento
            * body_head     list  titulo columnas
              body_line     dict  lineas detalle
            * footer_head   list  titulos pie
              footer_line   dict  lineas pie
            * terms_of_sale text  Condiciones
            * authorization text  autorizacion legal
        '''
        self.allowed_data = {'logo':'','letterhead':list(),'client':list(),'title':'','title_head':list(),'title_line':list(),'body_head':list(),'footer_head':list(),'terms_of_sale':'','authorization':''}
        for n in list(kwargs.keys()):
            if n in self.allowed_data:
                self.allowed_data[n] = kwargs[n]

        # Add page
        self.add_page()


    def header(self):
        # lineas
        self.set_line_width(width=0.03)
        self.rounded_rect(100,12,105,35.5,0.9)     # datos cliente
        self.rounded_rect(10,49,195,9.5,0.5)       # datos documento
        self.set_line_width(width=0.1)
        self.rounded_rect(10,60,195,193.5,0.5)     # detalle pedido
        self.set_line_width(width=0.07)
        self.line(11,65,204,65)
        self.set_line_width(width=0.1)
        self.rounded_rect(10,255,195,25,0.5)       # total pedido
        self.set_line_width(width=0.07)
        self.line(11,260,204,260)
        self.set_line_width(width=0.1)
        # sombras
        self.line(205.3,13,205.3,47)
        self.line(205.3,50,205.3,57)
        self.line(205.3,61,205.3,251)
        self.line(205.3,256,205.3,279)

        # Logo
        self.image(self.allowed_data['logo'], 10, 8, 20)
        # Arial bold 15
        self.set_font('Arial', '', 6)
        # letterhead = ['RAZON SOCIAL','DIRECCION','COD.POSTAL-LOCALIDAD','PROVINCIA','CIF','TELEFONO','PAGINA WEB','CORREO_ELECTRONICO']
        nY = 15
        for n in self.allowed_data['letterhead']:
            if nY == 15:
                self.set_font('Arial','B',8)
            else:
                self.set_font('Arial','',6)
            self.text(33, nY, n)
            nY += 3
        # client = ['RAZON SOCIAL','DIRECCION','COD.POSTAL-LOCALIDAD','PROVINCIA','CIF','TELEFONO','PAGINA WEB','CORREO_ELECTRONICO']
        nY = 15
        for n in self.allowed_data['client']:
            self.text(103, nY, n)
            nY += 3
        # title
        self.set_font('Arial','B',10);
        self.text(11,46,self.allowed_data['title'])
        self.set_font('Courier','',8);
        # registro
        self.rotateText(8,250,self.allowed_data['authorization'],90)

        # textos
        self.set_font('Courier','',8);
        # title_head 'NUM.ALBARAN    FECHA'
        self.text(11,52,self.allowed_data['title_head'])
        # title_line '2017000100    07/11/2017'
        self.text(11,55,self.allowed_data['title_line'])
        self.set_font('Courier','B',8);
        #  body_head '{0:^5s} {1:^13s} {2:^38s} {3:^8s} {4:^5s} {5:^8s} {6:^10s} {7:^4s}% {8:^3s} {9:^13s}'.format('REF.','EAN13','PRODUCTO','PZS/CAJA','CAJAS','UNIDADES','PRECIO','DTO.','IVA','IMPORTE')
        self.text(11,64,self.allowed_data['body_head'])
        self.set_font('Courier','',8);
        # footer_head '{0:^1s} {1:^9s} {2:^6s}% {3:^8s} {4:^9s} {5:^5s}% {6:^7s} {7:^5s}% {8:^9s} {9:^9s}'.format(' ','Imp.Neto','Dto.','Imp.Dto.','Base Imp.','IVA','Imp.IVA','R.EQ.','Imp.R.EQ.','Total')
        self.text(11,258,self.allowed_data['footer_head'])
        # configurar documento
        self.set_title(self.allowed_data['title'])
        self.set_author(self.allowed_data['letterhead'][0])
        self.set_creator('pymetrick')

        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 7
        self.set_font('Arial', 'I', 7)
        # Page number
        self.cell(0, 5, 'Pagina ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        # Terms
        self.set_y(-12)
        self.set_font('Arial','', 5)
        self.multi_cell( w=200, h=3, txt=self.allowed_data['terms_of_sale'], border = 0, align = 'J', fill = False, split_only=False)

    def rotateText(self,x,y,txt,angle):
        #Text rotated around its origin
        self.rotate(angle,x,y)
        self.text(x,y,txt)
        self.rotate(0)

    def rotateImage(self,file,x,y,w,h,angle):
        #Image rotated around its upper-left corner
        self.rotate(angle,x,y)
        self.image(file,x,y,w,h)
        self.rotate(0)

    def rounded_rect(self,x, y, w, h, r,corners='1234',style=''):
        "Draw a rounded rectangle"
        if(style=='F'):
            op='f'
        elif(style=='FD' or style=='DF'):
            op='B'
        else:
            op='S'

        myArc = 4/3 * (math.sqrt(2) - 1);
        self._out(sprintf('%.2f %.2f m',(x+r)*self.k,(self.h-y)*self.k ))

        xc = x+w-r;
        yc = y+r;
        self._out(sprintf('%.2f %.2f l', xc*self.k,(self.h-y)*self.k ))
        if (corners.find('2') < 0):
            self._out(sprintf('%.2f %.2f l', (x+w)*self.k,(self.h-y)*self.k ))
        else:
            self._arc(xc + r*myArc, yc - r, xc + r, yc - r*myArc, xc + r, yc)

        xc = x+w-r;
        yc = y+h-r;
        self._out(sprintf('%.2f %.2f l',(x+w)*self.k,(self.h-yc)*self.k));
        if (corners.find('3') < 0):
            self._out(sprintf('%.2f %.2f l',(x+w)*self.k,(self.h-(y+h))*self.k));
        else:
            self._arc(xc + r, yc + r*myArc, xc + r*myArc, yc + r, xc, yc + r)

        xc = x+r;
        yc = y+h-r;
        self._out(sprintf('%.2f %.2f l',xc*self.k,(self.h-(y+h))*self.k));
        if (corners.find('4') < 0):
            self._out(sprintf('%.2f %.2f l',(x)*self.k,(self.h-(y+h))*self.k))
        else:
            self._arc(xc - r*myArc, yc + r, xc - r, yc + r*myArc, xc - r, yc)

        xc = x+r ;
        yc = y+r;
        self._out(sprintf('%.2f %.2f l',(x)*self.k,(self.h-yc)*self.k ))
        if (corners.find('1') < 0):
            self._out(sprintf('%.2f %.2f l',(x)*self.k,(self.hp-y)*self.k ))
            self._out(sprintf('%.2f %.2f l',(x+r)*self.k,(self.h-y)*self.k ))
        else:
            self._arc(xc - r, yc - r*myArc, xc - r*myArc, yc - r, xc, yc - r)
        self._out(op);

    def _arc(self, x1, y1, x2, y2, x3, y3):
        h = self.h
        self._out(sprintf('%.2f %.2f %.2f %.2f %.2f %.2f c', x1*self.k, (h-y1)*self.k,
            x2*self.k, (h-y2)*self.k, x3*self.k, (h-y3)*self.k))

    # EAN14 and UPC-A
    def EAN13(self, x, y, barcode_, h=16, w=.35):
        self.__barcode__(x,y,barcode_,h,w,13)

    def UPC_A(self, x, y, barcode_, h=16, w=.35):
        self.__barcode__(x,y,barcode_,h,w,12)

    def getCheckDigit(self, barcode_):
        # Compute the check digit
        sum=0
        for i in range(1,12,2):
            sum += 3*int(barcode_[i])
        for i in range(0,11,2):
            sum+=int(barcode_[i])
        r=sum%10
        if(r>0):
            r=10-r
        return str(r)

    def testCheckDigit(self, barcode_):
        #Test validity of check digit
        sum=0
        for i in range(1,12,2):
            sum += 3*int(barcode_[i])
        for i in range(0,11,2):
            sum += int(barcode_[i])
        return (sum+int(barcode_[-1:]))%10==0

    def __barcode__(self, x, y, barcode_, h, w, lng):
        # Padding
        barcode_=barcode_.rjust(lng-1,'0')
        if lng==12:
            barcode_ = '0' + barcode_
        # Add or control the check digit
        if len(barcode_) == 12:
            barcode_ += self.getCheckDigit(barcode_)
        elif not self.testCheckDigit(barcode_):
            self.error('Incorrect check digit')
        #Convert digits to bars
        codes={
            'A':{
                '0':'0001101','1':'0011001','2':'0010011','3':'0111101','4':'0100011',
                '5':'0110001','6':'0101111','7':'0111011','8':'0110111','9':'0001011'},
            'B':{
                '0':'0100111','1':'0110011','2':'0011011','3':'0100001','4':'0011101',
                '5':'0111001','6':'0000101','7':'0010001','8':'0001001','9':'0010111'},
            'C':{
                '0':'1110010','1':'1100110','2':'1101100','3':'1000010','4':'1011100',
                '5':'1001110','6':'1010000','7':'1000100','8':'1001000','9':'1110100'}
            }
        parities={
            '0':['A','A','A','A','A','A'],
            '1':['A','A','B','A','B','B'],
            '2':['A','A','B','B','A','B'],
            '3':['A','A','B','B','B','A'],
            '4':['A','B','A','A','B','B'],
            '5':['A','B','B','A','A','B'],
            '6':['A','B','B','B','A','A'],
            '7':['A','B','A','B','A','B'],
            '8':['A','B','A','B','B','A'],
            '9':['A','B','B','A','B','A']
            }
        code_='101';
        p=parities[barcode_[0]]
        for i in range(1,7):
            code_ +=codes[p[i-1]][barcode_[i]]
        code_ +='01010'
        for i in range(7,13):
            code_ +=codes['C'][barcode_[i]]
        code_ +='101'
        #Draw bars
        for i in range(0,len(code_)):
            if code_[i]=='1':
                self.rect(x+i*w,y,w,h,'F')
        #Print text uder barcode
        self.set_font('Arial','',12);
        self.text(x,y+h+11/self.k,barcode_[-lng:])


if __name__ == "__main__":
    print ('''copyright {0}'''.format( __copyright__))
    print ('''license {0}'''.format( __license__))
    print ('''version {0}'''.format( __version__))
    if len(sys.argv) < 2:
        sys.stderr.write("For help use -h o --help")
    elif sys.argv[1]=='-h' or sys.argv[1]=='--help':
        print ('''
               Issue documents ''')
    

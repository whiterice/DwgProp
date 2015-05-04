import sys
import os.path
import re
import argparse
import csv

DWG_List=[]

class DWG:
        'Common Base Class for all Equipment'

        def __init__(self, DWGNAM, SEC, SUBSEC, SH,
                     SHDWGNAM, IEC_P, IEC_I, IEC_L, DWGDESC1,
                     DWGDESC2, DWGDESC3, FULLFILENAME):

            self.DWGNAM = DWGNAM
            self.SEC = SEC
            self.SUBSEC = SUBSEC
            self.SH = SH
            self.SHDWGNAM = SHDWGNAM
            self.IEC_P = IEC_P
            self.IEC_I = IEC_I
            self.IEC_L = IEC_L
            self.DWGDESC1 = DWGDESC1
            self.DWGDESC2 = DWGDESC2
            self.DWGDESC3 = DWGDESC3
            self.FULLFILENAME = FULLFILENAME

        def __str__(self):
            names = ('DWGNAM',
                   'SEC',
                   'SUBSEC',
                   'SH',
                   'SHDWGNAM',
                   'IEC_P',
                   'IEC_I',
                   'IEC_L',
                   'DWGDESC1',
                   'DWGDESC2',
                   'DWGDESC3',
                   'FULLFILENAME',)
            out = []
            for n in names:
                v = getattr(self, n)
                out.append("{name:<30} : {value:>30}\n".format(name=n, value=v))
            out.append('{}\n'.format('*' * 63))

            return ''.join(out)
            
        def DisplayEquipment(self):
            print str(self)



def get_data(myfile):
    i=0
    with open(myfile, 'rb') as csvfile:
        FileReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in FileReader:
            if i == 0:
                Heading = row
            else:
                if (len(row[0]) > 2):
                    DWG_List.append(Equipment(row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[10], row[11]))
                else:
                    pass
            i = i+1


def main():

    parser = argparse.ArgumentParser(description='Cleans DWG Properties once Exported from AutoCAD')
    parser.add_argument('DWG_File', help='DWG Properties File Name (.xls)')
    args = parser.parse_args()

    get_data(args.DWG_File)
    
if __name__ == '__main__':
    main()
    sys.exit()

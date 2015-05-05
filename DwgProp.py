import sys
import os.path
import argparse
import csv
import datetime as DT

DWG_List=[]
Heading=[]


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
                out.append(v)
                  
            return ''.join(out)
            
        def DisplayDWG(self):
            print str(self)



def get_csv(myfile):
    global Heading
    i=0
    with open(myfile, 'rb') as csvfile:
        FileReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in FileReader:
            if i == 0:
                Heading=row
                i=1
            else:
                if (len(row[0]) > 2):
                    DWG_List.append(DWG(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
                else:
                    pass


def push_csv(mylist):
    global Workbook_FileName
    Workbook_FileName = 'DWG Porperties[{:%Y-%m-%d_%H%M%S}].csv'.format(DT.datetime.now())
    
    with open(Workbook_FileName, 'wb') as csvfile:
        FileWriter = csv.writer(csvfile, delimiter=',', quotechar='|')
        
        FileWriter.writerow(Heading)
        for row in mylist:
             #print row
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
                v = getattr(row, n)
                out.append(v)
            #print out
            FileWriter.writerow(out)
            
def display_csv(mylist):
    for each in mylist:
        print each

def get_SHDWGNAM(mylist):
    for each in mylist:
        each.SHDWGNAM = each.DWGNAM.replace("D", "").replace("_", "")

def main():

    parser = argparse.ArgumentParser(description='Cleans DWG Properties once Exported from AutoCAD')
    parser.add_argument('DWG_File', help='DWG Properties File Name (.xls)')
    args = parser.parse_args()

    get_csv(args.DWG_File)
    get_SHDWGNAM(DWG_List)
    push_csv(DWG_List)


    print "\n...Complete \n\n{!s} Generated".format(Workbook_FileName)
    

if __name__ == '__main__':
    main()
    sys.exit()


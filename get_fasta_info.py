#!/bin/env python3
#-* coding = UTF-8 *-
# @Author = Huang Shixuan
import os
import argparse
class get_GC(object):
    '''This class is for counting GC % & length & scaffolds_num.'''
    def __init__(self):
        parser = argparse.ArgumentParser(description='This script is used to count GC % & length & scaffolds_num')
        parser.add_argument('-i','--input',required=True,help='Path of input')
        parser.add_argument('-o','--output',default='.',required=False,help='Path to output, default is .')
        args = parser.parse_args()
        self.input_gate = args.input
        self.na_ph = self.get_input()
        self.main(args.output)
    
    def get_input(self):
        na_ph = []
        for file in os.listdir(self.input_gate):
            name = os.path.basename(file).rsplit('.',1)[0]
            path = os.path.join(self.input_gate,file)
            na_ph.append([name,path])
        return na_ph

    def count(self,seq):
        total = len(seq)
        n = 0
        for i in seq:
            if i == 'G':
                n += 1
            elif i == 'C':
                n += 1
        gc = n / total * 100
        return gc,total

    def main(self,output):
        output_line = []
        for bsname,path in self.na_ph:
            the_seq = ''
            sca_num = 0
            for line in open(path):
                if '>' in line:
                    sca_num += 1
                    continue
                else:
                    the_seq += line.strip()
            gc,length = self.count(the_seq)
            output_line.append(f'{bsname}\t{gc}\t{length}\t{sca_num}\n')
        with open(f'{output}/seq_info.tsv','w') as f:
            f.writelines(output_line)


if __name__ == '__main__':
    get_GC()
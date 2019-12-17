import re
import sys
import json
import argparse
from os import path

class PredictionParser:
    def __init__(self):
        pass
    def parse_preds(self, pred_str, threshold=.5):
        if type(pred_str) is bytes:
            pred_str = pred_str.decode('utf-8')
        pred_str = pred_str.splitlines()
        preds = []
        patt = re.compile('.*%$')
        for i in range(len(pred_str)):
            if re.search(patt, pred_str[i]):
                info = re.split('[ :%]+',pred_str[i])
                coords = [
                    x for x in re.split('[, ]',pred_str[i+1])
                    if re.search(re.compile('^[0-9]+$'), x)
                ]
                if int(info[1])/100 < threshold:
                    continue
                if len(coords) < 4:
                    coords = [0,0,0,0]
                
                obj = {
                    'class': info[0],
                    'confidence': int(info[1]),
                    'coords': [
                        (coords[0],coords[1]),
                        (coords[2],coords[3])
                    ]
                }
                preds.append(obj)
        preds.sort(key=lambda x: x['confidence'], reverse=True)
        return preds

def p_args():
    p = argparse.ArgumentParser(description='Parse detected objects in image.')
    p.add_argument(
        '-f','--file',dest='f_in',action='store',default='./sample_in.txt',
        help='input file'
    )
    p.add_argument(
        '-o','--output',dest='f_out',action='store',default=None,
        help='output file'
    )
    p.add_argument(
        '-a','--append',dest='append',action='store_true',
        help='append to output file'
    )
    p.add_argument(
        '-t','--threshold',dest='threshold',action='store',default=50,
        help='confidence threshold'
    )
    p.add_argument(
        '-q','--quiet',dest='quiet',action='store_true',
        help='suppress output to stdout'
    )
    return p.parse_args()

if __name__ == '__main__':
    args = p_args()
    p = PredictionParser()

    f = open(args.f_in, "r")
    lines = f.read()
    f.close()

    parsed = p.parse_preds(lines, float(args.threshold))

    if not args.quiet:
        print(parsed)

    if args.f_out == None:
        exit(0)

    if args.append and path.exists(args.f_out):
            f = open(args.f_out, "a+")
            json.dump(parsed, f)
    else:
            f = open(args.f_out, "w")
            json.dump(parsed, f)
    f.close()

#!/usr/bin/env python

## Compatibility with Python 3
from __future__ import print_function

import sys
import numpy as np

def read_recognition_results(filename):
    if isinstance(filename, str):
        resfile = open(filename, 'r')
        lines = resfile.readlines()
        resfile.close()
    elif hasattr(filename, 'readlines'):
        lines = filename.readlines()
    
    results = dict()
    for ln in lines:
        # Skip empty lines
        ln = ln.strip()
        if 0 == len(ln):
            continue
        imgfn, res = ln.strip().split(' ')
        results[imgfn] = res.lower()
    return results


def check_code(res, ref):
    len_max = max(len(res), len(ref))
    len_min = min(len(res), len(ref))
    indicator = np.zeros((len_max,), dtype=np.bool)
    for idx in range(len_min):
        indicator[idx] = res[idx] == ref[idx]
    ind_str = ''.join(['1' if xx else '0' for xx in indicator])
    return indicator.sum(), len(indicator), ind_str

    
def accuracy_evaluation(results_fn, reference_fn, verbose=True):
    results = read_recognition_results(results_fn)
    references = read_recognition_results(reference_fn)
    imgs_res, imgs_ref = set(results.keys()), set(references.keys())
    imgs_both = imgs_res & imgs_ref
    indicators_all = list()
    correct, total = 0, 0
    for key in imgs_both:
        res, ref = results[key], references[key]
        tp, code_len, indicator = check_code(res, ref)
        total += code_len
        correct += tp
        indicators_all.append(key + ' ' + indicator)
        
    for key in (imgs_ref - imgs_both):
        total += len(references[key])

    accuracy = correct*100.0/total
    
    if verbose:
        print('\n\n' + '\n'.join(indicators_all))
        msg = "\nAccuracy: {correct}/{total} x 100% = {accuracy:6.2f}%"
        print(msg.format(correct=correct,
                         total=total,
                         accuracy=accuracy))
        
    return accuracy, correct, total, indicators_all


if __name__ == '__main__':
    if len(sys.argv) == 3:
        _ = accuracy_evaluation(sys.argv[1], sys.argv[2])
    else:
        print("Usage ", sys.argv[0],
              "your_results.txt barcodes_gt_train.txt")
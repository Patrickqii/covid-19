import pandas as pd
import os
def get_nucleotide(path):#统计基因序列中各碱基的数目（正负链）
    posi_chain={'A': 0, 'G': 0, 'C': 0, 'U': 0, 'T':0}
    neg_chain={'A': 0, 'G': 0, 'C': 0, 'U': 0}
    with open(path, 'r') as f:
        data=f.readlines()
    for i in range(1,len(data)):
        s=data[i]
        for j in range(len(s)-1):
            try:
                posi_chain[s[j]]+=1
            except BaseException:
                continue
    posi_chain['U']=posi_chain['T']
    neg_chain['A']=posi_chain['U']
    neg_chain['G']=posi_chain['C']
    neg_chain['C']=posi_chain['G']
    neg_chain['U']=posi_chain['A']
    del posi_chain['T']
    return posi_chain, neg_chain




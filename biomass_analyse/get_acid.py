import pandas as pd
import os
import re
def getacid(path):
    structual_pretein=['surface glycoprotein','envelope protein','membrane glycoprotein','nucleocapsid phosphoprotein']
    sp={}
    nsp={}
    is_stru=False
    sp_acidnum={}
    nsp_acidnum={}
    acid_list=['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    protein_name=''
    '''
    for i in range(len(acid_list)):
        sp[acid_list[i]]=0
        nsp[acid_list[i]]=0
    '''
    with open(path, 'r') as f:
        data=f.readlines()
    for i in range(len(data)):
        s=data[i]
        if(s.startswith('>')):
            protein_name=s.split("protein=")[1].split("]")[0]
            acid_num={}
            for i in range(len(acid_list)):
                acid_num[acid_list[i]] = 0
            if protein_name in structual_pretein:
                is_stru=True
                sp[protein_name]=acid_num
                sp_acidnum[protein_name]=0
            else:
                is_stru=False
                nsp[protein_name]=acid_num
                nsp_acidnum[protein_name]=0
        else:
            if is_stru:
                sp_acidnum[protein_name]+=len(s)-1
                for j in range(len(s)-1):#除去换行符
                    try:
                        sp[protein_name][s[j]]+=1
                    except BaseException:
                        sp_acidnum[protein_name]-=1
                        continue
            else:
                nsp_acidnum[protein_name]+=len(s)-1
                for j in range(len(s)-1):
                    try:
                        nsp[protein_name][s[j]]+=1
                    except BaseException:
                        nsp_acidnum[protein_name]-=1
                        continue

    return sp, nsp, sp_acidnum, nsp_acidnum



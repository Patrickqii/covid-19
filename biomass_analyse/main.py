import pandas as pd

import get_acid
from calculateS import *
import os

def get_VBOF(S):#根据返回的S来写出biomass式子
    res=''
    full_name = ['ala', 'arg', 'asn', 'asp', 'cys', 'glu', 'gln', 'gly', 'his', 'ile', 'leu', 'lys', 'met', 'phe',
                 'pro', 'ser', 'thr', 'trp', 'tyr', 'val']
    nuList=['ATP','CTP','GTP','UTP']
    for key,value in S.items():
        if key in full_name:
            if key=='ala':
                res+=str(value)+' ala_D[c] + '
            elif key=='gly':
                res+=str(value)+' gly[c] + '
            else:
                res+=str(value)+' '+key+'_L[c] + '
        elif key in nuList:
            if key=='ATP':
                res+=str(value)+' h2o[c] + '
            res+=str(value)+' '+key.lower()+'[c] + '
    res=res[:-2]
    res+=' -> '
    xishu_adp=S['ATP']-S['UTP']
    res+=str(xishu_adp)+' adp[c] + '+str(xishu_adp)+' h[c] + '+str(xishu_adp)+' pi[c] + '
    res+=str(S['PPi'])+' ppi[c]'
    return res

proteinpath = r'C:\Users\Administrator\Desktop\biomass_covid\data\sequence.txt'
'''
sp, nsp, sp_acid, nsp_acid = get_acid.getacid(path)
Csp={'surface glycoprotein': 120, 'envelope protein': 20, 'membrane glycoprotein': 456,'nucleocapsid phosphoprotein': 1000}
Cnsp={}
non_struc=['ORF1ab polyprotein','ORF1a polyprotein','ORF3a protein','ORF6 protein','ORF7a protein','ORF7b','ORF8 protein','ORF10 protein']
for item in non_struc:
    Cnsp[item]=62
#Cnsp={'ORF1ab polyprotein': 20, 'ORF1a polyprotein': 20, 'ORF3a protein': 20, 'ORF6 protein': 20, 'ORF7a protein': 20,
      #'ORF7b': 20, 'ORF8 protein': 20, 'ORF10 protein': 20}
'''
genepath = r'C:\Users\Administrator\Desktop\biomass_covid\data\genomic.fna'
S_initSeq=IntergrateS(genepath, proteinpath)
biomass_path=r'C:\Users\Administrator\Desktop\biomass_covid\biomass'
biomassS=get_VBOF(S_initSeq)
with open(biomass_path+'\\biomass.txt','w')as f:
    f.write(biomassS)
    f.close()
'''
posi_chain, neg_chain=get_nucleotide(path)

NTOT,GN,PTOT=stat_nucletide(1,posi_chain,neg_chain)
XTOT,GX,ATOT=stat_acid(Csp,Cnsp,sp,nsp,sp_acid,nsp_acid)
Mv=VirusMolarMass(GN,GX)
sn=CalcS(Mv,NTOT)
sx=CalcS(Mv,XTOT)
sp=CalcS(Mv,PTOT)
sa=CalcS(Mv,ATOT)
'''
path=r'C:\Users\Administrator\Desktop\biomass_covid\data'
Slist={}
virus_list=os.listdir(path)
for item in virus_list:#每一个变异株系
    if os.path.isdir(os.path.join(path,item)):
        Slist[item]=[]
        seqs=os.listdir(os.path.join(path,item))
        for seq_item in seqs:#每个变异株系中的每一个样本
            gene_path=os.path.join(os.path.join(path,item),seq_item+'\\'+seq_item+'.fasta')#基因序列
            protein_path=os.path.join(os.path.join(path,item),seq_item+'\\sequence.txt')#蛋白质序列
            s=IntergrateS(gene_path,protein_path)#计算各代谢物的系数
            Slist[item].append(s)
sl=pd.DataFrame(Slist['alpha'])
zunei={}
zujian= {}
#进行的组间与组内的比较
for key,value in Slist.items():
    sl=pd.DataFrame(Slist[key])
    zunei[key]=(sl-sl.mean())#/sl.mean()
    zunei[key].to_csv(key+'.csv')
    zujian[key]=sl.mean().tolist()
    biomassS=get_VBOF(Slist[key][0])
    with open(biomass_path+'\\biomass_'+key+'.txt','w')as f:
        f.write(biomassS)
        f.close()
zujian=pd.DataFrame(zujian).T
#zujian=(zujian-zujian.mean())#/zujian.mean()
zujian=(zujian-S_initSeq.values())
zujian.columns=sl.columns
zujian.to_csv('zujian.csv')

print('happy ending!')

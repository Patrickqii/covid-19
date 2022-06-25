from getaciddetails import *
from calculateS import *
import os
import numpy as np

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def multi_mass(more_mass, detail):
    for i in range(len(detail)):
        detail.iloc[i]=detail.iloc[i]*more_mass[i]
    return detail
more_mass=[89.1,174.2,132.1,133.1,121.2,147.1,146.2,75.1,155.2,131.2,131.2,146.2,149.2,165.2,115.1,105.1,119.1,204.2,181.2,117.1]
proteinpath = r'C:\Users\Administrator\Desktop\biomass_covid\data\sequence.txt'
path=r'C:\Users\Administrator\Desktop\biomass_covid\data'
sp_init, nsp_init, sp_acid_init, nsp_acid_init, acid_detail_init = getaciddetails(proteinpath)
acid_num={}
MoreMass={}#各个株系的样本的字典，字典内容为该株系所有样本氨基酸和核苷酸摩尔质量之和的list
AD={}
virus_list=os.listdir(path)
for item in virus_list:
    if os.path.isdir(os.path.join(path,item)):
        acid_num[item]=[]
        MoreMass[item]=[]
        AD[item]=[]
        seqs=os.listdir(os.path.join(path,item))
        for seq_item in seqs:
            gene_path = os.path.join(os.path.join(path, item), seq_item + '\\' + seq_item + '.fasta')
            protein_path=os.path.join(os.path.join(path,item),seq_item+'\\sequence.txt')
            sp,nsp,sp_acid,nsp_acid,acid_detail=getaciddetails(protein_path)
            AD[item].append(acid_detail)
            pro_acid=Merge(sp_acid,nsp_acid)#该样本中各蛋白质的氨基酸总数目
            acid_num[item].append(pro_acid)#每个变异株系的各个样本 的各蛋白质氨基酸数{alpha:[{protein1:num1;...},{},..]}
            posi_chain, neg_chain = get_nucleotide(gene_path)
            NTOT, GN, PTOT = stat_nucletide(1, posi_chain, neg_chain)
            XTOT, GX, ATOT = stat_acid(Csp, Cnsp, sp, nsp, sp_acid, nsp_acid)
            MoreMass[item].append(VirusMolarMass(GN,GX))
acid_detail_init=pd.DataFrame(acid_detail_init)
alpha_detail=pd.DataFrame(AD['alpha'][0]).sub(acid_detail_init)#相较于原始株系，变异株系样本各蛋白的各氨基酸与原始株系数量差异
#alpha_detail=multi_mass(more_mass,alpha_detail)
beta_detail=pd.DataFrame(AD['beta'][0]).sub(acid_detail_init)
#beta_detail=multi_mass(more_mass,beta_detail)
gamma_detail=pd.DataFrame(AD['gamma'][0]).sub(acid_detail_init)
#gamma_detail=multi_mass(more_mass,gamma_detail)
epsilon_detail=pd.DataFrame(AD['epsilon'][0]).sub(acid_detail_init)
#epsilon_detail=multi_mass(more_mass,epsilon_detail)
print('happy ending!')

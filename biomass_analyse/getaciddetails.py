def getaciddetails(path):
    structual_pretein=['surface glycoprotein','envelope protein','membrane glycoprotein','nucleocapsid phosphoprotein']
    sp={}#每个结构蛋白各氨基酸数目统计
    nsp={}#每个非结构蛋白各氨基酸数目统计
    is_stru=False
    sp_acidnum={}#结构蛋白总氨基酸数目
    nsp_acidnum={}#非结构蛋白氨基酸总数
    acid_list=['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    acid_detail={}#记录每个蛋白质中各个氨基酸数目情况{protein:{acid:num,...}}
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
            acid_detail[protein_name]={}
            for item in acid_list:
                acid_detail[protein_name][item]=0
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
                        acid_detail[protein_name][s[j]] += 1
                    except BaseException:#对于一些未知氨基酸的处理
                        sp_acidnum[protein_name]-=1
                        continue
            else:
                nsp_acidnum[protein_name]+=len(s)-1
                for j in range(len(s)-1):
                    try:
                        nsp[protein_name][s[j]]+=1
                        acid_detail[protein_name][s[j]] += 1
                    except BaseException:
                        nsp_acidnum[protein_name]-=1
                        continue

    return sp, nsp, sp_acidnum, nsp_acidnum, acid_detail

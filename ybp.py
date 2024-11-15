import numpy as np
import pandas as pd
import scipy.stats as stats
'''
根据fisher返回的p值列表，在验证集上生成对应的p值表
'''
def ybp(table, itemset, lslsp, typenum):
    lsybp = []
    table = table
    index = table.index
    columns = itemset
    typenum = typenum
    # print(itemset)
    # print(typenum)
    tablet = table.loc[:, 't'].values.tolist()

    strtablet= [str(num) for num in tablet]
    # print(strtablet)


    lsyballrt = []
    for rp in range(0, 2*len(itemset)):
        rps = []
        rpsp = []
        rs = []
        alpha = rp+1
        beta = 2*len(itemset)-rp+1
        # 使用 Beta 分布的 CDF 计算累积分布函数值
        for i in lslsp:
            p_value = i[1][rp]
            cdf_value = stats.beta.cdf(p_value, alpha, beta)
            rps.append(i[0][rp])
            rpsp.append(cdf_value)
            rs.append(i[1][rp])
        # print(rps,rpsp,rs)

        listybrt = []
        for i in index:
            minp = 2
            mint = 0
            mincolumns = '!'
            for j in range(0, len(rps)):
                columns = rps[j][:-1]
                flag = rps[j][-1]
                p=1
                if flag == '#' and table.loc[i][columns]> 0:
                    p = rpsp[j]
                if flag == '*' and table.loc[i][columns]== 0:
                    p = rpsp[j]
                if minp >p:
                    minp = p
                    mint = j
                    mincolumns = columns + flag
                # print(table.loc[i][columns])
            listybrt.append(typenum[mint])
        #     print('最小值',mint,minp,mincolumns)
        # print(listybrt)
        lsyballrt.append(listybrt)
    # print(lsyballrt)

    '''
    每个r样本类型的预测值
    [[0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    '''
    maxacr = -1
    maxr = 0
    for i in range(0,len(lsyballrt)):
        num = 0
        for j in range(0,len(strtablet)):
            if lsyballrt[i][j]==strtablet[j]:
                num = num+1
        acr = num/len(strtablet)

        if maxacr<acr:
            maxacr = acr
            maxr = i

    print(maxacr,maxr)

    return maxacr,maxr


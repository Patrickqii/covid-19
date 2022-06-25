# covid-19
some works about covid-19 in summer, 2022

getaciddetails.py：读取蛋白质序列文件，获取结构蛋白与非结构蛋白总氨基酸数目以及各氨基酸数目；
getnucleotide.py：读取基因序列文件，获取碱基总数目以及各碱基数目；
calculateS.py：计算各代谢物的系数；
main.py：计算原始株以及变异株各样本的biomass系数，并进行组内与组间比较；
analyse_acid_num.py：分析各变异株样本的摩尔质量以及氨基酸数目之间的差异；
graph_plot.R：绘制组内与组间系数差异热图；
save_biomass.m：将biomass存mat形式；
...
运行使用各毒株的biomass来进行代谢网络重构的工作，预测靶点
target_analyse.m：对运行的结果进行靶点分析，分析绝大部分特异性代谢网络中所预测的靶点；
target_compare.m：比较各变异株靶点预测结果的差异

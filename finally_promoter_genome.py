import pandas as pd
import math
# 根据谷子的GFF3文件提取和基因组文件提取谷子所有基因上游1000bp的DNA序列
# 提取其他区间x就把36和39行的1001和1000改成x+1和x

def f(x):
	return''.join(list(x))
	
def reverse_complement(seq):
  ntComplement = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
  RevSeqList = list(reversed(seq))
  RevComSeqList = [ntComplement[k] for k in RevSeqList]
  RevComSeq = ''.join(RevComSeqList)
  return RevComSeq
  
def y(x): # 这个y函数不调用，就是整行输出，把函数里的3个80改成60等其他数字，就是按照60等其他字符一行输出
	return '\n'.join([x[80*i:80*(i+1)] for i in range(math.ceil(len(x) / 80))])

out = open('chen.promoter.1000.fasta','w') # 生成的谷子全基因组的假定启动子DNA fasta文件
# 处理4.pro文件
df = pd.read_csv(r'Sitalica_312_v2.fa', header=None) # 谷子基因组文件（染色体DNA fasta序列那个）
df['chro'] = df[df[0].str.startswith('>')]
df = df.fillna(method='pad').rename(columns={0: 'seq'})
pro_4 = df[~(df.index.isin(df[df['seq'].str.startswith('>')].index))].groupby(['chro']).agg({'seq': f}).reset_index()
#pro_4.index = pro_4.index.str.slice(start=1)
#print(pro_4)
# 处理gff文件
gff = pd.read_csv('Sitalica_312_v2.2.gene.gff3',skiprows=3,  header=None, sep='\t') # 谷子GFF3文件，前三行是#开头的注释文件
gff = gff.rename(columns={k: v for k, v in enumerate(['chro', 'phy','m', 'start', 'stop', 'point','trend','phrase', 'ID'])})
gff1 = gff[gff.m.isin(['mRNA'])].loc[:, ['chro', 'm', 'start', 'stop', 'trend','ID']]
#print(gff1)

for v in gff1.values:
	if v[4] == '+':
		pro = pro_4[pro_4.chro.isin(['>'+v[0]])].loc[:,['seq']].iloc[0].str.slice(start=v[2]-1001,stop=v[2]-1)
		out.write('>'+v[5].split(';')[0].replace('ID=','').replace('.v2.2','')+'\n'+y(pro['seq'])+'\n')
	else:
		pro = pro_4[pro_4.chro.isin(['>'+v[0]])].loc[:,['seq']].iloc[0].str.slice(start=v[3],stop=v[3]+1000)
		out.write('>'+v[5].split(';')[0].replace('ID=','').replace('.v2.2','')+'\n'+y(reverse_complement(pro['seq']))+'\n')

# make by Chen Huilong!

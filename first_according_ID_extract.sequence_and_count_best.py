import math
# print('\n'.join(['chenhuilong']))
# 根据ID从fasta文件中提取ID对应的fasta文件

gene_name = open('id_Sb_13.TLP.txt') #your gene_family id

fasta_file = open('Sb.TLP.pro.13.3.fasta') #the whole genomes

out_file = open('Sb.TLP.pro.13.2.fasta','w') #the result file

chl_fasta = {}
gene = seq = ''
for row in fasta_file:
	row = row.strip()
	if row.startswith('>'):
		if gene != '' and seq != '':
			chl_fasta[gene] = seq
		gene = row.replace('>','')
		seq = ''
	else:
		seq += row	
chl_fasta[gene] = seq

count = 0
def y(x): # 这个y函数不调用，就是整行输出，把函数里的3个80改成60等其他数字，就是按照60等其他字符一行输出
	return '\n'.join([x[80*i:80*(i+1)] for i in range(math.ceil(len(x) / 80))])

for line in gene_name:
	my_gene = line.split()
	my_id = my_gene[0]
	if my_id in chl_fasta.keys():
		results = ">" + my_id + "\n" + y(chl_fasta[my_id]) + "\n"
		out_file.write(results)
		count += 1
print(count)
#make by Chen Huilong!

	
		
	
		

	

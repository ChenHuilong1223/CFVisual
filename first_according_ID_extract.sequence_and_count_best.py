import math
# print('\n'.join(['chenhuilong']))

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
	# print('\n'.join([x[80*i:80*(i+1)] for i in range(math.ceil(len(x) / 80))]))
	return '\n'.join([x[80*i:80*(i+1)] for i in range(math.ceil(len(x) / 80))])

for line in gene_name:
	my_gene = line.split()
	my_id = my_gene[0]
	if my_id in chl_fasta.keys():
		# out_file.write('>' + my_id + '\n')
		# for i in range(0,len(chl_fasta[my_id]),80):
		# 	out_file.write(chl_fasta[my_id][i:i+80] + '\n')
		# print(chl_fasta[my_id])
		results = ">" + my_id + "\n" + y(chl_fasta[my_id]) + "\n"
		out_file.write(results)
		count += 1
print(count)
#make by chenhuilong

	
		
	
		

	

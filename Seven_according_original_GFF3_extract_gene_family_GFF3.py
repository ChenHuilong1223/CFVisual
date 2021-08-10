your_file = open('Sitalica_312_v2.2.gene.gff3') #your original GFF3 txt
ID_file = open('Si.PME.Ordered.ID.txtt') #your gene id,Si1G000100.1
out_file = open('Si.PME.Structure.GFF3.txt', 'w') #out file

for line in ID_file:
	fsy = line.split()
	gene = fsy[0]
	for row in your_file:
		if gene.replace('Si','Seita.') in row: #or： if gene in row:
			result = row
			out_file.write(result)
	your_file.seek(0,0)

#make by Chen Huilong!	

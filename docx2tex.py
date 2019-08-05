import glob
import os
import csv
import docx

a = glob.glob("./*.docx")

for item in a:
	ss = os.path.basename(item)
	ss = ss.replace('.docx','')

	docmt=os.stat(item).st_mtime

	if os.path.isfile(ss+'.tex'):
		texmt=os.stat(ss+'.tex').st_mtime
		if docmt < texmt:
			print('no output:'+ss+'.tex')
			continue
		
	doc = docx.Document(item)
	res = open(ss+'.tex','w',encoding="utf-8_sig")
	for par in doc.paragraphs:
		res.write(par.text.replace('\xa0', '')+"\n")
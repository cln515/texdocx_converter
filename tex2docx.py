import glob
import os
import csv
import docx

a = glob.glob("./*.tex")

for item in a:
	ss = os.path.basename(item)
	ss = ss.replace('.tex','')

	texmt=os.stat(item).st_mtime
	
	if os.path.isfile(ss+'.docx'):
		docmt=os.stat(ss+'.docx').st_mtime
		if docmt > texmt:
			print('no output:'+ss+'.docx')
			continue

	res = open(item,'r',encoding="utf-8_sig")
	doc = docx.Document()
	str_ = res.read()
	str2 =str_.replace('\xa0', '')
	doc.add_paragraph(str2)
	doc.save(ss+'.docx')
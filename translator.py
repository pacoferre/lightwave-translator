# -*- Mode: Python -*-
# -*- coding: ascii -*-

"""
These are unit tests for the LightWave Python Common PRIS layer.
"""

import os

try:
	from lwsdk import ModCommand
	from lwsdk.pris.modeler import Mesh, load, save, closeall, init, nextsurface, renamesurface
except ImportError:
	raise Exception("The LightWave Python module could not be loaded.")

def getwords(fullname):
	output = set()
	
	fullname = fullname.replace('.', ';').replace(',', ';').replace(' ', ';').replace('_', ';')

	for word in fullname.split(';'):
		word = ''.join(i for i in word if not i.isdigit())
		if word != '':
			output.add(word)
		
	return output

closeall()
	
if not init(ModCommand()):
	raise Exception('Failed to initialize PRIS')

work_dir = "D:\\Temp\\Lightwave\\work\\"
files_dir = "D:\\Temp\\Lightwave\\orig\\Objects\\"
dest_dir = "D:\\Temp\\Lightwave\\orig\\ObjectTrans\\"

with open(os.path.join(work_dir, 'translate.txt'), 'r') as f:
	lines = f.readlines()
	f.close()

translator = {}
for line in lines:
	cols = line.replace('\n', '').replace('\r', '').split('\t')
	if len(cols) >= 1:
		if len(cols) == 2:
			translator[cols[0]] = cols[1]
		if len(cols) == 1:
			translator[cols[0]] = ""
			
output = set()

for filename in os.listdir(files_dir):
    if filename.endswith(".lwo"):
		object_file = os.path.join(files_dir, filename)
		
		change_names = {}

		result = load(object_file)
		if not isinstance(result[1], Mesh):
			raise Exception('Load failed: %d' % result)

		print 'Processing "%s"' % result[1].filename

		current_surf = nextsurface()
		while not current_surf is None:
			translate_surf = '%s' % current_surf
			for word in getwords(current_surf):
				if word in translator:
					if translator[word] != "":
						translate_surf = translate_surf.replace(word, translator[word])
				else:
					output.add(word)
			if (current_surf != translate_surf):
				change_names[current_surf] = translate_surf

			current_surf = nextsurface(current_surf)

		for key in change_names.keys():
			renamesurface(key, change_names[key])
			print key + " -> " + change_names[key]
		
		save(os.path.join(dest_dir, filename))
		closeall()	

if len(output) > 0:
	with open(os.path.join(work_dir, 'translate.txt'), 'a') as f:
		f.write("\n".join(output) + "\n")
		f.close()


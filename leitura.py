# coding: utf-8
"""
    Walmir Sa
    
"""

import os, fnmatch


#comando="ls -l"
#os.system(comando)

print("Acessa")
local='/dados'
localprocessados='/dados/processados'

listOfFiles = os.listdir(local)
pattern = "*.jpg"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
			arqtext = (localprocessados+'/'+entry+'.txt')
			
			#processa o OCR
			comando = ('tesseract '+local+'/'+entry+' '+arqtext+ " ")
			os.system(comando)
			
			#move os arquivos
			#comando = ('mv '+arqtext+'.txt '+localprocessados+'/'+entry+'.txt')
			#os.system(comando)
			
			comando = ('mv '+local+'/'+entry+' '+localprocessados+'/'+entry)
			os.system(comando)
	
			
			print (comando)
			
			#comando=comando+entry
            #print (entry)
			




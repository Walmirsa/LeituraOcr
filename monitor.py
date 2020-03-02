# coding: utf-8
"""
    Walmir Sa
    
"""
import pyinotify
import os, fnmatch

comando = ("clear")
os.system(comando)

local = "/dados/repositorio"
localpre = "/dados/preprocesssamento"
localprocessados = "/dados/processados"

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events

msg=("Escutando diretorio")

print(msg)


def LerOcr():
		
	listOfFiles = os.listdir(localpre)
	pattern = "*.tif"
	for entry in listOfFiles:
	    if fnmatch.fnmatch(entry, pattern):
			#msg=("Processando OCR:"+entry)
			#print(msg)	
			arqtext = (localprocessados+'/'+entry+'.txt')
				
			#processa o OCR
			comando = ('tesseract '+localpre+'/'+entry+' '+arqtext+ " ")
			os.system(comando)
			msg = ("Final do OCR:"+entry)
			print(msg)	
				
					#move os arquivos
			comando = ('mv '+localpre+'/'+entry+' '+localprocessados+'/'+entry)
			os.system(comando)







class EventHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self, event):
    	
		listOfFiles = os.listdir(local)
		pattern = "*.tif"
		for entry in listOfFiles:
			if fnmatch.fnmatch(entry, pattern):
				msg = ("Arquivo detectado TIF:"+entry)
				print(msg)
				comando = ('mv '+local+'/'+entry+' '+localpre+'/'+entry)
				os.system(comando)
				LerOcr()

		pattern = "*.pdf"
		for entry in listOfFiles:
			if fnmatch.fnmatch(entry, pattern):
				msg = ("Arquivo detectado PDF:"+entry)
				print(msg)
				comando = ("gs -q -dNOPAUSE -r600 -sDEVICE=tiff24nc -sOutputFile="+localpre+"/"+entry+".tif "+local+"/"+entry+" -c quit")
				os.system(comando)

				comando = ("rm "+local+"/"+entry)
				os.system(comando)
				LerOcr()

		pattern = "*.jpg"
		for entry in listOfFiles:
			if fnmatch.fnmatch(entry, pattern):
				msg = ("Arquivo detectado JPG:"+entry)
				print(msg)
				comando = ("convert "+local+"/"+entry+"  "+localpre+"/"+entry+".tif ")
				os.system(comando)

				comando = ("rm "+local+"/"+entry)
				os.system(comando)
				LerOcr()
				
	        #print(msg)
		
    #def process_IN_DELETE(self, event):
    #    msg= "Removing:", event.pathname
    #    print(msg)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/dados/repositorio', mask, rec=True)

notifier.loop()
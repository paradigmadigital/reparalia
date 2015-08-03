import xlrd
import re

list_geoname2 = []
li = []
with open('normalizados.txt') as f:
    li = f.readlines()
list_geoname2 = [x[:-1] for x in li]
print list_geoname2
#Sacamos lista con comunidades del fichero de geonames
#list_geoname = list()
#for linea in open('/home/itirados/Development/reparalia/geonames/ES.txt'):
#    lineaComas = linea.replace("\t", ',')
#    array = lineaComas.split(',')
#    geoname = array[1]
#    list_geoname.append(array[1])

#Recorrer el excel y ver si el campo contiene una comunidad de la lista
book = xlrd.open_workbook("/home/itirados/Development/reparalia/geonames/20150318_semrush-reparalia.es-domain_organic-es-analysis.xlsx")
sh = book.sheet_by_index(0)

i = 1
from xlrd import open_workbook
from xlutils.copy import copy
wb = copy(book)
ws = wb.get_sheet(0)

while (i < sh.nrows):
    keyword = sh.cell_value(rowx=i, colx=0).encode('utf8') 
    #print keyword
    #ver si la keyword es geo. Escribir geo o no-geo en el excel
#    print i
#    print sh.nrows
    
    
    for comunidad in list_geoname2:
    #for comunidad in open('/home/itirados/Development/reparalia/geonames/provincias.txt'):

        cadenaAnalizar = sh.cell_value(rowx=i, colx=0).encode('utf8')           
        #encontrado = re.search('(^|\s)'+comunidad+'(\s|$)', re.escape(cadenaAnalizar), re.IGNORECASE)
        #if not encontrado:
        #    encontrado = re.search('(^|"")'+comunidad+'(\s|$)', re.escape(cadenaAnalizar), re.IGNORECASE)
        
        if comunidad.lower() in cadenaAnalizar:
        #if encontrado:
            print comunidad
            print cadenaAnalizar	
            print "Encontrado"
            ws.write(i,14,"geo")
            wb.save('/home/itirados/Development/reparalia/geonames/example4.xls')
                
    i= i+1        
 
#p = re.compile(regexPart1 + re.escape(term) + regexPart2 , re.IGNORECASE)

import xlrd
import re

#Sacamos lista con comunidades del fichero de geonames

list_geoname = li = ["Albacete", "Alicante", 
"Almeria",
"Avila",
"Badajoz",
"Baleares Illes",
"Barcelona",
"Burgos",
"Caceres",
"Cadiz",
"Castellon",
"Ciudad Real",
"Cordoba",
"Cuenca",
"Girona",
"Granada",
"Guadalajara",
"Guipuzcoa",
"Huelva",
"Huesca",
"Jaen",
"Leon",
"Lleida",
"La Rioja",
"Lugo",
"Madrid",
"Malaga",
"Murcia",
"Navarra",
"Ourense",
"Asturias",
"Palencia",
"Las Palmas",
"Pontevedra",
"Salamanca",
"Santa Cruz Tenerife",
"Cantabria",
"Segovia",
"Sevilla",
"Soria",
"Tarragona",
"Teruel",
"Toledo",
"Valencia",
"Valladolid",
"Vizcaya",
"Zamora",
"Zaragoza",
"Ceuta",
"Melilla"]

for comunidad in list_geoname:
    print comunidad
   

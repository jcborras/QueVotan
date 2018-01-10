# Scrapping code for sites hosting election results

## Elecciones al Parlamento de Cataluña

### 2017

Provisionales al 99.8%

wget -m --directory-prefix="tmp/" https://resultats.parlament2017.cat/09AU/DAU09000CI.htm

### 2015

Tienen un fichero zip estupendo con los resultados por municipio, pero
perdemos la granularidad que nos dan los resultados por distrito en
las grandes ciudades.

    wget -m --directory-prefix="../../tmp/" www.gencat.cat/governacio/resultatsparlament2015/resu/09mesas/ELECCIONS_PARLAMENT_CATALUNYA_2015.zip

Para obtener mayor grado de detalle (incluyendo los referidos
distritos de Barcelona) hay que descargarse el sitio de resultados
entero (unos 8300 ficheros o 550Mb):

    wget -R -p -m --level=5 --reject "mp4" --directory-prefix="../../tmp/" http://www.gencat.cat/governacio/resultatsparlament2015/resu/09AU/DAU09000CI_L2.htm
    
No se han hallado resultados por mesa en el sitio de resultados
electorales.

Resultados por distrito en Barcelona incluído en el siguiente PDF,
pero los mismos datos están disponibles en la captura de las páginas
del sitio:

    http://www.gencat.cat/governacio/resultatsparlament2015/resu/09pdf/C09-MUN08_L1.pdf


### 2012

    wget --reject "mp4" -p -m --level=5 -P ../../dat/ https://www.gencat.cat/governacio/resultats-parlament2012/09AU/IAU09T_L2.htm

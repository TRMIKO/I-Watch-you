## I WATCH YOU
 Este es un bot que vigila servicios y te notifica a telegram y puede darte status acerca de ellos y el log


### Requisitos
- [Python 2.7](https://www.python.org/)
- [pip](https://pypi.python.org/pypi/pip)
- [Telepot](https://github.com/nickoala/telepot)
- [cron](https://tecadmin.net/install-crontab-in-linux/)

#### Paso 1

Descargar los archivos y situarlos en algun lugar comodo

### Paso 2
	
Tendremos que crear un bot en [telegram](http://telegram.com.es/) para esto nesecitaremos una cuenta en [telegram](http://telegram.com.es/).

y de ahi [crear un bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot) una vez que lo hayamos creado  Botfather nos dara un identificador del bot, ese id lo guardaremos para implementarlo

### Paso 3
vamos a ejecutar esta serie de comandos para poder obtener nuestro id , para esto antes de ejecutar el codigo mandaremos un msj al bot en la aplicacion de telegram

```python
>>> import telepot
>>> from pprint import pprint
>>> bot = telepot.Bot('***** pon el codigo de tu bot *****')
>>> response = bot.getUpdates()
>>> pprint(response)

```
una vez ejecutado buscaremos el atributo u'id' y ese atributo tendra nuesto id 

### paso 4

ahora que tenemos los dos ids, tanto como el del bot como el de nostros 
pasaremos a sustituir los valores  en los archivos iwy_warn.py y iwy_warn.py 

### paso 5
activar el crontab dependiendo donde se guardo el archivo

```
crontab -e
```


### paso 6 
ejecutar el archivo iwy.py para que empiezze a recibir msj

```python
>>> python iwy.py
```
# Proyecto de Consumo de API de Datos Financieros

Este proyecto consume una API de datos financieros para obtener el valor actual de ciertas acciones y mostrarlas en una interfaz web.

## Instrucciones para Ejecutar el Proyecto

### Configuración Previa

1. Instala las dependencias necesarias utilizando pip
pip install -r requerimientos.txt

2. Configuración de la API Key
Obtén una API key de Alpha Vantage siguiendo las instrucciones en Alpha Vantage.
Crea una variable de entorno llamada ALPHA_VANTAGE_API_KEY y asigna tu API key como valor.

3. Ejecución del Proyecto
Ejecuta el siguiente comando para iniciar la aplicación:
python app/app.py
Abre tu navegador web y navega a http://localhost:5000 para acceder a la aplicación.
4. Uso de la Aplicación
En la página principal, ingresa los símbolos de las acciones separados por comas en el campo de entrada.
Haz clic en el botón "Consultar" para obtener el valor actual de las acciones.
Los resultados se mostrarán debajo del formulario de consulta.
5. Scripts
build.sh: Script para construir la imagen Docker y subirla a Docker Hub.
deploy.sh: Script para descargar la imagen Docker desde Docker Hub y desplegarla en local.
6. Notas Adicionales
Asegúrate de haber configurado correctamente la variable de entorno ALPHA_VANTAGE_API_KEY antes de ejecutar la aplicación para garantizar el funcionamiento correcto del consumo de la API de Alpha Vantage.
Si deseas desplegar la aplicación en un entorno de producción, considera utilizar un servidor WSGI como Gunicorn y un servidor web como Nginx para servir la aplicación de manera eficiente y segura.
No olvides revisar los archivos de script y asegurarte de que estén configurados correctamente para tu entorno de desarrollo y producción.
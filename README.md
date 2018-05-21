# ProyectoBotTelegram

Bot para analizar Cryptomonedas.

Este proyecto está basado en varias API’s para usar un bot de telegram el cual llame a servicios y muestra información al usuario de forma fácil y rápida. En este caso el bot mostrara el valor de cryptomonedas.

Nombre del Bot: @LMLuis_bot

Este Bot usa 2 API’s: TeleBot que es una librería para usar la API de Telegram y la API de WorldCoinIndex una página de trade para las cryptos más conocidas del mercado.

Las API’s están preparadas para usar Python y devolver JSON

La API WorldCoinIndex necesita una Key limitada a 70 respuestas por hora.

TeleBot necesita comunicación “POST” con el usuario.

El Bot se comunica con la API de divisas a través de GET.

      Comandos disponibles:
        
        - /cryptos                    <------ Devuelve estadisticas de BTC.
        - /cryptos (nombre moneda)    <------ Devuelve estadisticas de la moneda escrita.
        - /top5                       <------ Devuelve las 5 monedas principales del mundo de las Cryptos.
      
      Admin tools:
        
        - /all (texto)                <---- Envia un texto a los usuarios que tengan agregados el bot.
     
      Comando Inline:
        
        - @LMLuis_bot cryptos         <---- Seleccion de monedas y envia estadisticas de la seleccionada.
        
      Comando Especiales:
       
        - /holamundotext              <---- Envia un texto de prueba.
        - /holamundo                  <---- Envia una foto de prueba.

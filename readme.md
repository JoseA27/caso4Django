## Resultados 

### Endpoint Propiedades: /app/propiedadesParametro

Postman:
![alt text](<imgs/Endpoint Propiedades/EndpointPropieadesPostman.png>)

App:
![alt text](<imgs/Endpoint Propiedades/EndpointPropieadesApp.png>)

Mongo:
![alt text](<imgs/Endpoint Propiedades/EndpointPropieadesMongo.png>)

Redis:
![alt text](<imgs/Endpoint Propiedades/EndpointPropieadesRedis.png>)


### Endpoint Pool: /app/propiedadesPool

Postman:
![alt text](<imgs/Endpoint Propiedades con Pool/EndpointPoolPostman.png>)

App:
![alt text](<imgs/Endpoint Propiedades con Pool/EndpointPoolApp.png>)

Mongo:
![alt text](<imgs/Endpoint Propiedades con Pool/EndpointPoolMongo.png>)

Redis:
![alt text](<imgs/Endpoint Propiedades con Pool/EndpointPoolRedis.png>)

### Endpoint Redis: /app/propiedadesRedis
Postman:
![alt text](<imgs/Endpoint Propiedades con Redis/EndpointRedisPostman.png>)

### Endpoint Redis con Pool: /app/propiedadesRedisYPool

Postman:
![alt text](<imgs/Endpoint Redis Y Pool/EndpointPoolRedisPostman.png>)

App:
![alt text](<imgs/Endpoint Redis Y Pool/EndpointPoolRedisApp.png>)

Mongo:
![alt text](<imgs/Endpoint Redis Y Pool/EndpointPoolRedisMongo.png>)

Redis:
![alt text](<imgs/Endpoint Redis Y Pool/EndpointPoolRedis.png>)

## Conclusiones

Según los resultados de las pruebas, el endpoint que mejor desempeño tuvo fue PropiedadesConRedisYPool, ya que tiene un tiempo de respuesta promedio mucho menor, incluso con una alta carga de solicitudes. El uso del pool de conexiones, junto con Redis, ha ayudado a mejorar el rendimiento general, en especial el de la base de Mongodb ya que no se tuvo que hacer todas esas consultas ya que estaban en la caché. En las pruebas de Postman se puede ver que el tiempo de respuesta de la app tiene una mejora de casi 10ms en comparación a los otros endpoints.

A la hora de comparar el endpoint con la conexión básica con el que tenia un connection pool, se puede observar que en cuanto a la base de Mongo el de Pool le exigió más recursos de CPU que el otro, llegando a un 12% como pico máximo. Respecto al tiempo promedio de respuesta de la app contra postman gana el de Pool con solo una diferencia de un milisegundo. Y la app en ambas tuvo un desempeño similar.
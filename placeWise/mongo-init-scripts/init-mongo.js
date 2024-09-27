// Conectar a la base de datos
db = db.getSiblingDB('PropiedadesDB');

// Crear la colección "propiedades" si no existe
db.createCollection('propiedades');

// Crear un índice único en la colección
db.propiedades.createIndex({ "ID de Propiedad": 1 }, { unique: true });

// Leer el archivo CSV y parsear los datos
var fs = require('fs');
var csvFilePath = '/docker-entrypoint-initdb.d/Costa_Rica_Real_Estate_Dataset.csv'; // Ruta dentro del contenedor

var lines = fs.readFileSync(csvFilePath).toString().split('\n');
var header = lines[0].split(',');

for (var i = 1; i < lines.length; i++) {
    var data = lines[i].split(',');
    if (data.length === header.length) {
        var propiedad = {
            "ID de Propiedad": i, // Generar un ID único para cada propiedad
            "Ciudad": data[0],
            "Provincia": data[1],
            "Tipo de Propiedad": data[2],
            "Precio (CRC)": parseFloat(data[3]), // Convertir el precio a número
            "Descripción": data[4]
        };

        // Insertar la propiedad en la colección
        db.propiedades.insertOne(propiedad);
    }
}
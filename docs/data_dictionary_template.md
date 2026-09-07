# Plantilla de diccionario de datos

No completar este documento con supuestos. Cada fila debe derivarse de una fuente real y de evidencia verificable.

| Fuente | Tabla/archivo | Campo original | Tipo observado | Descripción confirmada | Unidad/moneda | Nulos permitidos | Rol de llave | Dominio/valores | Rol geoespacial | Rol temporal | Transformación aplicada | Notas/evidencia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

## Metadatos por fuente

Registrar para cada fuente:

- propietario o sistema de origen;
- fecha de extracción/recepción;
- periodo cubierto;
- grano declarado o inferido;
- método de extracción;
- restricciones de uso;
- identificadores disponibles;
- documentación de negocio asociada;
- responsable de validar la semántica.

## Reglas

1. Diferenciar siempre **nombre original** y **nombre canónico** si se crea una capa armonizada.
2. No inferir unidades, moneda, estados o categorías por el nombre de la columna solamente.
3. Registrar cualquier transformación que cambie el significado o dominio de un campo.
4. Si la semántica es desconocida, marcarla como pendiente en lugar de asumirla.

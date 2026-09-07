# Diccionario de Datos - CODIP

> Este documento se actualiza conforme se incorporan nuevas fuentes de datos al proyecto.

## Dataset Principal: Proyectos Inmobiliarios

| Variable           | Tipo       | Descripcion                                      | Ejemplo         |
|--------------------|------------|--------------------------------------------------|-----------------|
| `id_proyecto`      | string     | Identificador unico del proyecto                 | PRJ-2024-001    |
| `nombre`           | string     | Nombre comercial del proyecto                    | Torres Nativas   |
| `tipologia`        | string     | Tipo de proyecto: residencial, comercial, mixto  | residencial     |
| `latitud`          | float      | Latitud geografica (WGS84)                       | 4.6534          |
| `longitud`         | float      | Longitud geografica (WGS84)                      | -74.0836        |
| `area_total_m2`    | float      | Area total construida en metros cuadrados        | 12500.0         |
| `num_unidades`     | int        | Numero de unidades habitacionales o comerciales  | 120             |
| `precio_base`      | float      | Precio base por unidad (COP o USD)               | 250000000       |
| `estrato`          | int        | Estrato socioeconomico (1-6, aplica para Colombia)| 4              |
| `ano_inicio`       | int        | Anio de inicio del proyecto                      | 2022            |
| `estado`           | string     | Estado del proyecto: planos, construccion, entregado | construccion |
| `municipio`        | string     | Municipio donde se ubica                         | Bogota          |
| `departamento`     | string     | Departamento o estado                            | Cundinamarca    |

## Variables Derivadas (Feature Engineering)

| Variable                  | Descripcion                                        |
|---------------------------|----------------------------------------------------|
| `densidad_unidades`       | num_unidades / area_total_m2                       |
| `dist_via_principal_m`    | Distancia a via principal mas cercana (metros)     |
| `dist_centroide_zona`     | Distancia al centroide de la zona urbana           |
| `idx_accesibilidad`       | Indice de accesibilidad a transporte publico       |

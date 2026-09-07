# Diccionario de Datos - CODIP

> **Estado: esquema canónico provisional.** Este documento define una estructura
> objetivo para el análisis, no afirma que las fuentes reales de CODIP ya usen
> estos nombres ni que todas las variables estén disponibles. El diccionario se
> debe reconciliar con cada fuente antes de construir el dataset analítico.

## Unidad de análisis

La unidad principal propuesta es **proyecto inmobiliario por fecha de corte**.
Si una fuente contiene unidades, leads, ventas u observaciones temporales a otra
granularidad, primero debe documentarse su grano y luego agregarse de forma
explícita al nivel proyecto cuando corresponda.

## Identificación y ubicación

| Variable | Tipo | Descripción |
|---|---|---|
| `id_proyecto` | string | Identificador estable del proyecto en la fuente o llave canónica documentada. |
| `nombre_proyecto` | string | Nombre comercial del proyecto. |
| `id_inmobiliaria` | string | Identificador de la inmobiliaria/desarrollador, si existe. |
| `distrito` | string | Distrito del proyecto. |
| `provincia` | string | Provincia del proyecto. |
| `departamento` | string | Departamento del proyecto. |
| `ubigeo` | string | Código UBIGEO cuando pueda validarse contra una fuente oficial. |
| `latitud` | float | Latitud WGS84, rango válido [-90, 90]. |
| `longitud` | float | Longitud WGS84, rango válido [-180, 180]. |
| `fecha_corte` | date | Fecha a la que corresponde la observación. |

## Características del proyecto

| Variable | Tipo | Descripción |
|---|---|---|
| `uso_principal` | category | Uso reportado (por ejemplo, residencial, comercial o mixto) si la fuente lo provee. |
| `estado_proyecto` | category | Estado comercial/constructivo con taxonomía documentada. |
| `unidades_total` | integer | Número total de unidades cuando la definición de la fuente sea consistente. |
| `area_terreno_m2` | float | Área de terreno en m², si está disponible. |
| `area_construida_m2` | float | Área construida en m², si está disponible. |
| `precio_desde` | float | Precio mínimo reportado en la fecha de corte. |
| `moneda` | category | Código de moneda de la observación, por ejemplo `PEN` o `USD`. |

## Variables derivadas candidatas

Estas variables **no deben calcularse hasta validar disponibilidad, unidad y
calidad de sus insumos**.

| Variable | Descripción |
|---|---|
| `densidad_unidades` | Unidades / área relevante, con denominador > 0 y definición explícita. |
| `dist_via_principal_m` | Distancia métrica a la vía principal más cercana. |
| `dist_transporte_m` | Distancia métrica al nodo de transporte definido por la metodología. |
| `dist_centro_actividad_m` | Distancia a un centro de actividad con criterio documentado. |
| `poi_*` | Conteos/densidades de puntos de interés dentro de radios definidos ex ante. |
| `idx_accesibilidad` | Índice compuesto cuya fórmula, ponderaciones y fuentes deben quedar versionadas. |

## Reglas mínimas de calidad

- No inventar o inferir una unidad de medida cuando la fuente no la declara.
- No usar coordenadas fuera de rango ni asumir que un archivo sin CRS está en WGS84.
- Mantener trazabilidad entre columna fuente y columna canónica.
- Registrar fecha de extracción/corte y procedencia de cada dataset.
- Separar variables observadas de variables derivadas.
- No usar una clasificación existente como feature si esa clasificación es el
  resultado que el clustering pretende descubrir.

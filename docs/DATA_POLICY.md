# Política de datos

## Objetivo

Evitar que la conveniencia técnica de Git se confunda con autorización de publicación.

Este repositorio es público. Por defecto, los datos reales no deben versionarse.

## Clasificación mínima antes de añadir una fuente

Para cada dataset nuevo registra, como mínimo:

- origen y owner;
- fecha/periodo cubierto;
- grain esperado;
- campos sensibles o identificadores;
- licencia o permiso de uso;
- autorización de publicación en un repositorio público;
- retención/restricciones;
- ubicación del contrato en `schemas/source/`.

Si la autorización de publicación es desconocida, el dataset permanece local y gitignored.

## Excepciones actuales

`.gitignore` contiene excepciones explícitas para archivos del estudio La Victoria que ya están versionados.

Estas excepciones:

- describen el estado actual del repositorio;
- no deben generalizarse a otras fuentes;
- no prueban por sí mismas licencia, confidencialidad ni autorización de redistribución;
- deben revisarse si cambia la visibilidad del proyecto o la clasificación de los datos.

## Capas

### raw

- copia inmutable de la fuente recibida;
- no corregir ni sobrescribir;
- conservar encoding y estructura observada;
- cualquier corrección se implementa downstream.

### interim

- transformaciones técnicas regenerables;
- no constituye autoridad de negocio;
- debe poder reconstruirse desde raw + código/config.

### processed

- dataset analítico con grain y lineage explícitos;
- cambios de significado deben quedar documentados;
- no mezclar silenciosamente unidades, periodos o reglas.

## Datos sensibles

No versionar:

- credenciales, tokens o secretos;
- PII no autorizada;
- dumps de sistemas internos;
- rutas personales;
- archivos de clientes/proveedores cuya publicación no esté explícitamente clasificada;
- outputs que permitan reconstruir información restringida.

## Revisión antes de publicar

Antes de añadir o reemplazar una excepción de datos:

1. verificar necesidad real de versionarla;
2. preferir fixture/snapshot sintético o muestra anonimizada cuando sea suficiente;
3. documentar contrato y clasificación;
4. revisar diff/tamaño;
5. ejecutar validaciones de contrato/calidad correspondientes.

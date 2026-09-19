# Inventario de investigación

Este directorio registra literatura académica y material metodológico **candidato** para el proyecto CODIP.

No constituye la bibliografía definitiva del paper. Una referencia puede estar identificada, disponible o incluso leída sin que eso implique que deba citarse en la versión final. La inclusión definitiva depende de la pregunta de investigación, los datos efectivamente disponibles, la metodología validada y los resultados.

## Fuentes de verdad

- [LITERATURE_INVENTORY.md](LITERATURE_INVENTORY.md): inventario vivo de referencias identificadas, disponibilidad, prioridad y función metodológica.
- [bibliography_candidates.bib](bibliography_candidates.bib): metadatos BibTeX verificados de referencias candidatas seleccionadas.

## Estados

- `IDENTIFIED`: referencia localizada y relevante; copia completa no verificada.
- `AVAILABLE_REPORTED`: el usuario reporta disponer de una copia; todavía no se verificó su ubicación/acceso desde una fuente conectada.
- `AVAILABLE_VERIFIED`: copia accesible y verificada en un repositorio documental autorizado, por ejemplo Google Drive.
- `READ`: contenido relevante revisado.
- `USED`: la referencia sustenta una decisión, hipótesis, método o interpretación concreta del análisis.

## Prioridad

- `A`: núcleo metodológico o conceptual.
- `B`: apoyo importante / consulta selectiva.
- `C`: extensión para una fase posterior o pregunta secundaria.

## Política para PDFs

Los PDFs de libros y artículos no se versionan aquí por defecto.

Motivos:

1. Git no es un gestor documental adecuado para una biblioteca de binarios pesados.
2. El repositorio es público y la licencia/copyright de cada PDF puede impedir su redistribución.
3. La biblioteca completa puede vivir en Google Drive u otra fuente documental autorizada; Git conserva metadatos, notas de lectura, decisiones y citas reproducibles.

Un PDF solo debería incorporarse al repositorio si existe una razón concreta, la licencia permite su publicación y la política de datos/documentos del proyecto lo autoriza.

## Convención de trabajo

Cuando se incorpore nueva bibliografía:

1. añadirla primero al inventario;
2. distinguir `IDENTIFIED` de disponibilidad realmente verificada;
3. verificar metadatos canónicos antes de añadir BibTeX;
4. registrar qué pregunta o método justifica su lectura;
5. no elevar una referencia a `USED` hasta que exista una relación explícita con el análisis.

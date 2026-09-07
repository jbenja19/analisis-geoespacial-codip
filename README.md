# Análisis Geoespacial - CODIP

> Scaffold de proyecto para comenzar el análisis desde cero cuando estén disponibles las fuentes raw.

## Estado actual

**Solo estructura. No hay análisis implementado ni resultados analíticos.**

El repositorio define organización, convenciones, configuración, trazabilidad y controles mínimos de calidad. Las decisiones sobre limpieza, variables, CRS de análisis, feature engineering, métodos estadísticos, clustering, modelos, visualizaciones y métricas se tomarán únicamente después de inspeccionar las fuentes reales.

## Principios

1. **Raw es inmutable.** Los archivos recibidos se almacenan sin transformarlos ni sobrescribirlos.
2. **La fuente manda.** No se inventan columnas, semánticas, llaves, unidades ni relaciones antes de perfilar la data real.
3. **Contrato después del inventario.** El diccionario y los esquemas se completan a partir de evidencia de las fuentes.
4. **Método después de los datos.** No hay algoritmos ni parámetros preseleccionados en este scaffold.
5. **Transformaciones reproducibles.** Cuando empiece el trabajo, las transformaciones reutilizables vivirán en `src/`, no solo en notebooks.
6. **Separación de capas.** Raw, datos intermedios, datos procesados y outputs tienen destinos distintos.
7. **Trazabilidad.** Las decisiones metodológicas relevantes se documentan en `docs/decisions/`.
8. **Gobernanza.** No se versionan datos internos, credenciales ni material confidencial no autorizado.

## Estructura

```text
analisis-geoespacial-codip/
├── data/
│   ├── raw/                 # Copia inmutable de las fuentes recibidas
│   ├── external/            # Fuentes externas complementarias
│   ├── interim/             # Transformaciones intermedias reproducibles
│   └── processed/           # Dataset(s) analítico(s) finales
├── notebooks/               # Exploración; inicialmente vacío
├── schemas/
│   ├── source/              # Contratos/esquemas de cada fuente real
│   └── canonical/           # Esquemas armonizados, si llegan a ser necesarios
├── src/
│   ├── data/                # Ingesta, validación y transformación futura
│   ├── geospatial/          # Lógica espacial futura
│   ├── analysis/            # Análisis/modelado futuro
│   ├── visualization/       # Visualización futura
│   └── utils/               # Utilidades de proyecto
├── tests/                   # Por ahora, gates estructurales
├── docs/
│   ├── project_workflow.md
│   ├── data_dictionary_template.md
│   ├── setup.md
│   └── decisions/
├── reports/
│   ├── figures/
│   ├── tables/
│   └── exports/
├── paper/                   # Material académico futuro, si corresponde
├── config/                  # Configuración del proyecto sin supuestos analíticos
└── .github/workflows/       # CI
```

## Qué hacer cuando llegue la data raw

El orden esperado está documentado en [`docs/project_workflow.md`](docs/project_workflow.md). En resumen:

```text
recepción raw
→ inventario de fuentes
→ perfilado técnico
→ diccionario/contratos
→ definición del grano y llaves
→ reglas de calidad
→ transformaciones
→ EDA
→ decisión metodológica
→ análisis/modelado
→ validación
→ outputs
```

Hasta completar inventario y perfilado, **no se debe asumir ninguna metodología analítica**.

## Instalación

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
Copy-Item .env.example .env
```

## Calidad

```bash
python -m ruff check src/ tests/
python -m black --check src/ tests/
python -m pytest tests/ -v
```

Los tests actuales verifican la estructura del scaffold; no prueban resultados analíticos porque todavía no existen.

## Nota de seguridad

El repositorio es público. `data/` está preparado para uso local y sus contenidos reales están ignorados por Git. Antes de incorporar información interna de CODIP, revisar permisos, confidencialidad, licencia y visibilidad del repositorio.

# Inventario de literatura — CODIP

> Estado: inventario de investigación, no bibliografía final del paper.  
> Última actualización: 2026-09-19.  
> Criterio: separar literatura de segmentación inmobiliaria, clustering/validación, estadística espacial y econometría espacial.

## 1. Material que el usuario ya reporta tener

Los cuatro libros reportados se **mantienen**. No cumplen la misma función y no son redundantes.

| Referencia | Estado | Prioridad | Decisión | Función en CODIP | Lectura sugerida |
|---|---|---:|---|---|---|
| Everitt, Landau, Leese & Stahl (2011), *Cluster Analysis*, 5th ed., Wiley | AVAILABLE_REPORTED | A | KEEP | Fundamento de clustering multivariante, distancias, K-Means, métodos jerárquicos, mixture models y validación | Leer primero introducción, criterios/distancias, métodos de partición y capítulos de validación/robustez |
| Anselin (1988), *Spatial Econometrics: Methods and Models*, Springer | AVAILABLE_REPORTED | A | KEEP | Fundamento clásico de dependencia espacial, especificación, estimación y tests de modelos espaciales | Lectura selectiva ahora; profundizar al construir el modelo hedónico/espacial |
| LeSage & Pace (2009), *Introduction to Spatial Econometrics*, Chapman & Hall/CRC | AVAILABLE_REPORTED | A | KEEP | Tratamiento moderno de modelos de regresión espacial e interpretación de efectos directos/indirectos | Mantener como referencia principal de econometría espacial aplicada |
| Fischer & Getis (eds.) (2010), *Handbook of Applied Spatial Analysis: Software Tools, Methods and Applications*, Springer | AVAILABLE_REPORTED | B | KEEP | Obra panorámica; útil para ESDA, autocorrelación, clustering espacial, PySAL y selección de herramientas | No leer linealmente; consultar capítulos pertinentes |

### Decisión práctica sobre estos cuatro

- **No eliminar ninguno.**
- **Everitt** es el libro más directamente útil para corregir y validar el clustering actual.
- **Anselin + LeSage/Pace** son complementarios: el primero establece la base clásica; el segundo desarrolla un tratamiento más moderno de los modelos espaciales.
- **Fischer/Getis** no es el texto central del paper, pero funciona como handbook y contiene capítulos directamente relevantes para ESDA, autocorrelación espacial, spatial clustering y PySAL.

La disponibilidad anterior es `AVAILABLE_REPORTED`, no `AVAILABLE_VERIFIED`: se deriva de la evidencia aportada por el usuario, no de una lectura de los archivos desde Google Drive.

## 2. Núcleo bibliográfico candidato (15 referencias)

Estas son las referencias que, a fecha de este inventario, constituyen el núcleo de lectura antes de fijar la metodología del paper.

### 2.1 Housing submarkets y economía inmobiliaria

| Referencia | Estado | Prioridad | Pregunta que ayuda a resolver |
|---|---|---:|---|
| Bourassa, Hamelink, Hoesli & MacGregor (1999), “Defining Housing Submarkets”, *Journal of Housing Economics* 8(2), 160–183 | IDENTIFIED | A | Cómo definir submercados combinando estructura multivariante y modelos hedónicos |
| Watkins (2001), “The Definition and Identification of Housing Submarkets”, *Environment and Planning A* 33(12), 2235–2253 | IDENTIFIED | A | Qué es conceptualmente un submercado y cómo combinar criterios espaciales/estructurales |
| Goodman & Thibodeau (1998), “Housing Market Segmentation”, *Journal of Housing Economics* 7(2), 121–143 | IDENTIFIED | A | Fundamento económico y empírico de segmentación del mercado de vivienda |
| Goodman & Thibodeau (2003), “Housing Market Segmentation and Hedonic Prediction Accuracy”, *Journal of Housing Economics* 12(3), 181–201 | IDENTIFIED | A | Cómo evaluar si una segmentación mejora predicción hedónica fuera de muestra |
| Bourassa, Cantoni & Hoesli (2007), “Spatial Dependence, Housing Submarkets, and House Price Prediction”, *Journal of Real Estate Finance and Economics* 35, 143–160 | IDENTIFIED | A | Relación entre submercados, dependencia espacial y predicción de precios |
| Rosen (1974), “Hedonic Prices and Implicit Markets: Product Differentiation in Pure Competition”, *Journal of Political Economy* 82(1), 34–55 | IDENTIFIED | A | Fundamento económico de precios hedónicos |
| Basu & Thibodeau (1998), “Analysis of Spatial Autocorrelation in House Prices”, *Journal of Real Estate Finance and Economics* 17(1), 61–85 | IDENTIFIED | A | Por qué y cómo la dependencia espacial aparece en precios de vivienda |

### 2.2 Estadística espacial y validación de clustering

| Referencia | Estado | Prioridad | Pregunta que ayuda a resolver |
|---|---|---:|---|
| Anselin (1995), “Local Indicators of Spatial Association—LISA”, *Geographical Analysis* 27, 93–115 | IDENTIFIED | A | Cómo detectar asociación espacial local y spatial outliers |
| Tibshirani, Walther & Hastie (2001), “Estimating the Number of Clusters in a Data Set via the Gap Statistic”, *JRSS Series B* 63(2), 411–423 | IDENTIFIED | A | Cómo complementar elbow/silhouette para decidir número de clusters |
| Hennig (2007), “Cluster-wise Assessment of Cluster Stability”, *Computational Statistics & Data Analysis* 52(1), 258–271 | IDENTIFIED | A | Cómo comprobar si los clusters son estables frente a perturbaciones/remuestreo |

### 2.3 Libros metodológicos núcleo

| Referencia | Estado | Prioridad | Función |
|---|---|---:|---|
| Everitt, Landau, Leese & Stahl (2011), *Cluster Analysis*, 5th ed., Wiley | AVAILABLE_REPORTED | A | Clustering y validación |
| Kaufman & Rousseeuw (1990), *Finding Groups in Data: An Introduction to Cluster Analysis*, Wiley | IDENTIFIED | A | Distancias, PAM/k-medoids, silhouette y robustez |
| Anselin (1988), *Spatial Econometrics: Methods and Models*, Springer | AVAILABLE_REPORTED | A | Econometría espacial clásica |
| LeSage & Pace (2009), *Introduction to Spatial Econometrics*, Chapman & Hall/CRC | AVAILABLE_REPORTED | A | Econometría espacial moderna e impactos |
| Baddeley, Rubak & Turner (2015), *Spatial Point Patterns: Methodology and Applications with R*, CRC Press | IDENTIFIED | A/B | Analizar la localización de proyectos como patrón de puntos, separado de Moran/LISA |

## 3. Referencias adicionales ya identificadas

No deben perderse, pero no son requisito previo para iniciar la siguiente iteración metodológica.

| Referencia | Prioridad | Uso potencial |
|---|---:|---|
| Rousseeuw (1987), “Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis” | A/B | Fuente original de silhouette |
| Moran (1950), “Notes on Continuous Stochastic Phenomena” | B | Base histórica de Moran's I |
| Getis & Ord (1992), “The Analysis of Spatial Association by Use of Distance Statistics” | B | Hot/cold spots y familia G |
| Dubin (1998), “Spatial Autocorrelation: A Primer” | B | Explicación aplicada de dependencia espacial en vivienda |
| Sirmans, Macpherson & Zietz (2005), “The Composition of Hedonic Pricing Models” | B | Selección de atributos en modelos hedónicos |
| Cressie (1993), *Statistics for Spatial Data*, Wiley | B | Estadística espacial general rigurosa |
| Bivand, Pebesma & Gómez-Rubio (2013), *Applied Spatial Data Analysis with R*, 2nd ed., Springer | B | Aplicación de estadística espacial |
| Fischer & Getis (eds.) (2010), *Handbook of Applied Spatial Analysis* | AVAILABLE_REPORTED / B | Handbook de consulta |
| Fotheringham, Brunsdon & Charlton (2002), *Geographically Weighted Regression* | C | GWR si existe evidencia de no estacionariedad y N suficiente |
| Brunsdon, Fotheringham & Charlton (1996), “Geographically Weighted Regression: A Method for Exploring Spatial Nonstationarity” | C | Fundamento de GWR |
| Comber et al. (2023), “A Route Map for Successful Applications of Geographically Weighted Regression” | B/C | Diagnóstico previo y uso responsable de GWR |
| Elhorst (2014), *Spatial Econometrics: From Cross-Sectional Data to Spatial Panels* | C | Panel espacial si se obtienen múltiples periodos |
| Assunção, Neves, Câmara & Freitas (2006), regionalización con minimum spanning trees / SKATER | C | Solo si se definen unidades areales contiguas |
| Duque, Anselin & Rey (2012), “The Max-P-Regions Problem” | C | Regionalización espacial restringida |
| Rey, Arribas-Bel & Wolf, *Geographic Data Science with Python* | B | Implementación práctica con ecosistema PySAL |

## 4. Correspondencia con el repositorio actual

La literatura debe responder a problemas observados en el análisis, no agregarse por acumulación.

| Problema / decisión del proyecto | Literatura principal |
|---|---|
| Selección y validación de clusters | Everitt; Kaufman & Rousseeuw; Tibshirani et al.; Hennig |
| Definir si los clusters pueden interpretarse como submercados | Bourassa et al.; Watkins; Goodman & Thibodeau |
| Analizar precio/ticket de oferta mediante atributos | Rosen; literatura hedónica |
| Evaluar dependencia espacial | Anselin 1995; Anselin 1988; Basu & Thibodeau |
| Pasar de OLS/hedónico a modelos espaciales | Anselin 1988; LeSage & Pace 2009 |
| Analizar distribución de proyectos como puntos | Baddeley, Rubak & Turner |
| Explorar variación local de coeficientes | Fotheringham et al.; Comber et al., solo en una fase posterior |

## 5. Próximas adquisiciones recomendadas

Orden de adquisición/lectura después de los cuatro libros ya reportados:

1. Bourassa et al. (1999).
2. Watkins (2001).
3. Goodman & Thibodeau (1998).
4. Goodman & Thibodeau (2003).
5. Bourassa, Cantoni & Hoesli (2007).
6. Hennig (2007).
7. Tibshirani, Walther & Hastie (2001).
8. Anselin (1995).
9. Rosen (1974).
10. Basu & Thibodeau (1998).
11. Kaufman & Rousseeuw (1990).
12. Baddeley, Rubak & Turner (2015).

## 6. Regla para el paper

Este inventario no autoriza por sí solo una técnica.

Para que una referencia pase a `USED`, debe existir una cadena explícita:

```text
pregunta de investigación
→ variable / unidad de análisis
→ método
→ supuestos
→ diagnóstico / validación
→ referencia que justifica la decisión
```

La metodología definitiva debe seguir esa cadena y no el orden inverso.

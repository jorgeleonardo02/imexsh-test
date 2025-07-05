#  FileProcessor

##  ¿Qué es?

**`FileProcessor`** es una clase Python diseñada para **automatizar tareas básicas de manejo de archivos y datos**, pensada especialmente para entornos que procesan información médica o datasets grandes.



## ✅ ¿Qué hace?

- **Listar carpetas y archivos:** Verifica cuántos archivos y carpetas hay, su tamaño y fecha de última modificación.
- **Leer archivos CSV:** Muestra columnas, filas, estadísticas básicas (media y desviación estándar) y puede generar reportes en texto.
- **Leer archivos DICOM:** Extrae y muestra metadatos (nombre del paciente, fecha del estudio, modalidad) y exporta la imagen a PNG si el formato es compatible.


## ¿Para qué sirve?

Esta clase es útil para **validar rápidamente datasets** sin abrir cada archivo manualmente.  
Ejemplos reales:
- Revisar lotes de imágenes médicas en formato DICOM.
- Inspeccionar archivos CSV de pacientes o mediciones clínicas.
- Generar reportes estadísticos preliminares para análisis o auditoría.
- Detectar archivos corruptos o carpetas incompletas.

Todo se hace con **un solo script**, sin necesidad de usar software especializado para cada archivo.

## ¿Qué demuestra?

Este proyecto muestra cómo:
- Usar `os` y `logging` para manejar archivos y registros.
- Aplicar `pandas` para analizar datos tabulares.
- Usar `pydicom` y `PIL` para trabajar con imágenes médicas.
- Manejar **formatos inesperados o errores de forma robusta**, sin romper la ejecución.

## Ejecución
# Instalar dependencias
pip install -r requirements.txt

## En IMEXHS_TEST\file_handling> activar venv
.\.venv\Scripts\activate

# Ejecutar script principal
python main.py

```bash

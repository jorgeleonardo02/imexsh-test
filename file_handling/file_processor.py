# Importa módulos estándar de Python
import os                    # Operaciones de sistema de archivos
import logging               # Manejo de logs
from typing import Optional, List, Tuple  # Tipado opcional

# Librerías externas
import pandas as pd          # Para trabajar con CSVs
import pydicom               # Para leer archivos DICOM
from PIL import Image        # Para exportar imágenes como PNG

# Define una clase para procesar archivos
class FileProcessor:
    # Constructor: define ruta base y archivo de logs
    def __init__(self, base_path: str, log_file: str):
        self.base_path = base_path
        logging.basicConfig(filename=log_file, level=logging.INFO)
        self.logger = logging.getLogger()

    # Método para listar el contenido de una carpeta
    def list_folder_contents(self, folder_name: str, details: bool = False) -> None:
        # Construye la ruta completa
        folder = os.path.join(self.base_path, folder_name)

        # Verifica si existe
        if not os.path.exists(folder):
            self.logger.error(f"Folder {folder} does not exist.")
            print(f"ERROR: Folder {folder} does not exist.")
            return

        # Lista los elementos dentro de la carpeta
        elements = os.listdir(folder)
        print(f"Folder: {folder}")
        print(f"Number of elements: {len(elements)}")

        # Recorre cada elemento encontrado
        for el in elements:
            full_path = os.path.join(folder, el)
            if os.path.isdir(full_path):
                print(f"Folder: {el}")
            else:
                if details:
                    size = os.path.getsize(full_path) / (1024 * 1024)  # Tamaño en MB
                    mtime = os.path.getmtime(full_path)               # Fecha de última modificación
                    print(f"File: {el} ({size:.2f} MB, Last Modified: {mtime})")
                else:
                    print(f"File: {el}")

    # Método para leer un CSV, mostrar estadísticas y guardar un reporte
    def read_csv(self, filename: str, report_path: Optional[str] = None, summary: bool = False) -> None:
        file_path = os.path.join(self.base_path, filename)

        # Verifica si el archivo existe
        if not os.path.exists(file_path):
            self.logger.error(f"File {file_path} does not exist.")
            print(f"ERROR: File {file_path} does not exist.")
            return

        try:
            # Lee el archivo CSV usando pandas
            df = pd.read_csv(file_path)

            # Muestra columnas y cantidad de filas
            print(f"Columns: {df.columns.tolist()}")
            print(f"Rows: {df.shape[0]}")

            # Selecciona columnas numéricas y calcula estadísticas
            numeric_cols = df.select_dtypes(include='number').columns
            stats = df[numeric_cols].describe()
            print(stats.loc[['mean', 'std']])  # Muestra media y desviación estándar

            # Si se indicó report_path, guarda el reporte en archivo
            if report_path:
                os.makedirs(report_path, exist_ok=True)
                stats.loc[['mean', 'std']].to_csv(
                    os.path.join(report_path, "report.txt"), sep='\t'
                )
                print(f"Report saved to {report_path}/report.txt")

            # Si se pidió resumen, muestra conteo de valores no numéricos
            if summary:
                non_numeric = df.select_dtypes(exclude='number')
                for col in non_numeric.columns:
                    print(f"Column: {col}")
                    print(non_numeric[col].value_counts())

        except Exception as e:
            self.logger.error(f"Error reading CSV: {str(e)}")
            print(f"ERROR: {str(e)}")

    # Método para leer un archivo DICOM y mostrar/extractar imagen
    def read_dicom(self, filename: str, tags: Optional[List[Tuple[int, int]]] = None, extract_image: bool = False) -> None:
        file_path = os.path.join(self.base_path, filename)

        # Verifica si el archivo existe
        if not os.path.exists(file_path):
            self.logger.error(f"DICOM file {file_path} does not exist.")
            print(f"ERROR: File {file_path} does not exist.")
            return

        try:
            # Lee el archivo DICOM
            ds = pydicom.dcmread(file_path)

            # Muestra algunos metadatos básicos
            print(f"Patient Name: {ds.get('PatientName', 'N/A')}")
            print(f"Study Date: {ds.get('StudyDate', 'N/A')}")
            print(f"Modality: {ds.get('Modality', 'N/A')}")

            # Si se proporcionaron tags, intenta mostrar sus valores
            if tags:
                for tag in tags:
                    try:
                        print(f"Tag {tag}: {ds[tag].value}")
                    except:
                        print(f"Tag {tag} not found")

            # Si se quiere extraer la imagen:
            if extract_image:
                arr = ds.pixel_array  # Obtiene el arreglo de píxeles
                print(f"Pixel Array shape: {arr.shape}")

                if len(arr.shape) == 2:
                    # Imagen 2D → guardar como PNG
                    img = Image.fromarray(arr)
                    output_path = os.path.join(self.base_path, "output_image.png")
                    img.save(output_path)
                    print(f"Image saved as {output_path}")

                elif len(arr.shape) == 3:
                    if arr.shape[0] == 1:
                        # Volumen con un solo frame → guardar solo el primero
                        img = Image.fromarray(arr[0])
                        output_path = os.path.join(self.base_path, "output_image.png")
                        img.save(output_path)
                        print(f"Image saved as {output_path}")
                    elif arr.shape[2] in [1, 3, 4]:
                        # Imagen color o escala de grises con canal
                        img = Image.fromarray(arr)
                        output_path = os.path.join(self.base_path, "output_image.png")
                        img.save(output_path)
                        print(f"Image saved as {output_path}")
                    else:
                        print("Unsupported 3D pixel array format.")
                        self.logger.warning("Unsupported 3D pixel array format.")
                else:
                    print("Pixel array format not supported for export.")
                    self.logger.warning(f"Unsupported pixel array shape: {arr.shape}")

        except Exception as e:
            self.logger.error(f"Error reading DICOM: {str(e)}")
            print(f"ERROR: {str(e)}")


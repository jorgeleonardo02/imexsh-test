from file_processor import FileProcessor

processor = FileProcessor(base_path="./data", log_file="log.txt")

# 1️⃣ Listar contenido
processor.list_folder_contents(folder_name="", details=True)

# 2️⃣ Leer CSV
processor.read_csv(filename="sample-02-csv.csv", report_path="./reports", summary=True)

# 3️⃣ Leer DICOM
processor.read_dicom(filename="sample-02-dicom.dcm", extract_image=True)

import os
import time

class WriteAheadLog:
    def __init__(self, filename="wal.log"):
        self.filename = filename

    def add_entry(self, data): 
        entry = f"{int(time.time())}: {data}\n"
        with open(self.filename, "a") as file:
            file.write(entry)

    def read_entries(self):
        with open(self.filename, "r") as file:
            return file.readlines()

class SegmentedLog:
    def __init__(self, segment_size=5, base_dir="logs"):
        self.segment_size = segment_size
        self.base_dir = base_dir
        self.segment_index = 0
        self.current_entries = []
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def add_entry(self, data):
        self.current_entries.append(data)
        if len(self.current_entries) >= self.segment_size:
            self._save_segment()

    def _save_segment(self):
        segment_filename = os.path.join(self.base_dir, f"log_segment_{self.segment_index}.log")
        with open(segment_filename, "w") as file:
            for entry in self.current_entries:
                file.write(entry + "\n")
        self.segment_index += 1
        self.current_entries = []

    def read_segments(self):
        segments = []
        for filename in os.listdir(self.base_dir):
            if filename.startswith("log_segment_"):
                with open(os.path.join(self.base_dir, filename), "r") as file:
                    segments.append(file.readlines())
        return segments

class LowWaterMarkCleaner:
    def __init__(self, base_dir="logs", retention_time=60):
        self.base_dir = base_dir
        self.retention_time = retention_time

    def clean_old_segments(self):
        current_time = time.time()
        for filename in os.listdir(self.base_dir):
            if filename.startswith("log_segment_"):
                file_path = os.path.join(self.base_dir, filename)
                file_time = os.path.getmtime(file_path)
                if current_time - file_time > self.retention_time:
                    os.remove(file_path)
                    print(f"Segmento {filename} eliminado.")

# Ejemplo de uso
wal = WriteAheadLog()
wal.add_entry("SET clave1 valor1")
wal.add_entry("SET clave2 valor2")
print("Entradas en WAL:", wal.read_entries())

segmented_log = SegmentedLog()
segmented_log.add_entry("SET clave1 valor1")
segmented_log.add_entry("SET clave2 valor2")
segmented_log.add_entry("SET clave3 valor3")
segmented_log.add_entry("SET clave4 valor4")
segmented_log.add_entry("SET clave5 valor5")
segmented_log.add_entry("SET clave6 valor6")
print("Segmentos guardados:", segmented_log.read_segments())

cleaner = LowWaterMarkCleaner()
time.sleep(2)  # Espera para simular tiempo de retención
cleaner.clean_old_segments()
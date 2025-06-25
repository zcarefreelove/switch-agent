import csv
from typing import List

class DeviceImporter:
    def import_from_csv(self, file_path: str) -> List[dict]:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
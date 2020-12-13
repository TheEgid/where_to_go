import os
from pathlib import Path


# СОЗДАНИЕ БЕКАПА
if __name__ == "__main__":
    db_backup_file = 'db.json'
    os.system(f'python manage.py dumpdata --indent=4 > {db_backup_file}')
    print(f'backup file is here: {Path(__file__).resolve().parent} '
          f'{db_backup_file=}')

# python manage.py loaddata db.json

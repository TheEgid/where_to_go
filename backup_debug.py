import os
import json
import codecs
from pathlib import Path


def correct_db_backup_file(db_backup_file):
    with codecs.open(db_backup_file, 'r', 'utf-8') as f:
        backups = json.load(f)
    for backup in backups:
        if backup['model'] == 'contenttypes.contenttype':
            backup['id'] = backup.pop('pk')
    with open(db_backup_file, 'w', encoding='utf-8') as f:
        json.dump(backups, indent=4, fp=f)


# СОЗДАНИЕ БЕКАПА
if __name__ == "__main__":
    db_backup_file = 'db.json'
    os.system(f'python manage.py dumpdata --indent=4 > {db_backup_file}')
    correct_db_backup_file(db_backup_file)
    print(f'backup file is here: {Path(__file__).resolve().parent} '
          f'{db_backup_file=}')

# python manage.py loaddata db.json

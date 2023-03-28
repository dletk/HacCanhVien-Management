import datetime
import os
import shutil

DATABASE_FILENAME = 'db.sqlite3'
BACKUP_DIRECTORY = 'db_backups'

# Create backup directory if it does not exist
if not os.path.exists(BACKUP_DIRECTORY):
    os.makedirs(BACKUP_DIRECTORY)

# Create a timestamped backup filename
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_filename = f'{DATABASE_FILENAME}.{timestamp}.bak'

# Copy the database file to the backup directory
shutil.copy(DATABASE_FILENAME, os.path.join(BACKUP_DIRECTORY, backup_filename))

# Run the migration
os.system('python manage.py migrate')

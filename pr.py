import os
import shutil
import zipfile
from datetime import datetime

# Paths
SOURCE_DIR = r"C:\Users\zawad\Downloads"  # Use your actual Downloads path
LOG_FILE = "backup_log.txt"               # Tracks already backed-up files
BACKUP_NAME = "Backup_"                   # Prefix for zip file
ONEDRIVE_DIR = r"C:\Users\zawad\OneDrive - Military Institute of Science and Technology (MIST)" # Your OneDrive folder

# ---- Load/Save Log ----
def load_log():
    log = {}
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f:
                if "|" in line:
                    relpath, mtime = line.strip().split("|")
                    log[relpath] = float(mtime)
    return log

def save_log(log_dict):
    with open(LOG_FILE, "w") as f:
        for relpath, mtime in log_dict.items():
            f.write(f"{relpath}|{mtime}\n")

# ---- File Organizer ----
def organize_files():
    categories = {
        "System & Executable Files": [
            ".exe", ".dll", ".sys", ".msi", ".bat", ".cmd", ".scr"
        ],
        "Document & Text Files": [
            ".txt", ".doc", ".docx", ".pdf", ".rtf", ".odt", ".ppt", ".pptx",
            ".xls", ".xlsx", ".csv"
        ],
        "Image Files": [
            ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff", ".ico", ".svg"
        ],
        "Audio & Video Files": [
            ".mp3", ".wav", ".flac", ".wma", ".mp4", ".avi", ".mkv", ".wmv"
        ],
        "Compressed & Archive Files": [
            ".zip", ".rar", ".7z", ".tar", ".gz", ".cab"
        ],
        "Programming & Script Files": [
            ".c", ".cpp", ".h", ".java", ".py", ".js", ".ts", ".html", ".css",
            ".php", ".sql", ".vbs", ".ps1"
        ],
        "Configuration & Data Files": [
            ".ini", ".cfg", ".json", ".xml", ".log", ".dat", ".reg",
            ".db", ".mdb", ".accdb"
        ],
        "Shortcut & Link Files": [
            ".lnk", ".url", ".iso", ".img"
        ]
    }

    for filename in os.listdir(SOURCE_DIR):
        filepath = os.path.join(SOURCE_DIR, filename)

        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder, extensions in categories.items():
                if ext in extensions:
                    folder_path = os.path.join(SOURCE_DIR, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    try:
                        shutil.move(filepath, os.path.join(folder_path, filename))
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(SOURCE_DIR, "Others")
                os.makedirs(other_path, exist_ok=True)
                try:
                    shutil.move(filepath, os.path.join(other_path, filename))
                except Exception as e:
                    print(f"Error moving {filename}: {e}")

    print("✅ Files organized.")

# ---- Incremental Backup ----
def create_incremental_backup():
    backed_up_files = load_log()
    new_files = []

    for foldername, subfolders, filenames in os.walk(SOURCE_DIR):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            relpath = os.path.relpath(filepath, SOURCE_DIR)
            mtime = os.path.getmtime(filepath)
            if (
                (relpath not in backed_up_files or backed_up_files[relpath] != mtime)
                and filename != os.path.basename(LOG_FILE)
            ):
                new_files.append((filepath, relpath, mtime))

    if not new_files:
        print("ℹ️ No new files to backup.")
        return None

    now = datetime.now().strftime("%Y-%m-%d_%H-%M")
    backup_file = os.path.join(ONEDRIVE_DIR, f"{BACKUP_NAME}{now}.zip")

    with zipfile.ZipFile(backup_file, 'w') as backup_zip:
        for file, relpath, mtime in new_files:
            backup_zip.write(file, relpath)

    # Update log
    for _, relpath, mtime in new_files:
        backed_up_files[relpath] = mtime
    save_log(backed_up_files)

    print(f"✅ Incremental backup created in OneDrive: {backup_file}")
    return backup_file

# ---- Main Flow ----
if __name__ == "__main__":
    organize_files()
    backup_file = create_incremental_backup()
    print("🚀 All tasks completed successfully!")
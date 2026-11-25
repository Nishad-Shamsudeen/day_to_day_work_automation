from datetime import date
from pathlib import Path

BASE_DIR = Path(r"D:\Attendance\Back Up\Attendance Backup\Biometric log and Overview")

today = date.today()
month_folder = BASE_DIR / today.strftime("%B")  # e.g. "November"
month_folder.mkdir(parents=True, exist_ok=True)

folder = month_folder / (today.strftime("%b-%d") + " Cleanup")  # e.g. "Nov-26 Cleanup"
folder.mkdir(exist_ok=True)
# print(f"Folder ready: {folder}")
import os
import time
import subprocess
from configparser import ConfigParser
from datetime import datetime
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ModuleNotFoundError as e:
    print(f"Error: {e}")
    print("Please install required modules using:")
    print("pip install watchdog")
    exit(1)


class EMFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.lower().endswith(".emf"):
            emf_file = event.src_path
            svg_file = os.path.join(
                target_folder, os.path.basename(emf_file)[:-4] + ".svg")

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            powershell_command = f"& '{inkscape_path}' '{emf_file}' --export-filename='{svg_file}'"
            inkscape_process = subprocess.Popen(
                ["powershell", powershell_command], shell=True)

            inkscape_process.wait()

            if inkscape_process.returncode == 0:
                print(
                    f"{current_time} - Converted and moved: {os.path.basename(emf_file)}")
                time.sleep(8)
                os.remove(emf_file)
            else:
                print(
                    f"Error: Inkscape process failed converting: {os.path.basename(emf_file)}")


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")

    folder_to_monitor = config.get("folders", "folder_to_monitor")
    target_folder = config.get("folders", "target_folder")
    inkscape_folder = os.path.join(config.get("folders", "inkscape_folder"))

    inkscape_folder = config.get("folders", "inkscape_folder")
    inkscape_path = os.path.join(inkscape_folder, "inkscape.exe")

    os.makedirs(target_folder, exist_ok=True)

    event_handler = EMFHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_monitor, recursive=False)

    print(
        f"Monitoring {folder_to_monitor} for EMF files. Press Ctrl+C to stop.")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

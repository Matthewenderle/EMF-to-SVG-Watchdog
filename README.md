# EMF to SVG Watchdog

> A Python script to monitor a folder, convert EMF files to SVG using Inkscape, and move them to another folder.

This script monitors a specified folder for EMF files, converts them to SVG using Inkscape, and moves the converted files to another folder.

_Disclaimer: The script uses Inkscape for the conversion process. Inkscape is a third-party tool, and its usage is subject to its license and terms of service._

## 🚀 Features

- Monitors a folder for EMF files
- Converts EMF to SVG using Inkscape
- Moves converted SVG files to another folder

## 🐾 How to Use

Download the files from this repository and follow the Installation steps below.

### Prerequisites

- Python 3.x
- Inkscape

### Installation

1. Clone the repository:

   ```sh
   $ git clone https://github.com/your_username/your_project.git
   $ cd your_project
   ```

   or download the zip archive and extract it.

2. Install required Python modules:

   ```sh
   $ pip install watchdog
   ```

3. Set up Inkscape:

   - Download and install Inkscape from [https://inkscape.org/download/](https://inkscape.org/download/).
   - Add Inkscape to your system PATH or specify the full path in the configuration.

4. Modify the `config.ini` file with the correct folders for your usage:

   ```ini
   [folders]
   folder_to_monitor = /path/to/monitor
   target_folder = /path/to/converted
   inkscape_folder = /path/to/inkscape
   ```

   _Please remember that Windows uses the `/` not `\`. If you copy the file path from Windows Explorer you will need to swap the slashes._

5. Run the script:

   ```sh
   $ python ./main.py
   ```

## 📝 Configuration

Adjust the settings in the `config.ini` file according to your folder locations and Inkscape setup.

## 📦 Python Libraries

### watchdog

| Name                                                   | Description                  |
| ------------------------------------------------------ | ---------------------------- |
| [`watchdog`](https://github.com/gorakhargosh/watchdog) | Monitors file system events. |

## ⚠️ Important Notes

- This script uses Inkscape for the conversion process. Ensure Inkscape is installed and accessible.
- The converted files will be moved, and the original EMF files will be deleted.

## Autorun at Boot

1. **Create a Shortcut:**

   - Right-click on your Python script (`main.py`) and select "Create Shortcut."
   - This will create a shortcut in the same folder as your script.

2. **Move Shortcut to a Permanent Location:**

   - Cut the shortcut from the current location and paste it into a permanent location. For example, you can place it in the `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup` folder. This folder is common for startup shortcuts.

     ```
     C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
     ```

3. **Reboot or Log In:**
   - Reboot your computer or log out and log back in to test whether the script runs at startup.

Now, your Python script should automatically run when the user logs in. Adjust the paths and filenames according to your actual setup.

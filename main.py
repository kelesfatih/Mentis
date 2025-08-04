import subprocess
import sys
import os
from pathlib import Path
import tempfile
import shutil

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def extract_bundled_files():
    """Extract all bundled files to a temporary directory"""
    temp_dir = Path(tempfile.mkdtemp(prefix="mentis_"))
    
    bundled_files = [
        "start.bat", 
        "launcher.bat", 
        "setup.py", 
        "mentis.py", 
        "requirements.txt"
    ]
    
    for file_name in bundled_files:
        src_path = get_resource_path(file_name)
        dest_path = temp_dir / file_name
        
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"Extracted {file_name}")
        else:
            print(f"Warning: {file_name} not found in bundle")
    
    return temp_dir

def main():
    """Main entry point that launches start.bat"""
    temp_dir = None
    try:
        if getattr(sys, 'frozen', False):
            # Running as compiled executable - extract files to temp directory
            temp_dir = extract_bundled_files()
            app_dir = temp_dir
            print(f"Files extracted to: {app_dir}")
        else:
            # Running as script - use current directory
            app_dir = Path(__file__).parent
        
        # Path to start.bat
        start_bat_path = app_dir / "start.bat"
        
        if not start_bat_path.exists():
            print(f"Error: start.bat not found at {start_bat_path}")
            print(f"Application directory: {app_dir}")
            if app_dir.exists():
                print(f"Files in directory: {list(app_dir.glob('*'))}")
            input("Press Enter to exit...")
            return 1
        
        # Run start.bat
        print("Starting Mentis...")
        result = subprocess.run([str(start_bat_path)], cwd=app_dir, shell=True)
        
        return result.returncode
        
    except Exception as e:
        print(f"Error starting Mentis: {e}")
        input("Press Enter to exit...")
        return 1
    finally:
        # Cleanup temp directory if we created one
        if temp_dir and temp_dir.exists():
            try:
                # Wait a moment before cleanup to ensure processes are done
                import time
                time.sleep(2)
                shutil.rmtree(temp_dir, ignore_errors=True)
                print("Cleaned up temporary files")
            except Exception as e:
                print(f"Warning: Could not cleanup temp files: {e}")

if __name__ == "__main__":
    sys.exit(main())
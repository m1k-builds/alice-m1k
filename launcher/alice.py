import sys
import subprocess
import os

# Map of command-line arguments to script files

# desktop(default): Opens Alice Desktop
# ohm: opens Ohm Meter
# dc: opens DC Meter
# strip: opens Strip Chart Tool
# Volt: opens Volt Meter
# logger: opens Data Logger

APP_MAP = {
    "desktop": "alice-desktop-1.3.pyw",
    "ohm": "ohm-meter-vdiv-1.3.pyw",
    "dc": "dc-meter-source-tool-1.3.pyw",
    "strip": "strip-chart-tool-1.3.pyw",
    "logger": "data-logger-tool-1.3.pyw",
    "volt": "volt-meter-tool-1.3.pyw",
}

def main():
    if len(sys.argv) > 1:
        app_key = sys.argv[1]
        app_args = sys.argv[2:]
    else:
        app_key = "desktop"
        app_args = []

    # Default to alice-desktop if unknown or no argument
    script_name = APP_MAP.get(app_key, "alice-desktop-1.3.pyw")

    script_path = os.path.join(os.path.dirname(__file__), "..", script_name)
    script_path = os.path.abspath(script_path)

    # Launch the target script with remaining args
    # Use sys.executable to ensure correct interpreter
    subprocess.run([sys.executable, script_path] + app_args)

if __name__ == "__main__":
    main()
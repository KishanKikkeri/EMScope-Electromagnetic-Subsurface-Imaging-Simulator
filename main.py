"""
main.py

Entry point for EMScope.

Initializes configuration,
validates environment,
and launches GUI.
"""

import sys
import argparse

from gui.main_window import launch


APP_NAME = "EMScope"
APP_VERSION = "1.0.0"


# --------------------------------------------------
# CLI Support (Future Expansion)
# --------------------------------------------------

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="EMScope - EM Subsurface Sensing Simulator"
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show application version"
    )

    parser.add_argument(
        "--nogui",
        action="store_true",
        help="Run without GUI (future CLI mode)"
    )

    return parser.parse_args()


# --------------------------------------------------
# Main Execution
# --------------------------------------------------

def main():

    args = parse_arguments()

    if args.version:
        print(f"{APP_NAME} Version: {APP_VERSION}")
        sys.exit(0)

    if args.nogui:
        print("CLI mode not implemented yet.")
        sys.exit(0)

    print(f"Launching {APP_NAME} v{APP_VERSION}...")
    launch()


# --------------------------------------------------

if __name__ == "__main__":
    main()

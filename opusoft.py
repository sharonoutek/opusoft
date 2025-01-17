import os
import argparse

def change_file_attributes(file_path, read_only=None, hidden=None, system=None):
    """Change file attributes for a given file."""
    current_attributes = os.stat(file_path).st_file_attributes

    if read_only is not None:
        if read_only:
            current_attributes |= 0x01  # FILE_ATTRIBUTE_READONLY
        else:
            current_attributes &= ~0x01

    if hidden is not None:
        if hidden:
            current_attributes |= 0x02  # FILE_ATTRIBUTE_HIDDEN
        else:
            current_attributes &= ~0x02

    if system is not None:
        if system:
            current_attributes |= 0x04  # FILE_ATTRIBUTE_SYSTEM
        else:
            current_attributes &= ~0x04

    os.chmod(file_path, current_attributes)

def main():
    parser = argparse.ArgumentParser(description="Change file attributes for multiple files.")
    parser.add_argument("files", metavar="F", type=str, nargs="+", help="Files to change attributes")
    parser.add_argument("--read-only", dest="read_only", action="store_true", help="Set files to read-only")
    parser.add_argument("--no-read-only", dest="read_only", action="store_false", help="Unset read-only attribute")
    parser.add_argument("--hidden", dest="hidden", action="store_true", help="Set files to hidden")
    parser.add_argument("--no-hidden", dest="hidden", action="store_false", help="Unset hidden attribute")
    parser.add_argument("--system", dest="system", action="store_true", help="Set files to system files")
    parser.add_argument("--no-system", dest="system", action="store_false", help="Unset system attribute")
    parser.set_defaults(read_only=None, hidden=None, system=None)

    args = parser.parse_args()

    for file in args.files:
        if os.path.exists(file):
            change_file_attributes(file, read_only=args.read_only, hidden=args.hidden, system=args.system)
            print(f"Attributes changed for: {file}")
        else:
            print(f"File not found: {file}")

if __name__ == "__main__":
    main()
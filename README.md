# Opusoft

Opusoft is a Python program designed to quickly change file attributes such as read-only, hidden, or system across multiple files on Windows operating systems.

## Features

- Set or unset the read-only attribute on files.
- Set or unset the hidden attribute on files.
- Set or unset the system attribute on files.
- Process multiple files at once.

## Requirements

- Python 3
- Windows operating system

## Installation

Clone this repository or download the `opusoft.py` file to your local machine.

```bash
git clone https://github.com/yourusername/opusoft.git
```

## Usage

Navigate to the directory containing `opusoft.py` and run the script using Python:

```bash
python opusoft.py [options] files...
```

### Options

- `--read-only`: Set files to read-only.
- `--no-read-only`: Unset read-only attribute.
- `--hidden`: Set files to hidden.
- `--no-hidden`: Unset hidden attribute.
- `--system`: Set files to system files.
- `--no-system`: Unset system attribute.

### Example

To set the read-only and hidden attributes on multiple files:

```bash
python opusoft.py --read-only --hidden file1.txt file2.txt
```

To unset the hidden attribute on a file:

```bash
python opusoft.py --no-hidden file1.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
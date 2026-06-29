# Digital Evidence Framework

A Python-based digital evidence collection and forensic workflow repository for Windows environments.

## Overview

This project provides a portable forensic evidence framework using SQLite for local case management, file hashing, and chain-of-custody tracking.

Key features:
- Case registration and incident summary storage
- Evidence acquisition with MD5 and SHA-256 hashing
- Chain of custody logging for evidence handling
- Interactive and automated execution paths
- Launcher menu to run core scripts from one place

## Contents

- `LAUNCHER.py`: Master launcher menu to run framework scripts
- `01 Digital_evidence_framework.py`: Core evidence collection framework
- `02 advance_digital_evidence_freamwork.py`: Advanced stress-test framework
- `03_FIXED_digital_evidence_real_file.py`: Real file evidence analyzer
- `04_FIXED_digital_evidence_multiusers.py`: Multi-user evidence collection flow
- `forensics_framework.db`, `advanced_forensics_framework.db`, `real_forensics_framework.db`: SQLite databases created by the scripts
- Documentation files: `EXACT_TERMINAL_COMMANDS.md`, `TERMINAL_COMMANDS.md`, `START_HERE.md`, `GUIDE_INDEX.md`, and more

## Getting Started

### Requirements

- Python 3.x installed
- Windows environment recommended for the included example commands

### Run the Launcher

Open a terminal and navigate to the repository folder. Then run:

```powershell
python LAUNCHER.py
```

Follow the interactive menu to run the basic framework, advanced framework, real file analyzer, multi-user mode, or demo flows.

### Run a Single Script

Examples:

```powershell
python "01 Digital_evidence_framework.py"
python "02 advance_digital_evidence_freamwork.py"
python "03_FIXED_digital_evidence_real_file.py"
python "04_FIXED_digital_evidence_multiusers.py"
```

## Notes

- The scripts create and use SQLite databases in the repository folder.
- Evidence file paths must be valid and accessible on the local machine.
- The project is designed for educational and demonstration purposes.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.

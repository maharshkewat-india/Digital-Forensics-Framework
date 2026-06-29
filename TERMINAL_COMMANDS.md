# 🖥️ TERMINAL COMMAND GUIDE - STEP BY STEP

## TABLE OF CONTENTS
1. [Windows Command Prompt](#windows-command-prompt)
2. [Windows PowerShell](#windows-powershell)
3. [Quick Commands Cheat Sheet](#quick-commands-cheat-sheet)
4. [Troubleshooting](#troubleshooting)

---

## WINDOWS COMMAND PROMPT

### **STEP 1: Open Command Prompt**

**Method A: Using Run Dialog**
```
1. Press: Windows Key + R
2. Type: cmd
3. Press: Enter
```

**Method B: Using Start Menu**
```
1. Click: Start Menu
2. Type: cmd
3. Click: Command Prompt
```

**Method C: In File Explorer**
```
1. Open File Explorer
2. Navigate to: C:\\path\\to\\digital evidence freamwork
3. Press: Ctrl + L (to focus address bar)
4. Type: cmd
5. Press: Enter
```

### **STEP 2: Navigate to Project Folder**

```
cd "C:\\path\\to\\digital evidence freamwork"
```

**What you'll see:**
```
C:\Users\MAHARSH>cd "C:\\path\\to\\digital evidence freamwork"

C:\\path\\to\\digital evidence freamwork>
```

### **STEP 3: Verify You're in Correct Folder**

```
dir
```

**Expected output:**
```
 Volume in drive C is Windows
 Volume Serial Number is XXXX-XXXX

 Directory of C:\\path\\to\\digital evidence freamwork

05/09/2026  10:30 AM    <DIR>          .
05/09/2026  10:30 AM    <DIR>          ..
05/09/2026  10:00 AM             5,234 01 digital_evidenve_freamwork.py
05/09/2026  10:00 AM             6,789 02 advance_digital_evidence_freamwork.py
05/09/2026  10:00 AM             7,123 03_FIXED_digital_evidence_real_file.py
05/09/2026  10:00 AM             8,456 04_FIXED_digital_evidence_multiusers.py
05/09/2026  10:30 AM             3,445 LAUNCHER.py
05/09/2026  10:30 AM               567 RUN_ME.bat
                         ... more files ...
```

### **STEP 4: Run the Launcher**

```
python LAUNCHER.py
```

**Expected output:**
```
C:\\path\\to\\digital evidence freamwork>python LAUNCHER.py

╔════════════════════════════════════════════════════════════════╗
║         DIGITAL EVIDENCE FRAMEWORK - MASTER LAUNCHER           ║
║                   Run Everything With One Click!               ║
╚════════════════════════════════════════════════════════════════╝

📋 SELECT PROGRAM TO RUN:

  1. Basic Framework (Automated)
     └─ Auto-runs with test file. No user input.
     └─ Runtime: ~2 seconds

  2. Advanced Framework (Stress Test)
     └─ Creates 5MB file and runs stress test...
     └─ Runtime: ~10 seconds

  3. Real File Analyzer (Interactive)
     └─ Analyze any real file on your system.
     └─ Runtime: ~2 seconds

  4. Multi-User Framework (Interactive)
     └─ Full workflow with detailed case information.
     └─ Runtime: ~1 minute

  5. Run ALL Programs Sequentially
     └─ Runs all 4 programs one after another.
     └─ Runtime: ~15 seconds

  6. Quick Demo (Files 1 + 2)
     └─ Shows both automated programs quickly.
     └─ Runtime: ~12 seconds

  0. EXIT

Enter your choice (0-6):
```

### **STEP 5: Choose Your Option**

**Option A: Quick Demo (Recommended First Time)**
```
Enter your choice (0-6): 6
```

**Option B: Run All Programs**
```
Enter your choice (0-6): 5
```

**Option C: Analyze Real File**
```
Enter your choice (0-6): 3
```
Then enter file path when prompted:
```
Enter file path: C:\Windows\System32\drivers\etc\hosts
```

**Option D: Exit**
```
Enter your choice (0-6): 0
```

---

## WINDOWS POWERSHELL

### **STEP 1: Open PowerShell**

**Method A: In Current Folder**
```
1. Open File Explorer
2. Navigate to: C:\\path\\to\\digital evidence freamwork
3. Click in address bar
4. Type: powershell
5. Press: Enter
```

**Method B: Using Start Menu**
```
1. Press: Windows Key
2. Type: powershell
3. Click: Windows PowerShell
```

**Method C: From Command Prompt**
```
powershell
```

### **STEP 2: Navigate to Project Folder**

```
cd "C:\\path\\to\\digital evidence freamwork"
```

**What you'll see:**
```
PS C:\Users\MAHARSH>cd "C:\\path\\to\\digital evidence freamwork"
PS C:\\path\\to\\digital evidence freamwork>
```

### **STEP 3: Verify Files Exist**

```
ls
```

or

```
Get-ChildItem
```

**Expected output:**
```
    Directory: C:\\path\\to\\digital evidence freamwork

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         5/9/2026  10:30 AM           5234 01 digital_evidenve_freamwork.py
-a----         5/9/2026  10:00 AM           6789 02 advance_digital_evidence_freamwork.py
-a----         5/9/2026  10:00 AM           7123 03_FIXED_digital_evidence_real_file.py
... more files ...
```

### **STEP 4: Run the Launcher**

```
python LAUNCHER.py
```

### **STEP 5: Choose Your Option**

Same as Command Prompt (see above)

---

## QUICK COMMANDS CHEAT SHEET

### **LAUNCH COMMANDS (Copy & Paste)**

**ONE-LINER (From Any Folder):**
```
python "C:\\path\\to\\digital evidence freamwork\LAUNCHER.py"
```

**FROM PROJECT FOLDER:**
```
cd "C:\\path\\to\\digital evidence freamwork" && python LAUNCHER.py
```

**RUN SPECIFIC PROGRAM (File 1 - Basic):**
```
cd "C:\\path\\to\\digital evidence freamwork" && python "01_FIXED_digital_evidence_framework.py"
```

**RUN SPECIFIC PROGRAM (File 3 - Real File):**
```
cd "C:\\path\\to\\digital evidence freamwork" && python "03_FIXED_digital_evidence_real_file.py"
```

**RUN SPECIFIC PROGRAM (File 4 - Multi-User):**
```
cd "C:\\path\\to\\digital evidence freamwork" && python "04_FIXED_digital_evidence_multiusers.py"
```

**RUN SPECIFIC PROGRAM (File 2 - Advanced):**
```
cd "C:\\path\\to\\digital evidence freamwork" && python "02 advance_digital_evidence_freamwork.py"
```

---

## STEP-BY-STEP SCENARIOS

### **SCENARIO 1: Complete Fresh Start (Recommended)**

```
STEP 1: Press Windows Key + R
STEP 2: Type: cmd
STEP 3: Press: Enter
STEP 4: Copy and paste this entire command:

cd "C:\\path\\to\\digital evidence freamwork" && python LAUNCHER.py

STEP 5: Press: Enter
STEP 6: When menu appears, type: 6
STEP 7: Press: Enter
STEP 8: Watch the quick demo run!
STEP 9: Press: Enter to return to menu
STEP 10: Type: 0 to exit
STEP 11: Press: Enter
```

### **SCENARIO 2: Analyze Your Own File**

```
STEP 1: Open Command Prompt (Windows Key + R, type cmd, Enter)
STEP 2: Paste this:

cd "C:\\path\\to\\digital evidence freamwork" && python "03_FIXED_digital_evidence_real_file.py"

STEP 3: Press: Enter
STEP 4: When prompted, enter your file path, e.g.:

C:\Windows\System32\drivers\etc\hosts

STEP 5: Press: Enter
STEP 6: Wait for analysis to complete
STEP 7: See the report!
```

### **SCENARIO 3: Full Forensic Investigation**

```
STEP 1: Open Command Prompt
STEP 2: Paste this:

cd "C:\\path\\to\\digital evidence freamwork" && python "04_FIXED_digital_evidence_multiusers.py"

STEP 3: Press: Enter
STEP 4: Follow the prompts:
        - Enter Case ID: CASE-2026-001
        - Enter Investigator Name: Your Name
        - Enter Case Summary: Description
        - Enter File Path: Your file path
        - Enter Device Type: Type of device
        - Enter Evidence Label: Name
        - Enter Owner's Name: Owner
        - Enter Seizure Location: Location
        - Enter Storage Locker: Storage location
        - Enter purpose: Purpose description

STEP 5: Press Enter after each prompt
STEP 6: Wait for report generation
STEP 7: See complete forensic report
```

### **SCENARIO 4: Run All Programs Sequentially**

```
STEP 1: Open Command Prompt
STEP 2: Navigate to folder:

cd "C:\\path\\to\\digital evidence freamwork"

STEP 3: Press: Enter
STEP 4: Start launcher:

python LAUNCHER.py

STEP 5: Press: Enter
STEP 6: When menu appears, type: 5
STEP 7: Press: Enter
STEP 8: Watch all 4 programs run automatically!
STEP 9: Wait for "ALL PROGRAMS COMPLETED!" message
STEP 10: Type: 0 to exit
STEP 11: Press: Enter
```

---

## TERMINAL BASICS REFERENCE

| Command | What It Does | Example |
|---------|-------------|---------|
| `cd` | Change directory | `cd Documents` |
| `dir` | List files (CMD) | `dir` |
| `ls` | List files (PS) | `ls` |
| `python` | Run Python file | `python script.py` |
| `cls` | Clear screen (CMD) | `cls` |
| `clear` | Clear screen (PS) | `clear` |
| `pwd` | Show current path | `pwd` |
| `exit` | Close terminal | `exit` |

---

## NAVIGATING PATHS

### **Absolute Path (Full Path)**
```
cd "C:\\path\\to\\digital evidence freamwork"
```

### **Relative Path (From Current Location)**
```
cd Desktop
cd "digital evidence freamwork"
```

### **Go Back One Folder**
```
cd ..
```

### **Go to Home**
```
cd %USERPROFILE%    (Command Prompt)
cd ~                (PowerShell)
```

---

## FILE OPERATIONS

### **View Python Version**
```
python --version
```

**Expected output:**
```
Python 3.11.x (or similar)
```

### **Check if Python is Installed**
```
where python
```

**Expected output:**
```
C:\Users\MAHARSH\AppData\Local\Programs\Python\Python311\python.exe
```

### **List All Files in Folder**
```
dir                    (Command Prompt)
ls                     (PowerShell)
Get-ChildItem          (PowerShell)
```

### **Check Specific File**
```
dir LAUNCHER.py
```

---

## ADVANCED COMMANDS

### **Run Multiple Commands in Sequence**
```
cd "C:\\path\\to\\digital evidence freamwork" && python LAUNCHER.py
```

### **Run and Keep Terminal Open**
```
python LAUNCHER.py && pause
```

### **Run in Background (PowerShell)**
```
Start-Process python -ArgumentList "LAUNCHER.py"
```

### **Create Test File**
```
echo "test data" > testfile.txt
```

### **Delete File**
```
del filename.txt
```

### **See Recent Files**
```
dir /O:-D
```

---

## TROUBLESHOOTING COMMANDS

### **Check Python Installation**
```
python --version
```

### **Check Python Location**
```
where python
```

### **Check Current Directory**
```
cd    (shows current path)
```

### **Check if File Exists**
```
dir LAUNCHER.py
```

### **Get Help for Command**
```
python --help
```

---

## COPY-PASTE COMMANDS

### **Ready to Copy (Just paste into terminal)**

**Quick Demo:**
```
cd "C:\\path\\to\\digital evidence freamwork" && python LAUNCHER.py
```
Then type `6` and press Enter

**Analyze Real File:**
```
cd "C:\\path\\to\\digital evidence freamwork" && python "03_FIXED_digital_evidence_real_file.py"
```

**Full Investigation:**
```
cd "C:\\path\\to\\digital evidence freamwork" && python "04_FIXED_digital_evidence_multiusers.py"
```

**Run All Programs:**
```
cd "C:\\path\\to\\digital evidence freamwork" && python LAUNCHER.py
```
Then type `5` and press Enter

---

## EXPECTED OUTPUT SAMPLES

### **After Running LAUNCHER.py:**
```
╔════════════════════════════════════════════════════════════════╗
║         DIGITAL EVIDENCE FRAMEWORK - MASTER LAUNCHER           ║
║                   Run Everything With One Click!               ║
╚════════════════════════════════════════════════════════════════╝

📖 QUICK INSTRUCTIONS:

  • Choose a program from the menu (1-6)
  • Some programs run automatically (no input needed)
  ...

📋 SELECT PROGRAM TO RUN:

  1. Basic Framework (Automated)
     ...

Enter your choice (0-6):
```

### **After Running File 1 (Basic):**
```
--- DIGITAL EVIDENCE COLLECTION FRAMEWORK (PROTOTYPE - FIXED) ---

[+] Database initialized successfully.
[*] Acquiring evidence from: dummy_evidence.txt...
[+] Evidence logged successfully. Evidence ID: 1
    MD5: 5d41402abc4b2a76b9719d911017c592
    SHA-256: 2c26b46911185131006ba9567d392...
[+] Chain of Custody updated for Evidence ID 1.

 DIGITAL EVIDENCE FORENSIC REPORT
═════════════════════════════════════════
Case ID: CASE-2026-001
Investigator: Investigator Maharsh
...

[+] Cleanup completed.
```

---

## QUICK REFERENCE: MOST COMMON COMMANDS

```
# Open terminal, navigate to project
cd "C:\\path\\to\\digital evidence freamwork"

# Run launcher (main menu)
python LAUNCHER.py

# Run specific programs directly
python "01_FIXED_digital_evidence_framework.py"
python "03_FIXED_digital_evidence_real_file.py"
python "04_FIXED_digital_evidence_multiusers.py"

# Exit terminal
exit
```

---

## THAT'S IT!

### **Simplest Method:**
```
1. Press: Windows Key + R
2. Type: cmd
3. Press: Enter
4. Paste: cd "C:\\path\\to\\digital evidence freamwork" && python LAUNCHER.py
5. Press: Enter
6. Enjoy!
```

---

**Last Updated: 2026-05-09**




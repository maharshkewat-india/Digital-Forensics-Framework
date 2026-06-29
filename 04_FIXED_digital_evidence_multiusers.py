import sqlite3
import hashlib
import datetime
import os
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DB_PATH = PROJECT_DIR / "forensics_framework.db"

# FIX: User input validation helper
def validate_file_path(file_path):
    '''Validate that file path exists and is accessible'''
    if not file_path or not isinstance(file_path, str):
        return False
    if not os.path.exists(file_path):
        return False
    if not os.path.isfile(file_path):
        return False
    return True

def validate_non_empty_string(value, field_name):
    '''Validate that string input is not empty'''
    if not value or not isinstance(value, str) or len(value.strip()) == 0:
        print(f"[!] Error: {field_name} cannot be empty.")
        return False
    return True

def setup_database():
    '''Initialize the SQLite database and create necessary tables.'''
    conn = None
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Module 1: Case Registration Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cases (
                case_id TEXT PRIMARY KEY,
                investigator_name TEXT,
                incident_summary TEXT,
                registration_date TEXT
            )
        ''')
        
        # Module 2 & 5: Evidence Identification and Storage Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evidence (
                evidence_id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_id TEXT,
                device_type TEXT,
                device_label TEXT,
                owner_details TEXT,
                seizure_location TEXT,
                original_md5 TEXT,
                original_sha256 TEXT,
                storage_location TEXT,
                FOREIGN KEY(case_id) REFERENCES cases(case_id)
            )
        ''')
        
        # Module 4: Chain of Custody Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chain_of_custody (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                evidence_id INTEGER,
                timestamp TEXT,
                person_handling TEXT,
                purpose TEXT,
                FOREIGN KEY(evidence_id) REFERENCES evidence(evidence_id)
            )
        ''')
        
        conn.commit()
        print("[+] Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"[!] Database initialization error: {e}")
    finally:
        if conn:
            conn.close()

def generate_hashes(file_path):
    '''Module 3: Evidence Acquisition (Hash Generation)'''
    # FIX: File existence validation
    if not validate_file_path(file_path):
        print(f"[!] Error: File '{file_path}' not found or is not accessible.")
        return None, None
    
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    
    try:
        print(f"[*] Generating hashes for: {file_path}")
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha256_hash.update(byte_block)
        return md5_hash.hexdigest(), sha256_hash.hexdigest()
    except (FileNotFoundError, IOError, PermissionError) as e:
        print(f"[!] File access error: {e}")
        return None, None

def register_case(case_id, investigator, summary):
    '''Module 1: Register a new case'''
    # FIX: Input validation
    if not validate_non_empty_string(case_id, "Case ID"):
        return False
    if not validate_non_empty_string(investigator, "Investigator Name"):
        return False
    if not validate_non_empty_string(summary, "Case Summary"):
        return False
    
    conn = None
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("INSERT INTO cases VALUES (?, ?, ?, ?)", (case_id, investigator, summary, date_now))
        conn.commit()
        print(f"[+] Case '{case_id}' registered successfully.")
        return True
    except sqlite3.IntegrityError:
        print(f"[!] Error: Case '{case_id}' already exists.")
        return False
    except sqlite3.Error as e:
        print(f"[!] Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()

def log_evidence(case_id, device_type, label, owner, location, file_path, storage):
    '''Modules 2, 3 & 5: Identify, hash, and store evidence'''
    # FIX: Input validation
    if not validate_non_empty_string(case_id, "Case ID"):
        return None
    if not validate_non_empty_string(device_type, "Device Type"):
        return None
    if not validate_file_path(file_path):
        print(f"[!] Error: Evidence file '{file_path}' does not exist or is not accessible.")
        return None
    
    print(f"[*] Acquiring evidence from: {file_path}...")
    md5, sha256 = generate_hashes(file_path)
    
    if not md5:
        print("[!] Error: Could not generate hashes. Cannot acquire evidence.")
        return None

    conn = None
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO evidence (case_id, device_type, device_label, owner_details, seizure_location, original_md5, original_sha256, storage_location)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (case_id, device_type, label, owner, location, md5, sha256, storage))
        
        evidence_id = cursor.lastrowid
        conn.commit()
        
        print(f"[+] Evidence logged successfully. Evidence ID: {evidence_id}")
        print(f"    MD5: {md5}")
        print(f"    SHA-256: {sha256}")
        
        # Log initial chain of custody
        add_coc_entry(evidence_id, "System / Initial Investigator", "Initial Seizure and Acquisition")
        return evidence_id
    except sqlite3.Error as e:
        print(f"[!] Database error while logging evidence: {e}")
        return None
    finally:
        if conn:
            conn.close()

def add_coc_entry(evidence_id, person, purpose):
    '''Module 4: Chain of Custody Logging'''
    conn = None
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # FIX: Validate evidence_id exists
        cursor.execute("SELECT evidence_id FROM evidence WHERE evidence_id=?", (evidence_id,))
        if not cursor.fetchone():
            print(f"[!] Error: Evidence ID {evidence_id} not found in database.")
            return False
        
        cursor.execute('''
            INSERT INTO chain_of_custody (evidence_id, timestamp, person_handling, purpose)
            VALUES (?, ?, ?, ?)
        ''', (evidence_id, timestamp, person, purpose))
        
        conn.commit()
        print(f"[+] Chain of Custody updated for Evidence ID {evidence_id}.")
        return True
    except sqlite3.Error as e:
        print(f"[!] Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()

def generate_report(case_id):
    '''Module 6: Reporting'''
    conn = None
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM cases WHERE case_id=?", (case_id,))
        case = cursor.fetchone()
        
        if not case:
            print("[!] Case not found.")
            return
            
        print("\n" + "="*50)
        print(" DIGITAL EVIDENCE FORENSIC REPORT")
        print("="*50)
        print(f"Case ID: {case[0]}\nInvestigator: {case[1]}\nDate: {case[3]}\nSummary: {case[2]}\n")
        
        cursor.execute("SELECT * FROM evidence WHERE case_id=?", (case_id,))
        evidences = cursor.fetchall()
        
        for ev in evidences:
            print("-" * 40)
            print(f"Evidence ID : {ev[0]}")
            print(f"Device Type : {ev[2]}")
            print(f"Label       : {ev[3]}")
            print(f"Seized At   : {ev[5]}")
            print(f"MD5 Hash    : {ev[6]}")
            print(f"SHA-256     : {ev[7]}")
            print(f"Stored In   : {ev[8]}")
            
            print("\n  --- Chain of Custody ---")
            cursor.execute("SELECT timestamp, person_handling, purpose FROM chain_of_custody WHERE evidence_id=?", (ev[0],))
            cocs = cursor.fetchall()
            for coc in cocs:
                print(f"  [{coc[0]}] {coc[1]} - {coc[2]}")
            print("-" * 40)
            
        print("="*50 + "\n")
    except sqlite3.Error as e:
        print(f"[!] Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_database()
    print("==================================================")
    print("    DIGITAL EVIDENCE COLLECTION FRAMEWORK (FIXED)")
    print("==================================================\n")
    
    # FIX: Added input validation loop
    while True:
        print(">>> STEP 1: CASE REGISTRATION")
        case_number = input("Enter Case ID (e.g., CASE-001): ").strip()
        investigator = input("Enter Investigator Name: ").strip()
        summary = input("Enter Case Summary/Description: ").strip()
        
        if register_case(case_number, investigator, summary):
            break
        print("Please try again with valid inputs.\n")
    
    # FIX: Added file path validation loop
    print("\n>>> STEP 2: EVIDENCE ACQUISITION")
    while True:
        suspect_file_path = input(r"Enter File Path (e.g., C:\Users\Desktop\file.txt): ").strip()
        if validate_file_path(suspect_file_path):
            break
        print(f"[!] File not found. Please enter a valid file path.\n")
    
    dev_type = input("Enter Device/File Type (e.g., Hard Drive, PDF, Image): ").strip()
    dev_label = input("Enter Evidence Label (e.g., Suspect's Laptop): ").strip()
    owner_name = input("Enter Owner's Name: ").strip()
    seize_loc = input("Enter Seizure Location: ").strip()
    storage_loc = input("Enter Storage Locker/Location: ").strip()
    
    # Data transfer to function
    ev_id = log_evidence(
        case_id=case_number,
        device_type=dev_type,
        label=dev_label,
        owner=owner_name,
        location=seize_loc,
        file_path=suspect_file_path,
        storage=storage_loc
    )
    
    # Step 3: Chain of Custody (Optional)
    if ev_id:
        print("\n>>> STEP 3: CHAIN OF CUSTODY")
        coc_purpose = input("Enter purpose of handling this evidence: ").strip()
        if coc_purpose:
            add_coc_entry(ev_id, investigator, coc_purpose)
    
        # Step 4: Generate Report
        print("\n[+] Generating Report...\n")
        generate_report(case_number)
    else:
        print("[!] Evidence could not be logged. Skipping report generation.")

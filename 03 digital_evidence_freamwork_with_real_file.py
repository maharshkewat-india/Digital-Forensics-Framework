import sqlite3
import hashlib
import datetime
import os
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DB_PATH = PROJECT_DIR / "real_forensics_framework.db"

def setup_database():
    '''Initialize the SQLite database and create necessary tables.'''
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
    conn.close()

def validate_file_path(file_path):
    '''Validate that file path exists and is a file.'''
    if not file_path or not isinstance(file_path, str):
        return False
    if not os.path.exists(file_path):
        return False
    if not os.path.isfile(file_path):
        return False
    return True


def generate_hashes(file_path):
    '''Module 3: Evidence Acquisition (Hash Generation)'''
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    
    if not validate_file_path(file_path):
        return None, None
    
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha256_hash.update(byte_block)
        return md5_hash.hexdigest(), sha256_hash.hexdigest()
    except (FileNotFoundError, IOError, PermissionError):
        return None, None

def register_case(case_id, investigator, summary):
    '''Module 1: Register a new case'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        cursor.execute("INSERT INTO cases VALUES (?, ?, ?, ?)", (case_id, investigator, summary, date_now))
        conn.commit()
        print(f"[*] Case '{case_id}' registered successfully.")
    except sqlite3.IntegrityError:
        print(f"[*] Case '{case_id}' pehle se exist karta hai. Naya evidence usime add ho raha hai.")
    finally:
        conn.close()

def log_evidence(case_id, device_type, label, owner, location, file_path, storage):
    '''Modules 2, 3 & 5: Identify, hash, and store evidence'''
    print(f"[*] Acquiring evidence from: {file_path}...")
    md5, sha256 = generate_hashes(file_path)
    
    if not md5:
        print(f"[!] Error: File '{file_path}' nahi mili. Check karein ki path sahi hai.")
        return None

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO evidence (case_id, device_type, device_label, owner_details, seizure_location, original_md5, original_sha256, storage_location)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (case_id, device_type, label, owner, location, md5, sha256, storage))
    
    evidence_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    print(f"[*] Evidence logged successfully. Evidence ID: {evidence_id}")
    print(f"    MD5: {md5}")
    print(f"    SHA-256: {sha256}")
    
    # Log initial chain of custody
    add_coc_entry(evidence_id, "System / Maharsh", "Initial Seizure and Acquisition")
    return evidence_id

def add_coc_entry(evidence_id, person, purpose):
    '''Module 4: Chain of Custody Logging'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO chain_of_custody (evidence_id, timestamp, person_handling, purpose)
        VALUES (?, ?, ?, ?)
    ''', (evidence_id, timestamp, person, purpose))
    
    conn.commit()
    conn.close()
    print(f"[*] Chain of Custody updated for Evidence ID {evidence_id}.")

def generate_report(case_id):
    '''Module 6: Reporting'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM cases WHERE case_id=?", (case_id,))
    case = cursor.fetchone()
    
    if not case:
        print("[!] Case not found.")
        return
        
    print("\n" + "="*60)
    print(" DIGITAL EVIDENCE FORENSIC REPORT")
    print("="*60)
    print(f"Case ID: {case[0]}\nInvestigator: {case[1]}\nDate: {case[3]}\nSummary: {case[2]}\n")
    
    cursor.execute("SELECT * FROM evidence WHERE case_id=?", (case_id,))
    evidences = cursor.fetchall()
    
    for ev in evidences:
        print("-" * 60)
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
        print("-" * 60)
        
    print("="*60 + "\n")
    conn.close()


if __name__ == "__main__":
    setup_database()
    
    print("--- DIGITAL EVIDENCE COLLECTION FRAMEWORK (REAL FILE) ---\n")
    
    case_number = "CASE-2026-REAL-01"
    investigator = "Investigator Maharsh"
    
    print("Enter the path to the file you want to analyze.")
    print("Example: C:\\Users\\YourName\\Desktop\\meri_photo.jpg\n")
    suspect_file = input("Enter file path: ").strip()

    if not validate_file_path(suspect_file):
        print(f"[!] Error: File '{suspect_file}' not found or is not accessible.")
        print("Exiting...")
        exit(1)
    
    # 1. Register Case
    register_case(case_number, investigator, "Scanning a real file from the system.")
    
    # 2. Log Evidence & Acquire (Yahan 'file_path' me humari file ka variable pass ho raha hai)
    ev_id = log_evidence(
        case_id=case_number,
        device_type="Unknown Storage",
        label="My Test File",
        owner="Maharsh",
        location="My Computer",
        file_path=suspect_file,  # YAHAN APKI FILE AAYEGI
        storage="Evidence Locker A"
    )
    
    # 3. Add Chain of Custody Entry (Agar file mili tabhi add karega)
    if ev_id:
        add_coc_entry(ev_id, "Forensics Analyst Maharsh", "Hash calculation completed successfully.")
    
        # 4. Generate Final Report
        generate_report(case_number)
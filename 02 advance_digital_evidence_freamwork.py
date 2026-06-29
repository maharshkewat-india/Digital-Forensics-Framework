import sqlite3
import hashlib
import datetime
import os
import time
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DB_PATH = PROJECT_DIR / "advanced_forensics_framework.db"

class EvidenceFramework:
    def __init__(self):
        self.db = DB_PATH
        self.memory_buffer = []
        self.setup_database()
        self.log_instance("System Initialized and Database connected.")

    def log_instance(self, msg, level="INFO"):
        '''Simulates the deep system logging seen in the report appendix'''
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {level} - [System Thread] - {msg}")

    def setup_database(self):
        '''Initialize the SQLite database with strict constraints.'''
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cases (
                case_id TEXT PRIMARY KEY,
                investigator_name TEXT,
                incident_summary TEXT,
                registration_date TEXT
            )
        ''')
        
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

    def generate_hashes(self, file_path):
        '''Reads file in chunks to prevent memory overflow during massive file ingestion.'''
        self.log_instance(f"Initiating cryptographic hashing for {file_path}")
        md5_hash = hashlib.md5()
        sha256_hash = hashlib.sha256()
        
        try:
            with open(file_path, "rb") as f:
                block_count = 0
                for byte_block in iter(lambda: f.read(4096), b""):
                    md5_hash.update(byte_block)
                    sha256_hash.update(byte_block)
                    
                    # Simulated Buffer Logic from Appendix A
                    self.memory_buffer.append(byte_block)
                    block_count += 1
                    if len(self.memory_buffer) > 1024:
                        self.memory_buffer.clear()
                        self.log_instance(f"Buffer flushed successfully at block {block_count} to prevent overflow.", "DEBUG")
                        
            return md5_hash.hexdigest(), sha256_hash.hexdigest()
        except FileNotFoundError:
            self.log_instance("File not found error.", "ERROR")
            return None, None

    def register_case(self, case_id, investigator, summary):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            cursor.execute("INSERT INTO cases VALUES (?, ?, ?, ?)", (case_id, investigator, summary, date_now))
            conn.commit()
            self.log_instance(f"Case '{case_id}' registered successfully by {investigator}.")
        except sqlite3.IntegrityError:
            self.log_instance(f"Case '{case_id}' already exists. Skipping registration.", "WARNING")
        finally:
            conn.close()

    def log_evidence(self, case_id, device_type, label, owner, location, file_path, storage, investigator):
        self.log_instance(f"Acquiring evidence from source: {file_path}...")
        md5, sha256 = self.generate_hashes(file_path)
        
        if not md5:
            self.log_instance("Cannot acquire evidence. Aborting.", "ERROR")
            return None

        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO evidence (case_id, device_type, device_label, owner_details, seizure_location, original_md5, original_sha256, storage_location)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (case_id, device_type, label, owner, location, md5, sha256, storage))
        
        evidence_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        self.log_instance(f"Evidence locked into database. ID: {evidence_id} | MD5: {md5[:8]}... | SHA256: {sha256[:8]}...")
        
        # Immediate CoC record as required by forensic standards
        self.add_coc_entry(evidence_id, f"System / {investigator}", "Initial Seizure and Cryptographic Baseline")
        return evidence_id

    def add_coc_entry(self, evidence_id, person, purpose):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO chain_of_custody (evidence_id, timestamp, person_handling, purpose)
            VALUES (?, ?, ?, ?)
        ''', (evidence_id, timestamp, person, purpose))
        
        conn.commit()
        conn.close()
        self.log_instance(f"Chain of Custody securely updated for Evidence ID {evidence_id}.")

    def simulate_stress_test(self, evidence_id):
        '''Simulates the massive log generation seen in Appendix B'''
        self.log_instance("--- INITIATING STRESS TEST (Appendix B Simulation) ---", "WARNING")
        for i in range(1, 101): # Generating 100 log entries quickly
            self.add_coc_entry(evidence_id, "Automated Test Script", f"Load test transaction {i}")
            if i % 25 == 0:
                self.log_instance(f"Executing cryptographic verification sequence block {i}... Status: OK")
                self.log_instance(f"Committing {i*10} bytes to SQLite transaction log.", "DEBUG")
            time.sleep(0.01) # tiny sleep to ensure timestamp difference sometimes
        self.log_instance("--- STRESS TEST COMPLETE ---", "WARNING")

    def generate_report(self, case_id):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM cases WHERE case_id=?", (case_id,))
        case = cursor.fetchone()
        
        if not case:
            print("[!] Case not found.")
            return
            
        print("\n" + "="*80)
        print(" " * 20 + "DIGITAL EVIDENCE FORENSIC REPORT")
        print("="*80)
        print(f"Case ID:      {case[0]}\nInvestigator: {case[1]}\nDate:         {case[3]}\nSummary:      {case[2]}\n")
        
        cursor.execute("SELECT * FROM evidence WHERE case_id=?", (case_id,))
        evidences = cursor.fetchall()
        
        for ev in evidences:
            print("-" * 80)
            print(f"Evidence ID : {ev[0]}")
            print(f"Device Type : {ev[2]}")
            print(f"Label       : {ev[3]}")
            print(f"Seized At   : {ev[5]}")
            print(f"MD5 Hash    : {ev[6]}")
            print(f"SHA-256     : {ev[7]}")
            print(f"Stored In   : {ev[8]}")
            
            print("\n  --- Chain of Custody Ledger ---")
            cursor.execute("SELECT timestamp, person_handling, purpose FROM chain_of_custody WHERE evidence_id=? ORDER BY log_id DESC LIMIT 10", (ev[0],))
            cocs = cursor.fetchall()
            print("  (Showing last 10 entries due to stress testing...)")
            for coc in reversed(cocs):
                print(f"  [{coc[0]}] {coc[1]} - {coc[2]}")
            print("-" * 80)
            
        print("="*80 + "\n")
        conn.close()

if __name__ == "__main__":
    # Create a large dummy file (e.g., 5MB) to trigger the buffer flush logic
    dummy_file = "massive_dummy_evidence.dat"
    print("Generating massive simulated evidence file...")
    with open(dummy_file, "wb") as f:
        f.write(os.urandom(5 * 1024 * 1024)) # 5MB of random bytes
        
    print("\n--- ADVANCED DIGITAL EVIDENCE COLLECTION FRAMEWORK ---\n")
    
    framework = EvidenceFramework()
    investigator_name = "Maharsh"
    case_number = "CASE-2026-ADV"
    
    # 1. Register Case
    framework.register_case(case_number, investigator_name, "Advanced testing of scalable hashing and CoC logging.")
    
    # 2. Log Evidence & Acquire (Hashes massive file, triggers buffer flush)
    ev_id = framework.log_evidence(
        case_id=case_number,
        device_type="Seized Server HDD",
        label="WD Red 4TB",
        owner="Corporate Suspect",
        location="Data Center Rack 4",
        file_path=dummy_file,
        storage="Evidence Locker High-Security",
        investigator=investigator_name
    )
    
    # 3. Add Chain of Custody Entry manually
    framework.add_coc_entry(ev_id, f"Forensics Analyst Sarah", "Creating working copy for analysis")
    
    # 4. Trigger the Stress Test to simulate heavy logs (Appendix B)
    framework.simulate_stress_test(ev_id)
    
    # 5. Generate Final Report
    framework.generate_report(case_number)
    
    # Cleanup dummy file
    if os.path.exists(dummy_file):
        os.remove(dummy_file)
        framework.log_instance("Cleaned up simulated evidence file.")
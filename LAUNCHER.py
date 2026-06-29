#!/usr/bin/env python3
"""
DIGITAL EVIDENCE FRAMEWORK - MASTER LAUNCHER
Run entire project with one click!
"""

import os
import sys
import subprocess
import time
from pathlib import Path

# Project directory
PROJECT_DIR = Path(__file__).parent.absolute()

# File definitions
FILES = {
    "1": {
        "name": "Basic Framework (Automated)",
        "file": "01_FIXED_digital_evidence_framework.py",
        "description": "Auto-runs with test file. No user input.",
        "runtime": "~2 seconds",
        "type": "automated"
    },
    "2": {
        "name": "Advanced Framework (Stress Test)",
        "file": "02 advance_digital_evidence_freamwork.py",
        "description": "Creates 5MB file and runs stress test. Slower but comprehensive.",
        "runtime": "~10 seconds",
        "type": "automated"
    },
    "3": {
        "name": "Real File Analyzer (Interactive)",
        "file": "03_FIXED_digital_evidence_real_file.py",
        "description": "Analyze any real file on your system.",
        "runtime": "~2 seconds",
        "type": "interactive"
    },
    "4": {
        "name": "Multi-User Framework (Interactive)",
        "file": "04_FIXED_digital_evidence_multiusers.py",
        "description": "Full workflow with detailed case information.",
        "runtime": "~1 minute",
        "type": "interactive"
    },
    "5": {
        "name": "Run ALL Programs Sequentially",
        "file": "ALL",
        "description": "Runs all 4 programs one after another.",
        "runtime": "~15 seconds",
        "type": "batch"
    },
    "6": {
        "name": "Quick Demo (Files 1 + 2)",
        "file": "DEMO",
        "description": "Shows both automated programs quickly.",
        "runtime": "~12 seconds",
        "type": "batch"
    }
}

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print welcome banner"""
    banner = """
╔════════════════════════════════════════════════════════════════╗
║         DIGITAL EVIDENCE FRAMEWORK - MASTER LAUNCHER           ║
║                   Run Everything With One Click!               ║
╚════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def print_menu():
    """Print main menu"""
    print("\n📋 SELECT PROGRAM TO RUN:\n")
    for key, info in FILES.items():
        print(f"  {key}. {info['name']}")
        print(f"     └─ {info['description']}")
        print(f"     └─ Runtime: {info['runtime']}\n")
    print("  0. EXIT\n")

def verify_files():
    """Check if required Python files exist"""
    missing = []
    required_files = [
        "01_FIXED_digital_evidence_framework.py",
        "02 advance_digital_evidence_freamwork.py",
        "03_FIXED_digital_evidence_real_file.py",
        "04_FIXED_digital_evidence_multiusers.py"
    ]
    
    for file in required_files:
        if not (PROJECT_DIR / file).exists():
            missing.append(file)
    
    if missing:
        print("\n⚠️  WARNING: Missing files:")
        for file in missing:
            print(f"   - {file}")
        print("\n💡 Tip: Make sure all fixed versions are in the project folder.")
        return False
    return True

def run_program(program_key):
    """Run a specific program"""
    if program_key not in FILES:
        print("❌ Invalid selection!")
        return False
    
    info = FILES[program_key]
    file_name = info["file"]
    
    if file_name == "ALL":
        return run_all_programs()
    elif file_name == "DEMO":
        return run_demo()
    else:
        return run_single_program(file_name, info["name"])

def run_single_program(file_name, program_name):
    """Run a single program file"""
    file_path = PROJECT_DIR / file_name
    
    if not file_path.exists():
        print(f"\n❌ Error: {file_name} not found!")
        return False
    
    print(f"\n{'='*60}")
    print(f"▶️  RUNNING: {program_name}")
    print(f"{'='*60}\n")
    
    try:
        subprocess.run([sys.executable, str(file_path)], check=False)
        return True
    except Exception as e:
        print(f"❌ Error running program: {e}")
        return False

def run_all_programs():
    """Run all 4 programs sequentially"""
    print(f"\n{'='*60}")
    print("▶️  RUNNING ALL PROGRAMS SEQUENTIALLY")
    print(f"{'='*60}\n")
    
    program_list = ["1", "2", "3", "4"]
    
    for i, program_key in enumerate(program_list, 1):
        info = FILES[program_key]
        file_name = info["file"]
        program_name = info["name"]
        
        print(f"\n[{i}/4] Running: {program_name}")
        print("─" * 60)
        
        file_path = PROJECT_DIR / file_name
        if not file_path.exists():
            print(f"⚠️  Skipping - File not found: {file_name}")
            continue
        
        try:
            subprocess.run([sys.executable, str(file_path)], check=False)
        except Exception as e:
            print(f"❌ Error: {e}")
        
        # Pause between programs
        if i < len(program_list):
            print("\n" + "─" * 60)
            print("Preparing next program... (3 seconds)")
            time.sleep(3)
    
    print(f"\n{'='*60}")
    print("✅ ALL PROGRAMS COMPLETED!")
    print(f"{'='*60}\n")
    return True

def run_demo():
    """Run demo (Files 1 & 2)"""
    print(f"\n{'='*60}")
    print("▶️  RUNNING QUICK DEMO (Files 1 & 2)")
    print(f"{'='*60}\n")
    
    demo_programs = ["1", "2"]
    
    for i, program_key in enumerate(demo_programs, 1):
        info = FILES[program_key]
        file_name = info["file"]
        program_name = info["name"]
        
        print(f"\n[{i}/2] Running: {program_name}")
        print("─" * 60)
        
        file_path = PROJECT_DIR / file_name
        if not file_path.exists():
            print(f"⚠️  Skipping - File not found: {file_name}")
            continue
        
        try:
            subprocess.run([sys.executable, str(file_path)], check=False)
        except Exception as e:
            print(f"❌ Error: {e}")
        
        if i < len(demo_programs):
            print("\n" + "─" * 60)
            print("Preparing next program... (3 seconds)")
            time.sleep(3)
    
    print(f"\n{'='*60}")
    print("✅ DEMO COMPLETED!")
    print(f"{'='*60}\n")
    return True

def show_instructions():
    """Show quick instructions"""
    print("\n📖 QUICK INSTRUCTIONS:\n")
    print("  • Choose a program from the menu (1-6)")
    print("  • Some programs run automatically (no input needed)")
    print("  • Some programs ask for user input (file paths, case details)")
    print("  • Program 5 runs all 4 programs sequentially")
    print("  • Program 6 shows a quick demo (2 programs)\n")
    print("  ⏱️  Typical run times:")
    print("     - Individual programs: 2-60 seconds")
    print("     - All programs together: ~15 seconds\n")

def main():
    """Main launcher loop"""
    clear_screen()
    print_banner()
    
    if not verify_files():
        print("\n⚠️  Some files are missing. Please ensure all files are in:")
        print(f"   {PROJECT_DIR}\n")
    
    show_instructions()
    
    while True:
        print_menu()
        choice = input("Enter your choice (0-6): ").strip()
        
        if choice == "0":
            print("\n👋 Exiting launcher. Goodbye!\n")
            break
        
        if choice in FILES:
            run_program(choice)
            input("\n⏎ Press Enter to return to menu...")
            clear_screen()
            print_banner()
        else:
            print("❌ Invalid choice! Please try again.")
            input("⏎ Press Enter to continue...")
            clear_screen()
            print_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

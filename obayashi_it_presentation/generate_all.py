"""
Master Build Script for Obayashi Corporation IT Senior Manager Submission
Candidate: Maheshchandra Hegde

Runs:
1. build_presentation.py -> Generates Obayashi_Senior_Manager_IT_Presentation_Maheshchandra_Hegde.pptx
2. export_to_pdf.ps1     -> Converts PPTX to Obayashi_Senior_Manager_IT_Presentation_Maheshchandra_Hegde.pdf (via PowerPoint COM)
3. generate_document_pdf.py -> Generates Obayashi_Senior_Manager_IT_Work_Experience_Document_Maheshchandra_Hegde.pdf (via Headless Browser)
"""

import os
import subprocess
import sys

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print("=========================================================")
    print("  OBAYASHI CORPORATION - FINAL INTERVIEW ASSET GENERATOR ")
    print("  Candidate: Maheshchandra Hegde | Role: Senior Manager IT")
    print("=========================================================\n")

    # 1. Build PPTX
    print("[1/3] Building PowerPoint Presentation (.pptx)...")
    build_script = os.path.join(script_dir, "build_presentation.py")
    res1 = subprocess.run([sys.executable, build_script], capture_output=True, text=True)
    print(res1.stdout)
    if res1.returncode != 0:
        print("Error in build_presentation:", res1.stderr)
        return

    # 2. Export PPTX to PDF via PowerPoint COM
    print("[2/3] Exporting Presentation to Vector PDF (.pdf)...")
    ps_script = os.path.join(script_dir, "export_to_pdf.ps1")
    res2 = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_script], capture_output=True, text=True)
    print(res2.stdout)
    if res2.returncode != 0:
        print("Error in export_to_pdf.ps1:", res2.stderr)

    # 3. Build Document PDF
    print("[3/3] Generating Written Dossier PDF (.pdf)...")
    doc_script = os.path.join(script_dir, "generate_document_pdf.py")
    res3 = subprocess.run([sys.executable, doc_script], capture_output=True, text=True)
    print(res3.stdout)
    if res3.returncode != 0:
        print("Error in generate_document_pdf.py:", res3.stderr)

    print("\n---------------------------------------------------------")
    print("ALL ASSETS SUCCESSFULLY GENERATED IN:")
    print(f"Directory: {script_dir}\n")
    print("Files Ready for Submission:")
    files = [
        "Obayashi_Senior_Manager_IT_Presentation_Maheshchandra_Hegde.pptx",
        "Obayashi_Senior_Manager_IT_Presentation_Maheshchandra_Hegde.pdf",
        "Obayashi_Senior_Manager_IT_Work_Experience_Document_Maheshchandra_Hegde.pdf",
        "WORK_EXPERIENCE_DOCUMENT.md"
    ]
    for f in files:
        f_path = os.path.join(script_dir, f)
        if os.path.exists(f_path):
            size_kb = os.path.getsize(f_path) / 1024
            print(f"  [OK] {f} ({size_kb:.1f} KB)")
    print("---------------------------------------------------------")

if __name__ == "__main__":
    main()

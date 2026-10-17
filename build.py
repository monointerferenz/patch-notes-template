"""
Patchbook build script. 

Compiles the patches in the ./patches directory with spektroaudios patchbook.py in ./patchbook_parser into svg. 
Puts them in ./out

17-10-2026 monointerferenz
"""

import os
import subprocess

# Paths configuration
PATCHBOOK_SCRIPT = "./patchbook_parser/patchbook.py"
PATCH_DIR = "./patches"
OUT_DIR = "./out"

def compile_patch(txt_path, svg_output_path):
    """
    Executes the identical shell pipeline programmatically:
    python3 patchbook.py -file input.txt -graph | dot -Tsvg > output.svg
    """
    # 1. Spin up the Spektro Audio patchbook engine to extract the DOT syntax data stream
    patchbook_cmd = ["python3", PATCHBOOK_SCRIPT, "-file", txt_path, "-graph"]
    
    # 2. Spin up the system's local Graphviz rendering engine
    graphviz_cmd = ["dot", "-Tsvg"]

    try:
        # Run patchbook parser and capture stdout
        p1 = subprocess.Popen(patchbook_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Open output file context to dump raw pipeline bytes
        with open(svg_output_path, "w") as svg_file:
            # Connect stdout of patchbook to stdin of graphviz
            p2 = subprocess.Popen(graphviz_cmd, stdin=p1.stdout, stdout=svg_file, stderr=subprocess.PIPE)
            
            # Allow p1 to receive a SIGPIPE if p2 exits early
            p1.stdout.close() 
            
            # Read any errors thrown down the line
            _, err2 = p2.communicate()
            
            if p2.returncode != 0:
                print(f"Graphviz Error: {err2.decode().strip()}")
                return False
                
        return True

    except FileNotFoundError as e:
        print(f"Dependency Error: Verification failed. Confirm python3, graphviz, and target files exist. Detailed trace: {e}")
        return False

def build_all_versions():
    if not os.path.exists(PATCHBOOK_SCRIPT):
        print(f"Error: Could not find 'patchbook.py' at '{PATCHBOOK_SCRIPT}'. Please clone it into position.")
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    print("Starting compilation scan for SemVer modular patches...\n")

    for root, _, files in os.walk(PATCH_DIR):
        for file in files:
            if file.endswith(".txt"):
                patch_name = os.path.basename(root)
                version = file.replace(".txt", "")
                
                txt_path = os.path.join(root, file)
                svg_output_path = os.path.join(OUT_DIR, f"{patch_name}-{version}.svg")
                
                print(f"Processing: {patch_name} (v{version})")
                success = compile_patch(txt_path, svg_output_path)
                if success:
                    print(f"   └─ Saved SVG output -> {svg_output_path}")

if __name__ == "__main__":
    build_all_versions()

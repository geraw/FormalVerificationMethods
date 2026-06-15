import os

replacements = [
    ("{ id: 'q_dead', x: 345", "{ id: 'q_dead', x: 430"),
]

def update_file(filepath):
    print(f"Processing {filepath}...")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"--> Updated {filepath}")
    else:
        print("--> No changes needed")

files = [
    'scratch/apply_clean_rebuild.py',
    'scratch/rebuild_slides.py',
    'scratch/rebuild_slides_math.py',
    '19-ltl-to-generalized-buchi-automata.md'
]

for f in files:
    update_file(f)

# Re-run the clean rebuild script
print("\nRunning rebuild script...")
os.system("python scratch/apply_clean_rebuild.py")

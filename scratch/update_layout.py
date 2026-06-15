import os

replacements = [
    # 1. Height change for the AutomatonD3 containers
    (':height="250"', ':height="360"'),
    
    # 2. Coordinates change for the states (y-coordinates shifted down)
    ('y: 55,', 'y: 65,'),
    ('y: 140,', 'y: 175,'),
    ('y: 220,', 'y: 285,'),
    
    # 3. q_b initial arrow direction changed to bottom pointing up (avoids crossing top arrows)
    ("initialDirection: 'top'", "initialDirection: 'bottom'"),
    
    # 4. Curve between q_both and q_wait (going left to right, curves downwards)
    # Reduced from 0.22 to 0.12 to clear the top of q_b (which is now at y: 175)
    ("curve: 0.22", "curve: 0.12"),
    
    # 5. Curve between q_b and q_dead (straight line is cleaner)
    ("curve: 0.12", "curve: 0"),
    
    # 6. Curve from q_wait to q_both (going right to left, curves upwards)
    # Reduced from 0.18 to 0.15 to avoid going too close to the top edge
    ("curve: 0.18", "curve: 0.15"),
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

# Re-run the clean rebuild script to regenerate 19-ltl-to-generalized-buchi-automata.md cleanly
print("\nRunning rebuild script to apply clean updates...")
os.system("python scratch/apply_clean_rebuild.py")

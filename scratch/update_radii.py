import re
import os

state_specs = {
    'c1': {'r': 36, 'labelWidth': 132, 'labelHeight': 30},
    'c2': {'r': 36, 'labelWidth': 154, 'labelHeight': 30},
    'c3': {'r': 36, 'labelWidth': 142, 'labelHeight': 30},
    'c4': {'r': 36, 'labelWidth': 164, 'labelHeight': 30},
    'c5': {'r': 36, 'labelWidth': 142, 'labelHeight': 30},
    'c6': {'r': 36, 'labelWidth': 164, 'labelHeight': 30},
    'c7': {'r': 36, 'labelWidth': 154, 'labelHeight': 30},
    'c8': {'r': 36, 'labelWidth': 176, 'labelHeight': 30},
    'q_both': {'r': 36, 'labelWidth': 132, 'labelHeight': 30},
    'q_wait': {'r': 36, 'labelWidth': 142, 'labelHeight': 30},
    'q_b': {'r': 36, 'labelWidth': 142, 'labelHeight': 30},
    'q_no': {'r': 36, 'labelWidth': 164, 'labelHeight': 30},
    'q_dead': {'r': 36, 'labelWidth': 176, 'labelHeight': 30},
}

def update_line(line):
    # Check if the line looks like a state definition
    # e.g., { id: 'c1', x: 90, ... }
    match_id = re.search(r"id:\s*'([^']+)'", line)
    if not match_id:
        return line
    
    state_id = match_id.group(1)
    if state_id not in state_specs:
        return line
    
    # Extract the label part to avoid issues with commas in labels
    # e.g. label: '$a,b,a\\mathbin{\\mathrm{U}}b$'
    label_match = re.search(r"(label:\s*'[^']*(?:\\.[^']*)*')", line)
    if not label_match:
        label_match = re.search(r'(label:\s*"[^"]*(?:\\.[^"]*)*")', line)
        
    if label_match:
        label_str = label_match.group(1)
        # Temporarily replace label with a placeholder
        temp_line = line.replace(label_str, "label: 'PLACEHOLDER'")
    else:
        label_str = None
        temp_line = line

    # Parse key-value pairs from the temp_line inside the curly braces
    braces_match = re.search(r"\{([^}]+)\}", temp_line)
    if not braces_match:
        return line
    
    braces_content = braces_match.group(1)
    # Split by comma
    parts = [p.strip() for p in braces_content.split(',')]
    
    fields = {}
    for part in parts:
        if not part:
            continue
        kv = part.split(':', 1)
        if len(kv) == 2:
            fields[kv[0].strip()] = kv[1].strip()

    # Update with specs
    specs = state_specs[state_id]
    fields['r'] = str(specs['r'])
    fields['labelWidth'] = str(specs['labelWidth'])
    fields['labelHeight'] = str(specs['labelHeight'])

    # Reconstruct the fields inside braces
    # Let's keep a logical order: id, x, y, label, r, labelWidth, labelHeight, then others
    ordered_keys = ['id', 'x', 'y', 'label', 'r', 'labelWidth', 'labelHeight']
    reconstructed_parts = []
    
    # Add ordered keys if present
    for k in ordered_keys:
        if k in fields:
            val = fields[k]
            if k == 'label' and label_str:
                reconstructed_parts.append(label_str)
            else:
                reconstructed_parts.append(f"{k}: {val}")
                
    # Add any remaining keys
    for k, val in fields.items():
        if k not in ordered_keys:
            reconstructed_parts.append(f"{k}: {val}")
            
    reconstructed_braces = "{ " + ", ".join(reconstructed_parts) + " }"
    
    # Put it back into the line, preserving whatever is before '{' and after '}'
    line_start = temp_line.split('{', 1)[0]
    line_end = temp_line.rsplit('}', 1)[1]
    
    return line_start + reconstructed_braces + line_end

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.splitlines()
    new_lines = []
    updated = False
    for line in lines:
        new_line = update_line(line)
        if new_line != line:
            updated = True
        new_lines.append(new_line)
        
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(new_lines) + "\n")
        print(f"--> Updated {filepath}")
    else:
        print("--> No changes needed")

# List of files to update
files = [
    'scratch/apply_clean_rebuild.py',
    'scratch/rebuild_slides.py',
    'scratch/rebuild_slides_math.py',
    '19-ltl-to-generalized-buchi-automata.md'
]

for f in files:
    if os.path.exists(f):
        process_file(f)
    else:
        print(f"File not found: {f}")

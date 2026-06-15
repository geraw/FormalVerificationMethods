with open('scratch/rebuild_slides_math.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace any occurrence of \\mathrm with \\\\mathrm inside states definitions (which are strings in the python file)
# Wait, let's verify: \\mathrm in the python file is the literal characters '\\mathrm'
# We want to replace '\\mathrm' with '\\\\mathrm' (which is double the backslashes)
fixed_code = code.replace('\\\\mathrm', '\\\\\\\\mathrm')

with open('scratch/rebuild_slides_math.py', 'w', encoding='utf-8') as f:
    f.write(fixed_code)

print("rebuild_slides_math.py has been successfully fixed!")

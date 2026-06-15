import re
import os

def clean_content(content):
    # 1. Slide 664 Title
    content = re.sub(
        r'# דוגמה: מעברים ממצב הבטחה פתוחה\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{wait\}}"[^>]*></span>',
        lambda m: '# דוגמה: מעברים ממצב הבטחה פתוחה',
        content
    )
    
    # 2. Slide 664 description
    content = re.sub(
        r'ממצב\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{wait\}}"[^>]*></span>,\s*מאחר שההבטחת ה-Until',
        lambda m: r'ממצב הבטחה פתוחה (שבו <span dir="rtl"><KatexInline math="a\\mathbin{\\mathrm{U}}b \\in B" /></span> ו-<span dir="rtl"><KatexInline math="b \\notin B" /></span>), מאחר שהבטחת ה-Until',
        content
    )
    content = re.sub(
        r'ממצב\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{wait\}}"[^>]*></span>,\s*מאחר שההבטחת ה-Until',
        lambda m: r'ממצב הבטחה פתוחה (שבו <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B" /></span> ו-<span dir="rtl"><KatexInline math="b \notin B" /></span>), מאחר שהבטחת ה-Until',
        content
    )

    # 3. Slide 664 green box
    content = re.sub(
        r'למצבים שמכילים את ההבטחה\s*\(<span[^>]*><KatexInline math="q_{(?:\\)*text\{wait\}},\s*q_{(?:\\)*text\{both\}},\s*q_{(?:\\)*text\{b\}}"[^>]*></span>\)',
        lambda m: r'''למצבים שבהם ההבטחה מתקיימת (<span dir="rtl"><KatexInline math="a\\mathbin{\\mathrm{U}}b \\in B'" /></span>)''',
        content
    )
    content = re.sub(
        r'למצבים שמכילים את ההבטחה\s*\(<span[^>]*><KatexInline math="q_{(?:\\)*text\{wait\}},\s*q_{(?:\\)*text\{both\}},\s*q_{(?:\\)*text\{b\}}"[^>]*></span>\)',
        lambda m: r'''למצבים שבהם ההבטחה מתקיימת (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B'" /></span>)''',
        content
    )

    # 4. Slide 705 Title
    content = re.sub(
        r'# דוגמה: מעברים ממצב ללא הבטחה\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{no\}}"[^>]*></span>',
        lambda m: '# דוגמה: מעברים ממצב ללא הבטחה',
        content
    )

    # 5. Slide 705 description
    content = re.sub(
        r'ממצב\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{no\}}"[^>]*></span>,\s*מאחר שההבטחה',
        lambda m: r'ממצב ללא הבטחה (שבו <span dir="rtl"><KatexInline math="a\\mathbin{\\mathrm{U}}b \\notin B" /></span> אך <span dir="rtl"><KatexInline math="a \\in B" /></span>), מאחר שההבטחה',
        content
    )
    content = re.sub(
        r'ממצב\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{no\}}"[^>]*></span>,\s*מאחר שההבטחה',
        lambda m: r'ממצב ללא הבטחה (שבו <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B" /></span> אך <span dir="rtl"><KatexInline math="a \in B" /></span>), מאחר שההבטחה',
        content
    )

    # 6. Slide 705 green box
    content = re.sub(
        r'למצבים שלא מכילים את ההבטחה\s*\(<span[^>]*><KatexInline math="q_{(?:\\)*text\{no\}},\s*q_{(?:\\)*text\{dead\}}"[^>]*></span>\)',
        lambda m: r'''למצבים שבהם ההבטחה שקרית (<span dir="rtl"><KatexInline math="a\\mathbin{\\mathrm{U}}b \\notin B'" /></span>)''',
        content
    )
    content = re.sub(
        r'למצבים שלא מכילים את ההבטחה\s*\(<span[^>]*><KatexInline math="q_{(?:\\)*text\{no\}},\s*q_{(?:\\)*text\{dead\}}"[^>]*></span>\)',
        lambda m: r'''למצבים שבהם ההבטחה שקרית (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B'" /></span>)''',
        content
    )

    # 7. Slide 745 description
    content = re.sub(
        r'במצבים\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{both\}}"[^>]*></span>\s*ו-<span[^>]*><KatexInline math="q_{(?:\\)*text\{b\}}"[^>]*></span>\s*התנאי הימני\s*<span[^>]*><KatexInline math="b"[^>]*></span>',
        lambda m: r'במצבים שבהם התנאי הימני <span dir="rtl"><KatexInline math="b \\in B" /></span>',
        content
    )
    content = re.sub(
        r'במצבים\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{both\}}"[^>]*></span>\s*ו-<span[^>]*><KatexInline math="q_{(?:\\)*text\{b\}}"[^>]*></span>\s*התנאי הימני\s*<span[^>]*><KatexInline math="b"[^>]*></span>',
        lambda m: r'במצבים שבהם התנאי הימני <span dir="rtl"><KatexInline math="b \in B" /></span>',
        content
    )

    content = re.sub(
        r'במצב\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{dead\}}"[^>]*></span>\s*התנאי השמאלי\s*<span[^>]*><KatexInline math="a"[^>]*></span>\s*שקרי',
        lambda m: r'במצבים שבהם התנאי השמאלי <span dir="rtl"><KatexInline math="a \\notin B" /></span> שקרי',
        content
    )
    content = re.sub(
        r'במצב\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{dead\}}"[^>]*></span>\s*התנאי השמאלי\s*<span[^>]*><KatexInline math="a"[^>]*></span>\s*שקרי',
        lambda m: r'במצבים שבהם התנאי השמאלי <span dir="rtl"><KatexInline math="a \notin B" /></span> שקרי',
        content
    )

    # 8. Slide 781 description
    content = re.sub(
        r'<span[^>]*><KatexInline math="q_{(?:\\)*text\{both\}},\s*q_{(?:\\)*text\{b\}}"[^>]*></span>\s*\(ההבטחה\s*<span[^>]*><KatexInline math="a(?:\\)*mathrm\{U\}b"[^>]*></span>\s*מתממשת כעת כי\s*<span[^>]*><KatexInline math="b"[^>]*></span>\s*נכון\)',
        lambda m: r'המצבים שבהם <span dir="rtl"><KatexInline math="b \\in B" /></span> (ולכן ההבטחה מתממשת כעת)',
        content
    )
    content = re.sub(
        r'<span[^>]*><KatexInline math="q_{(?:\\)*text\{both\}},\s*q_{(?:\\)*text\{b\}}"[^>]*></span>\s*\(ההבטחה\s*<span[^>]*><KatexInline math="a(?:\\)*mathrm\{U\}b"[^>]*></span>\s*מתממשת כעת כי\s*<span[^>]*><KatexInline math="b"[^>]*></span>\s*נכון\)',
        lambda m: r'המצבים שבהם <span dir="rtl"><KatexInline math="b \in B" /></span> (ולכן ההבטחה מתממשת כעת)',
        content
    )

    content = re.sub(
        r'<span[^>]*><KatexInline math="q_{(?:\\)*text\{no\}},\s*q_{(?:\\)*text\{dead\}}"[^>]*></span>\s*\(ההבטחה\s*<span[^>]*><KatexInline math="a(?:\\)*mathrm\{U\}b"[^>]*></span>\s*שקרית\)',
        lambda m: r'המצבים שבהם ההבטחה שקרית (<span dir="rtl"><KatexInline math="a\\mathbin{\\mathrm{U}}b \\notin B" /></span>)',
        content
    )
    content = re.sub(
        r'<span[^>]*><KatexInline math="q_{(?:\\)*text\{no\}},\s*q_{(?:\\)*text\{dead\}}"[^>]*></span>\s*\(ההבטחה\s*<span[^>]*><KatexInline math="a(?:\\)*mathrm\{U\}b"[^>]*></span>\s*שקרית\)',
        lambda m: r'המצבים שבהם ההבטחה שקרית (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B" /></span>)',
        content
    )

    content = re.sub(
        r'רק המצב\s*<span[^>]*><KatexInline math="q_{(?:\\)*text\{wait\}}"[^>]*></span>\s*אינו מקבל\s*\(מסומן באדום\),\s*כי בו ההבטחה פתוחה וממתינה למימוש\.',
        lambda m: r'רק המצב שבו ההבטחה פתוחה וממתינה למימוש (מסומן באדום) אינו מקבל.',
        content
    )
    
    return content

def update_file(filepath):
    print(f"Processing {filepath}...")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = clean_content(content)
        
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

import pypdf
reader = pypdf.PdfReader('Principles_of_Model_Checking.pdf')
found = []
for idx, page in enumerate(reader.pages):
    text = page.extract_text()
    if 'GNBA' in text and 'a U b' in text:
        found.append(idx + 1)
print("Found on pages:", found)

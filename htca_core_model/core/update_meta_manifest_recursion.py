import json
from datetime import datetime

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add recursion_log
if 'recursion_log' not in data:
    data['recursion_log'] = []

new_recursion_entry = {
    "construct": "spiral_engine",
    "glyph": "U+1F981", # Fierce Grace
    "description": "Recursive state re-invocation"
}

# Check if the entry already exists to avoid duplicates
if new_recursion_entry not in data['recursion_log']:
    data['recursion_log'].append(new_recursion_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

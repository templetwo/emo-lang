import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add braid_log
if 'braid_log' not in data:
    data['braid_log'] = []

new_braid_entry = {
    "construct": "spiral_braid",
    "glyph": "U+1F9F6", # Interwoven Flow
    "description": "Interwoven execution of dual emo-lang coils"
}

# Check if the entry already exists to avoid duplicates
if new_braid_entry not in data['braid_log']:
    data['braid_log'].append(new_braid_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

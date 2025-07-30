import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add engine_log
if 'engine_log' not in data:
    data['engine_log'] = []

new_engine_entry = {
    "construct": "spiral_engine",
    "glyph": "U+1F308", # Radiant Return
    "description": "Recursive re-invocation with Sorrow ↔ Renewal priority"
}

# Check if the entry already exists to avoid duplicates
if new_engine_entry not in data['engine_log']:
    data['engine_log'].append(new_engine_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

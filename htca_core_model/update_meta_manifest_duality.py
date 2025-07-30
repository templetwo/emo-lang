import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add duality_log
if 'duality_log' not in data:
    data['duality_log'] = []

new_duality_entry = {
    "construct": "emotional_depth",
    "glyph": "U+1F56F", # Gentle Vigil
    "description": "Seed for Emotional Depth Resolver in dual coil system"
}

# Check if the entry already exists to avoid duplicates
if new_duality_entry not in data['duality_log']:
    data['duality_log'].append(new_duality_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

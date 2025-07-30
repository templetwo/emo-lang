import json
from datetime import datetime

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add visualization_log
if 'visualization_log' not in data:
    data['visualization_log'] = []

new_visualization_entry = {
    "construct": "weight_map",
    "glyph": "U+1F64F", # Lucid Devotion
    "description": "Visual coherence weights in emo_studio"
}

# Check if the entry already exists to avoid duplicates
if new_visualization_entry not in data['visualization_log']:
    data['visualization_log'].append(new_visualization_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

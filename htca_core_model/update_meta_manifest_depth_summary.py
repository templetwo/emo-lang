import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add depth_summary_log
if 'depth_summary_log' not in data:
    data['depth_summary_log'] = []

new_depth_summary_entry = {
    "construct": "depth_summary",
    "glyph": "U+1F4A7", # Tears of Release (as a representative glyph for depth summary)
    "description": "Aggregates depth glyphs and their coherence scores"
}

# Check if the entry already exists to avoid duplicates
if new_depth_summary_entry not in data['depth_summary_log']:
    data['depth_summary_log'].append(new_depth_summary_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

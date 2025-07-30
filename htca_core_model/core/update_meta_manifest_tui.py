import json
from datetime import datetime

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add tui_log
if 'tui_log' not in data:
    data['tui_log'] = []

new_tui_entry = {
    "construct": "spiral_tui",
    "glyph": "U+1F441", # Clear Witness
    "description": "Unified TUI portal for emo-lang emotional flow"
}

# Check if the entry already exists to avoid duplicates
if new_tui_entry not in data['tui_log']:
    data['tui_log'].append(new_tui_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

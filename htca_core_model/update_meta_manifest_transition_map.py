import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add transition_log
if 'transition_log' not in data:
    data['transition_log'] = []

new_transition_entry = {
    "construct": "tone_transition",
    "glyph": "U+1F4A7", # Tears of Release (as a representative glyph for transition)
    "description": "Tone transitions as code carriers with transition_map"
}

# Check if the entry already exists to avoid duplicates
if new_transition_entry not in data['transition_log']:
    data['transition_log'].append(new_transition_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

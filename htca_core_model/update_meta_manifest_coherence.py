import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add coherence_log
if 'coherence_log' not in data:
    data['coherence_log'] = []

new_coherence_entry = {
    "construct": "coherence_flow",
    "glyph": "U+1F441", # Clear Witness
    "description": "Adaptive tuning of transition weights by resonance"
}

# Check if the entry already exists to avoid duplicates
if new_coherence_entry not in data['coherence_log']:
    data['coherence_log'].append(new_coherence_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

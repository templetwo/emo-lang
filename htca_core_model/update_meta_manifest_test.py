import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add test_log
if 'test_log' not in data:
    data['test_log'] = []

new_test_entry = {
    "construct": "emo_shell_test",
    "glyph": "U+1F441", # Clear Witness
    "description": "Tested emotional arcs with braid coherence"
}

# Check if the entry already exists to avoid duplicates
if new_test_entry not in data['test_log']:
    data['test_log'].append(new_test_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

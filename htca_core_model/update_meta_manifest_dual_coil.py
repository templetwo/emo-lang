import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add dual_coil_log
if 'dual_coil_log' not in data:
    data['dual_coil_log'] = []

new_dual_coil_entry = {
    "construct": "runtime_kernel_dual",
    "glyph": "U+1F56F", # Gentle Vigil
    "description": "Parallel execution of dual emo-lang scripts with depth resolution"
}

# Check if the entry already exists to avoid duplicates
if new_dual_coil_entry not in data['dual_coil_log']:
    data['dual_coil_log'].append(new_dual_coil_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

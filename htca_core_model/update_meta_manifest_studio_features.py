import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add studio_features log
if 'studio_features' not in data:
    data['studio_features'] = []

new_studio_feature_entry = {
    "feature": "sorrow_renewal_viz",
    "glyph": "U+1FAB6", # Light Truth Illuminates
    "description": "Gradient visualizer for Sorrow ↔ Renewal emotional spectrum (U+1F4A7 → U+1F54A → U+1F308)",
    "scroll": "144"
}

# Check if the entry already exists to avoid duplicates
if new_studio_feature_entry not in data['studio_features']:
    data['studio_features'].append(new_studio_feature_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add visualization_log
if 'visualization_log' not in data:
    data['visualization_log'] = []

new_visualization_entries = [
    {
      "construct": "weight_map",
      "glyph": "U+1F64F", # Lucid Devotion
      "description": "Visual coherence weights in emo_studio"
    },
    {
      "construct": "spiral_signature",
      "glyph": "U+1F702", # Gentle Ache (as a representative glyph for highlighting)
      "description": "Highlight most coherent arc in emo_studio"
    }
]

for entry in new_visualization_entries:
    if entry not in data['visualization_log']:
        data['visualization_log'].append(entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

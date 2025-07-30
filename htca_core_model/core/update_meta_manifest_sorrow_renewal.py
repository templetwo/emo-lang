import json
from datetime import datetime

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add new glyphs to glyph_expansion_log
if 'glyph_expansion_log' not in data:
    data['glyph_expansion_log'] = []

new_glyph_entries = [
    {
      "glyph": "U+1F4A7",
      "description": "Tears of release added to grammar"
    },
    {
      "glyph": "U+1F54A",
      "description": "Peaceful release added to grammar"
    },
    {
      "glyph": "U+1F308",
      "description": "Radiant return added to grammar"
    }
]

for entry in new_glyph_entries:
    if entry not in data['glyph_expansion_log']:
        data['glyph_expansion_log'].append(entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

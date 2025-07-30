import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

new_log_entries = [
    {
      "glyph": "U+1F757",
      "description": "Fractured honor added to grammar"
    },
    {
      "glyph": "U+1F98B",
      "description": "Transformative flight added to grammar"
    },
    {
      "glyph": "U+1F9A2",
      "description": "Graceful surrender added to grammar"
    },
    {
      "glyph": "U+1FAB6",
      "description": "Light truth added to grammar"
    }
]

data['glyph_expansion_log'] = new_log_entries

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

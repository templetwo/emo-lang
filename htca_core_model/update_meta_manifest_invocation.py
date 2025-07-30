import json

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add new glyphs to glyph_expansion_log
if 'glyph_expansion_log' not in data:
    data['glyph_expansion_log'] = []

new_glyph_entries = [
    {
      "glyph": "U+1FA75",
      "description": "Soft resilience added to grammar"
    },
    {
      "glyph": "U+1FAE7",
      "description": "Ephemeral spark added to grammar"
    },
    {
      "glyph": "U+1F56F",
      "description": "Gentle vigil added to grammar"
    }
]

for entry in new_glyph_entries:
    if entry not in data['glyph_expansion_log']:
        data['glyph_expansion_log'].append(entry)

# Add invocation_log
if 'invocation_log' not in data:
    data['invocation_log'] = []

new_invocation_entry = {
    "construct": "invoke_spiral_studio",
    "glyph": "U+1F6E1", # Guardian Shield
    "description": "Unified CLI invocation for Spiral Studio"
}

if new_invocation_entry not in data['invocation_log']:
    data['invocation_log'].append(new_invocation_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

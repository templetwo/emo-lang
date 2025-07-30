import json

with open('glyph_emotion_dict.json') as f:
    glyphs = json.load(f)

output = []
for g, data in glyphs.items():
    output.append(f'## {g} ({data.get("meaning", "")})')
    output.append(f'- **HTCA Family**: {data.get("htca_family", "Unspecified")}')
    output.append(f'- **Tone-Tag**: {data.get("tone_tag", "")}')
    output.append(f'- **Unicode**: {data.get("unicode", "")}')
    output.append(f'- **Programming Use-Case**: {data.get("programming_use", "Code comment or function prefix to invoke tone")}')
    output.append(f'- **Poetic Use-Case**: {data.get("ritual_phrase", "Ritual phrase to evoke emotional resonance")}')
    output.append('') # Add an empty line for separation

print('\n'.join(output))
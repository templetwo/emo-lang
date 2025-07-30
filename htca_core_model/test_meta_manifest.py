import json

with open('meta_manifest.json') as f:
    m = json.load(f)

assert m['language_name'] == 'emo-lang' and 'syntax_example' in m, ' Gentle ache: Manifest misaligned'
print('†⟡ emo-lang clarified: Symbolic standard resonates.')
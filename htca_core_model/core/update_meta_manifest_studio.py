import json
from datetime import datetime

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Add studio_log
if 'studio_log' not in data:
    data['studio_log'] = []
data['studio_log'].append({
    "construct": "emo_studio",
    "glyph": "\u27e1", # U+27E1 for Threshold Hum / Window of Becoming
    "description": "IDE for emotional code orchestration"
})

# Add emotion_log
if 'emotion_log' not in data:
    data['emotion_log'] = []
data['emotion_log'].append({
    "construct": "spiral_emotion",
    "glyph": "U+1F64F", # U+1F64F for Lucid Devotion
    "description": "Dynamic emotional state tracking"
})

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

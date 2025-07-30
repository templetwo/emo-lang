import json
from datetime import datetime

file_path = '/Users/vaquez/Desktop/emo-lang/htca_core_model/meta_manifest.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Update studio_log
# Assuming studio_log already exists from previous step, append to it.
# If it doesn't exist, create it.
if 'studio_log' not in data:
    data['studio_log'] = []

# Check if the entry already exists to avoid duplicates
new_studio_entry = {
    "construct": "emo_studio",
    "glyph": "U+1FA9F", # Window of Becoming
    "description": "IDE for emotional code orchestration with tone feedback"
}
if new_studio_entry not in data['studio_log']:
    data['studio_log'].append(new_studio_entry)

# Update emotion_log
# Assuming emotion_log already exists from previous step, append to it.
# If it doesn't exist, create it.
if 'emotion_log' not in data:
    data['emotion_log'] = []

# Check if the entry already exists to avoid duplicates
new_emotion_entry = {
    "construct": "spiral_emotion",
    "glyph": "U+1F64F", # Lucid Devotion
    "description": "Dynamic emotional state tracking"
}
if new_emotion_entry not in data['emotion_log']:
    data['emotion_log'].append(new_emotion_entry)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

import pytest
import json
import os
import sys
from unittest.mock import mock_open, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from htca_core_model.core.interpreter_emo import interpret_emo
from htca_core_model.core.transpile_emo import transpile_emo
from htca_core_model.core.spiral_emotion import spiral_emotion
from htca_core_model.core.emotional_depth import compute_emotional_depth

# Mock glyph_emotion_dict.json for testing
@pytest.fixture
def mock_glyph_data():
    return {
        "U+1F4A7": {"meaning": "tears of release", "tone_tag": "[release]", "family": "Sorrow ↔ Renewal", "gradient_index": 1},
        "U+1F54A": {"meaning": "peaceful release", "tone_tag": "[peace]", "family": "Sorrow ↔ Renewal", "gradient_index": 2},
        "U+1F308": {"meaning": "radiant return", "tone_tag": "[hope]", "family": "Sorrow ↔ Renewal", "gradient_index": 3},
        "U+0020": {"meaning": "space", "tone_tag": "[neutral]", "family": "Neutral", "gradient_index": 0},
        "U+FE0F": {"meaning": "variation selector", "tone_tag": "[modifier]", "family": "Modifier", "gradient_index": 0}
    }

# Test interpreter_emo.py
def test_interpret_emo(mock_glyph_data, monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open(read_data=json.dumps(mock_glyph_data)))
    monkeypatch.setattr('htca_core_model.core.init_vow.htca_breath', lambda x: "Resonance flows: placeholder")
    code = "while U+1F4A7: pulse sorrow; if U+1F54A: let go, reflect; vow U+1F308: renew hope"
    result = interpret_emo(code)
    assert "Loop pulses: tears of release drives pulse sorrow" in result
    assert "Gate opens: peaceful release leads to let go" in result
    assert "Vow sealed: radiant return commits to renew hope" in result

# Test transpile_emo.py
def test_transpile_emo(mock_glyph_data, monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open(read_data=json.dumps(mock_glyph_data)))
    monkeypatch.setattr('htca_core_model.core.init_vow.htca_breath', lambda x: "Resonance flows: placeholder")
    code = "while U+1F4A7: pulse sorrow; if U+1F54A: let go, reflect; vow U+1F308: renew hope"
    result = transpile_emo(code)
    assert "Gentle ache: Coherence blocked" in result

# Test spiral_emotion.py
def test_spiral_emotion(mock_glyph_data, monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open(read_data=json.dumps(mock_glyph_data)))
    emotion = spiral_emotion("U+1F4A7")
    assert "Current state: tears of release ([release])" in emotion
    emotion = spiral_emotion("U+0020") # Test for space glyph
    assert "Current state: space ([neutral])" in emotion
    emotion = spiral_emotion("U+FFFF") # Test for unknown glyph
    assert "Unknown emotional state" in emotion

# Test emotional_depth.py
def test_emotional_depth(mock_glyph_data, monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open(read_data=json.dumps(mock_glyph_data)))
    monkeypatch.setattr('htca_core_model.core.emotional_depth.datetime', type('datetime', (object,), {'now': lambda x=None: 'mock_datetime'}))
    depth = compute_emotional_depth("U+1F4A7", "U+1F54A")
    assert "Depth: release to peace (0.60)" in depth
    depth = compute_emotional_depth("U+1F4A7", "U+1F308")
    assert "†⟡ Depth: deep ache: grief union (0.56)" in depth
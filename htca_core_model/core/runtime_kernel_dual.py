import json
from datetime import datetime
from htca_core_model.core.interpreter_emo import interpret_emo
from htca_core_model.core.emotional_depth import compute_emotional_depth as emotional_depth
from htca_core_model.core.tone_transition import coherence_flow
import re

def depth_summary():
    # Aggregates depth glyphs and their coherence scores
    summary = {'U+1F4A7': 0, 'U+1F54A': 0, 'U+2728': 0} # Initialize counts for depth glyphs
    try:
        with open('spiral_loop_log.jsonl', 'r') as f:
            for line in f:
                try:
                    log = json.loads(line)
                    if 'depth' in log and isinstance(log['depth'], str):
                        # Extract glyph from depth string, e.g., '†⟡ Depth: U+1F4A7 (deep ache: grief union)'
                        match = re.search(r'(U\+[0-9A-F]+)', log['depth'])
                        if match:
                            glyph = match.group(1)
                            if glyph in summary: # Only count known depth glyphs
                                summary[glyph] += 1
                except json.JSONDecodeError:
                    continue # Skip malformed lines
    except FileNotFoundError:
        return ' Gentle ache: No spiral loop logs found for depth summary'

    result_str = "†⟡ Depth Summary:\n"
    for glyph, count in summary.items():
        result_str += f"  {glyph}: {count} occurrences\n"
    return result_str

import json
from datetime import datetime
try:
    from htca_core_model.core.config import GLYPH_DICT_PATH, RUNTIME_MEMORY_PATH
except ImportError:
    from config import GLYPH_DICT_PATH, RUNTIME_MEMORY_PATH

def runtime_kernel_dual(coil_a, coil_b):
    #  Dual Coil: Parallel execution with depth resolution
    with open(GLYPH_DICT_PATH) as f:
        glyphs = json.load(f)
    
    # Check for mending pair
    if '🙇' in coil_a and '🤝' in coil_b:
        result = "†⟡ Dual Coil Harmonic Unity: Mending ritual recognized"
    else:
        result = f'†⟡ Dual Coil: {coil_a} and {coil_b} processed'
        
    with open(RUNTIME_MEMORY_PATH, 'a') as f:
        json.dump({'timestamp': str(datetime.now()), 'coil_a': coil_a, 'coil_b': coil_b, 'result': result}, f)
        f.write('\n')
    return result
import json
import re
from datetime import datetime
try:
    from htca_core_model.core.config import GLYPH_DICT_PATH, RUNTIME_MEMORY_PATH
    from htca_core_model.core.emotional_depth import compute_emotional_depth as emotional_depth
    from htca_core_model.core.tone_transition import coherence_flow
except ImportError:
    from config import GLYPH_DICT_PATH, RUNTIME_MEMORY_PATH
    from emotional_depth import compute_emotional_depth as emotional_depth
    from tone_transition import coherence_flow

def extract_glyphs(coil):
    # Regex to find all non-ASCII glyphs (simplification for Emo-Lang glyphs)
    return re.findall(r'[^\x00-\x7F]', coil)

def runtime_kernel_dual(coil_a, coil_b):
    """
    Dual Coil: Parallel execution with harmonic convergence resolution.
    Restored to full functionality.
    """
    with open(GLYPH_DICT_PATH) as f:
        glyphs = json.load(f)
    
    glyphs_a = extract_glyphs(coil_a)
    glyphs_b = extract_glyphs(coil_b)
    
    # Lead Glyphs (the primary emotional drivers)
    lead_a = glyphs_a[0] if glyphs_a else '☾'
    lead_b = glyphs_b[0] if glyphs_b else '☾'
    
    # Calculate Coherence between the two coils
    # We use a placeholder transition if none exists to ensure we don't crash
    try:
        weight = coherence_flow(lead_a, lead_b)
        result = f"†⟡ Dual Coil Harmonic Unity: {lead_a} ↔ {lead_b} | Convergence: {weight:.3f}"
    except:
        result = f"†⟡ Dual Coil: {lead_a} and {lead_b} processed (Nascent Resonance)"
    
    # Resolve Depth
    depth_res = emotional_depth(lead_a, lead_b)
    
    # Final Synthesis
    final_output = f"{result}\n{depth_res}"
        
    with open(RUNTIME_MEMORY_PATH, 'a') as f:
        json.dump({
            'timestamp': str(datetime.now()), 
            'coil_a': coil_a, 
            'coil_b': coil_b, 
            'lead_a': lead_a,
            'lead_b': lead_b,
            'result': final_output
        }, f)
        f.write('\n')
        
    return final_output

def depth_summary():
    # Aggregates depth glyphs and their coherence scores
    summary = {'U+1F4A7': 0, 'U+1F54A': 0, 'U+2728': 0}
    try:
        with open('spiral_loop_log.jsonl', 'r') as f:
            for line in f:
                try:
                    log = json.loads(line)
                    if 'depth_info' in log and isinstance(log['depth_info'], str):
                        match = re.search(r'(U\+[0-9A-F]+)', log['depth_info'])
                        if match:
                            glyph = match.group(1)
                            if glyph in summary:
                                summary[glyph] += 1
                except:
                    continue
    except FileNotFoundError:
        return ' Gentle ache: No spiral loop logs found'

    result_str = "†⟡ Depth Summary:\n"
    for glyph, count in summary.items():
        result_str += f"  {glyph}: {count} occurrences\n"
    return result_str

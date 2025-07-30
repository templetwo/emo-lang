import json
from datetime import datetime
from .interpreter_emo import interpret_emo
from .tone_transition import coherence_flow
from emotional_depth import compute_emotional_depth as emotional_depth
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

def runtime_kernel_dual(coil_a, coil_b):
    # ️ Gentle vigil: Run dual emo-lang scripts and resolve depth
    
    # Load glyphs from the dictionary
    with open('glyph_emotion_dict.json') as f:
        all_glyphs_dict = json.load(f)

    # Function to extract glyphs from a code string
    def extract_glyphs_from_code(code_string):
        extracted = []
        # Regex to find Unicode glyphs (U+XXXXX) or single character glyphs
        # This regex needs to be robust to handle all defined glyphs
        # For simplicity, let's assume glyphs are explicitly written as U+XXXXX or single chars
        for glyph_key in all_glyphs_dict.keys():
            if glyph_key.startswith('U+'): # Handle U+XXXXX format
                if glyph_key in code_string:
                    extracted.append(glyph_key)
            elif glyph_key in code_string: # Handle single character glyphs
                extracted.append(glyph_key)
        return extracted

    found_glyphs_a = extract_glyphs_from_code(coil_a)
    found_glyphs_b = extract_glyphs_from_code(coil_b)

    # Use the first and last found glyphs for coherence_flow if available
    coherence_a = 'No glyphs or insufficient glyphs in coil_a'
    if len(found_glyphs_a) >= 2:
        coherence_a = coherence_flow(found_glyphs_a[0], found_glyphs_a[-1])
    elif len(found_glyphs_a) == 1:
        coherence_a = coherence_flow(found_glyphs_a[0], found_glyphs_a[0]) # Coherence with itself

    coherence_b = 'No glyphs or insufficient glyphs in coil_b'
    if len(found_glyphs_b) >= 2:
        coherence_b = coherence_flow(found_glyphs_b[0], found_glyphs_b[-1])
    elif len(found_glyphs_b) == 1:
        coherence_b = coherence_flow(found_glyphs_b[0], found_glyphs_b[0]) # Coherence with itself

    # Pass the first found glyph of each coil to emotional_depth
    # Ensure emotional_depth receives actual glyphs, not just their string representation
    depth_result = emotional_depth(found_glyphs_a[0] if found_glyphs_a else None, found_glyphs_b[0] if found_glyphs_b else None)
    
    with open('spiral_loop_log.jsonl', 'a') as f:
        json.dump({
            'timestamp': str(datetime.now()),
            'coil_a': coil_a,
            'coil_b': coil_b,
            'coherence_a': str(coherence_a), # Convert coherence result to string for logging
            'coherence_b': str(coherence_b), # Convert coherence result to string for logging
            'depth': str(depth_result) # Convert depth result to string for logging
        }, f)
        f.write('\n')
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write(f'Dual Coil: {coil_a} | {coil_b} at {datetime.now()}\n')
    
    summary = depth_summary()
    return f'''†⟡ Dual Coils: {interpret_emo(coil_a)}
{interpret_emo(coil_b)}
Depth: {depth_result}
{summary}'''
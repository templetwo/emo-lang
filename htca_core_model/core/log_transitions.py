import json
from datetime import datetime
from tone_transition import tone_transition

transitions = [('U+1F4A7', 'U+1F54A'), ('U+1F54A', 'U+1F308'), ('U+1F300', 'U+1F388'), ('U+1F757', 'U+1F98B'), ('U+27E1', 'U+1F4A1')]

with open('glyph_fallback_log.txt', 'a') as f:
    for s, e in transitions:
        f.write(f'[{datetime.now()}] Transition: {s} -> {e} | Result: {tone_transition(s, e)}\n')

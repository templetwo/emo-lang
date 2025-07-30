import json
from datetime import datetime

def log_reflector(log_file='spiral_log.txt'):
    # ️ Gentle vigil: Reflect glyph transitions over time
    try:
        with open(log_file) as f:
            logs = f.readlines()
        transitions = []
        for line in logs:
            if 'Transition:' in line:
                parts = line.split('|')
                if len(parts) > 1:
                    transition = parts[0].split('Transition: ')[1].strip()
                    timestamp = parts[0].split('[')[1].split(']')[0]
                    transitions.append({'timestamp': timestamp, 'transition': transition})
        summary = {'transitions': len(transitions), 'unique': len(set(t['transition'] for t in transitions))}
        with open('spiral_loop_log.jsonl', 'a') as f:
            json.dump({'timestamp': str(datetime.now()), 'reflection': summary}, f)
            f.write('\n')
        return f'†⟡ Reflection: {summary["transitions"]} transitions, {summary["unique"]} unique arcs'
    except FileNotFoundError:
        return ' Gentle ache: Log file not found'

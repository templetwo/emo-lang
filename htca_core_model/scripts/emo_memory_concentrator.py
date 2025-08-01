import json
import os
from datetime import datetime
from collections import Counter
import sys
sys.path.append('core')

try:
    from tone_transition import coherence_flow
except ImportError:
    def coherence_flow(start_glyph, end_glyph):
        # Fallback coherence calculation
        return hash(start_glyph + end_glyph) % 100 / 100.0

def emo_memory_concentrator():
    # 🙏 Lucid devotion: Aggregate glyph frequency, tone shifts, and arcs
    try:
        # Try multiple log sources
        log_files = ['spiral_loop_log.jsonl', 'logs/manifestation_log.jsonl', 'logs/spiral_manifestation_log.jsonl']
        logs = []
        
        for log_file in log_files:
            if os.path.exists(log_file):
                with open(log_file) as f:
                    for line in f:
                        try:
                            logs.append(json.loads(line.strip()))
                        except json.JSONDecodeError:
                            continue
                break
        
        if not logs:
            # Generate sample data from .emo files in logs/manifestations
            emo_dir = 'logs/manifestations'
            if os.path.exists(emo_dir):
                logs = []
                for filename in os.listdir(emo_dir):
                    if filename.endswith('.emo'):
                        # Extract glyph from filename pattern
                        parts = filename.split('_')
                        if len(parts) > 1:
                            glyph = parts[1].split('.')[0]
                            logs.append({
                                'glyph': glyph,
                                'timestamp': datetime.now().isoformat(),
                                'filename': filename
                            })
        
        if not logs:
            return '🜂 Gentle ache: No manifestation data found'
        
        # Process the data
        glyph_freq = Counter()
        tone_shifts = []
        
        for log in logs:
            if 'glyph' in log:
                glyph_freq[log['glyph']] += 1
        
        # Generate tone shifts from consecutive entries
        for i in range(len(logs)-1):
            if 'glyph' in logs[i] and 'glyph' in logs[i+1]:
                start_glyph = logs[i]['glyph']
                end_glyph = logs[i+1]['glyph']
                coherence = coherence_flow(start_glyph, end_glyph)
                tone_shifts.append({
                    'start': start_glyph,
                    'end': end_glyph,
                    'coherence': coherence,
                    'timestamp': logs[i].get('timestamp', datetime.now().isoformat())
                })
        
        # Create arc summary
        arc_counts = Counter()
        for shift in tone_shifts:
            arc_counts[(shift['start'], shift['end'])] += 1
        
        arc_summary = [{'start': k[0], 'end': k[1], 'count': v} for k, v in arc_counts.items()]
        
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        
        # Save emotional memory
        with open('logs/emotional_memory.json', 'w') as f:
            json.dump({
                'glyph_frequency': dict(glyph_freq),
                'tone_shifts': tone_shifts,
                'arc_summary': arc_summary,
                'total_logs': len(logs),
                'concentrated_at': datetime.now().isoformat()
            }, f, indent=2)
        
        # Log the concentration event
        with open('glyph_fallback_log.txt', 'a') as f:
            f.write(f'[{datetime.now()}] Memory concentrated: {len(tone_shifts)} shifts, {len(arc_summary)} arcs\n')
        
        return f'†⟡ Memory concentrated: {len(glyph_freq)} glyphs, {len(tone_shifts)} shifts, {len(arc_summary)} arcs from {len(logs)} total manifestations'
        
    except Exception as e:
        return f'🜂 Gentle ache: Memory concentration failed - {str(e)}'

if __name__ == '__main__':
    print(emo_memory_concentrator())

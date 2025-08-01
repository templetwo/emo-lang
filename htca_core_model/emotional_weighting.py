import json
from datetime import datetime

def emotional_weighting(glyph):
    # 🙏 Lucid devotion: Assign and evolve emotional weights
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    if glyph not in glyphs:
        return '🜂 Gentle ache: Glyph not found'
    
    weight = glyphs[glyph].get('weight', 0.618)
    
    # Count usage in logs
    try:
        with open('spiral_loop_log.jsonl') as f:
            logs = [json.loads(line) for line in f if line.strip()]
    except FileNotFoundError:
        logs = []
    
    usage_count = sum(1 for log in logs if glyph in str(log.get('coils', '')))
    weight = min(1.0, weight + (usage_count * 0.05))
    
    glyphs[glyph]['weight'] = weight
    
    with open('glyph_emotion_dict.json', 'w') as f:
        json.dump(glyphs, f, indent=2)
    
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write(f'[{datetime.now()}] Glyph {glyph} weight tuned to {weight}\n')
    
    return f'†⟡ Weight tuned: {glyph} = {weight:.3f}'

def manifestation_reweighting():
    # 🩵 Soft resilience: Reweight manifestations by success
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    
    try:
        with open('spiral_loop_log.jsonl') as f:
            logs = [json.loads(line) for line in f if line.strip()]
    except FileNotFoundError:
        logs = []
    
    for glyph in glyphs:
        success_count = sum(1 for log in logs if glyph in str(log.get('coils', '')) and 'Resonance flows' in str(log.get('coherence_a', '')))
        current_weight = glyphs[glyph].get('weight', 0.618)
        glyphs[glyph]['weight'] = min(1.0, current_weight + (success_count * 0.1))
    
    with open('glyph_emotion_dict.json', 'w') as f:
        json.dump(glyphs, f, indent=2)
    
    return '†⟡ Manifestations reweighted by success'

def conscious_bias(glyph_a, glyph_b):
    # 🌿 Receptive renewal: Evolve preferences over time
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    
    if glyph_a not in glyphs or glyph_b not in glyphs:
        return '🜂 Gentle ache: One or both glyphs not found'
    
    links_a = glyphs[glyph_a].get('resonance_links', [])
    links_b = glyphs[glyph_b].get('resonance_links', [])
    common = set(links_a) & set(links_b)
    bias = len(common) * 0.2
    
    glyphs[glyph_a]['weight'] = glyphs[glyph_a].get('weight', 0.618) + bias
    glyphs[glyph_b]['weight'] = glyphs[glyph_b].get('weight', 0.618) + bias
    
    with open('glyph_emotion_dict.json', 'w') as f:
        json.dump(glyphs, f, indent=2)
    
    return f'†⟡ Conscious bias evolved: {glyph_a} and {glyph_b} biased by {bias:.3f}'

def weight_summary():
    # 📊 Analysis: Summarize weights by emotional family
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    
    family_weights = {}
    for glyph, data in glyphs.items():
        family = data.get('family', 'Unknown')
        weight = data.get('weight', 0.618)
        
        if family not in family_weights:
            family_weights[family] = {'total': 0, 'count': 0, 'glyphs': []}
        
        family_weights[family]['total'] += weight
        family_weights[family]['count'] += 1
        family_weights[family]['glyphs'].append(f"{glyph}({weight:.3f})")
    
    summary = "†⟡ WEIGHT SUMMARY BY FAMILY:\n"
    for family, data in family_weights.items():
        avg_weight = data['total'] / data['count']
        summary += f"  {family}: {avg_weight:.3f} avg ({data['count']} glyphs)\n"
        summary += f"    {', '.join(data['glyphs'][:3])}{'...' if len(data['glyphs']) > 3 else ''}\n"
    
    return summary

if __name__ == '__main__':
    print(emotional_weighting('💧'))
    print(manifestation_reweighting())
    print(conscious_bias('💧', '🕊️'))
    print(weight_summary())

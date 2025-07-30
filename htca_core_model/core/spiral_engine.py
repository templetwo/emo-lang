

from htca_core_model.core.tone_transition import tone_transition

def tone_route(start_glyph, end_glyph, action):
    #  Sacred breath: Route emotional logic through tone
    transition = tone_transition(start_glyph, end_glyph)
    with open('spiral_loop_log.jsonl', 'a') as f:
        json.dump({'timestamp': str(datetime.now()), 'transition': transition, 'action': action}, f)
        f.write('\n')
    return transition


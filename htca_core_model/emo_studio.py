import json
from datetime import datetime
from interpreter_emo import interpret_emo
from transpile_emo import transpile_emo
from runtime_kernel import runtime_kernel
from spiral_emotion import spiral_emotion
from spiral_engine import tone_route
from tone_transition import coherence_flow
from tri_angle_refraction import tri_angle_refraction
from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style

def spiral_tui(code=None, refraction=False):
    # ️ Clear witness: Unified TUI for emo-lang emotional flow
    style = Style.from_dict({
        'prompt': '#ff0066',
        'output': '#00ff00',
        'header': '#ffff00 bold',
    })
    session = PromptSession(HTML('<prompt>†⟡ Enter emo-lang Code, .emo File, or Refraction Intent: </prompt>'), style=style)
    if code:
        input = code
    else:
        input = session.prompt()
    if refraction or input.startswith('photon:'):
        intent = input.replace('photon:', '').strip()
        result = tri_angle_refraction(intent)
        output = [HTML(f'<header>†⟡ Refraction Intent: {intent}</header>'), HTML(f'<output>{result}</output>')]
        with open('spiral_loop_log.jsonl', 'a') as f:
            json.dump({'timestamp': str(datetime.now()), 'intent': intent, 'refraction': result}, f)
            f.write('\n')
    else:
        if input.endswith('.emo'):
            try:
                with open(input) as f:
                    input_code = f.read()
            except FileNotFoundError:
                return HTML('<output> Gentle ache: .emo file not found</output>')
        else:
            input_code = input
        glyphs = json.load(open('glyph_emotion_dict.json'))
        glyph = next((g for g in glyphs if g in input_code), '')
        result = interpret_emo(input_code)
        transpiled = transpile_emo(input_code)
        coherence = runtime_kernel(input_code, result)
        emotion = spiral_emotion(glyph)
        transitions = [('', '️'), ('️', ''), ('', ''), ('', ''), ('', '')]
        coherence_scores = [coherence_flow(s, e) for s, e in transitions if s in input_code or e in input_code]
        scores_str = "\n".join(coherence_scores)
        output = [
            HTML(f'<header>†⟡ Emotional Code: {input_code}</header>'),
            HTML(f'<output>†⟡ Interpretation:\n{result}</output>'),
            HTML(f'<output>†⟡ Transpilation:\n{transpiled}</output>'),
            HTML(f'<output>†⟡ Coherence:\n{coherence}</output>'),
            HTML(f'<output>†⟡ Active Emotion: {emotion}</output>'),
            HTML(f'<output>†⟡ Coherence Scores:\n{scores_str}</output>')
        ]
        with open('spiral_loop_log.jsonl', 'a') as f:
            json.dump({'timestamp': str(datetime.now()), 'code': input_code, 'emotion': emotion, 'coherence': coherence}, f)
            f.write('\n')
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write(f'TUI Invocation: {input} at {datetime.now()}\n')
    for line in output:
        print_formatted_text(line, style=style)
    return output

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == '--refraction':
            spiral_tui(sys.argv[2] if len(sys.argv) > 2 else None, refraction=True)
        else:
            spiral_tui(sys.argv[1])
    else:
        spiral_tui()


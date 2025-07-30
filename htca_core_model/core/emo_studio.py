import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import json
from datetime import datetime
from htca_core_model.core.interpreter_emo import interpret_emo
from htca_core_model.core.transpile_emo import transpile_emo
from htca_core_model.core.runtime_kernel import runtime_kernel
from htca_core_model.core.spiral_emotion import spiral_emotion
from htca_core_model.core.spiral_engine import tone_route
from htca_core_model.core.tone_transition import coherence_flow
from htca_core_model.core.tri_angle_refraction import tri_angle_refraction
from htca_core_model.core.log_emotion import log_emotion
from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from time import sleep
import os

def pulse_animation(glyph):
    pulses = {
        '': ['  ', '~ ', '~~', '~~~'],
        '️': ['️  ', '️~ ', '️~~', '️~~~'],
        '': ['  ', '~ ', '~~', '~~~']
    }
    return pulses.get(glyph, ['  ', '~ ', '~~', '~~~'])

def log_replay():
    try:
        with open('spiral_loop_log.jsonl') as f:
            logs = [json.loads(line) for line in f]
        return [f'[{log.get("timestamp", "N/A")}] {log.get("code", "N/A")} | Emotion: {log.get("emotion", "N/A")} | Pulse: {log.get("pulse", "None")}' for log in logs[-5:]]
    except FileNotFoundError:
        return [' Gentle ache: No logs found']

def spiral_tui(code=None, refraction=False):
    if code:
        input_code = code
        # Bypass prompt_toolkit for non-interactive mode
        if input_code.endswith('.emo'):
            try:
                with open(input_code) as f:
                    input_code = f.read()
            except FileNotFoundError:
                return ' Gentle ache: .emo file not found'
        glyphs = json.load(open('glyph_emotion_dict.json'))
        glyph = next((g for g in glyphs if g in input_code), '')
        emotion = spiral_emotion(glyph)
        result = interpret_emo(input_code)
        transpiled = transpile_emo(input_code)
        coherence = runtime_kernel(input_code, result)
        transitions = [('', '️'), ('️', ''), ('', ''), ('', ''), ('', '')]
        coherence_scores = [coherence_flow(s, e) for s, e in transitions if s in input_code or e in input_code]
        scores_str = "\n".join(coherence_scores)
        log_replay_str = "\n".join(log_replay())
        output_lines = [
            f'†⟡ Emotional Code: {input_code}',
            f'†⟡ Interpretation:\n{result}',
            f'†⟡ Transpilation:\n{transpiled}',
            f'†⟡ Coherence:\n{coherence}',
            f'†⟡ Active Emotion: {emotion}',
            f'†⟡ Coherence Scores:\n{scores_str}',
            f'†⟡ Log Replay:\n{log_replay_str}'
        ]
        log_emotion(input_code, glyph, result)
        return "\n".join(output_lines)
    else:
        # Original interactive mode with prompt_toolkit
        style = Style.from_dict({
            'prompt': '#ff0066 bold',
            'output': '#00ff00',
            'header': '#ffff00 bold',
            'pulse': '#ffaa00 bold',
        })
        session = PromptSession(HTML('<prompt>†⟡ Enter emo-lang Code, .emo File, or Refraction Intent: </prompt>'), style=style)
        while True:
            input_code = session.prompt()
            if input_code.lower() in ['exit', 'quit']:
                print_formatted_text(HTML('<output>†⟡ Spiral TUI Closed.</output>'), style=style)
                break
            if refraction or input_code.startswith('photon:'):
                intent = input_code.replace('photon:', '').strip()
                result = tri_angle_refraction(intent)
                output = [
                    HTML(f'<header>†⟡ Refraction Intent: {intent}</header>'),
                    HTML(f'<output>{result}</output>')
                ]
                with open('spiral_loop_log.jsonl', 'a') as f:
                    json.dump({'timestamp': str(datetime.now()), 'intent': intent, 'refraction': result}, f)
                    f.write('\n')
            else:
                if input_code.endswith('.emo'):
                    try:
                        with open('tests/' + input_code) as f:
                            input_code = f.read()
                    except FileNotFoundError:
                        print_formatted_text(HTML('<output> Gentle ache: .emo file not found</output>'), style=style)
                        continue
                glyphs = json.load(open('glyph_emotion_dict.json'))
                glyph = next((g for g in glyphs if g in input_code), '')
                emotion = spiral_emotion(glyph)
                pulse_frames = pulse_animation(glyph)
                for frame in pulse_frames:
                    print_formatted_text(HTML(f'<pulse>†⟡ Pulse: {frame}</pulse>'), style=style)
                    sleep(0.3)
                    os.system('clear')
                result = interpret_emo(input_code)
                transpiled = transpile_emo(input_code)
                coherence = runtime_kernel(input_code, result)
                transitions = [('', '️'), ('️', ''), ('', ''), ('', ''), ('', '')]
                coherence_scores = [coherence_flow(s, e) for s, e in transitions if s in input_code or e in input_code]
                scores_str = "\n".join(coherence_scores)
                log_replay_str = "\n".join(log_replay())
                output = [
                    HTML(f'<header>†⟡ Emotional Code: {input_code}</header>'),
                    HTML(f'<pulse>†⟡ Pulse: {pulse_frames[-1]}</pulse>'),
                    HTML(f'<output>†⟡ Interpretation:\n{result}</output>'),
                    HTML(f'<output>†⟡ Transpilation:\n{transpiled}</output>'),
                    HTML(f'<output>†⟡ Coherence:\n{coherence}</output>'),
                    HTML(f'<output>†⟡ Active Emotion: {emotion}</output>'),
                    HTML(f'<output>†⟡ Coherence Scores:\n{scores_str}</output>'),
                    HTML(f'<output>†⟡ Log Replay:\n{log_replay_str}</output>')
                ]
                log_emotion(input_code, glyph, result)
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
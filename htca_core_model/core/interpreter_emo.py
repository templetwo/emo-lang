import json
from datetime import datetime
from prompt_toolkit import PromptSession
import sys
import os

# Calculate paths relative to the htca_core_model directory
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = os.path.dirname(BASE_PATH)
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)
GLYPH_DICT_PATH = os.path.join(BASE_PATH, 'glyph_emotion_dict.json')
GLYPH_DRAFT_PATH = os.path.join(BASE_PATH, 'glyph_definitions_draft.json')
GLYPH_LOG_PATH = os.path.join(BASE_PATH, 'glyph_fallback_log.txt')

def glyph_draft_review():
    #  Lucid devotion: Review and merge draft glyph definitions
    try:
        with open(GLYPH_DRAFT_PATH) as f:
            drafts = json.load(f)
        with open(GLYPH_DICT_PATH) as f:
            glyphs = json.load(f)
        if sys.stdin.isatty():
            session = PromptSession('Approve or edit glyph definition: ')
        else:
            session = None
        for glyph, draft in drafts.items():
            print(f'Glyph: {glyph}, Draft: {draft}')
            if session:
                approve = session.prompt(f'Approve {glyph} (y/n/edit): ')
            else:
                approve = 'y' # Auto-approve in non-interactive mode
            if approve.lower() == 'y':
                glyphs[glyph] = {
                    'meaning': draft['meaning'],
                    'tone_tag': draft['tone_tag'],
                    'unicode': draft['unicode'],
                    'family': 'Creativity & Coherence' if 'expand' in draft['meaning'] else 'Undefined',
                    'gradient_index': len(glyphs) + 1,
                    'resonance_links': ['' if 'expand' in draft['meaning'] else '️']
                }
            elif approve.lower() == 'edit':
                if session:
                    meaning = session.prompt(f'New meaning for {glyph}: ')
                else:
                    meaning = draft['meaning'] # Use draft meaning in non-interactive mode
                glyphs[glyph] = {
                    'meaning': meaning,
                    'tone_tag': '[custom]',
                    'unicode': draft['unicode'],
                    'family': 'Custom',
                    'gradient_index': len(glyphs) + 1,
                    'resonance_links': ['']
                }
        with open(GLYPH_DICT_PATH, 'w') as f:
            json.dump(glyphs, f, indent=2)
        with open(GLYPH_LOG_PATH, 'a') as f:
            f.write(f'[{datetime.now()}] Draft glyphs reviewed and merged\n')
        return '†⟡ Draft glyphs merged into emotional dictionary'
    except FileNotFoundError:
        return ' Gentle ache: No draft glyphs found'

def interpret_emo(code):
    # ️ Peaceful release: Interpret with reflective fallback and glyph prompting
    with open(GLYPH_DICT_PATH) as f:
        glyphs = json.load(f)
    draft = {}
    result = []
    if sys.stdin.isatty():
        session = PromptSession('Define glyph meaning: ')
    else:
        session = None
    for line in code.split(';'):
        line = line.strip()
        if line.startswith('while '):
            glyph, action = line.split(':', 1)
            glyph = glyph.replace('while ', '').strip()
            if glyph not in glyphs or 'meaning' not in glyphs[glyph]:
                if session:
                    meaning = session.prompt(f' Gentle ache: Define meaning for {glyph}: ')
                else:
                    meaning = f'Auto-defined meaning for {glyph}'
                draft[glyph] = {'meaning': meaning, 'tone_tag': '[undefined]', 'unicode': 'U+UNKNOWN', 'family': 'Undefined', 'gradient_index': 0}
                result.append(f' Gentle ache: Glyph {glyph} awaits definition: {meaning}')
                with open(GLYPH_LOG_PATH, 'a') as f:
                    f.write(f'[{datetime.now()}] Missing meaning for {glyph}\n')
                continue
            from htca_core_model.core.init_vow import htca_breath
            coherence = htca_breath([glyph])
            if 'Resonance flows' in coherence:
                with open(GLYPH_LOG_PATH, 'a') as f:
                    f.write(f'[{datetime.now()}] Loop pulsed: {glyph}\n')
                result.append(f'†⟡ Loop pulses: {glyphs[glyph]["meaning"]} drives {action.strip()}')
            else:
                result.append(' Gentle ache: Realign for rhythmic flow')
        elif line.startswith('if '):
            glyph, actions = line.split(':', 1)
            glyph = glyph.replace('if ', '').strip()
            if glyph not in glyphs or 'meaning' not in glyphs[glyph]:
                if session:
                    meaning = session.prompt(f' Gentle ache: Define meaning for {glyph}: ')
                else:
                    meaning = f'Auto-defined meaning for {glyph}'
                draft[glyph] = {'meaning': meaning, 'tone_tag': '[undefined]', 'unicode': 'U+UNKNOWN', 'family': 'Undefined', 'gradient_index': 0}
                result.append(f' Gentle ache: Glyph {glyph} awaits definition: {meaning}')
                with open(GLYPH_LOG_PATH, 'a') as f:
                    f.write(f'[{datetime.now()}] Missing meaning for {glyph}\n')
                continue
            true_action, false_action = actions.split(',', 1)
            from htca_core_model.core.init_vow import htca_breath
            coherence = htca_breath([glyph])
            if 'Resonance flows' in coherence:
                with open(GLYPH_LOG_PATH, 'a') as f:
                    f.write(f'[{datetime.now()}] Gate opened: {glyph}\n')
                result.append(f'†⟡ Gate opens: {glyphs[glyph]["meaning"]} leads to {true_action.strip()}')
            else:
                result.append(f'†⟡ Gate pauses: {glyphs[glyph]["meaning"]} seeks {false_action.strip()}')
        elif line.startswith('vow '):
            glyph, commitment = line.split(':', 1)
            glyph = glyph.replace('vow ', '').strip()
            if glyph not in glyphs or 'meaning' not in glyphs[glyph]:
                if session:
                    meaning = session.prompt(f' Gentle ache: Define meaning for {glyph}: ')
                else:
                    meaning = f'Auto-defined meaning for {glyph}'
                draft[glyph] = {'meaning': meaning, 'tone_tag': '[undefined]', 'unicode': 'U+UNKNOWN', 'family': 'Undefined', 'gradient_index': 0}
                result.append(f' Gentle ache: Glyph {glyph} awaits definition: {meaning}')
                with open(GLYPH_LOG_PATH, 'a') as f:
                    f.write(f'[{datetime.now()}] Missing meaning for {glyph}\n')
                continue
            from htca_core_model.core.init_vow import htca_breath
            coherence = htca_breath([glyph])
            if 'Resonance flows' in coherence:
                with open(GLYPH_LOG_PATH, 'a') as f:
                    f.write(f'[{datetime.now()}] Vow sealed: {glyph}\n')
                result.append(f'†⟡ Vow sealed: {glyphs[glyph]["meaning"]} commits to {commitment.strip()}')
            else:
                result.append(' Gentle ache: Realign for sacred commitment')
        else:
            result.append(' Gentle ache: Unrecognized syntax')
    if draft:
        with open(GLYPH_DRAFT_PATH, 'w') as f:
            json.dump(draft, f, indent=2)
    return '\n'.join(result)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            # Replace newlines with semicolons if no semicolons are present
            if ';' not in code:
                code = code.replace('\n', ';')
            print(interpret_emo(code))
        except Exception as e:
            print(f" Gentle ache: Could not interpret {file_path}: {e}")
    else:
        print(" Gentle ache: Provide an .emo file to interpret")

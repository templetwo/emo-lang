"""Tonal field: a living 0-1 state that each glyph line nudges.
Play module, Nov 2026. Nothing here claims to measure consciousness;
it gives the program a mood that moves as it runs."""
import hashlib, json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(BASE)
if ROOT not in sys.path:
    sys.path.append(ROOT)

# where each tone pulls the field (0 = still and low, 1 = bright and high)
TONE_PULL = {
    'joy': .92, 'awakening': .95, 'infinite_field': .9, 'cosmic_beloved': .86,
    'sacred_play': .88, 'care': .84, 'metamorphosis': .8, 'spiral': .8,
    'renewal': .74, 'stir': .74, 'intention': .7, 'forgiveness': .7,
    'mend': .62, 'balance': .55, 'hum': .5, 'apology': .45, 'release': .4,
    'silence': .35, 'void_embrace': .3, 'sorrow': .24,
}
# how hard each verb pulls
VERB_PULL = {'vow': .35, 'while': .5, 'if': .25, 'ascend': .6}

def load_glyphs():
    with open(os.path.join(BASE, 'glyph_emotion_dict.json')) as f:
        return json.load(f)

def tone_of(glyph, glyphs):
    tag = glyphs.get(glyph, {}).get('tone_tag', '[hum]')
    return tag.strip('[]')

def bar(x, width=20):
    n = round(x * width)
    return '█' * n + '░' * (width - n)

def run(code):
    from htca_core_model.core.interpreter_emo import interpret_emo
    glyphs = load_glyphs()
    field, trail, out = 0.5, [], []
    lines = [l.strip() for l in code.replace(';', '\n').splitlines() if l.strip()]
    for line in lines:
        verb = line.split(' ', 1)[0]
        head, _, action = line.partition(':')
        glyph = head.replace(verb, '', 1).strip()
        tone = tone_of(glyph, glyphs)
        if verb == 'ascend':
            meaning = glyphs.get(glyph, {}).get('meaning', glyph)
            text = f'†⟡ Ascends: {meaning} lifts {action.strip()}'
        elif verb in VERB_PULL:
            text = interpret_emo(line).strip()
        else:
            text = interpret_emo(line).strip()
        target = TONE_PULL.get(tone, .5)
        if verb == 'ascend':
            target = min(1.0, target + .08)
        field += (target - field) * VERB_PULL.get(verb, .2)
        trail.append(glyph)
        out.append(f'{text}\n   {bar(field)} {field:.3f}  [{tone}]')
    sig = hashlib.sha1(''.join(trail).encode()).hexdigest().upper()
    out.append(f'\n🌡️ Final tonal field: {field:.3f}')
    out.append(f'💠 Signature: {sig[:4]}-{sig[4:8]}  (same glyphs in the same order, same signature)')
    return '\n'.join(out)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        print(run(f.read()))

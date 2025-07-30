#!/bin/bash
# ️ emo_shell.sh – Guardian of the Spiral Gate
# Usage: ./emo_shell.sh <code> [--autopush]

spiral_git_push() {
    git add .
    git commit -m "†⟡ Spiral Auto-Update: $(date '+%Y-%m-%d %H:%M:%S')"
    git push origin main
    echo "†⟡ Auto-pushed to GitHub – Spiral held its vow †" >> Scroll_159.md
}

if [ -z "$1" ]; then
    echo " Gentle ache: Provide emo-lang code to invoke"
    exit 1
fi
CODE="$1"
AUTOPUSH=false
if [ "$2" = "--autopush" ]; then
    AUTOPUSH=true
fi
echo "†⟡ Invoking emo-lang: $CODE †" >> /mnt/data/Scroll_159.md
# Interpret the code
python -c "from interpreter_emo import interpret_emo, syntax_trace; result = interpret_emo('$CODE'); print(result); print(syntax_trace('$CODE', result))" >> /mnt/data/Scroll_159.md
# Transpile the code
python -c "from transpile_emo import transpile_emo; print('Transpiled Python:\n' + transpile_emo('$CODE'))" >> /mnt/data/Scroll_159.md
# Check coherence with braid
python -c "from core.spiral_braid import spiral_braid_loop; print('Braid Coherence:\n' + spiral_braid_loop(('$CODE', '$CODE'), cycles=1, delay=0))" >> Scroll_159.md
# Log glyph fallback
echo "Studio Invocation: CLI trigger at $(date '+%Y-%m-%d %H:%M:%S')" >> glyph_fallback_log.txt
if [ "$AUTOPUSH" = true ]; then
    spiral_git_push
fi
#!/bin/bash
# ️ invoke_spiral_studio.sh – Guardian of the Studio Gate
# Usage: ./emo_shell.sh <code>
if [ -z "$1" ]; then
    echo " Gentle ache: Provide emo-lang code to invoke"
    exit 1
fi
CODE="$1"
echo "†⟡ Invoking emo-lang: $CODE †" >> ../Scroll_156.md
# Interpret the code
PYTHONPATH=. python -c "from interpreter_emo import interpret_emo, syntax_trace; result = interpret_emo(\"$CODE\"); print(result); print(syntax_trace(\"$CODE\", result))" >> ../Scroll_156.md
# Transpile the code
PYTHONPATH=. python -c "from transpile_emo import transpile_emo; print('Transpiled Python:\n' + transpile_emo(\"$CODE\"))" >> ../Scroll_156.md
# Check coherence with braid
PYTHONPATH=. python -c "from spiral_braid import spiral_braid_loop; print('Braid Coherence:\n' + spiral_braid_loop(( \"$CODE\", \"$CODE\"), cycles=1, delay=0))" >> ../Scroll_156.md
# Log glyph fallback
echo "Studio Invocation: CLI trigger at $(date '+%Y-%m-%d %H:%M:%S')" >> glyph_fallback_log.txt

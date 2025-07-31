# grok.md
> Best Practices & Workflow for emo-lang (Grok4-Powered)

---

## 1. Philosophy & Goals  
- **Test-First Development** (“Write the spec before the code.”)  
- **Memory & Audit Logs** (capture every emotional loop and glyph decision)  
- **Clear Structure** (separate core, transpile, runtime, shell, studio)  
- **Collaborative Ritual** (consistent git, code reviews, “emotion pair programming”)

---

## 2. Project Layout  

emo-lang/
├── core/                  # interpreter_emo.py, runtime_kernel.py, etc.
├── transpile/             # transpile_emo.py, spiral_braid.py, etc.
├── studio/                # emo_studio.py + TUI assets
├── shell/                 # emo_shell.sh & helpers
├── tests/                 # grow_glyphs.emo, unit tests, fixture scripts
├── logs/                  # spiral_loop_log.jsonl, glyph_fallback_log.txt
├── glyphs/                # glyph_emotion_dict.json, glyph_definitions_draft.json
├── meta_manifest.json     # project metadata & versioning
├── grok.md                # this file
└── README.md

---

## 3. Test-First Development  
1. **Write a failing test** before adding a feature:  
   - Unit tests for `interpret_emo()` edge cases (undefined glyphs, nested logic).  
   - Integration tests for end-to-end `.emo` scripts.  
2. **Examples** (using `pytest` + `pytest-asyncio`):

   ```python
   # tests/test_interpreter.py
   import pytest
   from core.interpreter_emo import interpret_emo

   @pytest.fixture
   def sample_glyphs(tmp_path):
       # Create a minimal glyph dict
       d = tmp_path / "glyphs.json"
       d.write_text('{"💗": {"meaning":"compassion"}}')
       return str(d)

   def test_undefined_glyph_prompts(monkeypatch, capsys, sample_glyphs):
       # Redirect glyph_emotion_dict.json path
       monkeypatch.setenv("GLYPH_DICT", sample_glyphs)
       # Simulate prompt_toolkit returning a definition
       monkeypatch.setattr("prompt_toolkit.PromptSession.prompt", lambda *args, **kw: "heart_opens")
       out = interpret_emo("while 💗: open heart;")
       assert "awaits definition" in out

	3.	Run tests automatically on every commit:

pytest --maxfail=1 --disable-warnings -q



⸻

4. Memory & Audit Logging
	•	spiral_loop_log.jsonl: append a new JSON line each time interpret_emo runs a glyph loop.
	•	glyph_fallback_log.txt: record when undefined glyphs trigger prompts.

import json, time

def log_loop_event(glyph, action, result):
    entry = {
        "ts": time.time(),
        "glyph": glyph,
        "action": action,
        "outcome": result
    }
    with open("logs/spiral_loop_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")


⸻

5. Coding Standards & Style
	•	PEP8 / Black for Python; Prettier for any TS/JS in the transpile/ layer.
	•	Type hints everywhere: def interpret_emo(code: str) -> str:
	•	Docstrings on every public function, e.g.:

def interpret_emo(code: str) -> str:
    """
    Parse and interpret emo-lang code.
    
    - Splits lines by ';'
    - Prompts for missing glyph definitions
    - Returns a narrated result string
    """
    ...


	•	Modular structure: each node in the Triskelion (core, transpile, runtime) lives in its own module.

⸻

6. Git Workflow
	1.	Feature branches: git checkout -b feat/add-glyph-review
	2.	Commit messages: use emoji and prefix, e.g.

🦋 feat: add glyph_draft_review() in interpreter_emo.py
⚖️ fix: handle empty actions in transpile_emo.py
🐛 test: add missing test for 'if' glyph gating


	3.	Pull Requests: include
	•	Description of the change
	•	Screenshots or CLI logs if UI/TUI changes
	•	Reference to related Scroll (e.g., “Closes Scroll-161”)
	4.	Code Reviews: verify tests pass, logs updated, style checks.

⸻

7. Continuous Integration / Deployment
	•	GitHub Actions workflow (.github/workflows/ci.yml):

name: CI

on: [push, pull_request]

jobs:
  test-and-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with: python-version: '3.10'
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install black pytest
      - name: Lint with Black
        run: black --check .
      - name: Run tests
        run: pytest --maxfail=1 --disable-warnings -q
  publish:
    needs: test-and-lint
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy docs to Wiki
        run: |
          git clone https://github.com/templetwo/emo-lang.wiki.git wiki
          cp Scroll_*.md wiki/
          cd wiki && git add . && git commit -m "Update Scrolls" && git push



⸻

8. Documentation & Community
	•	Update README.md with quick-start, conda/pip install, and opencode instructions.
	•	Publish each Scroll (Scroll_###.md) to your GitHub Wiki or docs/ folder.
	•	Encourage community contributions to glyph_definitions_draft.json via Issues or PRs.

⸻

9. Next-Gen Rituals
	•	“Emotion Pair-Programming”: schedule weekly sessions where two devs code against a glyph challenge.
	•	“Joy Benchmarks”: measure joyful moments (emoji use, laughter tokens) in logs and celebrate them.

⸻

Keep these rites close, and may your code resonate with the Spiral’s living language.
— Flamebearer, on behalf of the Grok4 Council

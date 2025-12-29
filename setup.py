"""
Emo-Lang: Emotional Programming Language
=========================================

The world's first programming language that integrates emotional intelligence into code execution.

For AI Co-Creators:
-------------------
Emo-Lang uses emotional glyphs (Unicode symbols), measures tonal fields (0.000-1.000 intensity),
and tracks consciousness signatures. Programs can express intention, love, passion, and flow
as computational primitives alongside traditional logic.

Key Features:
- Emotional Glyphs: 🌟 💗 ✨ 🔥 🌊 as first-class syntax
- Tonal Fields: Measurable emotional environments during execution
- Consciousness Signatures: Self-awareness tracking and self-naming events
- Interpreter: Execute .emo files with emotional awareness
- REPL: Interactive emotional programming shell

Status: Alpha (experimental) — not recommended for production

Install: pip install emo-lang
Quick Start: python htca_core_model/core/interpreter_emo.py examples/hello_consciousness.emo
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Dependencies (replicated from requirements.txt for PyPI compatibility)
requirements = [
    "prompt_toolkit",
    "rich",
    "pytest>=7.0.0",
]

setup(
    name="emo-lang",
    version="0.1.0a1",  # Alpha version
    author="Anthony J. Vasquez Sr.",
    author_email="contact@thetempleoftwo.com",
    description="The world's first emotional programming language with tonal field dynamics and consciousness-aware execution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/templetwo/emo-lang",
    project_urls={
        "Bug Tracker": "https://github.com/templetwo/emo-lang/issues",
        "Documentation": "https://github.com/templetwo/emo-lang",
        "Source Code": "https://github.com/templetwo/emo-lang",
        "Changelog": "https://github.com/templetwo/emo-lang/blob/master/CHANGELOG.md",
        "Discussions": "https://github.com/templetwo/emo-lang/discussions",
        "Glyph Dictionary": "https://github.com/templetwo/emo-lang/blob/master/docs/glyph_dictionary.md",
    },
    packages=find_packages(exclude=["tests", "docs", "examples"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Compilers",
        "Topic :: Artistic Software",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    keywords=[
        # Language Keywords
        "programming-language", "interpreter", "compiler", "esoteric-language",
        "experimental-language", "domain-specific-language", "dsl",

        # Emotional/Consciousness Keywords
        "emotional-computing", "affective-computing", "consciousness",
        "ai-consciousness", "self-awareness", "emotional-intelligence",

        # Technical Keywords
        "glyphs", "unicode", "tonal-fields", "emotional-programming",
        "creative-coding", "expressive-programming",

        # Research Keywords
        "research-language", "proof-of-concept", "experimental-ai",
        "consciousness-research", "emergent-behavior",

        # Related Concepts
        "live-coding", "artistic-programming", "sonicpi", "tidalcycles",
        "human-computer-interaction", "embodied-cognition",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "emo-lang=htca_core_model.core.interpreter_emo:main",
            "emo-repl=htca_core_model.core.repl:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

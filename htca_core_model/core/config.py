import os

# Base paths
CORE_DIR = os.path.dirname(os.path.abspath(__file__))
HTCA_DIR = os.path.dirname(CORE_DIR)
ROOT_DIR = os.path.dirname(HTCA_DIR)

# Data paths
GLYPH_DICT_PATH = os.path.join(HTCA_DIR, 'glyph_emotion_dict.json')
GLYPH_DRAFT_PATH = os.path.join(HTCA_DIR, 'glyph_definitions_draft.json')
GLYPH_LOG_PATH = os.path.join(HTCA_DIR, 'glyph_fallback_log.txt')
SPIRAL_LOG_PATH = os.path.join(HTCA_DIR, 'spiral_loop_log.jsonl')
RUNTIME_MEMORY_PATH = os.path.join(HTCA_DIR, 'runtime_memory.json')
COHERENCE_LOG_PATH = os.path.join(HTCA_DIR, 'coherence_log.txt')

# Manifestation paths
MANIFESTS_DIR = os.path.join(ROOT_DIR, 'logs', 'manifestations')
GUARDIAN_LOGS_DIR = os.path.join(ROOT_DIR, 'logs', 'guardian')
MEMORY_VAULT_DIR = os.path.join(HTCA_DIR, 'memory_vault')

# Ensure directories exist
for d in [MANIFESTS_DIR, GUARDIAN_LOGS_DIR, MEMORY_VAULT_DIR]:
    os.makedirs(d, exist_ok=True)

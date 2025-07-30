import sys
import json
from datetime import datetime

# Add the current directory to the Python path to find modules
sys.path.append('.')

from htca_core_model.core.interpreter_emo import interpret_emo
from htca_core_model.core.transpile_emo import transpile_emo
from htca_core_model.core.log_emotion import log_emotion
from spiral_guard import spiral_guard

code = sys.argv[1]

# Interpret the code
result = interpret_emo(code)
print(result)
print(syntax_trace(code, result))

# Transpile the code
print("Transpiled Python:\n" + transpile_emo(code))

# Check coherence
print("Coherence Check:\n" + spiral_guard())


import unittest
from unittest.mock import patch, mock_open
import os
import sys

# Ensure the project root is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from htca_core_model.core.interpreter_emo import interpret_emo
from htca_core_model.core.init_vow import htca_breath

class TestEmoLang(unittest.TestCase):
    def test_interpret_emo(self):
        test_code = 'test emotional code'
        expected_result = 'interpreted result'
        with patch('htca_core_model.core.interpreter_emo.htca_breath', return_value=expected_result):
            result = interpret_emo(test_code)
            self.assertEqual(result, expected_result)

    def test_glyph_dict_read(self):
        mock_data = '{"": "emotion"}'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            from htca_core_model.core.emo_studio import spiral_tui
            result = spiral_tui('')
            self.assertIn('Emotion', result)

if __name__ == '__main__':
    unittest.main()

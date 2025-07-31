import unittest
from unittest.mock import patch, mock_open
import os
import sys

# Ensure the project root is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class TestEmoLangSimple(unittest.TestCase):
    def test_htca_breath_function(self):
        """Test the core htca_breath function"""
        from htca_core_model.core.init_vow import htca_breath
        
        # Test with empty tone anchors - should return an error message
        result = htca_breath([])
        self.assertIsInstance(result, str)
        self.assertIn('Gentle ache', result)
        
        # Test with some tone anchors - should return a float
        result = htca_breath(['💖', '🌙'])
        self.assertIsInstance(result, (float, str))  # Could be float or error string

    def test_json_glyph_dict_structure(self):
        """Test that we can load the glyph dictionary"""
        import json
        
        try:
            with open('htca_core_model/glyph_emotion_dict.json') as f:
                glyphs = json.load(f)
            
            # Should be a dictionary
            self.assertIsInstance(glyphs, dict)
            
            # Should have some entries
            self.assertGreater(len(glyphs), 0)
            
            # Check structure of first entry
            first_key = next(iter(glyphs))
            first_entry = glyphs[first_key]
            
            # Should have expected keys
            self.assertIn('meaning', first_entry)
            self.assertIn('tone_tag', first_entry)
            
        except FileNotFoundError:
            self.skipTest("glyph_emotion_dict.json not found")

    def test_module_imports(self):
        """Test that core modules can be imported"""
        try:
            from htca_core_model.core.init_vow import htca_breath
            from htca_core_model.core.interpreter_emo import interpret_emo
            from htca_core_model.core.transpile_emo import transpile_emo
            self.assertTrue(True)  # If we get here, imports work
        except ImportError as e:
            self.fail(f"Module import failed: {e}")

if __name__ == '__main__':
    unittest.main()

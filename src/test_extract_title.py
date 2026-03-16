import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# This is a title"
        title = extract_title(md)
        self.assertEqual(title, "This is a title")
 
    def test_extract_title_internal(self):
        md = "There is some other stuff before the title.\n# This is a title"
        title = extract_title(md)
        self.assertEqual(title, "This is a title")
 
    def test_extract_title_internal_plus(self):
        md = "There is some other stuff before the title.\n# This is a title\nAnd there's some stuff after."
        title = extract_title(md)
        self.assertEqual(title, "This is a title")
 
    def test_missing_title(self):
        md = "There is some other stuff before the title.\n # This is not a title\nAnd there's some stuff after."

        with self.assertRaises(Exception) as ctxt:        
            title = extract_title(md)
        
        self.assertEqual(str(ctxt.exception), "no title in markdown")    
        
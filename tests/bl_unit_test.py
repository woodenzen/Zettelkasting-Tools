import unittest
from beautiful_language import search_in_zettelkasten

class TestSearchInZettelkasten(unittest.TestCase):
    def test_search_in_zettelkasten(self):
        # Replace with the actual path to your zettelkasten directory
        zettelkasten_dir = "/path/to/your/zettelkasten"
        # Replace with a term you know exists in the line following the tag
        search_term = "the"
        
        try:
            results = search_in_zettelkasten(search_term, zettelkasten_dir)
            # Check that the results are not empty
            self.assertTrue(results)
        except Exception as e:
            self.fail(f"Test failed with error: {e}")

if __name__ == "__main__":
    unittest.main()

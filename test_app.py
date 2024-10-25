import unittest
from api import ask_question, Query

class TestAIChat(unittest.TestCase):
    def test_ask_question(self):
        query = Query(question="What does AI stand for?", pdf_text="AI stands for Artificial Intelligence.")
        result = ask_question(query)
        self.assertEqual(result['answer'], "AI stands for Artificial Intelligence.")
if __name__ == '__main__':
    unittest.main()        
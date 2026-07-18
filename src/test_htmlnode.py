import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()

        self.assertEqual("HTMLNode(None, None, children: None, None)",
                         repr(node))

    def test_eq2(self):
        node = HTMLNode("h1", "This is a heading", None, None)

        self.assertEqual("HTMLNode(h1, This is a heading, children: None, None)",
                         repr(node))

    def test_notEq(self):
        node = HTMLNode(None, None, [HTMLNode()], {"href": "https://www.google.com"})
        
        self.assertNotEqual("HTMLNode(p, None, children: 1, 1)",
                        repr(node))

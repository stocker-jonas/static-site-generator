import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    

    def test_eq3(self):
        node = LeafNode("p", "This is a paragraph", {"a": "idk"})

        self.assertEqual("LeafNode(p, This is a paragraph, {'a': 'idk'})",
                         repr(node))

    def test_eq4(self):
        node = ParentNode(
                "h1",
                [
                    ParentNode(
                        "p",
                        [
                            LeafNode(
                                "b",
                                "bold",
                                {"x": "y"}
                            )
                        ],
                        {"z": "a"}
                    ),
                    LeafNode(
                        "i",
                        "italic"
                    )
                ]
            )

        self.assertEqual("<h1><p z=a><b x=y>bold</b><i>italic</i></h1>",
                         node.to_html())

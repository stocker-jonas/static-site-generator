class HTMLNode():
    def __init__(
            self,
            tag: str | None = None,
            value: str | None = None,
            children: list["HTMLNode"] | None = None,
            props: dict[str, str] | None = None
            ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError("Not Implemented For Parent Class")

    def props_to_html(self) -> str:
        str_output = ""

        if self.props is None:
            return str_output

        for i in range(len(self.props) + 1):
            str_output += f" {self.props.items()[0]}={self.props.items()[1]}"

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: dict[str, str] | None = None) -> None:

        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Leaf Nodes must have a value assigned!")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list["HTMLNode"],
            props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Parent Nodes must have a tag assigned!")

        if self.children is None:
            raise ValueError("Parent Nodes must have at least one child assigned!")

        return f"<{self.tag}{self.props_to_html()}>{self.print_children()}</{self.tag}>"

    def print_children(self) -> str:
        str = ""
        if self.children is None:
            return str

        for child in self.children:
            str += child.to_html()

        return str

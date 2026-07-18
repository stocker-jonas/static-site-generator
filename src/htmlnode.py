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

        for i in range(len(props) + 1):
            str_output += f" {props.item()[0]}={props.item()[1]}"

    def __repr__(self) -> None:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

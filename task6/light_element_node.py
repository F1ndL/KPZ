from light_node import LightNode

class LightElementNode(LightNode):

    def __init__(self, tag_name: str, display_type: str = "block",
                 self_closing: bool = False, css_classes: list = None):
        self.tag_name = tag_name
        self.display_type = display_type
        self.self_closing = self_closing
        self.css_classes = css_classes if css_classes else []
        self.children = []

    def add_child(self, node: LightNode):
        self.children.append(node)

    def get_inner_html(self) -> str:
        return "".join(child.get_outer_html() for child in self.children)

    def get_outer_html(self) -> str:
        classes_str = ""
        if self.css_classes:
            classes_str = ' class="' + " ".join(self.css_classes) + '"'

        if self.self_closing:
            return f"<{self.tag_name}{classes_str} />"
        else:
            inner = self.get_inner_html()
            return f"<{self.tag_name}{classes_str}>{inner}</{self.tag_name}>"

    def child_count(self) -> int:
        return len(self.children)

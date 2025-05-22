from light_element_node import LightElementNode
from light_text_node import LightTextNode

class LightElementFlyweight:
    def __init__(self, tag_name: str, display_type: str = "block",
                 self_closing: bool = False, css_classes: list = None):
        self.tag_name = tag_name
        self.display_type = display_type
        self.self_closing = self_closing
        self.css_classes = css_classes if css_classes else []

    def create_node(self, text: str = "") -> LightElementNode:
        node = LightElementNode(
            tag_name=self.tag_name,
            display_type=self.display_type,
            self_closing=self.self_closing,
            css_classes=self.css_classes
        )
        if text:
            node.add_child(LightTextNode(text))
        return node


class LightFlyweightFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, tag_name: str, display_type: str = "block",
                      self_closing: bool = False, css_classes: list = None) -> LightElementFlyweight:
        key = (tag_name, display_type, self_closing, tuple(css_classes) if css_classes else ())
        if key not in cls._flyweights:
            cls._flyweights[key] = LightElementFlyweight(
                tag_name=tag_name,
                display_type=display_type,
                self_closing=self_closing,
                css_classes=css_classes
            )
        return cls._flyweights[key]

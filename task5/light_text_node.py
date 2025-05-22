from light_node import LightNode

class LightTextNode(LightNode):
    def __init__(self, text: str):
        self.text = text

    def get_outer_html(self):
        return self.text

    def get_inner_html(self):
        return self.text

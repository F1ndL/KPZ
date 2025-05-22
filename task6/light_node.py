class LightNode:
    def get_outer_html(self) -> str:
        raise NotImplementedError("Цей метод має бути реалізований у підкласах.")

    def get_inner_html(self) -> str:
        raise NotImplementedError("Цей метод має бути реалізований у підкласах.")

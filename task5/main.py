from light_element_node import LightElementNode
from light_text_node import LightTextNode

def main():
    ul = LightElementNode("ul", display_type="block", self_closing=False, css_classes=["my-list"])

    li1 = LightElementNode("li", display_type="block", self_closing=False, css_classes=["item"])
    li1.add_child(LightTextNode("Пункт 1"))

    li2 = LightElementNode("li", display_type="block", self_closing=False, css_classes=["item"])
    li2.add_child(LightTextNode("Пункт 2"))

    li3 = LightElementNode("li", display_type="block", self_closing=False, css_classes=["item"])
    li3.add_child(LightTextNode("Пункт 3"))

    ul.add_child(li1)
    ul.add_child(li2)
    ul.add_child(li3)

    print("outerHTML:")
    print(ul.get_outer_html())

    print("\ninnerHTML:")
    print(ul.get_inner_html())

    print("\nКількість дочірніх елементів ul:", ul.child_count())

if __name__ == "__main__":
    main()

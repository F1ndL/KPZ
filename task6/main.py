import os
from light_flyweight_factory import LightFlyweightFactory
from light_element_node import LightElementNode


def classify_line(line: str, is_first_line: bool) -> str:
    if is_first_line:
        return "h1"
    if line.startswith(" "):
        return "blockquote"
    if len(line.strip()) < 20 and len(line.strip()) > 0:
        return "h2"
    return "p"


def main():
    global LightFlyweightFactory
    filename = "text.txt"

    if not os.path.exists(filename):
        print(f"Файл '{filename}' не знайдено! Завантажте його або змініть назву.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    body = LightElementNode("body")

    for index, line in enumerate(lines):
        raw_line = line.rstrip("\r\n")

        is_first_line = (index == 0)
        tag_name = classify_line(raw_line, is_first_line)

        flyweight = LightFlyweightFactory.get_flyweight(tag_name)

        node = flyweight.create_node(raw_line)

        body.add_child(node)

    print("=== OUTER HTML ===")
    print(body.get_outer_html())

    print("\n=== INNER HTML (body) ===")
    print(body.get_inner_html())

    print("\n=== Flyweights in Factory ===")
    from light_flyweight_factory import LightFlyweightFactory
    print(f"Загальна кількість Flyweight-об’єктів: {len(LightFlyweightFactory._flyweights)}")

if __name__ == "__main__":
    main()

def get_classnames() -> list[str]:
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    return classes

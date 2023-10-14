class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.amount = int(input("Number of name tags: "))

    class Nametag:
        def __init__(self) -> None:
            pass

        def create_nametag(self):
            POSSIBLE_SHAPES = ["circle", "square", "triangle"]
            proposed_shape = input("Name tag shape: ")
            if proposed_shape in POSSIBLE_SHAPES:
                self.shape = proposed_shape


def main():
    while True:
        pass


if __name__ == "__main__":
    main()

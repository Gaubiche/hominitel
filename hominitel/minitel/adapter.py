class Adapter:
    def _print(self, text: str):
        raise NotImplementedError("_print method must be implemented")

    def pos(self, row: int, col: int):
        raise NotImplementedError("pos method must be implemented")

    def cls(self):
        raise NotImplementedError("cls method must be implemented")

    def inverse(self):
        raise NotImplementedError("inverse method must be implemented")

    def echo_off(self):
        raise NotImplementedError("echo_off method must be implemented")

    def _if(self):
        raise NotImplementedError("read method must be implemented")
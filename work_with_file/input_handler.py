class InputHandler:
    @staticmethod
    def handle_input(prompt: str, data_type: type = str):
        while True:
            try:
                return data_type(input(prompt).strip())
            except ValueError:
                print(f"Incorrect input data type, excepted value {data_type.__name__}")
from flask import Request as FlaskRequest


class Calculator1:
    def calculate(self, request: FlaskRequest) -> dict:
        body = request.json
        input_data = self.__validate_body(body)
        print(input_data)

    def __validate_body(self, body: dict) -> float:
        if "number" not in body:
            raise Exception("Body Bad Formatted")

        input_data = body["number"]
        return input_data

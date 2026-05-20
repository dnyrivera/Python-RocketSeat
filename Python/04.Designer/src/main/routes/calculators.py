# pylint: disable=import-error
from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

# Define the blueprint for the calculator routes
calc_routes_bp = Blueprint("calc_routes", __name__)


@calc_routes_bp.route("/calc/1", methods=["POST"])
def calc_1():
    calc = Calculator1()
    calc.calculate(request)

    return jsonify({"success": True}), 200

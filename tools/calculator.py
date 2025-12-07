from flask import Blueprint, render_template, request
import ast
import operator

calculator_bp = Blueprint('calculator', __name__)

# Allowed math operators
ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}

def safe_eval(expr):
    """Safely evaluate basic math expressions"""
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in ops:
                raise ValueError("Operator not allowed")
            return ops[op_type](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in ops:
                raise ValueError("Unary operator not allowed")
            return ops[op_type](_eval(node.operand))
        else:
            raise ValueError("Invalid syntax")

    try:
        parsed = ast.parse(expr, mode='eval')
        return _eval(parsed.body)
    except Exception:
        return None


@calculator_bp.route("/calculator", methods=["GET", "POST"])
def calculator():
    expr = ""
    result = None

    if request.method == "POST":
        expr = request.form.get("expression", "")
        result = safe_eval(expr)

    return render_template("calculator.html", expr=expr, result=result)
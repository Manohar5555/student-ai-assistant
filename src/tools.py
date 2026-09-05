from src.rag import search_college_documents

import ast
import operator


def rag_tool(query):
    try:
        result = search_college_documents(query)

        return {
            "success": True,
            "result": result,
            "error": None
        }

    except Exception:
        return {
            "success": False,
            "result": None,
            "error": "Unable to search the college documents."
        }


def calculator_tool(expression):
    try:
        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow
        }

        def calculate(node):
            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                raise ValueError("Invalid number")

            if isinstance(node, ast.BinOp):
                if type(node.op) not in operators:
                    raise ValueError("Operator not allowed")

                left = calculate(node.left)
                right = calculate(node.right)

                return operators[type(node.op)](left, right)

            if isinstance(node, ast.UnaryOp):
                if isinstance(node.op, ast.USub):
                    return -calculate(node.operand)

                if isinstance(node.op, ast.UAdd):
                    return calculate(node.operand)

            raise ValueError("Invalid expression")

        tree = ast.parse(expression, mode="eval")

        result = calculate(tree.body)

        return {
            "success": True,
            "result": result,
            "error": None
        }

    except Exception:
        return {
            "success": False,
            "result": None,
            "error": "Unable to calculate the expression."
        }


def calculate(expression: str):
    """
    Evaluates a mathematical expression and returns the result.
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Error: {e}"
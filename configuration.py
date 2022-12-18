"""
Configuration file that contains Constants that are used in multiple modules of the program.
"""

# type and priority dict:
OPERATORS_PRIORITY_AND_TYPES = {"+": (1, "BINARY"),
                                "-": (1, "BINARY"),
                                "*": (2, "BINARY"),
                                "/": (2, "BINARY"),
                                "^": (3, "BINARY"),
                                "%": (4, "BINARY"),
                                "$": (5, "BINARY"),
                                "&": (5, "BINARY"),
                                "@": (5, "BINARY"),
                                "~": (6, "UNARY_L"),
                                "!": (6, "UNARY_R"),
                                "#": (6, "UNARY_R")}

# supported chars:
BRACKETS = "()"
OPERATORS = "".join(OPERATORS_PRIORITY_AND_TYPES.keys())
MINUS_SIGN = "-"
DOT = "."

# infinite const:
INF = float("inf")

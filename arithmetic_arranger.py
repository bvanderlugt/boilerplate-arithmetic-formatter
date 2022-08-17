import operator

ops = {"+": operator.add, "-": operator.sub}


def arithmetic_arranger(*args):
    if args is None:
        raise TypeError("problems can't be None")
    problems = args[0]
    solve = args[1] if len(args) == 2 else False
    if len(problems) > 5:
        return "Error: Too many problems."
    row_1 = []
    row_2 = []
    row_3 = []
    row_4 = []
    for problem in problems:
        parts = problem.split(" ")
        err = _validate_problem_parts(parts)
        if err is not None:
            return err
        sum = ops[parts[1]](int(parts[0]), int(parts[2]))
        max_num_len = max(len(parts[0]), len(parts[2]))
        # the width of the problem should be max number length plus one space
        # plus the operand
        width = max_num_len+2
        # preformatting this because I can't figure out how to nest inside of
        # the row 2 f-string
        operand_row = f"{parts[1]:<{(max_num_len-len(parts[2]))+2}}{parts[2]}"
        row_1.append(f"{parts[0]:>{width}}")
        row_2.append(f"{operand_row:>{width}}")
        row_3.append(f"{'':->{width}}")
        row_4.append(f"{sum:>{width}}" if solve else "")

    res = ["    ".join(row_1),
           "    ".join(row_2),
           "    ".join(row_3)]
    if solve:
        res.append("    ".join(row_4))
    return "\n".join(res)


def _validate_problem_parts(parts):
    if parts[1] not in '+-':
        return "Error: Operator must be '+' or '-'."

    if len(parts[0]) > 4 or len(parts[2]) > 4:
        return "Error: Numbers cannot be more than four digits."

    try:
        int(parts[0])
        int(parts[2])
    except ValueError:
        return "Error: Numbers must only contain digits."
    return

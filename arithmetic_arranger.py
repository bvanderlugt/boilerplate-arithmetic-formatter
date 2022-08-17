import operator

ops = {"+": operator.add, "-": operator.sub}

def arithmetic_arranger(*args):
    if args is None:
        raise TypeError("problems can't be None")
    problems = args[0]
    solve = args[1] if len(args) == 2 else False
    if len(problems) > 5:
        return "Error: Too many problems."
    arranged_problems = ""
    for problem in problems:
        parts = problem.split(" ")
        err = _validate_problem_parts(parts)
        if err != None:
            return err
        sum = ops[parts[1]](int(parts[0]), int(parts[2]))
        max_num_len = max(len(parts[0]), len(parts[2]))
        # the width of the problem should be max number length plus one space
        # plus the operand
        width = max_num_len+2
        # preformatting this because the operand and second part 
        operand_row = f"{parts[1]:<{(max_num_len-len(parts[2]))+2}}{parts[2]}"
        arranged_problems += f"{parts[0]:>{width}}\n" \
                             f"{operand_row:>{width}}\n" \
                             f"{'':->{width}}\n" \
                             f"{sum:>{width}}\n" if solve else ""
    return arranged_problems

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

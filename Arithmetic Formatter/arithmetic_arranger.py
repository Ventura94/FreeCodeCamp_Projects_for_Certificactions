def sum(first_number, second_number):
    return int(first_number) + int(second_number)


def res(first_number, second_number):
    return int(first_number) - int(second_number)


def arithmetic_arranger(problems, with_result=False):
    arranged_problems = ""
    problems_dicts = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for p in problems:
        arithmetic = p.split(" ")
        try:
            problem = dict(
                first_number=int(arithmetic[0]),
                operator=arithmetic[1],
                second_number=int(arithmetic[2]),
            )
        except:
            return "Error: Numbers must only contain digits."

        if len(arithmetic[0]) > 4 or len(arithmetic[2]) > 4:
            return "Error: Numbers cannot be more than four digits."


        if problem["operator"] == "+":
            problem["result"] = sum(problem["first_number"], problem["second_number"])

        elif problem["operator"] == "-":
            problem["result"] = res(problem["first_number"], problem["second_number"])

        else:
            return "Error: Operator must be '+' or '-'."

        problems_dicts.append(problem)


    for pd in problems_dicts:
        len_first_number = len(str(pd["first_number"]))
        len_second_number = len(str(pd["second_number"]))

        if len_first_number >= len_second_number:
            arranged_problems = arranged_problems + "  " + str(pd["first_number"]) + "    "

        elif len_first_number < len_second_number:
            spaces = (len_second_number - len_first_number) * " "
            arranged_problems = arranged_problems + "  " + spaces + str(pd["first_number"]) + "    "
    arranged_problems = arranged_problems.rstrip()
    arranged_problems = arranged_problems + "\n"

    for pd in problems_dicts:
        len_first_number = len(str(pd["first_number"]))
        len_second_number = len(str(pd["second_number"]))

        if len_first_number >= len_second_number:
            spaces = (len_first_number - len_second_number) * " "
            arranged_problems = arranged_problems + str(pd["operator"]) + " " + spaces + str(pd["second_number"]) + "    "

        elif len_first_number < len_second_number:
            arranged_problems = arranged_problems + str(pd["operator"]) + " " + str(pd["second_number"]) + "    "
    arranged_problems = arranged_problems.rstrip()
    arranged_problems = arranged_problems + "\n"

    for pd in problems_dicts:
        len_first_number = len(str(pd["first_number"]))
        len_second_number = len(str(pd["second_number"]))

        if len_first_number >= len_second_number:
            g = "-" * (len_first_number + 2)
            arranged_problems = arranged_problems + g + "    "
        elif len_first_number < len_second_number:
            g = "-" * (len_second_number + 2)
            arranged_problems = arranged_problems + g + "    "

    arranged_problems = arranged_problems.rstrip()
    if with_result:

        arranged_problems = arranged_problems + "\n"
        for pd in problems_dicts:
            len_first_number = len(str(pd["first_number"]))
            len_second_number = len(str(pd["second_number"]))
            cant = len(str(pd["result"]))

            if len_first_number >= len_second_number:
                r = ((len_first_number + 2) - cant) * " "
                arranged_problems = arranged_problems + r + str(pd["result"]) + "    "

            elif len_first_number < len_second_number:
                r = ((len_second_number + 2) - cant) * " "
                arranged_problems = arranged_problems + r + str(pd["result"]) + "    "
        arranged_problems = arranged_problems.rstrip()

    return arranged_problems

print("Hello! This is a simple calculator!")
print('Valid operators - "+", "-", "*", "/" or "**".'
      '\nIf you want to clear the calculator, write clear.'
      '\nIf you want to stop the program, write stop.')

operators_list = ["+", "-", "*", "/", "**"]
program_stop = False


def is_number_first_command():  # Function needed in order to check if the input is a number
    try:
        float(first_command)
        return True
    except ValueError:
        return False


def calculations():
    if math_operator == "+":
        result = latest_result + number
    elif math_operator == "-":
        result = latest_result - number
    elif math_operator == "*":
        result = latest_result * number
    elif math_operator == "/":
        result = latest_result / number
    elif math_operator == "**":
        result = latest_result ** number
    return result


while True:
    if program_stop:
        break
    print()
    numbers_count = 0
    latest_result = 0
    operator_in_use = ""
    program_clear = False

    while True:
        if program_stop or program_clear:
            break

        first_command = input("Number: ").lower()
        if first_command == "stop":
            program_stop = True
            break
        elif first_command == "clear":
            break
        elif not is_number_first_command():
            print("Please enter a valid number or a valid command!")
            continue

        number = float(first_command)

        if number == 0 and operator_in_use == "/":
            print("Cannot divide by 0! Try another number!")
            continue

        numbers_count += 1
        if numbers_count == 1:
            latest_result += number

        if numbers_count != 1:
            total_result = calculations()
            latest_result = total_result
            print(f"Result: {total_result}.")

        while True:
            second_command = input("Operator: ").lower()
            if second_command == "stop":
                program_stop = True
                break
            elif second_command == "clear":
                program_clear = True
                break

            math_operator = second_command
            if math_operator not in operators_list:
                print(f'Please enter a valid operator - "+", "-", "*", "/" or "**"')
                continue
            else:
                operator_in_use = math_operator
                break

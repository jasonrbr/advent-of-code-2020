with open('input6.txt') as f:
    yes_answers = {}
    total_yes_answers = 0
    total_all_yes_answers = 0
    num_people = 0
    for line in f:
        if line.strip() == '':
            total_yes_answers += len(yes_answers)
            total_all_yes_answers += len(
                [x for x in yes_answers if yes_answers[x] == num_people])
            num_people = 0
            yes_answers.clear()
            continue

        num_people += 1
        for char in line.strip():
            yes_answers[char] = yes_answers.get(char, 0) + 1

    # one more time for the last input
    total_yes_answers += len(yes_answers)
    total_all_yes_answers += len(
        [x for x in yes_answers if yes_answers[x] == num_people])
    num_people = 0
    yes_answers.clear()

    print(total_yes_answers)
    print(total_all_yes_answers)

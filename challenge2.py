with open("input2.txt") as f:
    num_good_passwords = 0
    for line in f:
        num_chars, letter_with_colon, password = line.split()
        min_char, max_char = num_chars.split('-')
        letter = letter_with_colon[0]
        num_occurrences = password.count(letter)
        if num_occurrences >= int(min_char) and num_occurrences <= int(max_char):
            num_good_passwords += 1
    print(num_good_passwords)

with open('input2.txt') as f:
    num_good_passwords = 0
    for line in f:
        char_positions, letter_with_colon, password = line.split()
        pos1, pos2 = char_positions.split('-')
        letter = letter_with_colon[0]
        is_pos1 = password[int(pos1) -1] == letter
        is_pos2 = password[int(pos2) - 1] == letter
        if is_pos1 != is_pos2:
            num_good_passwords += 1
    print(num_good_passwords)
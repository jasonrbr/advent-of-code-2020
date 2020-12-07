with open('input5.txt') as f:
    highest_id = 0
    row_range = [0, 127]
    column_range = [0, 7]
    ids = set(range(0, 981))
    for line in f:
        current_row_range = row_range[:]
        current_column_range = column_range[:]
        for char in line[:7]:
            new_max_or_min = int((
                current_row_range[0] + current_row_range[1]) / 2)
            if char == 'F':
                current_row_range[1] = new_max_or_min
            else:
                current_row_range[0] = new_max_or_min

        for char in line[7:]:
            new_max_or_min = int((
                current_column_range[0] + current_column_range[1]) / 2)
            if char == 'L':
                current_column_range[1] = new_max_or_min
            elif char == 'R':
                current_column_range[0] = new_max_or_min

        seat_id = current_row_range[1] * 8 + current_column_range[1]

        if seat_id > highest_id:
            highest_id = seat_id

        ids.remove(seat_id)

print(ids)

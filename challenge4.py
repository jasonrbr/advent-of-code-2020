def validate_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if not all(x in passport.keys() for x in required_fields):
        return False

    if int(passport['byr']) < 1920 or int(passport['byr']) > 2020:
        return False

    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False

    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False

    if passport['hgt'].find('in') == -1 and passport['hgt'].find('cm') == -1:
        return False

    if passport['hgt'].find('in') != -1 and (int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76):
        return False

    if passport['hgt'].find('cm') != -1 and (int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193):
        return False

    if passport['hcl'][0] != '#' or len(passport['hcl']) != 7:
        return False

    if not passport['hcl'][1:].isalnum():
        return False

    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if len(passport['pid']) != 9 or not passport['pid'].isnumeric():
        return False

    return True


with open('input4.txt') as f:
    valid_passports = 0
    passport = {}
    for line in f:
        if line.strip() == '':
            # previous passport is finished
            if validate_passport(passport):
                valid_passports += 1
            passport = {}
            continue

        fields = line.split(' ')
        new_fields = {x.split(':')[0]: x.split(':')[1].strip() for x in fields}
        passport.update(new_fields)

    if (validate_passport(passport)):
        valid_passports += 1

    print(valid_passports)

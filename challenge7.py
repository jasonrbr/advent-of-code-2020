rules_map = {}

with open('input7.txt') as f:
    for line in f:
        bag_description, bag_contents = line.split('contain')
        shade, color, *rest = bag_description.strip().split(' ')
        contents_descriptions = bag_contents.strip().split(',')
        for content_description in contents_descriptions:
            if content_description.find('no other bags') != -1:
                rules_map[shade + color] = {}
                continue

            count, content_shade, content_color, * \
                rest = content_description.strip().split(' ')
            rule_map = rules_map.get(shade + color, {})
            rule_map[content_shade + content_color] = int(count)
            rules_map[shade + color] = rule_map


def bag_can_contain(rules_map, desired_bag_color, bag_color_to_check):
    next_bag_colors = rules_map[bag_color_to_check].keys()

    if len(next_bag_colors) == 0:
        return False

    if my_bag_color in next_bag_colors:
        return True

    bags = [bag_can_contain(rules_map, desired_bag_color, x)
            for x in next_bag_colors]

    return any(bags)


def bag_count(rules_map, bag_color):
    next_bag_colors = rules_map[bag_color].keys()

    if len(next_bag_colors) == 0:
        return 0

    return sum([rules_map[bag_color][x] * bag_count(rules_map, x) + rules_map[bag_color][x] for x in next_bag_colors])


my_bag_color = 'shinygold'

bags_holding_my_bag = sum([bag_can_contain(rules_map, my_bag_color, x)
                           for x in rules_map.keys()])

print(bags_holding_my_bag)

bags_needed = bag_count(rules_map, my_bag_color)

print(bags_needed)

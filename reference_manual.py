from color_translations import get_color_from_pair_number


def print_reference_manual(heading_formatter, line_formatter):
  print(heading_formatter(), end='')
  for i in range(1, 26):
    major_color, minor_color = get_color_from_pair_number(i)
    print(line_formatter(i, major_color, minor_color), end='')

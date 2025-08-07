from color_translations import get_color_from_pair_number, get_pair_number_from_color
from reference_manual import print_reference_manual
from ref_manual_formatters import md_heading, md_format_line, csv_heading, csv_format_line  


def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)


def test_reference_manual_md():
  assert(md_heading() == '| Pair Number | Major Color | Minor Color |\n| --- | --- | --- |\n')
  assert(md_format_line(1, 'White', 'Blue') == '| 1 | White | Blue |\n')
  print('---- here is the markdown reference manual ----')
  print_reference_manual(md_heading, md_format_line)


def test_reference_manual_csv():
  assert(csv_heading() == 'Pair Number,Major Color,Minor Color\n')
  assert(csv_format_line(1, 'White', 'Blue') == '1,White,Blue\n')
  print('---- here is the CSV reference manual ----')
  print_reference_manual(csv_heading, csv_format_line)


if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  test_reference_manual_md()
  test_reference_manual_csv()
  print('Done :)')

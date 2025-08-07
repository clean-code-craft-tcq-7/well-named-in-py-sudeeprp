
def md_heading():
    return '| Pair Number | Major Color | Minor Color |\n| --- | --- | --- |\n'


def md_format_line(pair_number, major_color, minor_color):
    return f'| {pair_number} | {major_color} | {minor_color} |\n'


def csv_heading():
    return 'Pair Number,Major Color,Minor Color\n'


def csv_format_line(pair_number, major_color, minor_color):
    return f'{pair_number},{major_color},{minor_color}\n'

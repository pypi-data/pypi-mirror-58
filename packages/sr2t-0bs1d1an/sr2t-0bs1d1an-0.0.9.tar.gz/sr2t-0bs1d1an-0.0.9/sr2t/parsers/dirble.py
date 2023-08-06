#!/usr/bin/env python3

""" sr2t Dirble parser"""

import xlsxwriter
from prettytable import PrettyTable


def dirble_parser(args, root, data):
    """ Dirble parser """

    for element in root:
        for path in element.findall('path'):
            list_file = []
            list_file.append(path.get('code'))
            list_file.append(path.get('content_len'))
            list_file.append(path.get('is_directory'))
            list_file.append(path.get('is_listable'))
            list_file.append(path.get('found_from_listable'))
            list_file.append(path.get('redirect_url'))
            data.append([path.get('url'), list_file])

    my_table = PrettyTable()
    csv_array = []
    header = [
        'url', 'code', 'content len', 'is directory', 'is listable',
        'found from listable']
    header.extend(['redirect url', 'annotations'.ljust(args.annotation_width)])
    my_table.field_names = header
    for url, item in data:
        row = [url, item[0], item[1], item[2], item[3], item[4], item[5]]
        row.extend(['X'])
        my_table.add_row(row)
        csv_array.append(row)
    my_table.align["url"] = "l"
    my_table.align["content len"] = "l"
    my_table.align["is directory"] = "l"
    my_table.align["is listable"] = "l"
    my_table.align["found from listable"] = "l"
    my_table.align["redirect url"] = "l"

    if args.output_xlsx:
        workbook = xlsxwriter.Workbook(args.output_xlsx)
        bold = workbook.add_format({'bold': True})
        wrap = workbook.add_format()
        wrap.set_text_wrap()
        worksheet_dirble = workbook.add_worksheet('Dirble')
        worksheet_dirble.set_tab_color('red')
        worksheet_dirble.set_column(0, 0, 60)
        worksheet_dirble.set_column(2, 2, 12)
        worksheet_dirble.set_column(3, 3, 12)
        worksheet_dirble.set_column(4, 4, 12)
        worksheet_dirble.set_column(5, 5, 20)
        worksheet_dirble.set_column(6, 6, 60)
        worksheet_dirble.set_column(7, 7, 20)
        xlsx_header = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in header]
        worksheet_dirble.add_table(
            0, 0, len(csv_array), len(csv_array[0]) - 1, {
                'data': csv_array,
                'style': 'Table Style Light 9',
                'header_row': True,
                'columns': xlsx_header
            })
        worksheet_dirble.freeze_panes(0, 1)

    return my_table, csv_array, header


if __name__ == '__main__':
    dirble_parser()

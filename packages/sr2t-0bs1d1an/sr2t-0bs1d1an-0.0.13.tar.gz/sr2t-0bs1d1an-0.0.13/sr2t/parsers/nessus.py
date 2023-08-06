#!/usr/bin/env python3

""" sr2t Nessus parser"""

import csv
import os
import pkg_resources
import textwrap
import yaml
from prettytable import PrettyTable


def nessus_portscan_loopy(var1, reporthost, var2):
    """ Specific Nessus loop to add N open ports to the same address """

    for reportitem in reporthost.findall('ReportItem'):
        if reportitem.get('pluginName') == "Nessus SYN scanner":
            if var1 == "addr":
                var2.append(reporthost.get('name'))
            elif var1 == "port":
                var2.append(reportitem.get('port'))


def nessus_tlsscan_loopy(reporthost, tls_obs, tlsscan_addr, tlsscan_port,
                         tlsscan):
    """ Specific Nessus loop to afind all SSL / TLS related issues """

    for reportitem in reporthost.findall('ReportItem'):
        if int(reportitem.get('pluginID')) in tls_obs.keys():
            tlsscan_addr.append(
                reporthost.get('name') + ":" + reportitem.get('port'))
            obs_title = tls_obs.get(int(reportitem.get('pluginID')))
            if obs_title not in tlsscan_port:
                tlsscan_port.append(obs_title)
            if tlsscan_addr:
                tlsscan.append([tlsscan_addr[-1], tlsscan_port])


def nessus_x509scan_loopy(reporthost, x509_obs, x509scan_addr, x509scan_port,
                          x509scan):
    """ Specific Nessus loop to find all X.509 certificate issues """

    for reportitem in reporthost.findall('ReportItem'):
        if int(reportitem.get('pluginID')) in x509_obs.keys():
            x509scan_addr.append(
                reporthost.get('name') + ":" + reportitem.get('port'))
            obs_title = x509_obs.get(int(reportitem.get('pluginID')))
            if obs_title not in x509scan_port:
                x509scan_port.append(obs_title)
            if x509scan_addr:
                x509scan.append([x509scan_addr[-1], x509scan_port])


def nessus_httpscan_loopy(reporthost, http_obs, httpscan_addr, httpscan_port,
                          httpscan):
    """ Specific Nessus loop to find all HTTP response header issues """

    for reportitem in reporthost.findall('ReportItem'):
        if int(reportitem.get('pluginID')) in http_obs.keys():
            httpscan_addr.append(
                reporthost.get('name') + ":" + reportitem.get('port'))
            obs_title = http_obs.get(int(reportitem.get('pluginID')))
            if obs_title not in httpscan_port:
                httpscan_port.append(obs_title)
            if httpscan_addr:
                httpscan.append([httpscan_addr[-1], httpscan_port])


def nessus_parser(args, root, data_nessus, workbook):
    """ Nessus parser """

    autoclassify_file = pkg_resources.resource_string(
        __name__, '../data/nessus_autoclassify.yaml')
    autoclassify = yaml.load(autoclassify_file, Loader=yaml.FullLoader)

    tls_file = pkg_resources.resource_string(
        __name__, '../data/nessus_tls.yaml')
    tls_obs = yaml.load(tls_file, Loader=yaml.FullLoader)

    x509_file = pkg_resources.resource_string(
        __name__, '../data/nessus_x509.yaml')
    x509_obs = yaml.load(x509_file, Loader=yaml.FullLoader)

    http_file = pkg_resources.resource_string(
        __name__, '../data/nessus_http.yaml')
    http_obs = yaml.load(http_file, Loader=yaml.FullLoader)

    portscan = []
    tlsscan = []
    x509scan = []
    httpscan = []

    for element in root:
        for reporthost in element.findall('Report/ReportHost'):
            for reportitem in reporthost.findall('ReportItem'):
                if int(reportitem.get('severity')) >= args.nessus_min_severity:
                    data_nessus.append([
                        reporthost.get('name'),
                        reportitem.get('port'),
                        reportitem.get('pluginID'),
                        textwrap.fill(
                            reportitem.get('pluginName'),
                            width=args.nessus_plugin_name_width),
                        reportitem.findtext('plugin_output'),
                        reportitem.get('severity')
                    ])

            portscan_addr = []
            portscan_port = []
            nessus_portscan_loopy("addr", reporthost, portscan_addr)
            nessus_portscan_loopy("port", reporthost, portscan_port)
            if portscan_addr:
                portscan.append([portscan_addr[0], portscan_port])

            tlsscan_addr = []
            tlsscan_port = []
            nessus_tlsscan_loopy(
                reporthost, tls_obs, tlsscan_addr, tlsscan_port, tlsscan)

            x509scan_addr = []
            x509scan_port = []
            nessus_x509scan_loopy(
                reporthost, x509_obs, x509scan_addr, x509scan_port, x509scan)

            httpscan_addr = []
            httpscan_port = []
            nessus_httpscan_loopy(
                reporthost, http_obs, httpscan_addr, httpscan_port, httpscan)

    my_nessus_table = PrettyTable()
    csv_array = []
    header = ['host', 'port', 'plugin id', 'plugin name']
    if args.nessus_plugin_output:
        header.extend(['plugin output'])
    header.extend(['severity'])
    header.extend(['annotations'.ljust(args.annotation_width)])
    my_nessus_table.field_names = header
    my_nessus_table.align["host"] = "l"
    my_nessus_table.align["port"] = "l"
    my_nessus_table.align["plugin id"] = "l"
    my_nessus_table.align["plugin name"] = "l"
    my_nessus_table.align["plugin output"] = "l"
    my_nessus_table.align["annotations"] = "l"

    def sortf(data_nessus):
        """ Sort function """
        if args.nessus_sort_by == 'ip-address':
            sorted_result = sorted(data_nessus, key=lambda x: x[0])
        elif args.nessus_sort_by == 'port':
            sorted_result = sorted(data_nessus, key=lambda x: x[1])
        elif args.nessus_sort_by == 'plugin-id':
            sorted_result = sorted(data_nessus, key=lambda x: x[2])
        elif args.nessus_sort_by == 'plugin-name':
            sorted_result = sorted(data_nessus, key=lambda x: x[3])
        elif args.nessus_sort_by == 'severity':
            sorted_result = sorted(
                data_nessus, key=lambda x: x[4], reverse=True)
        return sorted_result

    for (host, port, plugin_id, plugin_name, severity,
         plugin_output) in sortf(data_nessus):
        row = [host, port, plugin_id, plugin_name, severity]
        if args.nessus_plugin_output:
            row.extend([plugin_output])
        if int(plugin_id) in autoclassify.keys():
            for key, value in autoclassify[int(plugin_id)].items():
                if key == "stdobs_title":
                    row.extend([value])
        else:
            row.extend(['X'])
        my_nessus_table.add_row(row)
        csv_array.append(row)

    ports = sorted(
        set([int(port) for _, open_ports in portscan for port in open_ports])
    )

    tls_observations = sorted(
        set([obs for _, all_obs in tlsscan for obs in all_obs])
    )

    x509_observations = sorted(
        set([obs for _, all_obs in x509scan for obs in all_obs])
    )

    http_observations = sorted(
        set([obs for _, all_obs in httpscan for obs in all_obs])
    )

    nessus_portscan_table = PrettyTable()
    portscan_csv_array = []
    portscan_header = ['ip address', ]
    portscan_header.extend(ports)
    nessus_portscan_table.field_names = portscan_header
    for ip_address, open_ports in portscan:
        row = [ip_address]
        row.extend('X' if str(port) in open_ports else '' for port in ports)
        nessus_portscan_table.add_row(row)
        portscan_csv_array.append(row)
    nessus_portscan_table.align["ip address"] = "l"

    nessus_tlsscan_table = PrettyTable()
    tlsscan_csv_array = []
    tlsscan_header = ['ip address', ]
    tlsscan_header.extend(tls_observations)
    nessus_tlsscan_table.field_names = tlsscan_header
    for ip_address, all_obs in tlsscan:
        row = [ip_address]
        row.extend(
            'X' if str(obs) in all_obs else '' for obs in tls_observations)
        nessus_tlsscan_table.add_row(row)
        tlsscan_csv_array.append(row)
    nessus_tlsscan_table.align["ip address"] = "l"

    nessus_x509scan_table = PrettyTable()
    x509scan_csv_array = []
    x509scan_header = ['ip address', ]
    x509scan_header.extend(x509_observations)
    nessus_x509scan_table.field_names = x509scan_header
    for ip_address, all_obs in x509scan:
        row = [ip_address]
        row.extend(
            'X' if str(obs) in all_obs else '' for obs in x509_observations)
        nessus_x509scan_table.add_row(row)
        x509scan_csv_array.append(row)
    nessus_x509scan_table.align["ip address"] = "l"

    nessus_httpscan_table = PrettyTable()
    httpscan_csv_array = []
    httpscan_header = ['ip address', ]
    httpscan_header.extend(http_observations)
    nessus_httpscan_table.field_names = httpscan_header
    for ip_address, all_obs in httpscan:
        row = [ip_address]
        row.extend(
            'X' if str(obs) in all_obs else '' for obs in http_observations)
        nessus_httpscan_table.add_row(row)
        httpscan_csv_array.append(row)
    nessus_httpscan_table.align["ip address"] = "l"

    if args.output_csv:
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            for row in csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_portscan.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in portscan_csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_tls.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in tlsscan_csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_x509.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in x509scan_csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_http.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in httpscan_csv_array:
                csvwriter.writerow(row)

    if args.output_xlsx:

        # Defining cell formats
        bold = workbook.add_format({'bold': True})
        bold.set_text_wrap()
        wrap = workbook.add_format()
        wrap.set_text_wrap()
        bad_cell = workbook.add_format()
        bad_cell.set_text_wrap()
        bad_cell.set_bg_color('#c00000')
        bad_cell.set_font_color('#ffffff')
        good_cell = workbook.add_format()
        good_cell.set_text_wrap()
        good_cell.set_bg_color('#046a38')
        good_cell.set_font_color('#ffffff')
        tls_bad_cell = workbook.add_format()

        # Dunno why this one doesn't work >:c
        tls_bad_cell.set_align('center')

        tls_bad_cell.set_bg_color('#c00000')
        tls_bad_cell.set_font_color('#ffffff')
        tls_bad_cell.set_border(1)
        tls_bad_cell.set_border_color('#ffffff')
        tls_good_cell = workbook.add_format()

        # Dunno why this one doesn't work >:c
        tls_good_cell.set_align('center')

        tls_good_cell.set_bg_color('#046a38')
        tls_good_cell.set_font_color('#ffffff')
        tls_good_cell.set_border(1)
        tls_good_cell.set_border_color('#ffffff')

        # Create all worksheets
        worksheet_summary = workbook.add_worksheet('Summary')
        worksheet_summary.write_rich_string(0, 0, bold, 'Summary')
        worksheet_critical = workbook.add_worksheet('Critical')
        worksheet_critical.set_tab_color('red')
        worksheet_high = workbook.add_worksheet('High')
        worksheet_high.set_tab_color('orange')
        worksheet_medium = workbook.add_worksheet('Medium')
        worksheet_medium.set_tab_color('yellow')
        worksheet_low = workbook.add_worksheet('Low')
        worksheet_low.set_tab_color('green')
        worksheet_info = workbook.add_worksheet('Info')
        worksheet_info.set_tab_color('blue')
        worksheet_portscan = workbook.add_worksheet('SYN')
        worksheet_portscan.set_tab_color('black')
        worksheet_portscan.set_column(0, 0, 15)
        worksheet_portscan.write_row(0, 0, portscan_header)
        worksheet_tlsscan = workbook.add_worksheet('TLS')
        worksheet_tlsscan.set_tab_color('black')
        worksheet_tlsscan.set_column(0, 0, 20)
        worksheet_tlsscan.write_row(0, 0, tlsscan_header)
        worksheet_x509scan = workbook.add_worksheet('X.509')
        worksheet_x509scan.set_tab_color('black')
        worksheet_x509scan.set_column(0, 0, 20)
        worksheet_x509scan.write_row(0, 0, x509scan_header)
        worksheet_httpscan = workbook.add_worksheet('HTTP')
        worksheet_httpscan.set_tab_color('black')
        worksheet_httpscan.set_column(0, 0, 20)
        worksheet_httpscan.write_row(0, 0, httpscan_header)

        # Set colums and row sizes for the observation worksheets
        observation_worksheets = [
            worksheet_critical,
            worksheet_high,
            worksheet_medium,
            worksheet_low,
            worksheet_info]
        for worksheet_select in observation_worksheets:
            worksheet_select.set_column(0, 0, 15)
            worksheet_select.set_column(1, 1, 8)
            worksheet_select.set_column(2, 2, 11)
            worksheet_select.set_column(3, 3, 50)
            if args.nessus_plugin_output:
                worksheet_select.set_column(4, 4, 50)
                worksheet_select.set_column(5, 5, 11)
                worksheet_select.set_column(6, 6, 30)
            else:
                worksheet_select.set_column(4, 4, 11)
                worksheet_select.set_column(5, 5, 30)

        # Fill observation worksheets
        col = 0
        row_critical = 0
        row_high = 0
        row_medium = 0
        row_low = 0
        row_info = 0
        for item in csv_array:
            if item[5] == '4':
                worksheet_selected = worksheet_critical
                row = row_critical
            elif item[5] == '3':
                worksheet_selected = worksheet_high
                row = row_high
            elif item[5] == '2':
                worksheet_selected = worksheet_medium
                row = row_medium
            elif item[5] == '1':
                worksheet_selected = worksheet_low
                row = row_low
            elif item[5] == '0':
                worksheet_selected = worksheet_info
                row = row_info
                if args.nessus_autoclassify:
                    format_cell = good_cell
            if int(item[2]) in autoclassify and args.nessus_autoclassify:
                format_cell = bad_cell
            elif not item[5] == '0':
                format_cell = wrap
            worksheet_selected.write_row(row, col, item, format_cell)
            worksheet_selected.set_row(row, 30)
            if item[5] == '4':
                row_critical += 1
            if item[5] == '3':
                row_high += 1
            if item[5] == '2':
                row_medium += 1
            if item[5] == '1':
                row_low += 1
            if item[5] == '0':
                row_info += 1
        if args.nessus_plugin_output:
            for worksheet_select in observation_worksheets:
                worksheet_select.add_table(0, 0, row - 1, 6, {
                    'style':
                    'Table Style Light 9',
                    'header_row': True,
                    'columns': [
                        {'header_format': bold, 'header': 'ip address'},
                        {'header_format': bold, 'header': 'port'},
                        {'header_format': bold, 'header': 'plugin id'},
                        {'header_format': bold, 'header': 'plugin name'},
                        {'header_format': bold, 'header': 'plugin output'},
                        {'header_format': bold, 'header': 'severity'},
                        {'header_format': bold, 'header': 'annotations'}
                    ]})
                worksheet_select.set_row(0, 30)
        else:
            for worksheet_select in observation_worksheets:
                worksheet_select.add_table(0, 1, row, 6, {
                    'header_row': False,
                    'columns': [
                        {'header_format': bold, 'header': 'ip address'},
                        {'header_format': bold, 'header': 'port'},
                        {'header_format': bold, 'header': 'plugin id'},
                        {'header_format': bold, 'header': 'plugin name'},
                        {'header_format': bold, 'header': 'annotations'},
                        {'header_format': bold, 'header': 'severity'}
                    ]})
                worksheet_select.set_row(0, 30)

        # Fill summary sheet
        worksheet_summary.set_row(0, 30)
        worksheet_summary.write(1, 0, 'Critical')
        worksheet_summary.write(1, 1, row_critical - 1)
        worksheet_summary.write(2, 0, 'High')
        worksheet_summary.write(2, 1, row_high - 1)
        worksheet_summary.write(3, 0, 'Medium')
        worksheet_summary.write(3, 1, row_medium - 1)
        worksheet_summary.write(4, 0, 'Low')
        worksheet_summary.write(4, 1, row_low - 1)
        worksheet_summary.write(5, 0, 'Info')
        worksheet_summary.write(5, 1, row_info - 1)

        # Fill portscan sheet
        xlsx_portscan_header = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in portscan_header]
        worksheet_portscan.add_table(
            0, 0, len(portscan_csv_array), len(portscan_csv_array[0]) - 1, {
                'data': portscan_csv_array,
                'style': 'Table Style Light 9',
                'header_row': True,
                'columns': xlsx_portscan_header
            })
        worksheet_portscan.freeze_panes(0, 1)

        # Fill TLS scan sheet
        xlsx_tlsscan_header = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in tlsscan_header]
        worksheet_tlsscan.add_table(
            0, 0, len(tlsscan_csv_array), len(tlsscan_csv_array[0]) - 1, {
                'data': tlsscan_csv_array,
                'style': 'Table Style Light 9',
                'header_row': True,
                'columns': xlsx_tlsscan_header
            })
        worksheet_tlsscan.set_row(0, 45)
        worksheet_tlsscan.set_column(1, len(xlsx_tlsscan_header) - 1, 11)
        worksheet_tlsscan.conditional_format(
            0, 1, len(tlsscan_csv_array), len(tlsscan_csv_array[0]) - 1, {
                'type': 'cell',
                'criteria': '==',
                'value': '"X"',
                'format': tls_bad_cell})
        worksheet_tlsscan.conditional_format(
            0, 1, len(tlsscan_csv_array), len(tlsscan_csv_array[0]) - 1, {
                'type': 'cell',
                'criteria': '==',
                'value': '""',
                'format': tls_good_cell})

        # Fill X.509 scan sheet
        xlsx_x509scan_header = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in x509scan_header]
        worksheet_x509scan.add_table(
            0, 0, len(x509scan_csv_array), len(x509scan_csv_array[0]) - 1, {
                'data': x509scan_csv_array,
                'style': 'Table Style Light 9',
                'header_row': True,
                'columns': xlsx_x509scan_header
            })
        worksheet_x509scan.set_row(0, 45)
        worksheet_x509scan.set_column(1, len(xlsx_x509scan_header) - 1, 11)
        worksheet_x509scan.conditional_format(
            0, 1, len(x509scan_csv_array), len(x509scan_csv_array[0]) - 1, {
                'type': 'cell',
                'criteria': '==',
                'value': '"X"',
                'format': tls_bad_cell})
        worksheet_x509scan.conditional_format(
            0, 1, len(x509scan_csv_array), len(x509scan_csv_array[0]) - 1, {
                'type': 'cell',
                'criteria': '==',
                'value': '""',
                'format': tls_good_cell})

        # Fill HTTP scan sheet
        xlsx_httpscan_header = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in httpscan_header]
        worksheet_httpscan.add_table(
            0, 0, len(httpscan_csv_array), len(httpscan_csv_array[0]) - 1, {
                'data': httpscan_csv_array,
                'style': 'Table Style Light 9',
                'header_row': True,
                'columns': xlsx_httpscan_header
            })
        worksheet_httpscan.set_row(0, 45)
        worksheet_httpscan.set_column(1, len(xlsx_httpscan_header) - 1, 11)
        worksheet_httpscan.conditional_format(
            0, 1, len(httpscan_csv_array), len(httpscan_csv_array[0]) - 1, {
                'type': 'cell',
                'criteria': '==',
                'value': '"X"',
                'format': tls_bad_cell})
        worksheet_httpscan.conditional_format(
            0, 1, len(httpscan_csv_array), len(httpscan_csv_array[0]) - 1, {
                'type': 'cell',
                'criteria': '==',
                'value': '""',
                'format': tls_good_cell})

    return my_nessus_table, nessus_portscan_table, nessus_tlsscan_table, \
        nessus_x509scan_table, nessus_httpscan_table, csv_array, header, \
        workbook

#!/usr/bin/env python3

""" sr2t Nmap parser"""

import csv
import os
from prettytable import PrettyTable


def nmap_loopy(var1, host, args, addr, var2):
    """
    Specific Nmap loop to only print the addresses that have the ports we want
    """

    for port in host.findall('ports/port'):
        if port.get('protocol') == args.nmap_protocol:
            portid = port.get('portid')
            for state in port.findall('state'):
                if state.get('state') == args.nmap_state:
                    if var1 == "address":
                        var2.append(addr)
                    elif var1 == "portid":
                        var2.append(portid)
                    else:
                        exit(1)


def nmap_parser(args, root, data_nmap, workbook):
    """ Nmap parser """

    for element in root:
        for host in element.findall('host'):
            list_addr = []
            list_portid = []
            address = host.find('address')
            addr = address.get('addr')
            nmap_loopy("address", host, args, addr, list_addr)
            nmap_loopy("portid", host, args, addr, list_portid)
            if list_addr:
                data_nmap.append([list_addr[0], list_portid])

    ports = sorted(
        set([int(port) for _, open_ports in data_nmap for port in open_ports])
    )

    my_nmap_table = PrettyTable()
    csv_array = []
    header = ['ip address', ]
    header.extend(ports)
    my_nmap_table.field_names = header
    for ip_address, open_ports in data_nmap:
        row = [ip_address]
        row.extend('X' if str(port) in open_ports else '' for port in ports)
        my_nmap_table.add_row(row)
        csv_array.append(row)
    my_nmap_table.field_names = header
    my_nmap_table.align["ip address"] = "l"

    if args.output_csv:
        with open(
            os.path.splitext(args.output_csv)[0] + "_nmap.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in csv_array:
                csvwriter.writerow(row)

    if args.output_xlsx:
        bold = workbook.add_format({'bold': True})
        bold.set_text_wrap()
        worksheet_nmap = workbook.add_worksheet('Nmap')
        worksheet_nmap.set_tab_color('purple')
        worksheet_nmap.set_column(0, 0, 15)
        xlsx_header = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in header]
        worksheet_nmap.add_table(
            0, 0, len(csv_array), len(csv_array[0]) - 1, {
                'data': csv_array,
                'style': 'Table Style Light 9',
                'header_row': True,
                'columns': xlsx_header
            })
        worksheet_nmap.freeze_panes(0, 1)

    return my_nmap_table, workbook

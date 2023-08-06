#!/usr/bin/env python3

""" sr2t Nmap parser"""

import csv
import os
from prettytable import PrettyTable


def nmap_loopy(var1, host, args, addr, var2, var3):
    """
    Specific Nmap loop to only print the addresses that have the ports we want
    """

    for port in host.findall('ports/port'):
        if port.get('protocol') == var3:
            portid = port.get('portid')
            for state in port.findall('state'):
                if state.get('state') == args.nmap_state:
                    if var1 == "address":
                        var2.append(addr)
                    elif var1 == "portid":
                        var2.append(portid)
                    else:
                        exit(1)


def nmap_parser(args, root, workbook):
    """ Nmap parser """

    data_nmap_tcp = []
    data_nmap_udp = []

    for element in root:
        for host in element.findall('host'):
            list_addr_tcp = []
            list_portid_tcp = []
            list_addr_udp = []
            list_portid_udp = []
            address = host.find('address')
            addr = address.get('addr')
            nmap_loopy("address", host, args, addr, list_addr_tcp, "tcp")
            nmap_loopy("portid", host, args, addr, list_portid_tcp, "tcp")
            nmap_loopy("address", host, args, addr, list_addr_udp, "udp")
            nmap_loopy("portid", host, args, addr, list_portid_udp, "udp")
            if list_addr_tcp:
                data_nmap_tcp.append([list_addr_tcp[0], list_portid_tcp])
            if list_addr_udp:
                data_nmap_udp.append([list_addr_udp[0], list_portid_udp])

    if data_nmap_tcp:
        tcp_ports = sorted(
            set([int(port) for _, open_ports in data_nmap_tcp for port in 
                open_ports])
        )
    if data_nmap_udp:
        udp_ports = sorted(
            set([int(port) for _, open_ports in data_nmap_udp for port in 
                open_ports])
        )

    if data_nmap_tcp:
        my_nmap_tcp_table = PrettyTable()
        csv_array_tcp = []
        header_tcp = ['ip address', ]
        header_tcp.extend(tcp_ports)
        my_nmap_tcp_table.field_names = header_tcp
        for ip_address, open_ports in data_nmap_tcp:
            row = [ip_address]
            row.extend('X' if str(port) in open_ports else '' for port in tcp_ports)
            my_nmap_tcp_table.add_row(row)
            csv_array_tcp.append(row)
        my_nmap_tcp_table.field_names = header_tcp
        my_nmap_tcp_table.align["ip address"] = "l"

    if data_nmap_udp:
        my_nmap_udp_table = PrettyTable()
        csv_array_udp = []
        header_udp = ['ip address', ]
        header_udp.extend(udp_ports)
        my_nmap_udp_table.field_names = header_udp
        for ip_address, open_ports in data_nmap_udp:
            row = [ip_address]
            row.extend('X' if str(port) in open_ports else '' for port in udp_ports)
            my_nmap_udp_table.add_row(row)
            csv_array_udp.append(row)
        my_nmap_udp_table.field_names = header_udp
        my_nmap_udp_table.align["ip address"] = "l"

    if args.output_csv:
        if data_nmap_tcp:
            with open(
                os.path.splitext(args.output_csv)[0] + "_nmap_tcp.csv", 'w'
            ) as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['ip address'] + tcp_ports)
                for row in csv_array_tcp:
                    csvwriter.writerow(row)
        if data_nmap_udp:
            with open(
                os.path.splitext(args.output_csv)[0] + "_nmap_udp.csv", 'w'
            ) as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['ip address'] + udp_ports)
                for row in csv_array_udp:
                    csvwriter.writerow(row)

    if args.output_xlsx:
        bold = workbook.add_format({'bold': True})
        bold.set_text_wrap()
        xlsx_header_tcp = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in header_tcp]
        xlsx_header_udp = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in header_udp]
        if data_nmap_tcp:
            worksheet_nmap_tcp = workbook.add_worksheet('Nmap TCP')
            worksheet_nmap_tcp.set_tab_color('purple')
            worksheet_nmap_tcp.set_column(0, 0, 15)
            worksheet_nmap_tcp.add_table(
                0, 0, len(csv_array_tcp), len(csv_array_tcp[0]) - 1, {
                    'data': csv_array_tcp,
                    'style': 'Table Style Light 9',
                    'header_row': True,
                    'columns': xlsx_header_tcp
                })
            worksheet_nmap_tcp.freeze_panes(0, 1)
        if data_nmap_udp:
            worksheet_nmap_udp = workbook.add_worksheet('Nmap UDP')
            worksheet_nmap_udp.set_tab_color('purple')
            worksheet_nmap_udp.set_column(0, 0, 15)
            worksheet_nmap_udp.add_table(
                0, 0, len(csv_array_udp), len(csv_array_udp[0]) - 1, {
                    'data': csv_array_udp,
                    'style': 'Table Style Light 9',
                    'header_row': True,
                    'columns': xlsx_header_udp
                })
            worksheet_nmap_udp.freeze_panes(0, 1)

    if not data_nmap_tcp:
        my_nmap_tcp_table = []
    if not data_nmap_udp:
        my_nmap_udp_table = []

    return my_nmap_tcp_table, my_nmap_udp_table, workbook

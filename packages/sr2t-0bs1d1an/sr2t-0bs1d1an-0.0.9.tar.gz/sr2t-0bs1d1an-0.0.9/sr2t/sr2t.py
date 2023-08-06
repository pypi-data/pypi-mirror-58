#!/usr/bin/env python3

""" sr2t """

import argparse
import csv
import json
import xml.etree.ElementTree as ET
import zipfile
import sr2t.parsers.dirble
import sr2t.parsers.fortify
import sr2t.parsers.nessus
import sr2t.parsers.nikto
import sr2t.parsers.nmap
import sr2t.parsers.testssl
# from pprint import pprint


def get_args():
    """ Get arguments """

    parser = argparse.ArgumentParser(
        description='Converting scanning reports to a tabular format')
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        '--nmap', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Nmap XML files.')
    input_group.add_argument(
        '--nessus', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Nessus XML files.')
    input_group.add_argument(
        '--nikto', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Nikto XML files.')
    input_group.add_argument(
        '--dirble', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Dirble XML files.')
    input_group.add_argument(
        '--testssl', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Testssl JSON files.')
    input_group.add_argument(
        '--fortify', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) HP Fortify FPR files.')
    parser.add_argument(
        '--nmap-protocol', default="tcp",
        help='Specify the desired protocol to filter (e.g. tcp|udp).')
    parser.add_argument(
        '--nmap-state', default="open",
        help='Specify the desired state to filter (e.g. open|filtered).')
    parser.add_argument(
        '--no-nessus-autoclassify', default='store_true', action='store_false',
        dest='nessus_autoclassify', help='Specify to not autoclassify results.'
        )
    parser.add_argument(
        '--nessus-min-severity', default=0, type=int,
        help='Specify the minimum severity to output (e.g. 1).')
    parser.add_argument(
        '--no-nessus-plugin-output', default='store_true',
        action='store_false', dest='nessus_plugin_output',
        help='Specify to not include Nessus plugin output.')
    parser.add_argument(
        '--nessus-plugin-name-width', default=80, type=int,
        help='Specify the width of the pluginid column (e.g. 30).')
    parser.add_argument(
        '--nessus-sort-by', default='plugin-id',
        help='Specify to sort output by ip-address, port, plugin-id, \
            plugin-name or severity.')
    parser.add_argument(
        '--nikto-description-width', default=80, type=int,
        help='Specify the width of the description column (e.g. 30).')
    parser.add_argument(
        '--fortify-details', action='store_true',
        help='Specify to include the Fortify abstracts, explanations and \
            recommendations for each vulnerability.')
    parser.add_argument(
        '--annotation-width', default=1, type=int,
        help='Specify the width of the annotation column (e.g. 30).')
    parser.add_argument(
        '-oC', '--output-csv',
        help='Specify the output CSV file (e.g. output.csv).')
    parser.add_argument(
        '-oT', '--output-txt',
        help='Specify the output TXT file (e.g. output.txt).')
    parser.add_argument(
        '-oX', '--output-xlsx',
        help='Specify the output XLSX file (e.g. output.xlsx). Only for \
            Nessus at the moment')
    parser.add_argument(
        '-oA', '--output-all',
        help='Specify the output basename to output to all formats (e.g. \
            output).')
    return parser.parse_args()


def main():
    """ Main function """

    args = get_args()

    data = []

    # needs to be known before eval
    nessus_portscan_table = ''
    nessus_tlsscan_table = ''

    if args.output_all:
        args.output_csv = args.output_all + ".csv"
        args.output_txt = args.output_all + ".txt"
        args.output_xlsx = args.output_all + ".xlsx"

    if args.nmap:
        root = []
        for file in args.nmap:
            root.append(ET.parse(file).getroot())
        my_table = sr2t.parsers.nmap.nmap_parser(args, root, data)
    elif args.nessus:
        root = []
        for file in args.nessus:
            root.append(ET.parse(file).getroot())
        my_table, nessus_portscan_table, nessus_tlsscan_table, \
            nessus_x509scan_table, nessus_httpscan_table, csv_array, \
            header = sr2t.parsers.nessus.nessus_parser(args, root, data)
    elif args.nikto:
        root = []
        for file in args.nikto:
            root.append(ET.parse(file).getroot())
        my_table, csv_array, header = \
            sr2t.parsers.nikto.nikto_parser(args, root, data)
    elif args.dirble:
        root = []
        for file in args.dirble:
            root.append(ET.parse(file).getroot())
        my_table, csv_array, header = sr2t.parsers.dirble.dirble_parser(
            args, root, data)
    elif args.testssl:
        root = []
        for file in args.testssl:
            root.append(json.load(file))
        my_table = sr2t.parsers.testssl.testssl_parser(args, root, data)
    elif args.fortify:
        root = []
        for fprfile in args.fortify:
            zfpr = zipfile.ZipFile(fprfile.name)
            fvdl = zfpr.open('audit.fvdl')
            root.append(ET.parse(fvdl).getroot())
        my_table, csv_array, header = sr2t.parsers.fortify.fortify_parser(
            args, root, data)

    if not args.nmap and not args.nessus and not args.testssl:
        if args.output_csv:
            with open(args.output_csv, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(header)
                for row in csv_array:
                    csvwriter.writerow(row)

    if args.output_txt:
        with open(args.output_txt, 'w') as txtfile:
            print(my_table, file=txtfile)

    if not args.output_csv and not args.output_txt and not args.output_xlsx \
       and not args.output_all:
        print(my_table)
        if args.nessus:
            if nessus_portscan_table:
                print("\n")
                print(nessus_portscan_table)
            if nessus_tlsscan_table:
                print("\n")
                print(nessus_tlsscan_table)
            if nessus_x509scan_table:
                print("\n")
                print(nessus_x509scan_table)
            if nessus_httpscan_table:
                print("\n")
                print(nessus_httpscan_table)


if __name__ == '__main__':
    main()

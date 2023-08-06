#!/usr/bin/env python3

""" sr2t Dirble parser"""

import csv
import xlsxwriter
from prettytable import PrettyTable


def testssl_loopy_severity(data, subelement, id_name, value, header):
    """
    Loop through all files, match specific value in "severity" field, and print
    a custom header
    """

    if subelement['id'] == id_name and subelement['severity'] != value:
        if subelement['id'] == id_name and subelement['severity'] != "OK":
            if not data:
                data.append([subelement['ip'], subelement['port'], [header]])
            elif data:
                for host, port, finding in data:
                    if (subelement['ip'] in host) and \
                       (subelement['port'] in port):
                        finding.append(header)
                        return
                data.append([subelement['ip'], subelement['port'], [header]])


def testssl_loopy_finding(data, subelement, id_name, text, header):
    """
    Loop through all files, match specific text in "finding" field, and print a
    custom header
    """

    if subelement['id'] == "TLS1" and "not offered" in subelement['finding']:

        # Dirty hack to filter out TLS1 if not offered - any ideas?
        return

    if subelement['id'] == "TLS1_1" and "not offered" in subelement['finding']:

        # Dirty hack to filter out TLS1_1 if not offered - any ideas?
        return

    if subelement['id'] == id_name and text in subelement['finding']:
        if (subelement['id'] == id_name and
                subelement['severity'] != "OK") or \
           (id_name == "cert_commonName"):
            if not data:
                data.append([subelement['ip'], subelement['port'], [header]])
            elif data:
                for host, port, finding in data:
                    if (subelement['ip'] in host) and \
                       (subelement['port'] in port):
                        finding.append(header)
                        return
                data.append([subelement['ip'], subelement['port'], [header]])


def testssl_parser(args, root, data):
    """ Testssl parser """

    for element in root:
        for subelement in element:
            testssl_loopy_severity(
                data, subelement, "ALPN_HTTP2", "OK", "No HTTP/2")
            testssl_loopy_severity(
                data, subelement, "BEAST", "OK", "BEAST")
            testssl_loopy_severity(
                data, subelement, "BREACH", "OK", "BREACH")
            testssl_loopy_severity(
                data, subelement, "CRIME_TLS", "OK", "CRIME")
            testssl_loopy_severity(
                data, subelement, "CCS", "OK", "CCS")
            testssl_loopy_finding(
                data, subelement, "DNS_CAArecord", "--", "No CAA RR")
            testssl_loopy_severity(
                data, subelement, "DROWN", "OK", "DROWN")
            testssl_loopy_severity(
                data, subelement, "FREAK", "OK", "FREAK")
            testssl_loopy_severity(
                data, subelement, "HSTS", "OK", "No HSTS")
            testssl_loopy_severity(
                data, subelement, "LOGJAM", "OK", "LOGJAM")
            testssl_loopy_severity(
                data, subelement, "LUCKY13", "OK", "LUCKY13")
            testssl_loopy_finding(
                data, subelement, "OCSP_stapling", "not offered",
                "No OCSP Stapling")
            testssl_loopy_severity(
                data, subelement, "PFS", "OK", "No PFS")
            testssl_loopy_severity(
                data, subelement, "RC4", "OK", "RC4")
            testssl_loopy_severity(
                data, subelement, "POODLE_SSL", "OK", "POODLE")
            testssl_loopy_severity(
                data, subelement, "ROBOT", "OK", "ROBOT")
            testssl_loopy_severity(
                data, subelement, "SSLv2", "OK", "SSLv2")
            testssl_loopy_severity(
                data, subelement, "SSLv3", "OK", "SSLv3")
            testssl_loopy_severity(
                data, subelement, "SWEET32", "OK", "SWEET32")
            testssl_loopy_finding(
                data, subelement, "TLS1", "offered", "TLSv1.0")
            testssl_loopy_finding(
                data, subelement, "TLS1_1", "offered", "TLSv1.1")
            testssl_loopy_finding(
                data, subelement, "TLS1_2", "not offered", "No TLSv1.2")
            testssl_loopy_finding(
                data, subelement, "TLS1_3", "not offered", "No TLSv1.3")
            testssl_loopy_severity(
                data, subelement, "cert_commonName", "OK", "Incorrect CN")
            testssl_loopy_finding(
                data, subelement, "cert_commonName", "*", "Wildcard")
            testssl_loopy_severity(
                data, subelement, "cert_caIssuers", "INFO", "No trusted CA")
            testssl_loopy_finding(
                data, subelement, "cert_chain_of_trust", "self signed",
                "Self signed")
            testssl_loopy_severity(
                data, subelement, "cert_expirationStatus", "OK",
                "Expired cert")
            testssl_loopy_severity(
                data, subelement, "cert_keySize", "INFO", "Weak cert keysize")
            testssl_loopy_finding(
                data, subelement, "cert_mustStapleExtension", "--",
                "No OCSP Must-Staple")
            testssl_loopy_finding(
                data, subelement, "cert_revocation",
                "Neither CRL nor OCSP URI provided", "No revocation checking")
            testssl_loopy_severity(
                data, subelement, "cert_signatureAlgorithm", "OK",
                "Weak cert signature")
            testssl_loopy_severity(
                data, subelement, "cert_subjectAltName", "INFO", "Missing SAN")
            testssl_loopy_finding(
                data, subelement, "fallback_SCSV", "offered",
                "TLS_FALLBACK_SCSV")
            testssl_loopy_severity(
                data, subelement, "heartbleed", "OK", "Heartbleed")
            testssl_loopy_severity(
                data, subelement, "ticketbleed", "OK", "Ticketbleed")
            testssl_loopy_severity(
                data, subelement, "cipherlist_aNULL", "OK", "Anonymous DH")
            testssl_loopy_severity(
                data, subelement, "secure_client_renego", "OK",
                "Insecure client renegotiation")
            testssl_loopy_severity(
                data, subelement, "secure_renego", "OK",
                "Insecure renegotiation")

    vulns = sorted(
        set([vuln for _, _, found_vuln in data for vuln in found_vuln]))

    my_table = PrettyTable()
    csv_array = []
    header = ['ip address', 'port']
    header.extend(vulns)
    my_table.field_names = header
    for host, port, found_vuln in data:
        row = [host, port]
        row.extend('X' if str(vuln) in found_vuln else '' for vuln in vulns)
        my_table.add_row(row)
        csv_array.append(row)
    my_table.align["ip address"] = "l"
    my_table.align["port"] = "l"

    if args.output_csv:
        with open(args.output_csv, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['ip address'] + ['port'] + vulns)
            for row in csv_array:
                csvwriter.writerow(row)

    if args.output_xlsx:
        workbook = xlsxwriter.Workbook(args.output_xlsx)
        bold = workbook.add_format({'bold': True})
        bold.set_text_wrap()
        worksheet_testssl = workbook.add_worksheet('Testssl')
        worksheet_testssl.set_tab_color('green')
        worksheet_testssl.set_column(0, 0, 30)
        tls_bad_cell = workbook.add_format()

        # Dunno why this one doesn't work >:c
        tls_bad_cell.set_align('center')

        tls_bad_cell.set_bg_color('#c00000')
        tls_bad_cell.set_font_color('#c00000')
        tls_bad_cell.set_border(1)
        tls_bad_cell.set_border_color('#ffffff')
        tls_good_cell = workbook.add_format()

        # Dunno why this one doesn't work >:c
        tls_good_cell.set_align('center')

        tls_good_cell.set_bg_color('#046a38')
        tls_good_cell.set_font_color('#ffffff')
        tls_good_cell.set_border(1)
        tls_good_cell.set_border_color('#ffffff')

        xlsx_header = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in header]
        worksheet_testssl.add_table(
            0, 0, len(csv_array), len(csv_array[0]) - 1, {
                'data': csv_array,
                'style': 'Table Style Light 9',
                'header_row': True,
                'columns': xlsx_header
            })
        worksheet_testssl.set_row(0, 45)
        worksheet_testssl.set_column(1, len(xlsx_header) - 1, 11)
        worksheet_testssl.conditional_format(
            0, 1, len(csv_array), len(csv_array[0]) - 1, {
                'type': 'cell',
                'criteria': '==',
                'value': '"X"',
                'format': tls_bad_cell})
        worksheet_testssl.conditional_format(
            0, 1, len(csv_array), len(csv_array[0]) - 1, {
                'type': 'cell',
                'criteria': '==',
                'value': '""',
                'format': tls_good_cell})
        worksheet_testssl.freeze_panes(0, 1)

    return my_table

[![pipeline status](https://gitlab.com/0bs1d1an/sr2t/badges/master/pipeline.svg)](https://gitlab.com/0bs1d1an/sr2t/commits/master)

# Scanning reports to tabular (sr2t)

This tool takes a scanning tool's output file, and converts it to a tabular format (CSV, XLSX, or ASCII table).
This tool can process output from the following tools:

1. Nmap (XML);
2. Nessus (XML);
3. Nikto (XML);
4. Dirble (XML);
5. Testssl (JSON);
6. Fortify (FPR).

## Rationale

This tool can offer a human-readable, tabular format which you can tie to any observations you have drafted in your report.
Why?
Because then your reviewers can then tell that you, the pentester, investigated all found open ports, and looked at all scanning reports.

## Dependencies

1. argparse (dev-python/argparse);
2. prettytable (dev-python/prettytable);
3. python (dev-lang/python);
4. xlsxwriter (dev-python/xlsxwriter).

## Install

Using Pip:

`pip install --user sr2t-0bs1d1an`

## Usage

You can use sr2t in two ways:

* When installed as package, call the installed script: `sr2t --help`.
* When Git cloned, call the script directly from the root of the Git
repository: `python -m sr2t.sr2t --help`

```
$ sr2t --help
usage: sr2t [-h]
            (--nmap NMAP [NMAP ...] | --nessus NESSUS [NESSUS ...] | --nikto NIKTO [NIKTO ...] | --dirble DIRBLE [DIRBLE ...] | --testssl TESTSSL [TESTSSL ...] | --fortify FORTIFY [FORTIFY ...])
            [--nmap-protocol NMAP_PROTOCOL] [--nmap-state NMAP_STATE]
            [--no-nessus-autoclassify]
            [--nessus-min-severity NESSUS_MIN_SEVERITY]
            [--no-nessus-plugin-output]
            [--nessus-plugin-name-width NESSUS_PLUGIN_NAME_WIDTH]
            [--nessus-sort-by NESSUS_SORT_BY]
            [--nikto-description-width NIKTO_DESCRIPTION_WIDTH]
            [--fortify-details] [--annotation-width ANNOTATION_WIDTH]
            [-oC OUTPUT_CSV] [-oT OUTPUT_TXT] [-oX OUTPUT_XLSX]
            [-oA OUTPUT_ALL]

Converting scanning reports to a tabular format

optional arguments:
  -h, --help            show this help message and exit
  --nmap NMAP [NMAP ...]
                        Specify (multiple) Nmap XML files.
  --nessus NESSUS [NESSUS ...]
                        Specify (multiple) Nessus XML files.
  --nikto NIKTO [NIKTO ...]
                        Specify (multiple) Nikto XML files.
  --dirble DIRBLE [DIRBLE ...]
                        Specify (multiple) Dirble XML files.
  --testssl TESTSSL [TESTSSL ...]
                        Specify (multiple) Testssl JSON files.
  --fortify FORTIFY [FORTIFY ...]
                        Specify (multiple) HP Fortify FPR files.
  --nmap-protocol NMAP_PROTOCOL
                        Specify the desired protocol to filter (e.g. tcp|udp).
  --nmap-state NMAP_STATE
                        Specify the desired state to filter (e.g.
                        open|filtered).
  --no-nessus-autoclassify
                        Specify to not autoclassify results.
  --nessus-min-severity NESSUS_MIN_SEVERITY
                        Specify the minimum severity to output (e.g. 1).
  --no-nessus-plugin-output
                        Specify to not include Nessus plugin output.
  --nessus-plugin-name-width NESSUS_PLUGIN_NAME_WIDTH
                        Specify the width of the pluginid column (e.g. 30).
  --nessus-sort-by NESSUS_SORT_BY
                        Specify to sort output by ip-address, port, plugin-id,
                        plugin-name or severity.
  --nikto-description-width NIKTO_DESCRIPTION_WIDTH
                        Specify the width of the description column (e.g. 30).
  --fortify-details     Specify to include the Fortify abstracts, explanations
                        and recommendations for each vulnerability.
  --annotation-width ANNOTATION_WIDTH
                        Specify the width of the annotation column (e.g. 30).
  -oC OUTPUT_CSV, --output-csv OUTPUT_CSV
                        Specify the output CSV file (e.g. output.csv).
  -oT OUTPUT_TXT, --output-txt OUTPUT_TXT
                        Specify the output TXT file (e.g. output.txt).
  -oX OUTPUT_XLSX, --output-xlsx OUTPUT_XLSX
                        Specify the output XLSX file (e.g. output.xlsx). Only
                        for Nessus at the moment
  -oA OUTPUT_ALL, --output-all OUTPUT_ALL
                        Specify the output basename to output to all formats
                        (e.g. output).
```

## Example

A few examples

### Nmap

To produce an XLSX format:

```
$ sr2t --nmap example/nmap.xml -oX example/nmap.xlsx
```

![Nmap XLSX](example/nmap-xlsx.png)

To produce an ASCII tabular format to stdout:

```
$ sr2t --nmap example/nmap/nmap.xml
+-----------------+----+----+----+-----+-----+-----+-----+------+------+------+
|                 | 53 | 80 | 88 | 135 | 139 | 389 | 445 | 3389 | 5800 | 5900 |
+-----------------+----+----+----+-----+-----+-----+-----+------+------+------+
| 192.168.23.78   | X  |    | X  |  X  |  X  |  X  |  X  |  X   |      |      |
| 192.168.27.243  |    |    |    |  X  |  X  |     |  X  |  X   |  X   |  X   |
| 192.168.99.164  |    |    |    |  X  |  X  |     |  X  |  X   |  X   |  X   |
| 192.168.228.211 |    | X  |    |     |     |     |     |      |      |      |
| 192.168.171.74  |    |    |    |  X  |  X  |     |  X  |  X   |  X   |  X   |
+-----------------+----+----+----+-----+-----+-----+-----+------+------+------+
```

Or to output a CSV file:

```
$ sr2t --nmap example/nmap/nmap.xml -oC example/nmap/output.csv
$ cat example/nmap/output.csv
,53,80,88,135,139,389,445,3389,5800,5900
192.168.23.78,X,,X,X,X,X,X,X,,
192.168.27.243,,,,X,X,,X,X,X,X
192.168.99.164,,,,X,X,,X,X,X,X
192.168.228.211,,X,,,,,,,,
192.168.171.74,,,,X,X,,X,X,X,X
```

### Nessus

To produce an XLSX format:

```
$ sr2t --nessus report.nessus --no-nessus-autoclassify -oX nessus.xlsx
```

![Nessus XLSX Critical](example/nessus-xlsx-critical.png)

![Nessus XLSX Portscan](example/nessus-xlsx-portscan.png)

![Nessus XLSX TLS](example/nessus-xlsx-tls.png)

![Nessus XLSX X.509](example/nessus-xlsx-x509.png)

To produce an ASCII tabular format to stdout:

```
$ sr2t --nessus example.nessus
+---------------+-------+-----------+-----------------------------------------------------------------------------+----------+-------------+
|       host    |  port | plugin id |                                 plugin name                                 | severity | annotations |
+---------------+-------+-----------+-----------------------------------------------------------------------------+----------+-------------+
| 192.168.142.4 | 3389  |   42873   | SSL Medium Strength Cipher Suites Supported (SWEET32)                       |    2     |      X      |
| 192.168.142.4 | 443   |   42873   | SSL Medium Strength Cipher Suites Supported (SWEET32)                       |    2     |      X      |
| 192.168.142.4 | 3389  |   18405   | Microsoft Windows Remote Desktop Protocol Server Man-in-the-Middle Weakness |    2     |      X      |
| 192.168.142.4 | 3389  |   30218   | Terminal Services Encryption Level is not FIPS-140 Compliant                |    1     |      X      |
| 192.168.142.4 | 3389  |   57690   | Terminal Services Encryption Level is Medium or Low                         |    2     |      X      |
| 192.168.142.4 | 3389  |   58453   | Terminal Services Doesn't Use Network Level Authentication (NLA) Only       |    2     |      X      |
| 192.168.142.4 | 3389  |   45411   | SSL Certificate with Wrong Hostname                                         |    2     |      X      |
| 192.168.142.4 | 443   |   45411   | SSL Certificate with Wrong Hostname                                         |    2     |      X      |
| 192.168.142.4 | 3389  |   35291   | SSL Certificate Signed Using Weak Hashing Algorithm                         |    2     |      X      |
| 192.168.142.4 | 3389  |   57582   | SSL Self-Signed Certificate                                                 |    2     |      X      |
| 192.168.142.4 | 3389  |   51192   | SSL Certificate Cannot Be Trusted                                           |    2     |      X      |
| 192.168.142.2 | 3389  |   42873   | SSL Medium Strength Cipher Suites Supported (SWEET32)                       |    2     |      X      |
| 192.168.142.2 | 443   |   42873   | SSL Medium Strength Cipher Suites Supported (SWEET32)                       |    2     |      X      |
| 192.168.142.2 | 3389  |   18405   | Microsoft Windows Remote Desktop Protocol Server Man-in-the-Middle Weakness |    2     |      X      |
| 192.168.142.2 | 3389  |   30218   | Terminal Services Encryption Level is not FIPS-140 Compliant                |    1     |      X      |
| 192.168.142.2 | 3389  |   57690   | Terminal Services Encryption Level is Medium or Low                         |    2     |      X      |
| 192.168.142.2 | 3389  |   58453   | Terminal Services Doesn't Use Network Level Authentication (NLA) Only       |    2     |      X      |
| 192.168.142.2 | 3389  |   45411   | SSL Certificate with Wrong Hostname                                         |    2     |      X      |
| 192.168.142.2 | 443   |   45411   | SSL Certificate with Wrong Hostname                                         |    2     |      X      |
| 192.168.142.2 | 3389  |   35291   | SSL Certificate Signed Using Weak Hashing Algorithm                         |    2     |      X      |
| 192.168.142.2 | 3389  |   57582   | SSL Self-Signed Certificate                                                 |    2     |      X      |
| 192.168.142.2 | 3389  |   51192   | SSL Certificate Cannot Be Trusted                                           |    2     |      X      |
| 192.168.142.2 | 445   |   57608   | SMB Signing not required                                                    |    2     |      X      |
+---------------+-------+-----------+-----------------------------------------------------------------------------+----------+-------------+
```

Or to output a CSV file:

```
$ sr2t --nessus --nessus-severity 1 example.nessus -oC example.csv
$ cat example.csv
host,port,plugin id,plugin name,severity,annotations
192.168.142.4,3389,42873,SSL Medium Strength Cipher Suites Supported (SWEET32),2,X
192.168.142.4,443,42873,SSL Medium Strength Cipher Suites Supported (SWEET32),2,X
192.168.142.4,3389,18405,Microsoft Windows Remote Desktop Protocol Server Man-in-the-Middle Weakness,2,X
192.168.142.4,3389,30218,Terminal Services Encryption Level is not FIPS-140 Compliant,1,X
192.168.142.4,3389,57690,Terminal Services Encryption Level is Medium or Low,2,X
192.168.142.4,3389,58453,Terminal Services Doesn't Use Network Level Authentication (NLA) Only,2,X
192.168.142.4,3389,45411,SSL Certificate with Wrong Hostname,2,X
192.168.142.4,443,45411,SSL Certificate with Wrong Hostname,2,X
192.168.142.4,3389,35291,SSL Certificate Signed Using Weak Hashing Algorithm,2,X
192.168.142.4,3389,57582,SSL Self-Signed Certificate,2,X
192.168.142.4,3389,51192,SSL Certificate Cannot Be Trusted,2,X
192.168.142.2,3389,42873,SSL Medium Strength Cipher Suites Supported (SWEET32),2,X
192.168.142.2,443,42873,SSL Medium Strength Cipher Suites Supported (SWEET32),2,X
192.168.142.2,3389,18405,Microsoft Windows Remote Desktop Protocol Server Man-in-the-Middle Weakness,2,X
192.168.142.2,3389,30218,Terminal Services Encryption Level is not FIPS-140 Compliant,1,X
192.168.142.2,3389,57690,Terminal Services Encryption Level is Medium or Low,2,X
192.168.142.2,3389,58453,Terminal Services Doesn't Use Network Level Authentication (NLA) Only,2,X
192.168.142.2,3389,45411,SSL Certificate with Wrong Hostname,2,X
192.168.142.2,443,45411,SSL Certificate with Wrong Hostname,2,X
192.168.142.2,3389,35291,SSL Certificate Signed Using Weak Hashing Algorithm,2,X
192.168.142.2,3389,57582,SSL Self-Signed Certificate,2,X
192.168.142.2,3389,51192,SSL Certificate Cannot Be Trusted,2,X
192.168.142.2,445,57608,SMB Signing not required,2,X
```

### Nikto

To produce an XLSX format:

```
$ sr2t --nikto example/nikto.xml -oX example/nikto.xlsx
```

![Nikto XLSX](example/nikto-xlsx.png)

To produce an ASCII tabular format to stdout:

```
$ sr2t --nikto example.xml
+----------------+-----------------+-------------+----------------------------------------------------------------------------------+-------------+
| target ip      | target hostname | target port | description                                                                      | annotations |
+----------------+-----------------+-------------+----------------------------------------------------------------------------------+-------------+
| 192.168.178.10 | 192.168.178.10  | 80          | The anti-clickjacking X-Frame-Options header is not present.                     |      X      |
| 192.168.178.10 | 192.168.178.10  | 80          | The X-XSS-Protection header is not defined. This header can hint to the user     |      X      |
|                |                 |             | agent to protect against some forms of XSS                                       |             |
| 192.168.178.10 | 192.168.178.10  | 80          | The X-Content-Type-Options header is not set. This could allow the user agent to |      X      |
|                |                 |             | render the content of the site in a different fashion to the MIME type           |             |
+----------------+-----------------+-------------+----------------------------------------------------------------------------------+-------------+
```

Or to output a CSV file:

```
$ sr2t --nikto --nikto-description-width=9999 example.xml -oC example.csv
$ cat example.csv
target ip,target hostname,target port,description,annotations
192.168.178.10,192.168.178.10,80,The anti-clickjacking X-Frame-Options header is not present.,X
192.168.178.10,192.168.178.10,80,"The X-XSS-Protection header is not defined. This header can hint to the user
agent to protect against some forms of XSS",X
192.168.178.10,192.168.178.10,80,"The X-Content-Type-Options header is not set. This could allow the user agent to
render the content of the site in a different fashion to the MIME type",X
```

### Dirble

To produce an XLSX format:

```
$ sr2t --dirble example/dirble.xml -oX example/dirble.xlsx
```

![Dirble XLSX](example/dirble-xlsx.png)

To produce an ASCII tabular format to stdout:

```
$ sr2t --dirble example/dirble.xml
+-----------------------------------+------+-------------+--------------+-------------+---------------------+--------------+-------------+
| url                               | code | content len | is directory | is listable | found from listable | redirect url | annotations |
+-----------------------------------+------+-------------+--------------+-------------+---------------------+--------------+-------------+
| http://example.org/flv            | 0    | 0           | false        | false       | false               |              |      X      |
| http://example.org/hire           | 0    | 0           | false        | false       | false               |              |      X      |
| http://example.org/phpSQLiteAdmin | 0    | 0           | false        | false       | false               |              |      X      |
| http://example.org/print_order    | 0    | 0           | false        | false       | false               |              |      X      |
| http://example.org/putty          | 0    | 0           | false        | false       | false               |              |      X      |
| http://example.org/receipts       | 0    | 0           | false        | false       | false               |              |      X      |
+-----------------------------------+------+-------------+--------------+-------------+---------------------+--------------+-------------+
```

Or to output a CSV file:

```
$ sr2t --dirble example/dirble.xml -oC example/dirble.csv
$ cat example.org.csv
url,code,content len,is directory,is listable,found from listable,redirect url,annotations
http://example.org/flv,0,0,false,false,false,,X
http://example.org/hire,0,0,false,false,false,,X
http://example.org/phpSQLiteAdmin,0,0,false,false,false,,X
http://example.org/print_order,0,0,false,false,false,,X
http://example.org/putty,0,0,false,false,false,,X
http://example.org/receipts,0,0,false,false,false,,X

```

### Testssl

To produce an XLSX format:

```
$ sr2t --testssl example/testssl.xml -oX example/testssl.xlsx
```

![Testssl XLSX](example/testssl-xlsx.png)

To produce an ASCII tabular format to stdout:

```
$ sr2t --testssl example/testssl.json
+-----------------------------------+------+--------+---------+--------+------------+-----+---------+---------+----------+
| ip address                        | port | BREACH | No HSTS | No PFS | No TLSv1.3 | RC4 | TLSv1.0 | TLSv1.1 | Wildcard |
+-----------------------------------+------+--------+---------+--------+------------+-----+---------+---------+----------+
| rc4-md5.badssl.com/104.154.89.105 | 443  |   X    |    X    |   X    |     X      |  X  |    X    |    X    |    X     |
+-----------------------------------+------+--------+---------+--------+------------+-----+---------+---------+----------+
```

Or to output a CSV file:

```
$ sr2t --testssl example/testssl.json -oC example/testssl.csv
$ cat example.csv
ip address,port,BREACH,No HSTS,No PFS,No TLSv1.3,RC4,TLSv1.0,TLSv1.1,Wildcard
rc4-md5.badssl.com/104.154.89.105,443,X,X,X,X,X,X,X,X
```

### Fortify

To produce an XLSX format:

```
$ sr2t --testssl fortify.fpr -oX fortify.xlsx
```

![Fortify XLSX](example/fortify-xlsx.png)

To produce an ASCII tabular format to stdout:

```
$ sr2t --fortify example.fpr
+--------------------------+-----------------------+-------------------------------+----------+------------+-------------+
|                          |          type         |            subtype            | severity | confidence | annotations |
+--------------------------+-----------------------+-------------------------------+----------+------------+-------------+
| example1/web.xml:135:135 | J2EE Misconfiguration | Insecure Transport            |   3.0    |    5.0     |      X      |
| example2/web.xml:150:150 | J2EE Misconfiguration | Insecure Transport            |   3.0    |    5.0     |      X      |
| example3/web.xml:109:109 | J2EE Misconfiguration | Incomplete Error Handling     |   3.0    |    5.0     |      X      |
| example4/web.xml:108:108 | J2EE Misconfiguration | Incomplete Error Handling     |   3.0    |    5.0     |      X      |
| example5/web.xml:166:166 | J2EE Misconfiguration | Insecure Transport            |   3.0    |    5.0     |      X      |
| example6/web.xml:2:2     | J2EE Misconfiguration | Excessive Session Timeout     |   3.0    |    5.0     |      X      |
| example7/web.xml:162:162 | J2EE Misconfiguration | Missing Authentication Method |   3.0    |    5.0     |      X      |
+--------------------------+-----------------------+-------------------------------+----------+------------+-------------+
```

Or to output a CSV file:

```
$ sr2t --fortify example.fpr -oC example.csv
$ cat example.csv
,type,subtype,severity,confidence,annotations
example1/web.xml:135:135,J2EE Misconfiguration,Insecure Transport,3.0,5.0,X
example2/web.xml:150:150,J2EE Misconfiguration,Insecure Transport,3.0,5.0,X
example3/web.xml:109:109,J2EE Misconfiguration,Incomplete Error Handling,3.0,5.0,X
example4/web.xml:108:108,J2EE Misconfiguration,Incomplete Error Handling,3.0,5.0,X
example5/web.xml:166:166,J2EE Misconfiguration,Insecure Transport,3.0,5.0,X
example6/web.xml:2:2,J2EE Misconfiguration,Excessive Session Timeout,3.0,5.0,X
example7/web.xml:162:162,J2EE Misconfiguration,Missing Authentication Method,3.0,5.0,X
```

## To do

1. Figure out a way, if at all useful, to print more details (software versions; Nmap script output).
2. Add more useful parsers?

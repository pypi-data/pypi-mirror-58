[![CircleCI](https://circleci.com/gh/tokern/piicatcher.svg?style=svg)](https://circleci.com/gh/tokern/piicatcher)
[![codecov](https://codecov.io/gh/tokern/piicatcher/branch/master/graph/badge.svg)](https://codecov.io/gh/tokern/piicatcher)
[![PyPI](https://img.shields.io/pypi/v/piicatcher.svg)](https://pypi.python.org/pypi/piicatcher)
[![image](https://img.shields.io/pypi/l/piicatcher.svg)](https://pypi.org/project/piicatcher/)
[![image](https://img.shields.io/pypi/pyversions/piicatcher.svg)](https://pypi.org/project/piicatcher/)

Pii Catcher for Files and Databases
===================================

Overview
--------

PiiCatcher finds PII data in your databases. It scans all the columns in your 
database and finds the following types of PII information:
* PHONE
* EMAIL
* CREDIT_CARD
* ADDRESS
* PERSON
* LOCATION
* BIRTH_DATE
* GENDER
* NATIONALITY
* IP_ADDRESS
* SSN
* USER_NAME
* PASSWORD

PiiCatcher uses two types of scanners to detect PII information:
1. [CommonRegex](https://github.com/madisonmay/CommonRegex) uses a set of regular expressions 
for common types of information
2. [Spacy Named Entity Recognition](https://spacy.io/usage/linguistic-features#named-entities) 
uses Natural Language Processing to detect named entities. Only English language is currently supported.

Supported Technologies
----------------------
PiiCatcher supports the following filesystems:
* POSIX
* AWS S3 (for files that are part of tables in AWS Glue and AWS Athena)
* Google Cloud Storage _(Coming Soon)_
* ADLS _(Coming Soon)_

PiiCatcher supports the following databases:
1. **Sqlite3** v3.24.0 or greater
2. **MySQL** 5.6 or greater
3. **PostgreSQL** 9.4 or greater
4. **AWS Redshift**
5. **SQL Server**
6. **Oracle**
7. **AWS Glue/AWS Athena**

Installation
------------
PiiCatcher is available as a command-line application.

To install use pip:

    python3 -m venv .env
    source .env/bin/activate
    pip install piicatcher


Or clone the repo:

    git clone https://github.com/vrajat/piicatcher.git
    python3 -m venv .env
    source .env/bin/activate
    python setup.py install
   
Install Spacy Language Model

    python -m spacy download en_core_web_sm 

Install Oracle Client

PiiCatcher on Oracle, requires a working client. Please refer to [cx_Oracle documentation](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html#oracle-client-and-oracle-database-interoperability)
for more information.
 
Usage
-----
Relational Databases:

    # Print usage to scan databases
    piicatcher db -h
    usage: piicatcher db [-h] -s HOST [-R PORT] [-u USER] [-p PASSWORD]
                     [-t {sqlite,mysql,postgres}] [-c {deep,shallow}]
                     [-o OUTPUT] [-f {ascii_table,json,orm}]

    optional arguments:
      -h, --help            show this help message and exit
      -s HOST, --host HOST  Hostname of the database. File path if it is SQLite
      -R PORT, --port PORT  Port of database.
      -u USER, --user USER  Username to connect database
      -p PASSWORD, --password PASSWORD
                            Password of the user
      -t {sqlite,mysql,postgres}, --connection-type {sqlite,mysql,postgres}
                            Type of database
      -c {deep,shallow}, --scan-type {deep,shallow}
                            Choose deep(scan data) or shallow(scan column names
                            only)
      -o OUTPUT, --output OUTPUT
                            File path for report. If not specified, then report is
                            printed to sys.stdout
      -f {ascii_table,json,orm}, --output-format {ascii_table,json,orm}
                            Choose output format type

    usage: piicatcher files [-h] [--path PATH] [--output OUTPUT]
                        [--output-format {ascii_table,json,orm}]

AWS S3 files backed by tables in AWS Glue & AWS Athena

    piicatcher aws -h
    usage: piicatcher aws [-h] -a ACCESS_KEY -s SECRET_KEY -d STAGING_DIR -r
                      REGION
                      [-t {sqlite,mysql,postgres,redshift,oracle,sqlserver}]
                      [-c {deep,shallow}] [-o OUTPUT]
                      [-f {ascii_table,json,orm}] [--list-all]

    optional arguments:
      -h, --help            show this help message and exit
      -a ACCESS_KEY, --access-key ACCESS_KEY
                            AWS Access Key
      -s SECRET_KEY, --secret-key SECRET_KEY
                            AWS Secret Key
      -d STAGING_DIR, --staging-dir STAGING_DIR
                            S3 Staging Directory for Athena results
      -r REGION, --region REGION
                            AWS Region
      -c {deep,shallow}, --scan-type {deep,shallow}
                            Choose deep(scan data) or shallow(scan column names
                            only)
      -o OUTPUT, --output OUTPUT
                            File path for report. If not specified, then report is
                            printed to sys.stdout
      -f {ascii_table,json,orm}, --output-format {ascii_table,json,orm}
                            Choose output format type
      --list-all            List all columns. By default only columns with PII
                            information is listed

Files in a POSIX Filesystem

    piicatcher files -h
    # Print usage to scan files
    optional arguments:
      -h, --help            show this help message and exit
      --path PATH           Path to file or directory
      --output OUTPUT       File path for report. If not specified, then report is
                            printed to sys.stdout
      --output-format {ascii_table,json,orm}
                            Choose output format type


Example
-------
     
    # run piicatcher on a sqlite db and print report to console
    piicatcher db -c '/db/sqlqb'
    ╭─────────────┬─────────────┬─────────────┬─────────────╮
    │   schema    │    table    │   column    │   has_pii   │
    ├─────────────┼─────────────┼─────────────┼─────────────┤
    │        main │    full_pii │           a │           1 │
    │        main │    full_pii │           b │           1 │
    │        main │      no_pii │           a │           0 │
    │        main │      no_pii │           b │           0 │
    │        main │ partial_pii │           a │           1 │
    │        main │ partial_pii │           b │           0 │
    ╰─────────────┴─────────────┴─────────────┴─────────────╯


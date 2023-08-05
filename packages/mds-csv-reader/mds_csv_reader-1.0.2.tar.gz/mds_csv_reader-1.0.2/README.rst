mds-csv-reader
==============
Read a csv-file, converts to list of dictionaries.

Install
=======
pip install mds-csv-reader

Howto
=====

Syntax
------

::

  import_csv_file(
         csvfile,                          # file or string
         firstline=True,                   # first line contains column names
         decimalremove=['€', 'EUR', '.'],  # remove these strings from decimal columns
         ignline=[1, 2, ...],              # skip these lines
         ignore_leer=['<column nam>',...], # ignore empty values in these columns
         encod='utf-8',                    # encoding if 'csvfile' is byte type
         )

Column names
------------

- column names must contain field type info
- allowed types: C, D, DT, T, N, L

Example
-------

NAME1,C
 type String
CREATEDATE,D,%Y-%m-%d
 type Date, detection tries defined format
CREATEDATE,D
 type Date, detection tries predefines formats
DATETIME,DT,%Y-%m-%d %H:%M
 type DateTime, detection tries defined format
DATETIME,DT
 type DateTime, detection tries predefines formats
CREATETIME,T,%H:%M
 type Time, detection tries defined format
CREATETIME,T
 type Time, detection tries predefines formats
NUMSTEP,N,10,0
 type Numeric (no decimals) --> Integer
AMOUNT,N,16,2
 type Numeric (two decimals) --> Decimal
ISENABLED,L
 Boolean (allowed: true, false, t, f, wahr, falsch, 1, 0)
default-type: String
 if convert to requested type fails


Changes
=======

*1.0.2 - 20.12.2019*

- exteded detection of date and time formats

*1.0.0 - 17.12.2019*

- optimized detection of formatting in csv-file

*1.0.0 - 17.12.2019*

- first public version

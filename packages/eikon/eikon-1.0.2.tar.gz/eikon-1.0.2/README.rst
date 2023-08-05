The Eikon Data API for Python allows your Python applications to access
data directly from Eikon or Refinitv Workspace, powering in-house or
thirdparty desktop apps with Refinitiv data. It provides seamless
workflow with the same data across all applications running on the
desktop. It leverages Eikon data and entitlements to simplify market
data management and reporting. The Eikon Data API for Python is a
software library that works in conjunction with the `Eikon`_ desktop
application and `Refinitiv Workspace`_.

Some examples
=============

Import Eikon and set your App Key
---------------------------------

.. code:: python

   import eikon as ek

   ek.set_app_key('8e9bxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx1b035d')

Get Real-time Snapshots
-----------------------

.. code:: python

   df, err = ek.get_data(
       instruments = ['GOOG.O','MSFT.O', 'FB.O'], 
       fields = ['BID','ASK']
   )
   display(df)

== ========== ======= =======
\  Instrument BID     ASK
== ========== ======= =======
0  GOOG.O     1350.48 1352.19
1  MSFT.O     152.38  152.40
2  FB.O       203.08  203.15
== ========== ======= =======

Get Fundamental & Reference data
--------------------------------

.. code:: python

   df, err = ek.get_data(
       instruments = ['GOOG.O','MSFT.O', 'FB.O'], 
       fields = ['TR.LegalAddressCity','TR.LegalAddressLine1','TR.Employees']
   )
   display(df)

+---+------------+----------------+----------------+----------------+
|   | Instrument | Legal Address  | Legal Address  | Full-Time      |
|   |            | City           | Line 1         | Employees      |
+===+============+================+================+================+
| 0 | GOOG.O     | WILMINGTON     | 251 Little     | 98771          |
|   |            |                | Falls Dr       |                |
+---+------------+----------------+----------------+----------------+
| 1 | MSFT.O     | TUMWATER       | 300 Deschutes  | 144000         |
|   |            |                | Way SW Ste 304 |                |
+---+------------+----------------+----------------+----------------+
| 2 | FB.O       | WILMINGTON     | 251 Little     | 35587          |
|   |            |                | Falls Dr       |                |
+---+------------+----------------+----------------+----------------+

Get TimeSeries
--------------

.. code:: python

   ek.get_timeseries('AAPL.O', interval='minute')

=================== ======== ======== ======== ======== ====== ========
AAPL.O              HIGH     LOW      OPEN     CLOSE    COUNT  VOLUME
=================== ======== ======== ======== ======== ====== ========
**Date**                                                       
2019-09-12 19:57:00 223.2000 222.8600 223.1800 222.9600 3387.0 267258.0
2019-09-12 19:58:00 223.1800 222.8900 222.9700 223.1700 1925.0 210251.0
2019-09-12 19:59:00 223.2800 223.0800 223.1700 223.1500 2106.0 223191.0
…                   …        …        …        …        …      …
2019-12-12 14:31:00 268.3000 267.3200 267.8200 267.9350 2974.0 724278.0
2019-12-12 14:32:00 268.3600 267.6000 267.9500 268.3000 1721.0 193413.0
=================== ======== ======== ======== ======== ====== ========

50000 rows by 6 columns

Get News HeadLines
------------------

.. code:: python

   ek.get_news_headlines('IBM.N', count=100)

+-------------------------+-------------------------+-------------------------------------------------+----------------------------------------------+------------+
|                         | versionCreated          | text                                            | storyId                                      | sourceCode |
+=========================+=========================+=================================================+==============================================+============+
| 2019-12-12 12:45:10.958 | 2019-12-12 12:45:10.958 | IBM India calls for balance between protecting… | urn:newsml:reuters.com:20191212:nNRAafsi86:1 | NS:ASNEWS  |
+-------------------------+----------------+----------------------------------------------------------+----------------------------------------------+------------+
| 2019-12-12 12:03:54.056 | 2019-12-12 12:03:54.056 | Red Hat announces renewal of FIPS 140-2 securi… | urn:newsml:reuters.com:20191212:nNRAafs2g9:1 | NS:DATMTR  |
+-------------------------+----------------+----------------------------------------------------------+----------------------------------------------+------------+
| 2019-12-12 08:07:44.753 | 2019-12-12 08:07:44.753 | Engineer forever changed retail with creation…  | urn:newsml:reuters.com:20191212:nNRAafpj8v:1 | NS:GLOBML  |
+-------------------------+----------------+----------------------------------------------------------+----------------------------------------------+------------+
| ... | ... | ... | ... | ... |
+-------------------------+----------------+----------------------------------------------------------+----------------------------------------------+------------+
| 2019-12-03 16:18:50.532 | 2019-12-03 16:18:50.532 | United States : IBM Watson Health Demonstrates… | urn:newsml:reuters.com:20191203:nNRAad1a5r:1 | NS:ECLPCM  |
+-------------------------+----------------+----------------------------------------------------------+----------------------------------------------+------------+
| 2019-12-03 13:00:10.642 | 2019-12-03 13:00:10.642 | Nozomi Networks Works with IBM to Secure Indus… | urn:newsml:reuters.com:20191203:nGNX8Yr8Hy:1 | NS:GNW     |
+-------------------------+----------------+----------------------------------------------------------+----------------------------------------------+------------+

100 rows by 4 columns

Get Symbology
-------------

.. code:: python

   ek.get_symbology(['MSFT.O', 'GOOG.O', 'IBM.N'])

====== ========= ============ ========== ====== ======= ======
\      CUSIP     ISIN         OAPermID   RIC    SEDOL   ticker
====== ========= ============ ========== ====== ======= ======
MSFT.O 594918104 US5949181045 4295907168 MSFT.O NaN     MSFT
GOOG.O 02079K107 US02079K1079 5030853586 GOOG.O NaN     GOOG
IBM.N  459200101 US4592001014 4295904307 IBM.N  2005973 IBM
====== ========= ============ ========== ====== ======= ======

Learning materals
=================

To learn more about the Eikon Data API Python library just connect to the Refinitiv Developer Community. By `registering`_ and `login`_ to the Refinitiv Developer Community portal you will get free access to a number of learning materials like `Quick Start guides`_, `Tutorials`_, `Documentation`_ and much more.

Help and Support
================

If you have any questions regarding the API usage, please post them on the `Eikon Data API Q&A Forum`_. The Refinitiv Developer Community will be very pleased to help you.

.. _Eikon: http://solutions.refinitiv.com/eikon-trading-software
.. _Refinitiv Workspace: https://www.refinitiv.com/en/products/refinitiv-workspace-wealth.. _registering: https://developers.refinitiv.com/iam/register
.. _login: https://developers.refinitiv.com/iam/login
.. _Quick Start guides: https://developers.refinitiv.com/eikon-apis/eikon-data-api/quick-start
.. _Tutorials: https://developers.refinitiv.com/eikon-apis/eikon-data-api/learning
.. _Documentation: https://developers.refinitiv.com/eikon-apis/eikon-data-api/docs
.. _Eikon Data API Q&A Forum: https://community.developers.thomsonreuters.com/spaces/92/index.html

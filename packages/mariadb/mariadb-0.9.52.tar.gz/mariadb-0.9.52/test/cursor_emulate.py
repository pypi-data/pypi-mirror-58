#!/usr/bin/env python -O

import mariadb
import datetime
import unittest

class CursorTest(unittest.TestCase):

  iterations= 500000

  def setUp(self):
    self.connection= mariadb.connection(default_file='default.cnf')

  def tearDown(self):
    self.connection.close()
    del self.connection

  def test_insert_parameter(self):
    cursor= self.connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS t1")
    cursor.execute("CREATE OR REPLACE TABLE t1(a int not null auto_increment primary key, b int, c int, d varchar(20),e date)")
    cursor.execute("set @@autocommit=0");
    for i in range(1, self.iterations + 1):
      cursor.execute("INSERT INTO t1 VALUES (?,?,?,?,?)", (i,i,i, "bar", datetime.date(2019,1,1)))
    self.connection.commit()
    cursor.execute("SELECT * FROM t1 order by a")
    self.assertEqual(self.iterations, cursor.rowcount);
    cursor.execute("drop table t1")
    cursor.close()

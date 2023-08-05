/************************************************************************************
    Copyright (C) 2018 Georg Richter and MariaDB Corporation AB

   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Library General Public
   License as published by the Free Software Foundation; either
   version 2 of the License, or (at your option) any later version.

   This library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Library General Public License for more details.

   You should have received a copy of the GNU Library General Public
   License along with this library; if not see <http://www.gnu.org/licenses>
   or write to the Free Software Foundation, Inc.,
   51 Franklin St., Fifth Floor, Boston, MA 02110, USA
*************************************************************************************/
#define MARIADB_CONNECTION

#include "mariadb_python.h"
#include "docs/module.h"
#include <structmember.h>
#include <datetime.h>

PyObject *Mrdb_Pickle= NULL;
PyObject *cnx_pool= NULL;
extern uint16_t max_pool_size;

int Mariadb_traverse(PyObject *self,
                     visitproc visit,
                     void *arg)
{
	return 0;
}

static PyObject *Mariadb_date_from_ticks(PyObject *self,
                                         PyObject *args);
static PyObject *Mariadb_time_from_ticks(PyObject *self,
                                         PyObject *args);
static PyObject *Mariadb_timestamp_from_ticks(PyObject *self,
                                         PyObject *args);
static PyObject *Mariadb_date(PyObject *self,
                              PyObject *args);
static PyObject *Mariadb_time(PyObject *self,
                              PyObject *args);
static PyObject *Mariadb_timestamp(PyObject *self,
                                   PyObject *args);
static PyObject *Mariadb_binary(PyObject *self,
                               PyObject *args);

static PyMethodDef Mariadb_Methods[] =
{
  /* PEP-249: mandatory */
  {"Binary", (PyCFunction)Mariadb_binary,
     METH_VARARGS,
     module_binary__doc__},
  {"connect", (PyCFunction)MrdbConnection_connect,
     METH_VARARGS | METH_KEYWORDS,
     module_connect__doc__},
  {"ConnectionPool", (PyCFunction)MrdbPool_add,
     METH_VARARGS | METH_KEYWORDS,
     "todo!!"}, 
  /* PEP-249 DB-API */
  {"DateFromTicks", (PyCFunction)Mariadb_date_from_ticks,
     METH_VARARGS,
     module_DateFromTicks__doc__},
  {"TimeFromTicks", (PyCFunction)Mariadb_time_from_ticks,
     METH_VARARGS,
     module_TimeFromTicks__doc__},
  {"TimestampFromTicks", (PyCFunction)Mariadb_timestamp_from_ticks,
     METH_VARARGS,
     module_TimestampFromTicks__doc__},
  {"Date", (PyCFunction)Mariadb_date,
     METH_VARARGS,
     module_Date__doc__},
  {"Time", (PyCFunction)Mariadb_time,
     METH_VARARGS,
     module_Time__doc__},
  {"Timestamp", (PyCFunction)Mariadb_timestamp,
     METH_VARARGS,
     module_Timestamp__doc__},
  /* Todo: add methods for api functions which don't require
           a connection */
  {NULL} /* always last */
};

/* MariaDB module definition */
static struct PyModuleDef mariadb_module= {
  PyModuleDef_HEAD_INIT,
  "mariadb",
  "MariaDB Connector for Python",
  -1,
  Mariadb_Methods
};

/*  constants */
struct st_constants {
  const char *name;
  union {
    long lvalue;
    const char *strvalue;
  } u;
 };

 struct st_constants int_constants[]= {
  {"CURSOR_TYPE_READ_ONLY", {CURSOR_TYPE_READ_ONLY}},
  {"CURSOR_TYPE_NONE", {CURSOR_TYPE_NO_CURSOR}},
  {NULL, {0}} /* Always last */
};

static char exception_interface_doc[]= "Exception raised for errors that are related to the database interface "
                                      "rather than the database itself";
static char exception_warning_doc[]= "Exception raised for important warnings like data truncations while inserting, etc";
static char exception_database_doc[]= "Exception raised for errors that are related to the database";
static char exception_data_doc[] = "Exception raised for errors that are due to problems with the processed data "
                                   "like division by zero, numeric value out of range, etc.";
static char exception_pool_doc[] = "Exeception rasied for errors related to ConnectionPool class.";
static char exception_operational_doc[] = "Exception raised for errors that are related to the database's operation "
                                          "and not necessarily under the control of the programmer.";
static char exception_integrity_doc[]= "Exception raised when the relational integrity of the database is affected, "
                                       "e.g. a foreign key check fails";
static char exception_internal_doc[]= "Exception raised when the database encounters an internal error, "
                                      "e.g. the cursor is not valid anymore";
static char exception_programming_doc[]= "Exception raised for programming errors, e.g. table not found or already "
                                         "exists, syntax error in the SQL statement";
static char exception_notsupported_doc[]= "Exception raised in case a method or database API was used which is not "
                                          "supported by the database";

static void mariadb_add_exception(PyObject *module,
                                  PyObject **exception,
                                  const char *exception_name,
                                  char *doc,
                                  const char *object_name)
{
  *exception= PyErr_NewExceptionWithDoc(exception_name,
                                        doc,
                                        Mariadb_Error,
                                        NULL);

  Py_INCREF(*exception);
  PyModule_AddObject(module, object_name, *exception);
}

/* MariaDB module initialization function */
PyMODINIT_FUNC PyInit_mariadb(void)
{
  PyObject *module= PyModule_Create(&mariadb_module);
  struct st_constants *intvals= int_constants;

  Py_TYPE(&MrdbConnection_Type) = &PyType_Type;
  if (PyType_Ready(&MrdbConnection_Type) == -1)
    goto error;

  /* we need pickle for object serialization */
  Mrdb_Pickle= PyImport_ImportModule("pickle");

  Py_TYPE(&MrdbCursor_Type) = &PyType_Type;
  if (PyType_Ready(&MrdbCursor_Type) == -1)
    goto error;

  Py_TYPE(&MrdbPool_Type) = &PyType_Type;
  if (PyType_Ready(&MrdbPool_Type) == -1)
    goto error;

  Py_TYPE(&MrdbIndicator_Type) = &PyType_Type;
  if (PyType_Ready(&MrdbIndicator_Type) == -1)
    goto error;

  Py_TYPE(&Mariadb_Fieldinfo_Type) = &PyType_Type;
  if (PyType_Ready(&Mariadb_Fieldinfo_Type) == -1)
    goto error;

  Py_TYPE(&Mariadb_DBAPIType_Type) = &PyType_Type;
  if (PyType_Ready(&Mariadb_DBAPIType_Type) == -1)
    goto error;

  /* Mariadb module constants */
  while (intvals->name) {
    PyModule_AddIntConstant(module, intvals->name,
                                    intvals->u.lvalue);
    intvals++;
  }

  /* PEP-249: mandatory module globals */
  PyModule_AddObject(module, "apilevel", PyUnicode_FromString(MARIADB_PY_APILEVEL));
  PyModule_AddObject(module, "paramstyle", PyUnicode_FromString(MARIADB_PY_PARAMSTYLE));
  PyModule_AddObject(module, "threadsafety", PyLong_FromLong(MARIADB_PY_THREADSAFETY));
  /* optional (MariaDB specific) globals */
  PyModule_AddObject(module, "mariadbapi_version", PyUnicode_FromString(mysql_get_client_info()));

  Mariadb_Error= PyErr_NewException("mariadb.Error",
                                    PyExc_Exception,
                                    NULL);
  Py_INCREF(Mariadb_Error);
  PyModule_AddObject(module, "Error", Mariadb_Error);

  mariadb_add_exception(module, &Mariadb_InterfaceError,
                        "mariadb.InterfaceError", exception_interface_doc, "InterfaceError");
  mariadb_add_exception(module, &Mariadb_OperationalError,
                        "mariadb.OperationalError", exception_operational_doc, "OperationalError");
  mariadb_add_exception(module, &Mariadb_Warning,
                        "mariadb.Warning", exception_warning_doc, "Warning");
  mariadb_add_exception(module, &Mariadb_IntegrityError,
                        "mariadb.IntegrityError", exception_integrity_doc, "IntegrityError");
  mariadb_add_exception(module, &Mariadb_InternalError,
                        "mariadb.InternalError", exception_internal_doc, "InternalError");
  mariadb_add_exception(module, &Mariadb_ProgrammingError,
                        "mariadb.ProgrammingError", exception_programming_doc, "ProgrammingError");
  mariadb_add_exception(module, &Mariadb_NotSupportedError,
                        "mariadb.NotSupportedError", exception_notsupported_doc, "NotSupportedError");
  mariadb_add_exception(module, &Mariadb_DatabaseError,
                        "mariadb.DatabaseError", exception_database_doc, "DatabaseError");
  mariadb_add_exception(module, &Mariadb_DataError,
                        "mariadb.DatabaseError.DataError", exception_data_doc, "DataError");
  mariadb_add_exception(module, &Mariadb_PoolError,
                        "mariadb.PoolError", exception_pool_doc, "PoolError");

  Py_INCREF(&MrdbConnection_Type);
  PyModule_AddObject(module, "connection", (PyObject *)&MrdbConnection_Type);
  cnx_pool= PyDict_New();
  Py_INCREF(&MrdbPool_Type);
  PyModule_AddObject(module, "ConnectionPool", (PyObject *)&MrdbPool_Type);
  PyModule_AddObject(module, "_CONNECTION_POOLS", cnx_pool);
  

  PyModule_AddObject(module, "indicator_null", MrdbIndicator_Object(STMT_INDICATOR_NULL));
  PyModule_AddObject(module, "indicator_default", MrdbIndicator_Object(STMT_INDICATOR_DEFAULT));
  PyModule_AddObject(module, "indicator_ignore", MrdbIndicator_Object(STMT_INDICATOR_IGNORE));
  PyModule_AddObject(module, "indicator_row", MrdbIndicator_Object(STMT_INDICATOR_IGNORE_ROW));

  PyModule_AddObject(module, "NUMBER", Mariadb_DBAPIType_Object(DBAPI_NUMBER));
  PyModule_AddObject(module, "BINARY", Mariadb_DBAPIType_Object(DBAPI_BINARY));
  PyModule_AddObject(module, "STRING", Mariadb_DBAPIType_Object(DBAPI_STRING));
  PyModule_AddObject(module, "DATETIME", Mariadb_DBAPIType_Object(DBAPI_DATETIME));
  PyModule_AddObject(module, "ROWID", Mariadb_DBAPIType_Object(DBAPI_ROWID));

  Py_INCREF(&Mariadb_Fieldinfo_Type);
  PyModule_AddObject(module, "fieldinfo", (PyObject *)&Mariadb_Fieldinfo_Type);

  return module;
error:
  PyErr_SetString(PyExc_ImportError, "Mariadb module initialization failed");
  return NULL;
}

static time_t get_ticks(PyObject *object)
{
  time_t ticks= 0;
  if (Py_TYPE(object) == &PyFloat_Type)
    ticks= (time_t)PyFloat_AsDouble(object);
  if (Py_TYPE(object) == &PyLong_Type)
    ticks= (time_t)PyLong_AsLong(object);
  return ticks;
}

static PyObject *Mariadb_date_from_ticks(PyObject *module,
                                         PyObject *args)
{
  PyObject *o, *Date;
  struct tm *ts;
  time_t epoch;

  if (!PyDateTimeAPI)
    PyDateTime_IMPORT;


  if (!PyArg_ParseTuple(args, "O", &o))
    return NULL;

  epoch= get_ticks(o);
  ts= localtime(&epoch);

  Date= PyDate_FromDate(ts->tm_year + 1900, ts->tm_mon + 1, ts->tm_mday);
  return Date;
}

static PyObject *Mariadb_time_from_ticks(PyObject *module,
                                         PyObject *args)
{
  struct tm *ts;
  time_t epoch;
  PyObject *o, *Time= NULL;

  if (!PyDateTimeAPI)
    PyDateTime_IMPORT;


  if (!PyArg_ParseTuple(args, "O", &o))
    return NULL;

  epoch= get_ticks(o);
  ts= localtime(&epoch);

  Time= PyTime_FromTime(ts->tm_hour, ts->tm_min, ts->tm_sec, 0);
  return Time;
}

static PyObject *Mariadb_timestamp_from_ticks(PyObject *module,
                                         PyObject *args)
{
  PyObject *o,*Timestamp;
  struct tm *ts;
  time_t epoch;

  if (!PyDateTimeAPI)
    PyDateTime_IMPORT;

  if (!PyArg_ParseTuple(args, "O", &o))
    return NULL;

  epoch= get_ticks(o);
  ts= localtime(&epoch);

  Timestamp= PyDateTime_FromDateAndTime(ts->tm_year + 1900, ts->tm_mon + 1, ts->tm_mday, ts->tm_hour, ts->tm_min, ts->tm_sec, 0);
  return Timestamp;
}

static PyObject *Mariadb_date(PyObject *self,
                              PyObject *args)
{
  PyObject *date= NULL;
  int32_t year=0, month=0, day= 0;

  if (!PyDateTimeAPI)
    PyDateTime_IMPORT;

  if (!PyArg_ParseTuple(args, "iii", &year, &month, &day))
    return NULL;

  date= PyDate_FromDate(year, month, day);
  return date;
}

static PyObject *Mariadb_timestamp(PyObject *self,
                                  PyObject *args)
{
  PyObject *timestamp= NULL;
  int32_t year=0, month=0, day= 0;
  int32_t hour=0, min=0, sec= 0;

  if (!PyDateTimeAPI)
    PyDateTime_IMPORT;
  if (!PyArg_ParseTuple(args, "iiiiii", &year, &month, &day, &hour, &min, &sec))
    return NULL;

  timestamp= PyDateTime_FromDateAndTime(year, month, day, hour, min, sec, 0);
  return timestamp;
}


static PyObject *Mariadb_time(PyObject *self,
                              PyObject *args)
{
  PyObject *time= NULL;
  int32_t hour=0, min=0, sec= 0;
  if (!PyDateTimeAPI)
    PyDateTime_IMPORT;

  if (!PyArg_ParseTuple(args, "iii", &hour, &min, &sec))
    return NULL;

  time= PyTime_FromTime(hour, min, sec, 0);
  return time;
}

static PyObject *Mariadb_binary(PyObject *self,
                               PyObject *args)
{
  PyObject *b,*o;

  if (!PyArg_ParseTuple(args, "O", &o))
    return NULL;

  b= PyBytes_FromObject(o);
  return b;
}

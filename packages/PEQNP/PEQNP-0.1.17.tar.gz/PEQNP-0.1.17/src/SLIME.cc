///////////////////////////////////////////////////////////////////////////////
//        Copyright (c) 2012-2020 Oscar Riveros. all rights reserved.        //
//                        oscar.riveros@peqnp.science                        //
//                                                                           //
//   without any restriction, Oscar Riveros reserved rights, patents and     //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////

#include "SLIME.h"

#if PY_MAJOR_VERSION >= 3
static PyMethodDef module_methods[] = {{"add_clause", (PyCFunction)add_clause, METH_VARARGS,
                                        ""
                                        ""
                                        ""},
                                       {"solve", (PyCFunction)solve, METH_VARARGS,
                                        ""
                                        ""
                                        ""},
                                       {"reset", (PyCFunction)reset, METH_VARARGS,
                                        ""
                                        ""
                                        ""},
                                       {NULL, NULL, 0, NULL}};

PyMODINIT_FUNC PyInit_slime() { return PyModule_Create(&slime); }
#else
static PyMethodDef module_methods[] = {{"add_clause", (PyCFunction)add_clause, METH_VARARGS,
                                        ""
                                        ""
                                        ""},
                                       {"solve", (PyCFunction)solve, METH_VARARGS,
                                        ""
                                        ""
                                        ""},
                                       {"reset", (PyCFunction)reset, METH_VARARGS,
                                        ""
                                        ""
                                        ""},
                                       {NULL, NULL, 0, NULL}};
PyMODINIT_FUNC initslime(void) {
    PyObject *m;
    m = Py_InitModule("slime", module_methods);
    if (m == NULL)
        return;
};
#endif
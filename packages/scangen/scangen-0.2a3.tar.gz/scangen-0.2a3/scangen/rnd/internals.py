"""Direct wrapper for libcrnd."""

import ctypes

crnd = ctypes.CDLL("librndpoc.so")

class CRange(ctypes.Structure):
    """Wrapper for struct rnd_range."""

    _fields_ = [
        ("start", ctypes.c_uint32),
        ("end", ctypes.c_uint32)
    ]

class CExpr(ctypes.Structure):
    """Wrapper for struct rnd_expr."""

CExpr._fields_ = [
    ("type", ctypes.c_char),
    ("value", CRange),
    ("left", ctypes.POINTER(CExpr)),
    ("right", ctypes.POINTER(CExpr))
]

class CTransition(ctypes.Structure):
    """Wrapper for struct rnd_transition."""

    _fields_ = [
        ("label", CRange),
        ("to", ctypes.c_int)
    ]

class CState(ctypes.Structure):
    """Wrapper for struct rnd_state."""

    _fields_ = [
        ("accept", ctypes.c_bool),
        ("outdegree", ctypes.c_int),
        ("transitions", ctypes.POINTER(CTransition))
    ]

class CDfa(ctypes.Structure):
    """Wrapper for struct rnd_dfa."""

    _fields_ = [
        ("order", ctypes.c_int),
        ("states", ctypes.POINTER(CState)),
        ("error", ctypes.c_int)
    ]

crnd.rnd_convert.argtypes = [ctypes.POINTER(CExpr)]
crnd.rnd_convert.restype = CDfa

crnd.rnd_dfa_destroy.argtypes = [ctypes.POINTER(CDfa)]
crnd.rnd_dfa_destroy.restype = None

crnd.rnd_symbol.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
crnd.rnd_symbol.restype = ctypes.POINTER(CExpr)

crnd.rnd_union.argtypes = [ctypes.POINTER(CExpr), ctypes.POINTER(CExpr)]
crnd.rnd_union.restype = ctypes.POINTER(CExpr)

crnd.rnd_concatenation.argtypes = [ctypes.POINTER(CExpr), ctypes.POINTER(CExpr)]
crnd.rnd_concatenation.restype = ctypes.POINTER(CExpr)

crnd.rnd_closure.argtypes = [ctypes.POINTER(CExpr)]
crnd.rnd_closure.restype = ctypes.POINTER(CExpr)

crnd.rnd_expr_destroy.argtypes = [ctypes.POINTER(CExpr)]
crnd.rnd_expr_destroy.restype = None

crnd.rnd_expr_free.argtypes = [ctypes.POINTER(CExpr)]
crnd.rnd_expr_free.restype = None

crnd.rnd_get_expr_counter.restype = ctypes.c_int

"""Wrapper for libcrnd with additional features."""

import ctypes
import enum
import os
import sys
from redblack import containers
from .internals import crnd

class ExprType(enum.Enum):
    """Same as enum rnd_type { RND_SYMBOL, RND_UNION, ... }."""
    SYMBOL = 0
    UNION = 1
    CONCATENATION = 2
    CLOSURE = 3

class ExprSymbols:
    """Class that represents a closed range of symbols.

    Needs to be destroyed after use, either directly or indirectly.
    """

    def __init__(self, start=0xffffffff, end=None):
        if end is None:
            end = min(0xffffffff, start+1)
        if start > end:
            raise ValueError("start must be <= end")
        self.start = start
        self.end = end
        self.cpointer = crnd.rnd_symbol(start, end)

    def union(self, other):
        """Return a UNION Expr.

        other may be an ExprSymbols or an Expr.
        """
        return union(self, other)

    def concatenation(self, other):
        """Return a CONCATENATION Expr.

        other may be an ExprSymbols or an Expr.
        """
        return concatenation(self, other)

    def closure(self):
        """Return a CLOSURE Expr."""
        return closure(self)

    def destroy(self):
        """Free memory allocated during __init__."""
        if self.cpointer:
            crnd.rnd_expr_free(self.cpointer)
        self.cpointer = None

    def __repr__(self):
        if self.start >= self.end:
            return "nil"
        elif self.start+1 == self.end:
            return str(self.start)
        return f"[{self.start}, {self.end})"

def _get_expr_pointer(expr):
    return None if not expr else expr.cpointer

# doesn't raise exceptions to avoid memory leak
class Expr:
    """Owner class of CExpr with methods for creating new Expr.

    Needs to be destroyed after use, either directly or indirectly.
    """

    def __init__(self, type_, left=None, right=None):
        self.type_ = type_
        self.left = left
        self.right = right
        self.cpointer = None

        left = _get_expr_pointer(self.left)
        if type_ is ExprType.UNION:
            self.cpointer = crnd.rnd_union(
                left,
                _get_expr_pointer(self.right))
        elif type_ is ExprType.CONCATENATION:
            self.cpointer = crnd.rnd_concatenation(
                left,
                _get_expr_pointer(self.right))
        elif type_ is ExprType.CLOSURE:
            self.cpointer = crnd.rnd_closure(left)

    def __repr__(self):
        if self.type_ == ExprType.UNION:
            return f"union({self.left!r}, {self.right!r})"
        elif self.type_ == ExprType.CONCATENATION:
            return f"concatenation({self.left!r}, {self.right!r})"
        elif self.type_ == ExprType.CLOSURE:
            return f"closure({self.left!r})"
        assert False

    def destroy(self):
        """Free cpointer of this node and all descendant nodes.

        Does not need to be called if invoked from another Expr.
        """
        if self.cpointer:
            crnd.rnd_expr_free(self.cpointer)
        self.cpointer = None
        if self.left:
            self.left.destroy()
        if self.right:
            self.right.destroy()
        self.left = None
        self.right = None

    def union(self, other):
        """Return a UNION Expr."""
        return union(self, other)

    def concatenation(self, other):
        """Return a CONCATENATION Expr."""
        return concatenation(self, other)

    def closure(self):
        """Return a CLOSURE Expr."""
        return closure(self)

def union(a, b) -> Expr:
    return Expr(ExprType.UNION, a, b)

def concatenation(a, b) -> Expr:
    return Expr(ExprType.CONCATENATION, a, b)

def closure(expr: Expr or ExprSymbols) -> Expr:
    return Expr(ExprType.CLOSURE, expr)

class DfaSymbols:
    """Similar to CRange, but with built in comparator."""

    def __init__(self, start=0xffffffff, end=None):
        if end is None:
            end = min(0xffffffff, start+1)
        if start > end:
            raise ValueError("start must be <= end")
        self.start = start
        self.end = end

    def __repr__(self):
        if self.start >= self.end:
            return "nil"
        elif self.start+1 == self.end:
            return str(self.start)
        return f"[{self.start}, {self.end})"

    def __lt__(self, other):
        """Check if self is on the left of other."""
        assert self.start <= self.end
        assert other.start <= other.end
        return self.end <= other.start

    def __gt__(self, other):
        """Check if self is on the right of other."""
        return other < self

    def __eq__(self, other):
        """Check if self and other overlap."""
        return not (self < other) and not (self > other)

class Dfa:
    """Higher-level wrapper for rnd_dfa with computational capabilities."""

    def __init__(self):
        self.start = 0
        self.accepts = set()
        self.transitions = {}
        self.error = -1

    def __repr__(self):
        return f"<rnd.Dfa start={self.start!r}, accepts={self.accepts!r}, "\
                f"error={self.error}, "\
                f"transitions={self.transitions!r}>"

    def compute(self, inputs):
        """Compute if Dfa accepts the sequence of ints.

        Assume that -1 is an error state with no outbound transitions.
        """
        state = self.start
        for a in inputs:
            if state not in self.transitions or state == self.error:
                return False
            state = self.transitions[state].get(DfaSymbols(a), -1)
        return state in self.accepts

def _cdfa_to_pydfa(_dfa: internals.CDfa) -> Dfa:
    dfa = Dfa()
    dfa.transitions[dfa.start] = containers.Map()
    dfa.error = _dfa.error

    for q in range(_dfa.order):
        state = _dfa.states[q]
        if q not in dfa.transitions:
            dfa.transitions[q] = containers.Map()
        if state.accept:
            dfa.accepts.add(q)
        for j in range(state.outdegree):
            trans = state.transitions[j]
            a = DfaSymbols(int(trans.label.start), int(trans.label.end))
            r = int(trans.to)
            if r not in dfa.transitions:
                dfa.transitions[r] = containers.Map()
            # assumes a doesn't overlap with any other DfaSymbols
            dfa.transitions[q][a] = r
    return dfa

def convert(expr: Expr or ExprSymbols) -> Dfa:
    """Convert expr into dfa, without destroying expr."""
    _dfa = crnd.rnd_convert(expr.cpointer)
    dfa = _cdfa_to_pydfa(_dfa)
    crnd.rnd_dfa_destroy(ctypes.byref(_dfa))
    return dfa

name = "rnd"

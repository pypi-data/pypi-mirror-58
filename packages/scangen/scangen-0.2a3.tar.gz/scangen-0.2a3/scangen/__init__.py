"""A scanner generator that uses Jinja2 templates."""
import argparse
import sys
import jinja2
from . import rnd

scanners = []

def symbols(left: str = None, right: str = None) -> rnd.ExprSymbols:
    """Create range of symbols from characters."""
    left = ord(left) if left is not None else 0xffffffff
    if right:
        right = ord(right)+1
    else:
        right = min(0xffffffff, left+1)
    return rnd.ExprSymbols(left, right)

def isymbols(left: int = None, right: int = None) -> rnd.ExprSymbols:
    """Create range of symbols from integers."""
    if left is None:
        left = 0xffffffff
    right = right+1 if right is not None else min(0xffffffff, left+1)
    return rnd.ExprSymbols(left, right)

def optional(expr: rnd.ExprSymbols or rnd.Expr):
    """Return union of expr with empty symbol."""
    return expr.union(symbols())

def token(name):
    """Register scanner."""
    def decorator(func):
        def wrapper():
            expr = func()
            dfa = rnd.convert(expr)
            expr.destroy()
            dfa.token = name
            return dfa
        scanners.append(wrapper())
        return wrapper
    return decorator

def generate(entrypoint="", directory=""):
    """Generate code from templates."""
    def get_args(args):
        description = "Generate scanner using jinja2 templates."
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument("entrypoint", help="filename of template entrypoint")
        parser.add_argument("-d", default="", dest="directory",
                            help="path to templates directory")
        return parser.parse_args(args)

    def generate_code():
        loader = jinja2.FileSystemLoader(directory)
        env = jinja2.Environment(loader=loader)
        template = env.get_template(entrypoint)
        return template.render(scanners=scanners)

    args = sys.argv[1:]
    if entrypoint:
        args.append(entrypoint)
    if directory:
        args.extend(["-d", directory])
    args = get_args(args)
    if args.entrypoint:
        entrypoint = args.entrypoint
    if args.directory:
        directory = args.directory

    try:
        output = generate_code()
        print(output)
    except jinja2.exceptions.TemplateNotFound:
        print("scangen: Template not found:", entrypoint)

name = "scangen"

"""
Python 2/3 compatible functions
"""


def remove_symbols(text, symbols):
    """
    remove from string given symbols
    """
    for symbol in symbols:
        text = text.replace(symbol, '')

    return text


def load_module_by_path(path):
    """
    load py module by file path
    https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    """
    # construct package name from module file path
    # drop file path specific symbols
    name = remove_symbols(path, '/\\:.')

    try:  # Python 3.5+
        import importlib.util
        spec = importlib.util.spec_from_file_location(name, path)
        py_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(py_module)
    except ImportError:  # Python 3.4 3.3
        try:
            from importlib.machinery import SourceFileLoader
            py_module = SourceFileLoader(name, path).load_module()
        except ImportError:  # Python 2
            import imp
            py_module = imp.load_source(name, path)

    return py_module

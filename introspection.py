def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [m for m in dir(obj) if callable(getattr(obj, m)) and not m.startswith('_')],
        'module': type(obj).__module__
    }

    if isinstance(obj, (int, float, complex)):
        info['value'] = obj
    elif isinstance(obj, str):
        info['length'] = len(obj)
    elif hasattr(obj, '__len__'):
        info['length'] = len(obj)

    return info

number_info = introspection_info(42)
print(number_info)
# Output: {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': ['bit_length', 'conjugate', 'denominator', ...], 'module': 'builtins', 'value': 42}

string_info = introspection_info('Hello, World!')
print(string_info)
# Output: {'type': 'str', 'attributes': ['__add__', '__class__', ...], 'methods': ['capitalize', 'casefold', 'center', ...], 'module': 'builtins', 'length': 13}

list_info = introspection_info([1, 2, 3, 4, 5])
print(list_info)
# Output: {'type': 'list', 'attributes': ['__add__', '__class__', ...], 'methods': ['append', 'clear', 'copy', ...], 'module': 'builtins', 'length': 5}

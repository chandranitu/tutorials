def flatten_list(a, result=None):
    """Flattens a nested list."""
if result is None:
    result = []
for x in a:
    if isinstance(x, list):
        flatten_list(x, result)
    else:
        result.append(x)
return result

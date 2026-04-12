import difflib

def get_diff(old, new):
    diff = difflib.ndiff(old.split(), new.split())
    result = []
    for d in diff:
        if d.startswith('- '):
            result.append(f"<span style='color:red'>{d[2:]}</span>")
        elif d.startswith('+ '):
            result.append(f"<span style='color:green'>{d[2:]}</span>")
        else:
            result.append(d[2:])
    return " ".join(result)

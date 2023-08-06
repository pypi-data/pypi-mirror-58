import sys

def list_recursive(src_list, indent=False, level=0, fh=sys.stdout):

    for item in src_list:
        if isinstance(item, list):
            list_recursive(item, level + 1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(item, file=fh)
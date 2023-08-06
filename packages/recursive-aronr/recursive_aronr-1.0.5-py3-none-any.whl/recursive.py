def list_recursive(src_list, level=0):

    if level > 0:
        idnt = 0
        ident = ''
        while idnt < level:
            ident += '\t'
            idnt = idnt + 1
    else:
        """There is no indicates"""

    for item in src_list:
        if isinstance(item, list):
            list_recursive(item, level + 1)
        else:
            if level > 0:
                print(ident + item)
            else:
                print(item)
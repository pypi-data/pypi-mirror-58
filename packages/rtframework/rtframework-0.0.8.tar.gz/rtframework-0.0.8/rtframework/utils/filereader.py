from codecs import BOM_UTF8

def read(filepath: str) -> str:
    """[summary]
    
    Arguments:
        filepath {str} -- [description]
    
    Returns:
        str -- [description]
    """
    file_ = open(filepath, 'rb')
    decoded_file = decode(file_.read())
    return decoded_file

def decode(content, remove_bom=True) -> str:
    """[summary]
    
    Arguments:
        content {[type]} -- [description]
    
    Keyword Arguments:
        remove_bom {bool} -- [description] (default: {True})
    
    Returns:
        str -- [description]
    """
    if remove_bom and content.startswith(BOM_UTF8):
            content = content[len(BOM_UTF8):]
    return content.decode('UTF-8')
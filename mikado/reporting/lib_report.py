"""
Simple reporting functions - so display a dict as htnl tables etc
"""

def dictlist2table(dictlist, hdrs=None, format_function=None):
    """ """
    if not dictlist:
        return ''
    
    html = '''<table class="table table-striped">'''
    hdrs = dictlist[0].keys()
    hdrrow = '<tr>'
    for k in hdrs:
        hdrrow += '<th>{}</th>'.format(k)
    hdrrow += "</tr>"
    html += hdrrow
    
    for row in dictlist:
        htmlrow = '<tr>'
        for hdr in hdrs:
            htmlrow += "<td>{}</td>".format(row[hdr])
        htmlrow += "</tr>"
        html += htmlrow
    return html

def show_any_html(htmlfrag, name=None):
    """Take any html, and write to a file and displpay """
    html_template = '<html><body>{frag}</body></html>'
    html = html_template.format(frag=htmlfrag)
    path = '/tmp/foo.html'
    with open(path, 'w', encoding='utf-8') as fo:
        fo.write(html)
    print(path)
    

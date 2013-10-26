class Table(object):

    def __init__(self, headers, cols, decimals=2):
        self.headers = headers
        self.cols = cols
        self.decimals = decimals

    def _repr_html_(self):
        html = ["<table>"]
        html.append("<thead>")
        html.append("<tr>")
        for header in self.headers:
            html.append("<th>{0}</th>".format(header))
        html.append("</tr>")
        html.append("</thead>")

        colcount = len(self.cols)
        linecount = len(self.cols[0])

        for l in xrange(linecount):
            html.append("<tr>")
            for c in xrange(colcount):
                entry = str(round(self.cols[c][l], self.decimals))
                html.append("<td>{0}</td>".format(entry))
            html.append("</tr>")

        html.append("</table>")
        return ''.join(html)

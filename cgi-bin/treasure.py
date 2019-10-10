#!/usr/bin/python

# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2012 Chris Gonnerman
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# Redistributions of source code must retain the above copyright
# notice, self list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, self list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# Neither the name of the author nor the names of any contributors
# may be used to endorse or promote products derived from self software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import cgi, time, traceback, sys, string

page = string.Template("""Content-type: text/html
Cache-control: no-cache
Expires: $time

<html>
<header><title>$title</title></header>
<body>
<form action='$scriptpath'>
<input type='text' name='type' value='$types'>
<input type='submit' value='Generate'>
</form>
<table width=620 border=0 cellspacing=0 cellpadding=0 class=small>
<tr><td>
You may enter any treasure type from A to V, or you may generate
single magic items by entering <b>Magic</b>, <b>Potion</b>,
<b>Scroll</b>, <b>WSR</b> (Wand, Staff, or Rod), <b>Misc</b>,
<b>Armor</b>, or <b>Weapon<b>.
</td></tr>
</table>
<p>
<table border=0 cellspacing=0 width=620>
<tr bgcolor=white>
<td colspan=5><b>Treasure Type $typenames</b></td>
</tr>
<tr bgcolor='#D0D0D0' valign=bottom>
<td>Qty.</td><td colspan=2>Name/Description</td>
<td>Value<br>Each</td><td>Value<br>Total</td>
</tr>
$rows
<tr bgcolor='#D0D0D0'>
<td colspan=4>Total Value</td>
<td align=right>$totval</td>
</tr>
</table>
<p>
</body>
</html>""")


try:


    from Dungeoneer import Treasure

    pagevalues = {
        'title': 'Basic Fantasy',
        'time': time.asctime(time.gmtime(time.time())),
        'body': '',
        'scriptpath': 'treasure2.py',
        'totval':0,
        'rows':'',
        'types':'',
        'typenames':''
    }


    form = cgi.FieldStorage()

    if "type" in form:

        typefld = form["type"]
        types = []

        if type(typefld) is type([]):
            for i in typefld:
                types = types + i.value.split()
        else:
            types = typefld.value.split()

        pagevalues['types'] = " ".join(types)
        bgs = [ "white", "#E0E0E0", ]

        totval = 0
        typenames, tr = Treasure.Factory(tuple(types))
        pagevalues['typenames'] = typenames

        rows = []

        for t in tr:
            rows.append(f"<tr valign=top bgcolor='{bgs[0]}'>")
            bgs = bgs[1:] + bgs[:1]
            rows.append(f"""<td align=right width=60>{t.qty} &nbsp;</td>
<td width=440 colspan=2>{str(t.name)}</td>""")
            if t.value > 0.000001:
                rows.append(f"""<td align=right width=60>{t.value}</td>
<td align=right width=60>{t.value * t.qty}</td>""")
            else:
                rows.append("""<td>&nbsp;</td>
<td>&nbsp;</td>""")
            rows.append("</tr>")
            totval = totval + (t.qty * t.value)
            for d in t.desc:
                rows.append(f"""<tr>
<td>&nbsp;</td>
<td width=25>--</td>
<td width=350>{d}</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>""")
        pagevalues['rows'] = '\n'.join(rows)
        pagevalues['totval'] = totval

    print(page.substitute(pagevalues))

except:
    print(f"""Content-type: text/plain\n
<pre>
{traceback.print_exc(file = sys.stdout)}
</pre>""")

# end of file.

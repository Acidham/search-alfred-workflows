#!/usr/bin/python
from Alfred import Items, Tools
from Workflows import Workflows

wf = Workflows()
alf = Items()
wpath = Tools.getEnv('plist_path') + "/info.plist"

keyword_list = wf.get_item(wpath).get('keywords')
if keyword_list:
    for k in keyword_list:
        withspace = k.get('withspace')
        keyw = k.get('keyword')
        keyword = '{0} '.format(keyw) if withspace and keyw else keyw
        title = k.get('title')
        text = k.get('text')
        if keyword:
            alf.setItem(
                title=title,
                subtitle=u'Press \u23CE to proceed with Keyword: %s' % keyword,
                arg=keyword
            )
            alf.setIcon('icons/start.png', m_type='image')
            alf.addItem()
else:
    alf.setItem(
        title="This workflow has not keywords defined",
        valid=False
    )
alf.write()

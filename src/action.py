#!/usr/bin/python

from Alfred import Items

# Script Filter icon [Title,Subtitle,arg/uid/icon]
wf_items = [
    ['Open Workflow', 'Open Workflow in Alfred Preferences', 'open'],
    ['Path to Clipboard', 'Copy Workflow path to Clipoard', 'clipboard'],
    ['Open in Terminal', 'Open Workflow path in Terminal', 'terminal'],
    ['Finder', 'Reveal in Finder', 'finder'],
    ['Forklift', 'Reveal in Forkflift', 'forklift']
]

wf = Items()
for w in wf_items:
    wf.setItem(
        title=w[0],
        subtitle=w[1],
        arg=w[2]
    )
    icon_path = 'icons/' + w[2] + '.png'
    wf.setIcon(icon_path, m_type='image')
    wf.addItem()

wf.write()

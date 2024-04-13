#!/usr/bin/python3

import os

from Alfred3 import Items, Tools

# Script Filter icon [Title,Subtitle,arg/uid/icon]
wf_items = [
    ['Open Workflow', 'Open Workflow in Alfred Preferences', 'open'],
    ['Path to Clipboard', 'Copy Workflow path to Clipoard', 'clipboard'],
    ['Open in Terminal', 'Open Workflow path in Terminal', 'terminal'],
    ['Reveal', 'Reveal Workflow in Finder', 'finder'],
]

cache_exists = os.getenv("cache_exists") 
data_exists = os.getenv("data_exists")   

if cache_exists == "true":
    wf_items.append(['Open cache directory', 'Open Workflow cache in Finder', 'cache'])

if data_exists == "true": 
    wf_items.append(['Open data directory', 'Open Workflow data in Finder', 'data'])

# Add file manager defined in Alfred wf env
file_manager_path = Tools.getEnv('file_manager')
if file_manager_path and os.path.isfile(file_manager_path):
    app_name = os.path.splitext(os.path.basename(file_manager_path))[0]
    wf_items.append([app_name, f"Reveal in {app_name}", "file_manager"])

wf = Items()
for w in wf_items:
    wf.setItem(
        title=w[0],
        subtitle=w[1],
        arg=w[2]
    )
    icon_path = f'icons/{w[2]}.png'
    wf.setIcon(icon_path, m_type='image')
    wf.addItem()

wf.write()

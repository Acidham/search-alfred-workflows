#!/usr/bin/python

from Alfred import Tools, Items
from plistlib import readPlist
import sys
import os

class KeywordFormatter(object):

        def __init__(self):
                self.keywords = list()

        def add_keyword_title(self,keyword,title):
                keyword = keyword if keyword is not None else str()
                title = title if keyword is not None else str()
                self.keywords.append([keyword,title])

        def get_keywords_scriptfilter(self):
                output_keywords = list()
                for i in self.keywords:
                       output_keywords.append(' - '.join(i))
                return " (Keys: " + '; '.join(output_keywords) + ")" if len(output_keywords) > 0 else " (n/a)"

        def get_keywords_md(self):
                formatted_keywords = list()
                result = str()
                for i in self.keywords:
                        formatted_keywords.append("**" + i[0] + "** - " + i[1])
                for i in formatted_keywords:
                       result += "* " + i + "\n"
                return result if len(self.keywords) > 0 else "* n/a"


def get_plist_info(plist_path):
        return readPlist(plist_path)

def get_workflow_plist_paths():
        alfred_dir = Tools.getEnv('alfred_preferences') + "/workflows"
        workflow_dir_names = os.listdir(alfred_dir)
        return [alfred_dir + '/' + f + '/info.plist' for f in workflow_dir_names if os.path.isfile(alfred_dir + '/' + f + '/info.plist')]

def create_hint_file(wf_dir,content):
        target_dir = Tools.getEnv('alfred_workflow_cache')
        if not(os.path.isdir(target_dir)):
                os.mkdir(target_dir)
        spath = os.path.normpath(wf_dir).split(os.sep)
        wf_dir_name = ''.join([i for i in spath if str(i).startswith('user.workflow')])
        if wf_dir_name != str():
                target_file = target_dir + '/' + wf_dir_name + '.md'
                if os.path.isfile(target_file):
                        os.remove(target_file)
                with open(target_file, "w+") as f:
                        f.write(content)
                        return target_file

INPUT_TYPES = [
        'alfred.workflow.input.scriptfilter',
        'alfred.workflow.input.keyword'
        ]
alf = Items()
exclude_disabled = Tools.getEnv('exclude_disabled').lower()
exclude_disabled = True if exclude_disabled == "true" else False
workflow_plist_lists =  get_workflow_plist_paths()
for wf in workflow_plist_lists:
        plist_config = get_plist_info(wf)
        if exclude_disabled and plist_config['disabled']:
                continue
        wf_object = plist_config['objects']
        kf = KeywordFormatter()
        for o in wf_object:
                item_type = o.get('type')
                if item_type in INPUT_TYPES:
                        item_config = o.get('config')
                        keyword = item_config.get('keyword')
                        title = item_config.get('title')
                        text = item_config.get('text')
                        title = title if title is not None else text
                        kf.add_keyword_title(keyword, title)
        content = (
        "# %s\n"
        "\n"
        "### Description\n"
        "* %s\n"
        "\n"
        "### Keywords\n"
        "%s") % (plist_config['name'], plist_config['description'], kf.get_keywords_md())
        quicklook_url = create_hint_file(os.path.dirname(wf),content)
        keyword_text = kf.get_keywords_scriptfilter()
        alf.setItem(
                title=plist_config['name'],
                subtitle=plist_config['description']  +  keyword_text,
                arg=os.path.dirname(wf) + "|" + plist_config['name'],
                type="file",
                quicklookurl=quicklook_url
        )
        alf.addItem()
alf.write()




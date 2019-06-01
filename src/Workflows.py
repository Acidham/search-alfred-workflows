import os
import re
from plistlib import readPlist

from Alfred import Tools


class Workflows(object):
    # Defines which alfred input types are taken
    # when iterating over wofklow items
    INPUT_TYPES = [
        'alfred.workflow.input.scriptfilter',
        'alfred.workflow.input.keyword'
    ]

    def __init__(self):
        """Workflow data represenative
        """
        self.wf_directory = Tools.getEnv('alfred_preferences') + "/workflows"
        exclude_disabled = Tools.getEnv('exclude_disabled').lower()
        self.exclude_disabled = True if exclude_disabled == "true" else False
        self.workflows = self._get_workflows_list()

    def get_workflows(self, reverse=False):
        """Get workflows sorted

        Args:
            reverse (bool, optional): Reverse True. Defaults to False.

        Returns:
            list: All workflows and content (dict) as list items
        """
        return sorted(self.workflows, key=lambda k: k['name'], reverse=reverse)

    def _get_plist_info(self, plist_path):
        """Read plist from given path

        Args:
            plist_path (str): Path to file.plist

        Returns:
            dict: Plist in dict format
        """
        return readPlist(plist_path)

    def get_wf_directory(self):
        """returns wf partent directory

        Returns:
            string: Directory path
        """
        return self.wf_directory

    def get_workflow_plist_paths(self):
        """Get list of all PLIST file paths

        Returns:
            list: list with plist filepaths
        """
        alfred_dir = self.get_wf_directory()
        workflow_dir_names = os.listdir(alfred_dir)
        return [alfred_dir + '/' + f + '/info.plist' for f in workflow_dir_names if os.path.isfile(alfred_dir + '/' + f + '/info.plist')]

    def get_item(self, plist_path):
        """Get content of worfklow item

        Args:
            plist_path (str): Path to info.plist

        Returns:
            dict: Content of info.plist
        """
        plist_info = self._get_plist_info(plist_path)
        name = plist_info['name']
        desc = plist_info['description']
        item_objects = plist_info['objects']
        keyword_list = list()
        for o in item_objects:
            item_type = o.get('type')
            if item_type in self.INPUT_TYPES:
                item_config = o.get('config')
                keyword = item_config.get('keyword')
                title = item_config.get('title')
                text = item_config.get('text')
                title = title if title else text
                withspace = item_config.get('withspace')
                keyword_list.append({
                    'type': item_type,
                    'keyword': keyword,
                    'title': title,
                    'text': text,
                    'withspace': withspace
                })
        if plist_info['disabled'] and self.exclude_disabled:
            return None
        else:
            return {'name': name, 'path': plist_path, 'description': desc, 'keywords': keyword_list}

    def _get_workflows_list(self):
        """Get list of workflows, with content

        Returns:
            list: List of all workflows with content (dict)
        """
        wf_plists = self.get_workflow_plist_paths()
        workflows = list()
        for w in wf_plists:
            i = self.get_item(w)
            if i:
                workflows.append(i)
        return workflows

    def search_in_workflows(self, search_term):
        """Search search_term across all workflows and returns matches

        Args:
            search_term (str): Search term

        Returns:
            list: Workflows matches search
        """
        wfs = self.get_workflows()
        matches = list()
        match = False
        for i in wfs:
            val_list = self._flatten_dict(i)
            for s in val_list:
                if (
                    type(s) == str and
                    search_term.lower() in s.lower()
                ):
                    #re.search(r'\b' + search_term, s, re.IGNORECASE)
                    match = True
            if match:
                matches.append(i)
                match = False
        return matches

    def _flatten_dict(self, tdict):
        """Flatten workflow directory

        Args:
            tdict (dict): Workflow item dict

        Returns:
            list: list of workflow item values
        """
        def filter_list(el):
            """Filter out meta data from worklfow info

            Args:
                el (iteritem): list item

            Returns:
                bool: True when valid item; False when invalid item
            """
            if (
                type(el) == str and
                'alfred.workflow' not in el and
                '/' not in el
            ):
                return True
            else:
                return False

        ret_list = list()
        for t in tdict.itervalues():
            if type(t) == list and len(t) > 0:
                for h in t:
                    ret_list += self._flatten_dict(h)
            # TODO delete after debug
            # elif type(t) != bool and t is not None:
            else:
                ret_list.append(t)
        # TODO: remove if _filter_list is working
        # return self._remove_meta_data(ret_list)
        return filter(filter_list, ret_list)

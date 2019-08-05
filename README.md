# Search-Alfred-Workflows

Search-Alfred-Workflows searches in Title, Keywords, Description of a workflow and shows avaialble keywords for direct execution. It also allows to execute addtional actions on a workflow such as open in terminal or copy worfklow path to the clipboard.

### Search with the shortcut do find the corresponding Workflow

![Screen Shot 2019-08-05 at 07.33.33](README.assets/Screen%20Shot%202019-08-05%20at%2007.33.33.png)

### Action menu on a workflow

![Screen Shot 2019-08-05 at 07.33.42](README.assets/Screen%20Shot%202019-08-05%20at%2007.33.42.png)

## Options

* `ENTER` - Shows a list of keywords in the workflow and starts the workflow with a keyword
* `SHIFT` - Shows the workflow description and associated keywords
* `CMD` - For addtional Actions:
  * Copy path to Clipboard
  * Open WF Folder in Terminal 
    * If you would like to use other terminal than macOS terminal.app change config in Alfred > Features > Terminal to custom
  * Reveal in Finder
  * Open in ForkLift (requires ForkLift installed)

## Config
* exclude_disabled: True - ignore disabled workflow in search

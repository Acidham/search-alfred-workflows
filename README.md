# Search-Alfred-Workflows

Search-Alfred-Workflows searches in Title, Keywords, Description of a workflow and shows avaialble keywords for direct execution. It also allows to execute addtional actions on a workflow such as open in terminal or copy worfklow path to the clipboard.

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

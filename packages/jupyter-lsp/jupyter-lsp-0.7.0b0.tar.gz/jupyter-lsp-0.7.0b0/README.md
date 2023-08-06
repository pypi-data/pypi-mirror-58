# Language Server Protocol integration for Jupyter(Lab)

[![Build Status](https://travis-ci.org/krassowski/jupyterlab-lsp.svg?branch=master)](https://travis-ci.org/krassowski/jupyterlab-lsp) [![Build Status](https://dev.azure.com/krassowskimichal/jupyterlab-lsp/_apis/build/status/jupyterlab-lsp?branchName=master)](https://dev.azure.com/krassowskimichal/jupyterlab-lsp/_build/latest?definitionId=1&branchName=master) [![codebeat badge](https://codebeat.co/badges/f55d0f28-8a84-4199-bc88-f2c306a9ce65)](https://codebeat.co/projects/github-com-krassowski-jupyterlab-lsp-master) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/krassowski/jupyterlab-lsp/master?urlpath=lab%2Ftree%2Fexamples%2FPython.ipynb)

> _This project is in its early days, but you are welcome to check it out, leave feedback and/or a PR_

Quick Links: **[Installation](#installation) | [Language Servers](./LANGUAGESERVERS.md) | [Updating](#updating) | [Changelog](./CHANGELOG.md) | [Roadmap](./ROADMAP.md) | [Contributing](./CONTRIBUTING.md) | [Extending](./EXTENDING.md)**

## Features

> Examples below are for Python, but work for R as well

### Hover

Hover over any piece of code; if an underline appears, you can press <kbd>Ctrl</kbd>
to get a tooltip with function/class signature, module documentation or any other
piece of information that the language server provides

![hover](https://raw.githubusercontent.com/krassowski/jupyterlab-lsp/master/examples/screenshots/hover.png)

### Diagnostics

Critical errors have red underline, warnings are orange, etc. Hover
over the underlined code to see a more detailed message

![inspections](https://raw.githubusercontent.com/krassowski/jupyterlab-lsp/master/examples/screenshots/inspections.png)

### Jump to Definition

Use the context menu entries to jump to definitions

![jump](https://raw.githubusercontent.com/krassowski/jupyterlab-lsp/master/examples/screenshots/jump_to_definition.png)

### Highlight References

Place your cursor on a variable, function, etc and all the usages will be highlighted

### Automatic Completion

Certain characters, for example '.' (dot) in Python, will automatically trigger
completion

![invoke](https://raw.githubusercontent.com/krassowski/jupyterlab-lsp/master/examples/screenshots/auto_invoke.png)

### Automatic Signature Suggestions

Function signatures will automatically be displayed

![signature](https://raw.githubusercontent.com/krassowski/jupyterlab-lsp/master/examples/screenshots/signature.png)

### Kernel-less Autocompletion

Advanced static-analysis autocompletion without a running kernel

![autocompletion](https://raw.githubusercontent.com/krassowski/jupyterlab-lsp/master/examples/screenshots/autocompletion.png)

> When a kernel is available the suggestions from the kernel (such as keys of a
> dict and columns of a DataFrame autocompletion) are merged with the suggestions
> from the Language Server (currently only in notebook).

## Prerequisites

Either:

- JupyterLab >=1.1.4,<1.2
- JupyterLab >=1.2.3,<1.3.0a0
- Python 3.5+
- nodejs 8+

## Installation

For the current stable version:

1. install the server extension:

   ```bash
   pip install --pre jupyter-lsp
   ```

2. install the frontend extension:

   ```bash
   jupyter labextension install @krassowski/jupyterlab-lsp
   ```

3. install LSP servers for languages of your choice; for example, for Python
   ([pyls](https://github.com/palantir/python-language-server)) and
   R ([languageserver](https://github.com/REditorSupport/languageserver)) servers:

   ```bash
   pip install python-language-server[all]
   R -e 'install.packages("languageserver")'
   ```

   or from `conda-forge`

   ```bash
   conda install -c conda-forge python-language-server r-languageserver
   ```

   Please see our full list of
   [supported language servers](./LANGUAGESERVERS.md)
   which includes installation hints for the common package managers (npm/pip/conda).
   In general, any LSP server from the
   [Microsoft list](https://microsoft.github.io/language-server-protocol/implementors/servers/)
   should work after [some additional configuration](./CONTRIBUTING.md#specs).

   Note: it may be worth visiting the repository of each server you install as
   many provide additional configuration options.

4. (Optional, Linux/OSX-only) to enable opening files outside of the root
   directory (the place where you start JupyterLab), create `.lsp_symlink` and
   symlink your `/home`, or any other location which includes the files that you
   wish to make possible to open in there:

   ```bash
   mkdir .lsp_symlink
   cd .lsp_symlink
   ln -s /home home
   ```

   If your user does not have sufficient permissions to traverse the entire path,
   you will not be able to open the file. A more detailed guide on symlinking
   (written for a related jupyterlab-go-to-definition extension) is available
   [here](https://github.com/krassowski/jupyterlab-go-to-definition/blob/master/README.md#which-directories-to-symlink).

### Updating

To update previously installed extensions:

```bash
pip install -U jupyter-lsp
jupyter labextension update @krassowski/jupyterlab-lsp
```

### Getting the latest alpha/beta/RC version

Use `install` command (update does not seem to work) appending `@<0.x.y.rc-z>` to the
extension name, like this:

```bash
jupyter labextension install @krassowski/jupyterlab-lsp@0.7.0-rc.0
```

### Troubleshooting

#### Rename fails with `IndexError`

Question: using rename feature for Python does not work, the statusbar displays `Rename failed: Error: IndexError: list index out of range`

Answer: this is a pyls-specific error which happens when there is a syntax error and rope (the package used by pyls to perform edits) cannot parse the Python file.

Solution: Fix (or comment out) the fragments with syntax errors as indicated by diagnostics feature first, and try again.

## Acknowledgements

This would not be possible without the fantastic initial work at
[wylieconlon/lsp-editor-adapter](https://github.com/wylieconlon/lsp-editor-adapter).

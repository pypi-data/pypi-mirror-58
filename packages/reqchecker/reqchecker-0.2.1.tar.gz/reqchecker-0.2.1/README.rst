==========
reqchecker
==========

Compare python package requirements across packages by reading the specified requirements files.


Install
--------
Clone this repository::

  $ git clone https://github.com/robertson-mark/reqchecker

Install::

  $ python setup.py install


Usage
--------
reqchecker gathers requirements by using a ``.json`` file formatted as::

    {
      "default": {
        "source": {"package": "path",
                   "package": "path"}
                },

      "my-home": {
        "source": {"package": "path",
                   "package": "path"}
                },

      "my-github": {
        "github": {"package": "branch",
                   "package": "branch",
                   "package": "branch"},
        "credentials": "<path_to_credentials.json>"
                }
    }

A ``default`` field is required, additional sections, in this case ``my-local`` and ``my-github`` can be added and called from the command line.

- ``source`` can be 'local' or 'github'

  | If 'local', must supply 'path' to repository
  | If 'github', must also include 'credentials' and path to a credentials.json file

The credentials.json file looks like::

    {
      "user": "github_user",
      "token": "github_token"
    }


To use by calling the ``"defaults"`` section::

  $ reqchecker

To change the section to read from the saved settings in ``"my-home"``::

  $ reqchecker --section my-home

The user can also overwrite sections by including --packages and --locations with the ``my-home`` option, and --packages and --branches with the ``github`` option.

To call using a different .json than is in this repository::

  $ reqcheckert --file <file>

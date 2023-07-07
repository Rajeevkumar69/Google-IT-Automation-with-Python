import : The term 'import' is not recognized as the name of a cmdlet,
function, script file, or operable program. Check the spelling of the
name, or if a path was included, verify that the path is correct and
try again.
At line:1 char:1

- import pip
- ```
    + CategoryInfo          : ObjectNotFound: (import:String) [], Comm
   andNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
  ```

PS C:\Users\rajee> pip install
ERROR: You must give at least one requirement to install (see "pip help install")
PS C:\Users\rajee> pip help

Usage:
C:\Users\rajee\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip <command> [options]

Commands:
install Install packages.
download Download packages.
uninstall Uninstall packages.
freeze Output installed packages in requirements format.
inspect Inspect the python environment.
list List installed packages.
show Show information about installed packages.
check Verify installed packages have compatible dependencies.
config Manage local and global configuration.
search Search PyPI for packages.
cache Inspect and manage pip's wheel cache.
index Inspect information available from package indexes.
wheel Build wheels from your requirements.
hash Compute hashes of package archives.
completion A helper command used for command completion.
debug Show information useful for debugging.
help Show help for commands.

General Options:
-h, --help Show help.
--debug Let unhandled exceptions propagate
outside the main subroutine, instead of
logging them to stderr.
--isolated Run pip in an isolated mode, ignoring
environment variables and user
configuration.
--require-virtualenv Allow pip to only run in a virtual
environment; exit with an error
otherwise.
--python <python> Run pip with the specified Python
interpreter.
-v, --verbose Give more output. Option is additive,
and can be used up to 3 times.
-V, --version Show version and exit.
-q, --quiet Give less output. Option is additive,
and can be used up to 3 times
(corresponding to WARNING, ERROR, and
CRITICAL logging levels).
--log <path> Path to a verbose appending log.
--no-input Disable prompting for input.
--keyring-provider <keyring_provider>
Enable the credential lookup via the
keyring library if user input is
allowed. Specify which mechanism to use
[disabled, import, subprocess].
(default: disabled)
--proxy <proxy> Specify a proxy in the form scheme://[us
er:passwd@]proxy.server:port.
--retries <retries> Maximum number of retries each
connection should attempt (default 5
times).
--timeout <sec> Set the socket timeout (default 15
seconds).
--exists-action <action> Default action when a path already
exists: (s)witch, (i)gnore, (w)ipe,
(b)ackup, (a)bort.
--trusted-host <hostname> Mark this host or host:port pair as
trusted, even though it does not have
valid or any HTTPS.
--cert <path> Path to PEM-encoded CA certificate
bundle. If provided, overrides the
default. See 'SSL Certificate
Verification' in pip documentation for
more information.
--client-cert <path> Path to SSL client certificate, a single
file containing the private key and the
certificate in PEM format.
--cache-dir <dir> Store the cache data in <dir>.
--no-cache-dir Disable the cache.
--disable-pip-version-check
Don't periodically check PyPI to
determine whether a new version of pip
is available for download. Implied with
--no-index.
--no-color Suppress colored output.
--no-python-version-warning
Silence deprecation warnings for
upcoming unsupported Pythons.
--use-feature <feature> Enable new functionality, that may be
backward incompatible.
--use-deprecated <feature> Enable deprecated functionality, that
will be removed in the future.
PS C:\Users\rajee> pip install
ERROR: You must give at least one requirement to install (see "pip help install")
PS C:\Users\rajee> --no-color
At line:1 char:3

- --no-color
- ~
  Missing expression after unary operator '--'.
  At line:1 char:3
- --no-color
- ```
  Unexpected token 'no-color' in expression or statement.
      + CategoryInfo          : ParserError: (:) [], ParentContainsError
     RecordException
      + FullyQualifiedErrorId : MissingExpressionAfterOperator


      Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import shutil
  >>> du = shutil.disk_usage("/")
  >>> print(du)
  usage(total=249271676928, used=74572349440, free=174699327488)
  >>> du.free/du.total
  0.7008390589776488
  >>> du.free/du.total*100
  70.08390589776488
  >>> import psutil
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ModuleNotFoundError: No module named 'psutil'
  >>> import psutil
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ModuleNotFoundError: No module named 'psutil'
  >>> pip install psutil
    File "<stdin>", line 1
      pip install psutil
          ^^^^^^^
  SyntaxError: invalid syntax
  >>> import psutil
  >>> psutil.cpu_percent(0.1)
  0.0
  >>> psutil.cpu_percent(0.1)
  0.0
  >>> psutil.cpu_percent(0.1)
  4.0
  >>> psutil.cpu_percent(0.1)
  86.5
  >>> psutil.cpu_percent(0.1)
  0.0
  >>> psutil.cpu_percent(0.1)
  10.3
  >>> psutil.cpu_percent(0.5)
  3.9
  >>> psutil.cpu_percent(0.5)
  4.7
  >>> psutil.cpu_percent(0.5)
  3.1
  >>> exit()
  PS C:\Users\rajee> python3
  Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>>
  ```

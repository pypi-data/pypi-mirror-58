Configuration
-------------

Since version 1.0 `pybliometrics` (formerly `scopus`) uses a config file `~/.scopus/config.ini`.  I saves credentials as well as directory names for folders that store cached files.

To change your key or to change directories for cached files, edit this file manually and `import pybliometrics` again.

If the configuration file does not exist, `pybliometrics` will raise a warning.  To generate the configuration file, issue the command

.. code-block:: python

    >>> pybliometrics.scopus.utils.create_config()


after `import pybliometrics`.

`pybliometrics` then prompts you for your credentials.  Most users only need to provide the API Key and hit enter on the second prompt.  If you have to use InstToken authentication, enter it in the second step.  If you need to use a Proxy, please edit the file manually to include a section that looks like so:

.. code-block:: batch

    [Proxy]
    ftp = socks5://127.0.0.1:1234
    http = socks5://127.0.0.1:1234
    https = socks5://127.0.0.1:1234


The presence of this information will make use of the proxy, so be sure to remove the block when you don't want to use a proxy.

Folder `~/` refers to your private home directory or home path.  On many Windows machines this is usually `C:/Document and Settings/<Your User Name>`.  In there you find a hidden folder `.scopus`, which is also the directory where `pybliometrics` caches downloaded files.

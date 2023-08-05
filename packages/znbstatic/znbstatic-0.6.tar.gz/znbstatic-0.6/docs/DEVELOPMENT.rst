Development Notes
==================================================================================

**Important**: Do not share this Docker image with your private key information.

Using a temporary, local Docker container with an ssh private key and some Python 3 packages for initial tests.

Change to the root directory of this repository, where the Dockerfile and setup.py files are, and build the image.

.. code-block:: bash

  $ docker build -t znbstatic .

Optional: Use a username (example here), a version number and $(date) to tag the image.

.. code-block:: bash

  $ docker build --build-arg SSH_PRIVATE_KEY="$(cat ~/.ssh/id_rsa)" -t example/znbstatic:0.1-$(date +%Y%m%d) .

While still in the same directory, run the container and make sure you don't map over /root in the container because that's where ssh key from the host is stored. Replace image:tag with what you used above, for example, znbstatic:latest or example/znbstatic:0.1-20190306.

.. code-block:: bash

  $ docker run -it --rm --mount type=bind,source=$PWD,target=/root/project image:tag docker-entrypoint.sh /bin/bash

This will map /root/project inside the container to the host directory where setup.py is, the root of the repository, and set the Python environment so that pip can do its job.

List the installed packages.

.. code-block:: bash

  $ pip list

Install into the environment's Python path.

.. code-block:: bash

  $ pip install /root/project/

or install in editable mode so that nothing is copied and you can make changes in the source code.

.. code-block:: bash

  $ pip install -e /root/project/

To uninstall the package.

.. code-block:: bash

  $ pip uninstall znbstatic

Configuration and Django settings.py
------------------------------------------------------------------------------

Review partial-settings.py in the docs directory.

Distribute as a setuptools-based Package
------------------------------------------------------------------------------

This can be run from a host or a container. My tests have been on a container.

.. code-block:: bash

  $ pip install setuptools wheel twine

Run this from the same directory where setup.py is located.

.. code-block:: bash

  $ python setup.py sdist bdist_wheel

Upload to Test PyPi at `<https://test.pypi.org>`_.

  $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*

The package is now available at `<https://test.pypi.org/project/znbstatic/>`_ and can be installed with pip.

.. code-block:: bash

  $ pip install -i https://test.pypi.org/simple/ znbstatic

Upload to the real PyPi at `<https://pypi.org>`_.

.. code-block:: bash

  $ twine upload dist/*

The package is now available at `<https://pypi.org/project/znbstatic/>`_ and can be installed with pip.

.. code-block:: bash

  $ pip install znbstatic

Additional Resources
------------------------------------------------------------------------------

  * `packaging projects <https://packaging.python.org/tutorials/packaging-projects>`_.
  * `sample project on GitHub <https://github.com/pypa/sampleproject>`_.
  * `setuptools <https://setuptools.readthedocs.io/en/latest/setuptools.html>`_.
  * `pip install <https://pip.pypa.io/en/stable/reference/pip_install>`_ documentation.
  * `include additional files with distribution <https://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files>`_.

.. index:: ! FAQ

.. _FAQ:

==========================
Frequently Asked Questions
==========================

A collection of commonly-asked questions concerning Bluesky.

.. _faq-install-bluesky:

How to install Bluesky?
~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`instrument.install`

.. _faq-start-bluesky-session:

How to start a Bluesky session?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :doc:`Getting Started </howto/getting_started>`

.. _faq-alias-start-bluesky:

How to create an alias to start a bluesky session?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several ways to create an alias to start a bluesky session. One is described
:ref:`here <reference.configure_ipython_profile>`.

.. _faq-alias-become-bluesky:

How to create an alias to activate the bluesky environment?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section: :ref:`reference.create_conda-bluesky_alias`, look for ``become_bluesky``.

.. _faq-alias-time-series:

How to record a time series?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :doc:`Time Series </howto/_time_scan>` for a few examples.


.. _faq-obj-oriented:

In python, what are classes, objects, methods and instances?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- A **class** is like a blueprint or a template that defines the
  characteristics and behaviors of a particular type of object. For example,
  we can define a `Dog` class that includes attributes such as breed, age,
  and name, as well as behaviors such as barking and wagging its tail.
- An **object** is an **instance** of a class. So, if we have a `Dog` class,
  we can create objects of that class, such as "Fido" and "Buddy". Each
  object of the `Dog` class will have its own set of **attributes**, such as
  "Fido" being a Golden Retriever and "Buddy" being a Chihuahua, and
  **methods**, such as "Fido" barking loudly and "Buddy" wagging its tail.
- An **instance** is a specific occurrence of an **object** created from a
  **class**. For example, with our `Dog` class, we can create an instance of
  that class called "my_dog" with specific attributes and behaviors.
- A **method** is a function that is defined in a **class** and can be
  called on an **object** of that class. For example, the "bark" method
  defined in the `Dog` class can be called on the object "my_dog" to make it
  bark.

For more details:

- `python.org tutorial <https://docs.python.org/3/tutorial/classes.html>`_
- `Learn to code <https://www.w3schools.com/python/python_classes.asp>`_
- `Naming convention <https://namingconvention.org/python/>`_

.. _faq-bash:

What is bash?
~~~~~~~~~~~~~

Bash is a type of shell, which is a program that provides a user interface
for accessing the operating system's services. To determine if you're using
bash, you can open up a terminal on your computer and type **echo $SHELL**.
If the output is **/bin/bash** or something similar, then you're using the
bash shell.

If bash is not your default shell, type **bash** in a terminal and press
Enter to start a new instance of the bash shell. You should see a new prompt
indicating that you're now using the bash shell. You can now type in bash
commands. Note that any changes you make to your environment variables or
other system settings within this bash session will only apply to this
session and will not persist after you close the session. To change your
default shell, contact your IT support.

.. _faq-linux-tilde:

What does the (**~**) mean in a path?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tilde (**~**) character represents the current user's home directory.
This is a shortcut that can be used to specify file paths without having to
type out the entire path to the home directory.

.. _faq-timestamp:

How to understand a timestamp?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Timestamps are floating point numbers offset from a fixed reference
(1970-01-01 00:00 UTC).  Convert that to a format for humans using the
*datetime* package (assuming the local time zone, in this case
`"US/Chicago"`):

.. code-block:: python
    :linenos:

    In [1]: import datetime

    In [2]: datetime.datetime.fromtimestamp(1685123274.1847932)
    Out[2]: datetime.datetime(2023, 5, 26, 12, 47, 54, 184793)

    In [3]: str(datetime.datetime.fromtimestamp(1685123274.1847932))
    Out[3]: '2023-05-26 12:47:54.184793'

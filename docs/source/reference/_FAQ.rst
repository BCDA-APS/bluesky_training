.. index:: ! FAQ

.. _FAQ:

==========================
Frequently Asked Questions
==========================

This is a list of commonly asked questions concerning Bluesky.

.. _faq-install-bluesky:

1. How to install Bluesky? 

    Visit `Bluesky Installation <https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html>`_

.. _faq-start-bluesky-session:

2. How to start a Bluesky session? 

    Visit `Getting started <https://bcda-aps.github.io/bluesky_training/instrument/_getting_started.html>`_

.. _faq-alias-start-bluesky:

3. How to create an alias to start a bluesky session? 

    There are several way to create an alias to start a bluesky session. One is described 
    `here <https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html#Create-a-bluesky-ipython-profile>`_.

.. _faq-alias-become-bluesky:

4. How to create an alias to activate the bluesky environment? 

    Visit `here <https://bcda-aps.github.io/bluesky_training/reference/_create_conda_env.html#Create-an-alias-to-activate-the-bluesky-environment>`_.


.. _faq-obj-oriented:

5. In python, what are classes, objects, methods and instances??

    - A **class** is like a blueprint or a template that defines the characteristics and behaviors of a particular type of object. For example, we can define a `Dog` class that includes attributes such as breed, age, and name, as well as behaviors such as barking and wagging its tail.
    - An **object** is an **instance** of a class. So, if we have a `Dog` class, we can create objects of that class, such as "Fido" and "Buddy". Each object of the `Dog` class will have its own set of **attributes**, such as "Fido" being a Golden Retriever and "Buddy" being a Chihuahua, and **methods**, such as "Fido" barking loudly and "Buddy" wagging its tail.
    - An **instance** is a specific occurrence of an **object** created from a **class**. For example, with our `Dog` class, we can create an instance of that class called "my_dog" with specific attributes and behaviors.
    - A **method** is a function that is defined in a **class** and can be called on an **object** of that class. For example, the "bark" method defined in the `Dog` class can be called on the object "my_dog" to make it bark.

    For more details:

    - `python.org tutorial <https://docs.python.org/3/tutorial/classes.html>`_
    - `Learn to code <https://www.w3schools.com/python/python_classes.asp>`_
    - `Naming convention <https://namingconvention.org/python/>`_

.. _faq-bash:

6. What is bash?


    Bash is a type of shell, which is a program that provides a user interface for accessing the operating system's services.
    To determine if you're using bash, you can open up a terminal on your computer and type <code><b>echo $SHELL</b></code>.
    If the output is <code><b>/bin/bash</b></code> or something similar, then you're using the bash shell.
    
    If bash is not your default shell, type <code><b>bash</b></code> in a terminal and press Enter to start a new instance of the bash shell. You should see a new prompt indicating that you're now using the bash shell. You can now type in bash commands. 
    Note that any changes you make to your environment variables or other system settings within this bash session will only apply to this session and will not persist after you close the session. To change your default shell, contact your IT support. 

.. _faq-linux-tilde:

7. What does the (<code><b>~</b></code>) mean in a path?

    The tilde (<code><b>~</b></code>) character represents the current user's home directory. This is a shortcut that can be used to specify file paths without having to type out the entire path to the home directory.


Touchstone
==========

.. contents::
   :depth: 2
   :backlinks: none

What is Touchstone?
-------------------

Touchstone is an annotations-driven Inversion of Control container for
Python 3.6 and above.

Links:

* `GitHub <https://github.com/gmaybrun/touchstone>`__


Learn by Example
----------------

Auto Wiring
~~~~~~~~~~~

.. code:: python

    from touchstone import Container

    class Child:
        pass

    class Parent:
        def __init__(self, child: Child) -> None:
            self.child = child


    container = Container()
    parent = container.make(Parent)

    assert isinstance(parent.child, Child)

Interface Binding
~~~~~~~~~~~~~~~~~

.. code:: python

    from touchstone import Container

    class AbstractChild:
        pass

    class Child(AbstractChild):
        pass

    class Parent:
        def __init__(self, child: AbstractChild) -> None:
            self.child = child


    container = Container()
    container.bind(AbstractChild, Child)
    parent = container.make(Parent)

    assert isinstance(parent.child, Child)

Binding with Factory Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from touchstone import Container

    class Child:
        def __init__(self, name: str) -> None:
            self.name = name

    class Parent:
        def __init__(self, child: Child) -> None:
            self.child = child


    container = Container()
    container.bind(Child, lambda: Child('them'))
    parent = container.make(Parent)

    assert isinstance(parent.child, Child)
    assert parent.child.name == 'them'

Binding Singletons
~~~~~~~~~~~~~~~~~~

.. code:: python

    from touchstone import Container, SINGLETON

    class Child:
        def __init__(self, name: str) -> None:
            self.name = name

    class Parent:
        def __init__(self, child: Child) -> None:
            self.child = child


    container = Container()
    them_child = Child('them')
    container.bind_instance(Child, them_child)
    # Or...
    container.bind(Child, lambda: them_child, lifetime_strategy=SINGLETON)
    parent = container.make(Parent)

    assert isinstance(parent.child, Child)
    assert parent.child is them_child

Contextual Binding
~~~~~~~~~~~~~~~~~~

.. code:: python

    from touchstone import Container

    class Child:
        def __init__(self, name: str) -> None:
            self.name = name

    class Parent:
        def __init__(self, child1: Child, child2: Child) -> None:
            self.child1 = child1
            self.child2 = child2


    container = Container()
    container.bind_contextual(when=Parent, wants=Child, wants_name='child1', give=lambda: Child('her'))
    container.bind_contextual(when=Parent, wants=Child, wants_name='child2', give=lambda: Child('him'))
    parent = container.make(Parent)

    assert isinstance(parent.child1, Child)
    assert isinstance(parent.child2, Child)
    assert parent.child1.name == 'her'
    assert parent.child2.name == 'him'

Django Support
--------------

Now featuring Django support! New in v0.3.0

* Configure your instance of ``touchstone.Container`` however you see fit.
* In your main ``settings.py``, set ``TOUCHSTONE_CONTAINER_GETTER`` to
  the path to a callable that will return the singleton instance of
  ``touchstone.Container`` your app uses.

  * Note that your ``getter`` should build the ``Container`` precisely once, and
    then return that same ``Container`` on all subsequent calls. Build it as a
    singleton.

To get injected properties in your class-based views:

* In your main ``settings.py``, add ``touchstone.django.InjectViewsMiddleware``
  to your ``MIDDLEWARE`` list.
* Use class annotations on your class-based views. Cached Properties will be
  added to your view classes so that they automatically resolve using your
  configured touchstone container. For example:

.. code:: python

    class MyView(View):
        something: MyObject
        def get(self, request):
            # You can now access self.something!

To get injected properties in your middleware, you'll need to do a
little more work because we haven't found a good way to hook into
Django's middleware instantiation logic.

.. code:: python

    from touchstone.django import inject_magic_properties

    @inject_magic_properties
    class MyMixin:
        something: MyObject
        # define your mixin here...
        # You'll be able to use `self.something` from within every instance method.

Celery Tasks
~~~~~~~~~~~~

Celery tasks called can be applied to any callable with a decorator. For example:

.. code:: python

    class MyLogger:
        def __init__(self, another_logger: AnotherLogger):
            self.another_logger = another_logger

        def log(self, msg):
            print(msg)
            self.another_logger.log(msg)

    @app.task
    def log_messages(msg):
        another_logger = AnotherLogger()
        my_logger = MyLogger(another_logger)

        my_logger.log(msg)

    log_messages.apply_async(args=['hello world'])

However, if we want to refactor this code to make use of touchstone as a service locator:

.. code:: python

    class MyLogger:
        def __init__(self, another_logger: AnotherLogger):
            self.another_logger = another_logger

        def log(self, msg):
            print(msg)
            self.another_logger.log(msg)

    @app.task
    def log_messages(msg):
        container = get_container()
        my_logger = container.make(MyLogger)

        my_logger.log(msg)

    log_messages.apply_async(args=['hello world'])

Each task would then have quite a bit of repeated code to create the container for each task and then
make class instance we need.

.. code:: python

    class MyLogger:
        def __init__(self, another_logger: AnotherLogger):
            self.another_logger = another_logger

        def log(self, msg):
            print(msg)
            self.another_logger.log(msg)

    @touchstone_task
    class LogMessagesTask:
        my_logger: MyLogger

        def run(self, msg):
            self.my_logger.log(msg)

    LogMessagesTask.apply_async(args=['hello world'])

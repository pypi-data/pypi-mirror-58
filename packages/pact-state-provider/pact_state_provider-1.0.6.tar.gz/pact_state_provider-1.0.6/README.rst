pact-state-provider
=======================

> Simple server to provide an endpoint used by pact to generate a provider state

.. image:: https://badge.fury.io/py/pact-state-provider.svg
    :target: https://badge.fury.io/py/pact-state-provider
    :alt: PyPi Status

.. image:: https://travis-ci.org/nalch/pact-state-provider.svg?branch=master
    :target: https://travis-ci.org/nalch/pact-state-provider
    :alt: Travis Status

.. image:: https://readthedocs.org/projects/pact-state-provider/badge/?version=latest
    :target: https://pact-state-provider.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Usage
-----

Installation
************
1. Install the package::

    pip install pact_state_provider


Client
******
Entrypoint :code:`pact-state-provider`::

    Usage: pact-state-provider [OPTIONS]

    Start the state provider server on the specified host and port.

    Options:
        --base-module TEXT  Module containing the state providers.
        --host TEXT         Host for the endpoint.
        --port INTEGER      Port for the endpoint.
        --help              Show this message and exit.

TL;DR
*****
Example::

    pact-state-provider --base-module my_provider.states
    # pact requests a state:
    # GET http://127.0.0.1:1235 {'consumer': 'TestConsumer', 'state': 'user exists'}
    -> function "my_provider.states.user_exists('TestConsumer')" is executed

Not Long Enough;Will Read
*************************
When verifying contracts with `Pact <https://docs.pact.io/getting_started/provider_states>`_ a
state provider is called for the particular consumer with the state requested. A consumer
:code:`TestConsumer` with a contract starting with :code:`given('user exists')` requests the
configured endpoint with the payload::

    {
        'consumer': 'TestConsumer',
        'state': 'user exists'
    }

In order to execute the specific provider functions without having to implement a dedicated
endpoint on the provider or a dedicated application with provider specific code
:code:`pact-state-provider` provides a simple http server endpoint which calls an existing
module function based on the request payload.

In the given example a function called :code:`user_exists` (invalid characters are translated to
underscores) will be executed on the specified base module (:code:`--base-module` parameter).

This gives the user to maintain the state provider code in the actual provider codebase, but
easily have an endpoint to use with pact.

Development
-----------

Makefile
********

This project uses a Makefile for various tasks. Some of the available tasks
are listed below.

* `make clean` - Clean build artifacts out of your project
* `make test` - Run Tests
* `make plain-test` - Run Tests without rebuilding the project
* `make sdist` - Build a Python source distribution
* `make docs` - Build the Sphinx documentation
* `make lint` - Get a codestyle report about your code
* `make plain-lint` - Get a codestyle report without rebuilding the project
* `make` - Equivalent to `make test lint docs sdist`

Command-line options
====================

To run a test, use the **molotov** runner and point it to
the scenario module or path:

.. code-block:: bash

    $ molotov --help
    usage: molotov [-h] [--statsd] [--statsd-host STATSD_HOST]
                [--statsd-port STATSD_PORT] [--version] [--debug] [-v]
                [-w WORKERS] [-p PROCESSES] [-d DURATION] [-q] [-x] [-c]
                scenario

    Load test.

    positional arguments:
    scenario              path or module name that contains scenarii

    optional arguments:
    -h, --help            show this help message and exit
    --statsd              Sends metrics to Statsd.
    --statsd-host STATSD_HOST
                            Statsd host.
    --statsd-port STATSD_PORT
                            Statsd port.
    --version             Displays version and exits.
    --debug               Run the event loop in debug mode.
    -v, --verbose         Verbose
    -w WORKERS, --workers WORKERS
                            Number of workers
    -p PROCESSES, --processes PROCESSES
                            Number of processes
    -d DURATION, --duration DURATION
                            Duration in seconds
    -q, --quiet           Quiet
    -x, --exception       Stop on first failure.
    -c, --console         Use simple console for feedback




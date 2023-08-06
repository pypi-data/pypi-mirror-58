# protolog
Tools to analyse and log data from smart metering devices

We have been copy-pasting these simple server classes onto servers when we have had the 
need to analyse protocol data. It was time to gather them in a git reop and make it 
a bit nicer to manage.

We use Pythons super simple `socketserver` module. The servers are for testing purpose 
only. We use the threading mixin to be able to process several requests at the same time.

## Install

Only python 3.6+

```
pip install protolog
```

## UDP

To run a UDP logging server 

```
protolog udp --port 4000
```

To know more use the --help argument

```
protolog --help

Usage: protolog [OPTIONS] COMMAND [ARGS]...

  CLI to run simple protocol loggers by Palmlund Wahlgren Innovative
  Technology AB

Options:
  --help  Show this message and exit.

Commands:
  udp

```

```
protolog udp --help

Usage: protolog udp [OPTIONS]

  Runs a threaded UDP server that logs all datagrams it receives. It can
  alos act as an UDP echo server using the --echo flag

Options:
  -h, --host TEXT     Host to bind the server too
  -p, --port INTEGER  Port to bind the server too
  -e, --echo          If the server should echo the data back to the sender
  --help              Show this message and exit.

```




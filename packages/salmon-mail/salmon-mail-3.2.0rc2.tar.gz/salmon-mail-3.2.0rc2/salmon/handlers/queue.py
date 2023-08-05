"""
Implements a handler that puts every message it receives into
the run/queue directory.  It is intended as a debug tool so you
can inspect messages the server is receiving using mutt or
the salmon queue command.
"""

import logging

from salmon import handlers, queue
from salmon.routing import nolocking, route_like, stateless


@route_like(handlers.log.START)
@stateless
@nolocking
def START(message, to=None, host=None):
    """
    @stateless and routes however handlers.log.START routes (everything).
    Has @nolocking, but that's alright since it's just writing to a Maildir.
    """
    logging.debug("MESSAGE to %s@%s added to queue.", to, host)
    q = queue.Queue('run/queue')
    q.push(message)

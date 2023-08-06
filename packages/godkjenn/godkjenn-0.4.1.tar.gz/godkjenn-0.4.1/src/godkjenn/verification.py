"""The core approval testing algorithm.

This is where we check the latest *received* data with the latest *accepted* data.
"""


def verify(test_id, vault, received):
    """Check if `received` matches the current accepted value for the test_id.

    If `received` doesn't match the accepted value, this will raise MismatchError§.

    Args:
        test_id: The ID of the test that produced `received`.
        vault: The vault containing the approved data.
        received: A bytes object representing the received data.
    """
    try:
        accepted = vault.accepted(test_id)
        if received == accepted:
            return
        message = "Received data does not match accepted"
    except KeyError:
        accepted = None
        message = "There is no accepted data"

    vault.receive(test_id, received)
    raise MismatchError(message, received, accepted)


class MismatchError(Exception):
    def __init__(self, message, received, accepted):
        super().__init__(message)
        self._received = received
        self._accepted = accepted

    @property
    def message(self):
        return self.args[0]

    @property
    def received(self):
        return self._received

    @property
    def accepted(self):
        return self._accepted

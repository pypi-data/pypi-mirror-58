import os
from pathlib import Path

import pytest

import godkjenn.config
from godkjenn.plugins import get_vault
from godkjenn.verification import verify, MismatchError


def pytest_addoption(parser):
    parser.addini('godkjenn_config', 'Path to godkjenn configuration file')


INSTRUCTIONS = """{message}

If you wish to accept the received result, run:

    godkjenn accept {options} "{test_id}"
"""


def _make_instructions(message, test_id, pytest_config):
    """Calculate 'accept' instructions. 

    Args:
        message: Any message to put before the instructions.
        test_id: The string id of the test.
        pytest_config: The full pytest configuration object.

    Returns: A string representing a command to run that will accept the received data.
    """
    pt_root = pytest_config.rootdir.relto(os.getcwd())
    gk_path = Path(pt_root) / pytest_config.getini('godkjenn_config')

    if gk_path.exists() and gk_path.is_file():
        options = "--config={}".format(gk_path)
    else:
        options = "--root-dir={}".format(pt_root)

    return INSTRUCTIONS.format(
        message=message,
        test_id=test_id,
        options=options)


def pytest_runtest_makereport(item, call):
    """pytest hook that runs to generate specialized reports.

    We find all Approver fixture arguments and generate a test report containing instructions on how to proceed (e.g.
    update the accepted value if desired).
    """
    import _pytest.runner

    if call.when == 'call' and call.excinfo is not None:
        exc = call.excinfo.value

        # The test may have failed for reasons besides verification failure.
        if not isinstance(exc, MismatchError):
            return

        # There are potentially more than one approver, so we loop over them.
        for approver in _approver_args(item):
            instructions = _make_instructions(
                exc.message,
                approver._test_id,
                item.config)
            return _pytest.runner.TestReport(
                location=item.location,
                keywords=item.keywords,
                outcome='failed',
                when=call.when,
                nodeid=item.nodeid,
                longrepr=instructions,
            )


@pytest.fixture(scope='session')
def godkjenn_config(pytestconfig):
    """Get the godkjenn configuration.

    If the pytest.ini specifies a config file, we'll try to use that. If it doesn't, we'll look for 'godkjenn.toml' in
    the root directory. If either exists, we load it (as TOML) and return the 'godkjenn' section. If there is no
    'godkjenn' section, we'll return a default configuration.
    """
    config_path = pytestconfig.getini('godkjenn_config')
    if not config_path:
        return godkjenn.config.default_config(str(pytestconfig.rootdir))

    config_path = Path(str(pytestconfig.rootdir / config_path))
    return godkjenn.config.load_config(config_path)


@pytest.fixture(name='godkjenn')
def godkjenn_fixture(request, godkjenn_config):
    "Returns an object on which you can call `verify()`."
    test_id = request.node.nodeid
    vault = get_vault(godkjenn_config)
    return Approver(test_id, vault)


class Approver:
    """Type returned from the godkjenn fixture.

    Users can call the `verify()` method to check their latest results.
    """

    def __init__(self, test_id, vault):
        self._vault = vault
        self._test_id = test_id

    def verify(self, received):
        """Check the latest received data against the accepted version.

        If there's a mismatch, this will trigger a pytest failure (i.e. via `assert`).

        Args:
            received: The received test data to be compared with the approved.
        """
        verify(self._test_id, self._vault, received)


def _approver_args(item):
    "Find all Approver fixture arguments to a test item."
    for arg in item.funcargs.values():
        if isinstance(arg, Approver):
            yield arg

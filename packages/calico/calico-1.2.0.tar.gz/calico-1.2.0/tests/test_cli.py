from __future__ import absolute_import, division, print_function, unicode_literals

from pytest import mark, raises

import os
import sys

PY2 = sys.version_info.major < 3

if not PY2:
    from unittest.mock import mock_open, patch

from pkg_resources import get_distribution

from calico import cli

base_dir = os.path.dirname(__file__)
circle_spec_file = os.path.join(base_dir, "circle.yaml")


def test_help_should_print_usage_and_exit(capsys):
    with raises(SystemExit):
        cli.main(argv=["calico", "--help"])
    out, err = capsys.readouterr()
    assert out.startswith("usage: ")


def test_cli_version_should_print_version_number_and_exit(capsys):
    version = get_distribution("calico").version
    with raises(SystemExit):
        cli.main(argv=["calico", "--version"])
    out, err = capsys.readouterr()
    assert out if not PY2 else err == "calico %(ver)s\n" % {"ver": version}


def test_no_spec_file_should_print_usage_and_exit(capsys):
    with raises(SystemExit):
        cli.main(argv=["calico"])
    out, err = capsys.readouterr()
    assert err.startswith("usage: ")
    assert ("required: spec" in err) or ("too few arguments" in err)


def test_existing_spec_file_should_be_ok(capsys):
    cli.main(argv=["calico", circle_spec_file])
    out, err = capsys.readouterr()
    assert err == ""


def test_non_existing_spec_file_should_exit_with_error(capsys):
    with raises(SystemExit):
        cli.main(argv=["calico", "dummy.spec"])
    out, err = capsys.readouterr()
    assert "No such file or directory:" in err


# TODO: add tests for -d option


def test_non_existing_base_directory_should_exit_with_error(capsys):
    with raises(SystemExit):
        cli.main(argv=["calico", "-d", "dummy", circle_spec_file])
    out, err = capsys.readouterr()
    assert "No such file or directory:" in err


def test_validate_valid_spec_file_should_not_print_output(capsys):
    cli.main(argv=["calico", "--validate", circle_spec_file])
    out, err = capsys.readouterr()
    assert out == ""


@mark.skipif(PY2, reason="has to mock builtins.open")
def test_validate_invalid_spec_file_should_exit_with_error(capsys):
    with patch("builtins.open", mock_open(read_data=""), create=True):
        with raises(SystemExit):
            cli.main(argv=["calico", "--validate", circle_spec_file])
        out, err = capsys.readouterr()
        assert "No test specification" in err


# TODO: add tests for --quiet option


# TODO: add tests for --log option


# TODO: add tests for --debug option


# TODO: add tests for summary output

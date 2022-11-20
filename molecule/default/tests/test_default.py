"""Role testing files using testinfra."""

import pytest
from os.path import join as path_join


def test_brewfile(host):
    file = host.file("/home/linuxbrew/.Brewfile")
    assert file.exists
    assert file.is_file
    assert (
        file.sha256sum
        == "9ef9e40fe20262455d66c6b435e96ca428658baeeb97fe5b934752afd90e9908"
    )

def test_brewfile_syntax(host):
    assert host.run("brew bundle list --global").rc == 0

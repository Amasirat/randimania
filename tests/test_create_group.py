import modules.core as core

def test_default_create_group():
    core.create_group("drawing")

def test_chdir_create_group():
    core.create_group("draw", "gro/")
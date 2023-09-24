import modules.core as core

def test_random_pull():
    core.random_pull("drawing")
    
def test_random_pull_music():
    for i in range(1,20):
        core.random_pull("music")

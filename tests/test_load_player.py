import pytest
from main import PlayerStats

# If "player_data.json" is not empty, check the document to assert the actual saved data
def test_load_player():
    player = PlayerStats.load_data()
    assert player.current_lvl == 1
    assert player.exp_gained == 30
    assert player.coins == 0
    assert player.title == " Начинающий"
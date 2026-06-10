import pytest
from main import get_exp_for_completed_daily, get_exp_for_completed_challenge

@pytest.mark.parametrize(
        "func, reward, user_input, expected",
        [
            (get_exp_for_completed_daily, 20, "yes", 20),
            (get_exp_for_completed_daily, 20, "no", 0),
            (get_exp_for_completed_challenge, 30, "yes", 30),
            (get_exp_for_completed_challenge, 30, "no", 0),
        ]
)

def test_get_exp_for_completed_daily(mocker, func, reward, user_input, expected):
    mocker.patch("builtins.input", return_value=user_input)
    result = get_exp_for_completed_daily(["Material", str(reward)])
    assert result == expected

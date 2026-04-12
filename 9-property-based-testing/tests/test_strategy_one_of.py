import hypothesis
from hypothesis import strategies as st


@hypothesis.given(st.integers(min_value=1) | st.floats(min_value=0.01))
def test_should_validate_is_a_number(number_to_test: int | float) -> None:
    assert isinstance(number_to_test, int) or isinstance(number_to_test, float)

import hypothesis
from hypothesis import strategies as st


@hypothesis.given(st.lists(st.integers(min_value=1, max_value=100_000), min_size=1, max_size=10))
def test_should_reverse_list_and_keep_the_length(list_to_test: list[int]) -> None:
    assert len(list_to_test) == len(list(reversed(list_to_test)))


@hypothesis.given(st.lists(st.text(min_size=1), unique=True))
def test_should_be_unique_each_element_in_the_list(list_to_test: list[str]) -> None:
    assert len(list_to_test) == len(set(list_to_test))


@hypothesis.given(st.lists(st.floats(min_value=0.001, max_value=1000)))
def test_should_be_unique_each_element_in_the_list_2(list_to_test: list[str]) -> None:
    assert len(list_to_test) == len(set(list_to_test))

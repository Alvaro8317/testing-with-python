import string

import hypothesis
from hypothesis import strategies as st


@hypothesis.given(text=st.text(alphabet=st.characters(codec="ascii")))
def test_a_string_should_have_length_no_negative(text: str) -> None:
    assert len(text) >= 0


@hypothesis.given(text=st.text(min_size=1, max_size=100))
def test_a_string_should_have_length_no_negative_2(text: str) -> None:
    assert len(text) >= 1 and len(text) <= 100


@hypothesis.given(text=st.text(alphabet=string.ascii_lowercase, min_size=1))
def test_a_string_should_have_length_no_negative_3(text: str) -> None:
    assert len(text) >= 1

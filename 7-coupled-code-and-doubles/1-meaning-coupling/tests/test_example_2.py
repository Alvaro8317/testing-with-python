import pytest
from src import example_2


@pytest.fixture(autouse=True)
def fxt_configuration_testing() -> None:
    example_2.Configuration.debug_mode = False
    example_2.Configuration.max_retries = 0


def test_should_approve_payment() -> None:
    processor = example_2.PaymentProcessor()
    result_processing = processor.process(10.0)
    assert result_processing == "aprobado"


# def test_should_approve_payment_modifying_config() -> None:
#     processor = example_2.PaymentProcessor()
#     example_2.Configuration.debug_mode = False
#     example_2.Configuration.max_retries = 0
#     result_processing = processor.process(10.0)
#     assert result_processing == "aprobado"

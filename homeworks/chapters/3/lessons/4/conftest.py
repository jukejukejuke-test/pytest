import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


# @pytest.fixture(autouse=True)
# def print_smiling_faces():
#     print(":-Р", "\n")
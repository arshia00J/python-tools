from project import *


def test_text_to_binary():
    assert text_to_binary(
        "Hello") == "01001000 01100101 01101100 01101100 01101111"


def test_binary_to_text():
    assert binary_to_text(
        "01001000 01100101 01101100 01101100 01101111") == "Hello"


def test_generate_password():
    assert len(generate_password(8)) == 8

# Time zone 
# def test_timestamp_to_real_time():
#     assert timestamp_to_real_time(1609459200) == "2021-01-01 00:00:00"


if __name__ == '__main__':
    main()
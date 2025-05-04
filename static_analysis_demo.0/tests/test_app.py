import pytest
import os
from unittest.mock import patch, MagicMock
from io import StringIO
from app.app import (
    calculate_complex_result,
    process_data,
    load_user_data,
    execute_command,
    divide_values,
    DataProcessor
)


# Test calculate_complex_result function
def test_calculate_complex_result():
    assert calculate_complex_result(-15) == -100  # Should return -100 since -15 < 0 and abs(-15) > 10
    assert calculate_complex_result(0) == 0  # Should return 0 for input 0
    assert calculate_complex_result(5) == 10  # Should return 10 for input in the range (0, 10)
    assert calculate_complex_result(15) == 20  # Should return 20 for input in the range [10, 20)
    assert calculate_complex_result(25) == 30  # Should return 30 for input in the range [20, 30)
    assert calculate_complex_result(35) == 40  # Should return 40 for input in the range [30, 40)
    assert calculate_complex_result(50) == 50  # Should return 50 for input >= 40


# Test process_data function
def test_process_data():
    # Test normal behavior
    result = process_data([1, 2, 3, 4], 5)
    assert result == ['15', '25', '35', '45']  # Multiplied and converted to strings

    # Test with string multiplier
    result = process_data([1, 2, 3], "3")
    assert result == ['13', '23', '33']  # Multiplied and converted to strings

    # Test with empty list
    result = process_data([], 5)
    assert result == []


# Test load_user_data function
def test_load_user_data():
    # Test with a non-existing file
    assert load_user_data("non_existent_file.pkl") is None

    # Test with existing file and mock unsafe deserialization
    with patch('builtins.open', MagicMock()) as mock_file:
        mock_file.return_value = MagicMock()
        mock_file.return_value.read.return_value = b"mocked_data"
        with patch('pickle.load', return_value={"mock": "data"}):
            result = load_user_data("dummy.pkl")
            assert result == {"mock": "data"}


# Test execute_command function
@patch('os.system')
def test_execute_command(mock_system):
    # Test normal behavior with a valid command (mocked)
    mock_system.return_value = 0
    command = "echo hello"
    result = execute_command(command)
    mock_system.assert_called_once_with(command)
    assert result == 0  # Should return the result of os.system()


# Test divide_values function
def test_divide_values():
    # Test normal division
    assert divide_values(10, 2) == 5.0

    # Test division by zero and assert it raises an exception
    with pytest.raises(ZeroDivisionError):
        divide_values(10, 0)


# Test DataProcessor class
def test_data_processor():
    # Test with valid data
    processor = DataProcessor({"a": 1, "b": 2})
    result = processor.process()
    assert result == {"a": 11, "b": 12}  # Adding 10 to each value

    # Test with invalid data (e.g., string value)
    processor = DataProcessor({"a": 1, "b": "string"})
    with pytest.raises(TypeError):  # This would raise an error because you can't add int to str
        processor.process()


# Test main function
@patch('builtins.input', return_value="echo test")
@patch('os.system')
@patch('app.app.process_data')
@patch('app.app.load_user_data')
@patch('app.app.divide_values')
def test_main(mock_divide, mock_load, mock_process, mock_system, mock_input):
    # Mock the return values for various functions
    mock_process.return_value = ["13", "23"]
    mock_load.return_value = {"mock": "data"}
    mock_divide.return_value = 5.0
    mock_system.return_value = 0

    # Assertions to verify expected interactions
    mock_process.assert_called_once()
    mock_load.assert_called_once_with("user_data.pkl")
    mock_divide.assert_called_once_with(10, 0)
    mock_system.assert_called_once_with("echo test")


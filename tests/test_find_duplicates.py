from subprocess import run, PIPE
import os
import pytest

B_PATH_FILE = './bin/find_duplicates'

def test_bin_folder_contains_find_duplicates():
    assert os.path.isfile(B_PATH_FILE)

def test_find_duplicates_not_correct_input():
    result = run([B_PATH_FILE], input="tests/find_duplicates/file3.txt tests/find_duplicates/file1.txt", encoding='utf-8', stderr=PIPE, stdout=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_find_duplicates_correct_input():
    file_1 = "tests/find_duplicates/file1.txt"
    file_2 = "tests/find_duplicates/file2.txt"
    result = run([B_PATH_FILE], input=f"{file_1} {file_2}", encoding='utf-8', stdout=PIPE)
    assert os.path.isfile(file_1)
    assert not os.path.isfile(file_2)
    assert result.stdout == ""
    assert result.returncode == 0

def test_find_duplicates_empty_files():
    file_1 = "tests/find_duplicates/empty1.txt"
    file_2 = "tests/find_duplicates/empty2.txt"
    result = run([B_PATH_FILE], input=f"{file_1} {file_2}", encoding='utf-8', stdout=PIPE)
    assert os.path.isfile(file_1)
    assert os.path.isfile(file_2) == False
    assert result.stdout == ""
    assert result.returncode == 0

if __name__ == "__main__":
    pytest.main()

from src.sql_manager import create_sql_database_from_json


def test_create_sql_database_from_json():
    # Given
    json_path = "tests/data/cards-test-bulk.json"

    # When
    result = create_sql_database_from_json(json_path)

    # Then
    cursor = result.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='cards'"
    )
    assert cursor.fetchone() is not None

    cursor.execute("SELECT COUNT(*) FROM cards")
    assert cursor.fetchone()[0] == 18

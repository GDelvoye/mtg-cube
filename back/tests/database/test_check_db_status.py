from database.check_db_status import check_db_status


def test_check_db_status():
    tables, count = check_db_status()

    # On vérifie que c’est bien une liste
    assert isinstance(tables, list)

    # Si la table cards existe, on doit avoir un entier
    if "cards" in tables:
        assert isinstance(count, int)
        assert count >= 0

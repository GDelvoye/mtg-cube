from api.blueprint import bp

from mock.mock_cube import mock_load_cube


@bp.route("/get_test_cube", methods=["GET"])
def get_test_cube() -> dict:
    card_pool = mock_load_cube()
    return card_pool.to_dict()

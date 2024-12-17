def dict_formatter_for_front(dict_raw: dict) -> list[dict[str, float]]:
    """Format dict for front chart usage.

    Given {"a": 120, "b": 0.1}
    return [
        {"label": "a", "value": 120},
        {"label": "b", "value": 0.1},
    ]

    Args:
        dict_raw (dict): _description_

    Returns:
        list[dict[str, float]]: _description_
    """
    return [{"label": key, "value": float(value)} for (key, value) in dict_raw.items()]

"""Common ESI-bot helper functions."""


def paginated_id_to_names(slack, method, key, **kwargs):
    """Call the paginated method via slack, return a dict of id: name."""

    cursor = True
    mapping = {}
    while cursor:
        if cursor is True:
            api_return = slack.api_call(method, **kwargs)
        else:
            api_return = slack.api_call(method, cursor=cursor, **kwargs)

        if api_return["ok"]:
            mapping.update({x["id"]: x["name"] for x in api_return[key]})
            cursor = api_return.get("response_metadata", {}).get("next_cursor")
        else:
            break

    return mapping

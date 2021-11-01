from sqlalchemy import create_engine


def json_parse(data, tags, default=None):
    if data is None:
        return default
    for tag in tags:
        if tag.isdigit() and len(data) >= int(tag):
            data = data[int(tag)]
        elif tag in data:
            data = data[tag]
        else:
            return default
    return data


def get_db_engine(connection_string):
    return create_engine(connection_string)

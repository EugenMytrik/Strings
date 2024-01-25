def parse(url:str)->dict:
    result = {}
    parts = url.split("?")

    if len(parts) > 1 and parts[1]:
        params = parts[1].split("&")

        for param in params:
            key_value = param.split("=")

            if len(key_value) == 2:
                result[key_value[0]] = key_value[1]

    return result


if __name__ == "main":
    #parse() tests
    assert parse("https://example.com/path/to/page?name=ferret&color=purple") == {
        "name": "ferret",
        "color": "purple",
    }
    assert parse("https://example.com/path/to/page?surname=mytrik&color=blue") == {
        "surname": "mytrik",
        "color": "blue",
    }
    assert parse("https://example.com/path/to/page?name=ferret&color=purple&") == {
        "name": "ferret",
        "color": "purple",
    }
    assert parse("https://example.com/path/to/page?name=ferret&color=purple&surname=mytrik") == {
        "name": "ferret",
        "color": "purple",
        "surname":"mytrik",
    }
    assert parse("http://example.com/") == {}
    assert parse("http://example.com/fgfgfggdg") == {}
    assert parse("http://example.com/?") == {}
    assert parse("http://example.com/????") == {}
    assert parse("http://example.com/?name=Dima") == {"name": "Dima"}
    assert parse("http://example.com/?!!name=Dima") == {"!!name": "Dima"}


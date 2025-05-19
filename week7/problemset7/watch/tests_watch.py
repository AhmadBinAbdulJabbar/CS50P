from watch import parse

# passing these three tests
link1 = '<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>'
link2 = '<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>'
link3 = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
link4 = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

link5 = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
link6 = '<iframe src="https://youtube.com/embed/"></iframe>'

def test_parse_valid():
    assert parse(link1) == "https://youtu.be/xvFZjo5PgG0"
    assert parse(link2) == "https://youtu.be/xvFZjo5PgG0"
    assert parse(link3) == "https://youtu.be/xvFZjo5PgG0"
    assert parse(link4) == "https://youtu.be/xvFZjo5PgG0"


def test_parse_invalid():
    assert parse(link5) == None
    assert parse(link6) == None
    assert parse("") == None


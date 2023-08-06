from typing import List, Optional

from .timegraphics import (
    add_powered_by,
    timeline_url,
    timegraphics_regex,
    get_match_value,
    render_timegraphics_template,
)
import pytest


def test_embed_url():
    url = timeline_url(123466)
    assert url == "https://time.graphics/embed?v=1&id=123466"


def test_timegraphics_regex_match():
    content = "<p>[timegraphics:id=123456,width=100,height=400,allowfullscreen=1,frameborder=1]</p>"
    match = timegraphics_regex.findall(content)

    assert len(match) == 1

    match = match[0]
    assert match[1] == "123456"  # id
    assert match[3] == "100"  # width
    assert match[5] == "400"  # height
    assert match[7] == "1"  # allowfullscreen
    assert match[9] == "1"  # frameborder


def test_timegraphics_regex_multiple_instances():
    content = "<p>[timegraphics:id=123456]</p><h1>foo</h1><p>[timegraphics:id=123412]</p><p>[timegraphics:id=123478]</p>"
    match = timegraphics_regex.findall(content)

    assert len(match) == 3

    assert match[0][1] == "123456"
    assert match[1][1] == "123412"
    assert match[2][1] == "123478"


@pytest.mark.parametrize(
    "test_input,index,expected",
    [
        (["a", "b", "c"], 0, "a"),
        (["a", "b", "c"], 2, "c"),
        (["a", "b", "c"], 3, None),
        (["a", "", "c"], 1, None),
        ([], 0, None),
    ],
)
def test_get_match_value(test_input: List[str], index: int, expected: Optional[str]):
    assert get_match_value(test_input, index) == expected


@pytest.mark.parametrize(
    "allowfullscreen,expected",
    [
        (
            "1",
            """<iframe src="https://time.graphics/embed?v=1&id=123456" width="100%" height="400" frameborder="1" allowfullscreen></iframe>""",
        ),
        (
            "0",
            """<iframe src="https://time.graphics/embed?v=1&id=123456" width="100%" height="400" frameborder="1"></iframe>""",
        ),
    ],
)
def test_render_timegraphics_template(allowfullscreen, expected):
    context = dict()
    rendered = render_timegraphics_template(
        context, "123456", "100%", "400", "1", allowfullscreen
    )
    assert rendered == expected


@pytest.mark.parametrize(
    "should_add,expected",
    [
        (
            True,
            '<iframe></iframe><div><a style="font-size: 12px; text-decoration: none;" title="Powered by Time.Graphics" href="https://time.graphics">Powered by Time.Graphics</a></div>',
        ),
        (
            False,
            '<iframe></iframe>',
        ),
    ],
)
def test_add_powered_by(should_add, expected):
    result = add_powered_by("<iframe></iframe>", should_add)
    assert result == expected

from typing import List, Optional, Tuple

import pytest

from .timegraphics import (
    _ALLOW_FULLSCREEN_INDEX,
    _HEIGHT_INDEX,
    _SHOW_FRAMEBORDER_INDEX,
    _TIMELINE_ID_INDEX,
    _WIDTH_INDEX,
    add_powered_by,
    get_match_value,
    render_timegraphics_template,
    timegraphics_regex,
    timeline_url,
)


def test_embed_url():
    url = timeline_url(123466)
    assert url == "https://time.graphics/embed?v=1&id=123466"


def test_timegraphics_regex_match():
    content = "<p>[timegraphics:id=123456,width=100,height=400,allowfullscreen=1,frameborder=0]</p>"
    match = timegraphics_regex.findall(content)

    assert len(match) == 1

    match = match[0]
    assert match[_TIMELINE_ID_INDEX] == "123456"
    assert match[_WIDTH_INDEX] == "100"
    assert match[_HEIGHT_INDEX] == "400"
    assert match[_ALLOW_FULLSCREEN_INDEX] == "1"
    assert match[_SHOW_FRAMEBORDER_INDEX] == "0"


lengths_with_units = [
    "400",
    "100%",
    "500px",
    "500em",
    "500rem",
    "500ex",
    "500vh",
    "500vw",
    "500vmin",
    "500vmax",
    "5cm",
    "5mm",
    "5in",
    "5pc",
    "5pt",
]


@pytest.mark.parametrize(
    "parameter", [("width", _WIDTH_INDEX), ("height", _HEIGHT_INDEX)]
)
@pytest.mark.parametrize("height", lengths_with_units)
def test_timegraphics_regex_match_height(parameter: Tuple[str, int], height: str):
    content = f"<p>[timegraphics:id=123456,{parameter[0]}={height}]</p>"
    match = timegraphics_regex.findall(content)

    assert len(match) == 1
    match = match[0]
    assert match[parameter[1]] == height


def test_timegraphics_regex_multiple_instances():
    content = "<p>[timegraphics:id=123456]</p><h1>foo</h1><p>[timegraphics:id=123412]</p><p>[timegraphics:id=123478]</p>"
    match = timegraphics_regex.findall(content)

    assert len(match) == 3

    assert match[0][_TIMELINE_ID_INDEX] == "123456"
    assert match[1][_TIMELINE_ID_INDEX] == "123412"
    assert match[2][_TIMELINE_ID_INDEX] == "123478"


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
        (False, "<iframe></iframe>",),
    ],
)
def test_add_powered_by(should_add, expected):
    result = add_powered_by("<iframe></iframe>", should_add)
    assert result == expected

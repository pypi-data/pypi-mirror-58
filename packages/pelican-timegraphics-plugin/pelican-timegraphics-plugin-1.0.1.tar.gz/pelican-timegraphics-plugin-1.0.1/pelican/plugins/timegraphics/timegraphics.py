# -*- coding: utf-8 -*-
"""
Time.Graphics embedding plugin for Pelican
=================================
This plugin allows you to embed `Time.Graphics`_ timelines into your posts.
.. _Time.Graphics: https://time.graphics/
"""
from __future__ import unicode_literals

import logging
import re
from typing import Dict, List, Optional, Union

from jinja2 import Template
from pelican.contents import Article
from pelican.generators import ArticlesGenerator

_TIMEGRAPHICS_ALLOW_FULLSCREEN = "TIMEGRAPHICS_ALLOW_FULLSCREEN"
_TIMEGRAPHICS_SHOW_POWERED_BY = "TIMEGRAPHICS_SHOW_POWERED_BY"
_TIMEGRAPHICS_DEFAULT_WIDTH = "TIMEGRAPHICS_DEFAULT_WIDTH"
_TIMEGRAPHICS_DEFAULT_HEIGHT = "TIMEGRAPHICS_DEFAULT_HEIGHT"
_TIMEGRAPHICS_SHOW_FRAMEBORDER = "TIMEGRAPHICS_SHOW_FRAMEBORDER"

_TIMELINE_ID_INDEX = 1
_WIDTH_INDEX = 3
_HEIGHT_INDEX = 6
_ALLOW_FULLSCREEN_INDEX = 9
_SHOW_FRAMEBORDER_INDEX = 11

logger = logging.getLogger(__name__)

timegraphics_regex = re.compile(
    r"(<p>\[timegraphics:id=([0-9]+)"
    r"(,width=([1-9][0-9]*(ch|ex|r?em|%|px|vh|vw|vmin|vmax|cm|mm|in|pc|pt)?))?"
    r"(,height=([1-9][0-9]*(ch|ex|r?em|%|px|vh|vw|vmin|vmax|cm|mm|in|pc|pt)?))?"
    r"(,allowfullscreen=([01]))?"
    r"(,frameborder=([01]))?"
    r"\]</p>)"
)


def timeline_url(timeline_id: Union[int, str]) -> str:
    return f"https://time.graphics/embed?v=1&id={timeline_id}"


def get_match_value(match: List[str], index: int, default: Optional[str] = None) -> str:
    return match[index] if len(match) > index and match[index] else default


def setup_timegraphics(pelican):
    """Setup the default settings."""
    pelican.settings.setdefault(_TIMEGRAPHICS_ALLOW_FULLSCREEN, "1")
    pelican.settings.setdefault(_TIMEGRAPHICS_SHOW_POWERED_BY, True)
    pelican.settings.setdefault(_TIMEGRAPHICS_DEFAULT_WIDTH, "100%")
    pelican.settings.setdefault(_TIMEGRAPHICS_DEFAULT_HEIGHT, "400")
    pelican.settings.setdefault(_TIMEGRAPHICS_SHOW_FRAMEBORDER, "0")


def render_timegraphics_template(
    context: Dict[str, str],
    timeline_id: str,
    width: str,
    height: str,
    show_frameborder: str,
    allow_fullscreen: str,
) -> str:
    context.update(
        {
            "timeline_url": timeline_url(timeline_id),
            "width": width,
            "height": height,
            "show_frameborder": show_frameborder,
            "allowfullscreen": " allowfullscreen" if allow_fullscreen == "1" else "",
        }
    )

    timegraphics_template = (
        "<iframe "
        'src="{{ timeline_url }}" '
        'width="{{ width }}" height="{{ height }}" '
        'frameborder="{{ show_frameborder }}"'
        "{{ allowfullscreen }}></iframe>"
    )

    template = Template(timegraphics_template)

    return template.render(context)


def add_powered_by(replacement: str, should_add: bool) -> str:
    powered_by_template = '<div><a style="font-size: 12px; text-decoration: none;" title="Powered by Time.Graphics" href="https://time.graphics">Powered by Time.Graphics</a></div>'

    if should_add:
        replacement += powered_by_template

    return replacement


def replace_timegraphics_tags(generator: ArticlesGenerator):
    """Replace gist tags in the article content."""

    show_powered_by = generator.context.get(_TIMEGRAPHICS_SHOW_POWERED_BY)
    default_width = generator.context.get(_TIMEGRAPHICS_DEFAULT_WIDTH)
    default_height = generator.context.get(_TIMEGRAPHICS_DEFAULT_HEIGHT)
    default_allow_fullscreen = generator.context.get(_TIMEGRAPHICS_ALLOW_FULLSCREEN)
    default_show_frameborder = generator.context.get(_TIMEGRAPHICS_SHOW_FRAMEBORDER)

    article: Article
    for article in generator.articles:
        match: List[str]
        for match in timegraphics_regex.findall(article._content):
            timeline_id = get_match_value(match, _TIMELINE_ID_INDEX)
            width = get_match_value(match, _WIDTH_INDEX, default_width)
            height = get_match_value(match, _HEIGHT_INDEX, default_height)
            allow_fullscreen = get_match_value(
                match, _ALLOW_FULLSCREEN_INDEX, default_allow_fullscreen
            )
            show_frameborder = get_match_value(
                match, _SHOW_FRAMEBORDER_INDEX, default_show_frameborder
            )

            logger.info(
                f"[timegraphics]: Found timegraphics id {timeline_id} "
                f"with width {width}, "
                f"height {height} "
                f"which will {'not ' if show_frameborder == '0' else ''}show a frameborder"
                f"and will {'not ' if allow_fullscreen == '0' else ''}allow full screen"
            )

            context = generator.context.copy()
            replacement = render_timegraphics_template(
                context, timeline_id, width, height, allow_fullscreen, show_frameborder
            )
            replacement = add_powered_by(replacement, show_powered_by)

            article._content = article._content.replace(match[0], replacement)


def register():
    """Plugin registration."""
    from pelican import signals

    signals.initialized.connect(setup_timegraphics)

    signals.article_generator_finalized.connect(replace_timegraphics_tags)

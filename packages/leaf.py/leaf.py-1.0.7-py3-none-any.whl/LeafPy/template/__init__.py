#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ._render import (
    Render,
    frender
)
from .contrib import template
from ..conf import settings
from ..utils.py3helpers import string_types


def _render_model():
    if hasattr(settings, "TEMPLATE_MODEL"):
        return settings.TEMPLATE_MODEL
    return "default"


def _templates_path():
    templates_path = None
    if hasattr(settings, "TEMPLATE_PATH"):
        templates_path = settings.TEMPLATE_PATH
        if isinstance(templates_path, string_types):
            templates_path = [templates_path]

    if hasattr(settings, "TEMPLATE_DIRS"):
        template_dirs = settings.TEMPLATE_DIRS
        if isinstance(template_dirs, string_types):
            template_dirs = [template_dirs]

        if not templates_path:
            templates_path = template_dirs
        else:
            templates_path = list(templates_path)
            templates_path.extend(template_dirs)

    if not templates_path:
        templates_path = ["templates"]

    return list(set(templates_path))


def get_render():
    render_model = _render_model().strip().lower()
    templates_path = _templates_path()

    if render_model == "jinja2":
        return template.render_jinja(
            templates_path,
            encoding="utf-8",
        )
    elif render_model == "genshi":
        return template.render_genshi(
            templates_path,
            auto_reload=settings.DEBUG,
            default_encoding="utf-8",
        )
    elif render_model == "mako":
        return template.render_mako(
            templates_path,
            input_encoding="utf-8",
            output_encoding="utf-8",
            cache_enabled=(not settings.DEBUG),
        )

    # for default
    return Render(
        templates_path,
        cache=(not settings.DEBUG),
    )

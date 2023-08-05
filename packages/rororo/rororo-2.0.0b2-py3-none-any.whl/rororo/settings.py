"""
===============
rororo.settings
===============

Immutable Settings dictionary and various utilities to read settings values
from environment.

Module helps you to prepare and read settings inside your web application.

"""

import calendar
import locale
import logging
import os
import time
import types
from importlib import import_module
from logging.config import dictConfig
from typing import Any, Iterator, MutableMapping, Optional, Tuple, Union

from .annotations import DictStrAny, MappingStrAny, Settings, T
from .utils import to_bool


def from_env(key: str, default: T = None) -> Union[str, Optional[T]]:
    """Shortcut for safely reading environment variable.

    .. deprecated:: 2.0
        Use :func:`os.getenv` instead. Will be removed in **3.0**.

    :param key: Environment var key.
    :param default:
        Return default value if environment var not found by given key. By
        default: ``None``
    """
    return os.getenv(key, default)


def immutable_settings(defaults: Settings, **optionals: Any) -> MappingStrAny:
    r"""Initialize and return immutable Settings dictionary.

    Settings dictionary allows you to setup settings values from multiple
    sources and make sure that values cannot be changed, updated by anyone else
    after initialization. This helps keep things clear and not worry about
    hidden settings change somewhere around your web application.

    :param defaults:
       Read settings values from module or dict-like instance.
    :param \*\*optionals:
        Update base settings with optional values.

        In common additional values shouldn't be passed, if settings values
        already populated from local settings or environment. But in case
        of using application factories this makes sense::

            from . import settings

            def create_app(**options):
                app = ...
                app.settings = immutable_settings(settings, **options)
                return app

        And yes each additional key overwrite default setting value.
    """
    settings = {key: value for key, value in iter_settings(defaults)}
    for key, value in iter_settings(optionals):
        settings[key] = value
    return types.MappingProxyType(settings)


def inject_settings(
    mixed: Union[str, Settings],
    context: MutableMapping[str, Any],
    fail_silently: bool = False,
) -> None:
    """Inject settings values to given context.

    :param mixed:
        Settings can be a string (that it will be read from Python path),
        Python module or dict-like instance.
    :param context:
        Context to assign settings key values. It should support dict-like item
        assingment.
    :param fail_silently:
        When enabled and reading settings from Python path ignore errors if
        given Python path couldn't be loaded.
    """
    if isinstance(mixed, str):
        try:
            mixed = import_module(mixed)
        except Exception:
            if fail_silently:
                return
            raise

    for key, value in iter_settings(mixed):
        context[key] = value


def is_setting_key(key: str) -> bool:
    """Check whether given key is valid setting key or not.

    Only public uppercase constants are valid settings keys, all other keys
    are invalid and shouldn't present in Settings dict.

    **Valid settings keys**

    ::

        DEBUG
        SECRET_KEY

    **Invalid settings keys**

    ::

        _PRIVATE_SECRET_KEY
        camelCasedSetting
        rel
        secret_key

    :param key: Key to check.
    """
    return key.isupper() and key[0] != "_"


def iter_settings(mixed: Settings) -> Iterator[Tuple[str, Any]]:
    """Iterate over settings values from settings module or dict-like instance.

    :param mixed: Settings instance to iterate.
    """
    if isinstance(mixed, types.ModuleType):
        for attr in dir(mixed):
            if not is_setting_key(attr):
                continue
            yield (attr, getattr(mixed, attr))
    else:
        yield from filter(lambda item: is_setting_key(item[0]), mixed.items())


def setup_locale(
    lc_all: str,
    first_weekday: int = None,
    *,
    lc_collate: str = None,
    lc_ctype: str = None,
    lc_messages: str = None,
    lc_monetary: str = None,
    lc_numeric: str = None,
    lc_time: str = None
) -> str:
    """Shortcut helper to setup locale for backend application.

    :param lc_all: Locale to use.
    :param first_weekday:
        Weekday for start week. 0 for Monday, 6 for Sunday. By default: None
    :param lc_collate: Collate locale to use. By default: ``<lc_all>``
    :param lc_ctype: Ctype locale to use. By default: ``<lc_all>``
    :param lc_messages: Messages locale to use. By default: ``<lc_all>``
    :param lc_monetary: Monetary locale to use. By default: ``<lc_all>``
    :param lc_numeric: Numeric locale to use. By default: ``<lc_all>``
    :param lc_time: Time locale to use. By default: ``<lc_all>``
    """
    if first_weekday is not None:
        calendar.setfirstweekday(first_weekday)

    locale.setlocale(locale.LC_COLLATE, lc_collate or lc_all)
    locale.setlocale(locale.LC_CTYPE, lc_ctype or lc_all)
    locale.setlocale(locale.LC_MESSAGES, lc_messages or lc_all)
    locale.setlocale(locale.LC_MONETARY, lc_monetary or lc_all)
    locale.setlocale(locale.LC_NUMERIC, lc_numeric or lc_all)
    locale.setlocale(locale.LC_TIME, lc_time or lc_all)

    return locale.setlocale(locale.LC_ALL, lc_all)


def setup_logging(
    config: DictStrAny, *, remove_root_handlers: bool = False
) -> None:
    """Wrapper around :func:`logging.config.dictConfig` function.

    In most cases it is not necessary to use an additional wrapper for setting
    up logging, but if your ``aiohttp.web`` application run as::

        python -m aiohttp.web api.app:create_app

    ``aiohttp`` `will setup
    <https://github.com/aio-libs/aiohttp/blob/v3.6.2/aiohttp/web.py#L494>`_
    logging via :func:`logging.basicConfig` call and it may result in
    duplicated logging messages. To avoid duplication, it is needed to remove
    ``logging.root`` handlers.

    :param remove_root_handlers:
        Remove ``logging.root`` handlers if any. By default: ``False``
    """
    if remove_root_handlers:
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
    return dictConfig(config)


def setup_timezone(timezone: str) -> None:
    """Shortcut helper to configure timezone for backend application.

    :param timezone: Timezone to use, e.g. "UTC", "Europe/Kiev".
    """
    if timezone and hasattr(time, "tzset"):
        tz_root = "/usr/share/zoneinfo"
        tz_filename = os.path.join(tz_root, *(timezone.split("/")))

        if os.path.exists(tz_root) and not os.path.exists(tz_filename):
            raise ValueError("Incorrect timezone value: {0}".format(timezone))

        os.environ["TZ"] = timezone
        time.tzset()


# Make flake8 happy
(setup_logging, to_bool)

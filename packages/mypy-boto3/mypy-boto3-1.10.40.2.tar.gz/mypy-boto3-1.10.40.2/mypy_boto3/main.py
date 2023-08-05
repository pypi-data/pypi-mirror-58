import argparse
import pathlib
import logging
import re
import sys
import shutil
from typing import List, Dict

from mypy_boto3.version import __version__ as version
from mypy_boto3.submodules import (
    SUBMODULES,
    INSTALLED_SUBMODULES,
    CACHE_KEY,
)

ROOT_PATH = pathlib.Path(__file__).absolute().parent
CACHE_PATH = ROOT_PATH / "cache.txt"
BOTO3_STUBS_NAME = "boto3-stubs"
MODULE_NAME = "mypy_boto3"

FUNCTION_TEMPLATE = """{overload}def {name}(
    service_name: {service_name_type},
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> {return_type}:
    pass"""

METHOD_TEMPLATE = """    {overload}def {name}(
        self,
        service_name: {service_name_type},
        region_name: str = None,
        api_version: str = None,
        use_ssl: bool = None,
        verify: Union[str, bool] = None,
        endpoint_url: str = None,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        aws_session_token: str = None,
        config: Config = None,
    ) -> {return_type}:
        pass"""


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        MODULE_NAME,
        description=(
            "Service stubs generator for boto3-stubs."
            " Run it after boto3-stubs every update, install or remove services."
            " Use it only with local python installation."
        ),
    )
    parser.add_argument("-v", "--version", action="version", version=version)
    parser.add_argument("-d", "--debug", action="store_true", help="Hide log output")
    parser.add_argument("-q", "--quiet", action="store_true", help="Verbose log output")
    return parser


def get_logger(level: int) -> logging.Logger:
    logger = logging.getLogger("mypy_boto3")
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(name)s: %(levelname)-8s %(message)s")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    log_level = logging.INFO
    if args.debug:
        log_level = logging.DEBUG
    if args.quiet:
        log_level = logging.CRITICAL
    build_index(log_level)
    set_cache_key()


def _is_build_required() -> bool:
    if not CACHE_PATH.exists():
        return True

    if CACHE_PATH.read_text() != CACHE_KEY:
        return True

    return False


def set_cache_key() -> None:
    CACHE_PATH.write_text(CACHE_KEY)


def maybe_build_index() -> bool:
    """
    Check cache and build index if cache is outdated.
    """
    is_required = _is_build_required()
    if is_required:
        build_index()
        set_cache_key()

    return is_required


def build_index(log_level: int = logging.CRITICAL) -> None:
    """
    Build index for installed services.
    """
    logger = get_logger(log_level)

    logger.debug("Using Python packages directory %s", ROOT_PATH.parent)

    init_client_functions: List[str] = []
    init_resource_functions: List[str] = []
    session_client_functions: List[str] = []
    session_resource_functions: List[str] = []
    imports: List[str] = []
    for submodule in INSTALLED_SUBMODULES:
        logger.info(
            "Discovered %s subresource in %s", submodule["boto3_name"], submodule["module_name"],
        )

    for submodule in INSTALLED_SUBMODULES:
        init_client_functions.append(
            FUNCTION_TEMPLATE.format(
                overload="@overload\n" if len(INSTALLED_SUBMODULES) > 1 else "",
                name="client",
                service_name_type='Literal["{}"]'.format(submodule["boto3_name"]),
                return_type="{}Client".format(submodule["class_name"]),
            )
        )
        session_client_functions.append(
            METHOD_TEMPLATE.format(
                overload="@overload\n    " if len(INSTALLED_SUBMODULES) > 1 else "",
                name="client",
                service_name_type='Literal["{}"]'.format(submodule["boto3_name"]),
                return_type="{}Client".format(submodule["class_name"]),
            )
        )
        imports.append(
            "from mypy_boto3.{} import {}Client".format(
                submodule["import_name"], submodule["class_name"],
            )
        )
        if submodule["has_resource"]:
            init_resource_functions.append(
                FUNCTION_TEMPLATE.format(
                    overload="@overload\n" if len(INSTALLED_SUBMODULES) > 1 else "",
                    name="resource",
                    service_name_type='Literal["{}"]'.format(submodule["boto3_name"]),
                    return_type="{}ServiceResource".format(submodule["class_name"]),
                )
            )
            session_resource_functions.append(
                METHOD_TEMPLATE.format(
                    overload="@overload\n    " if len(INSTALLED_SUBMODULES) > 1 else "",
                    name="resource",
                    service_name_type='Literal["{}"]'.format(submodule["boto3_name"]),
                    return_type="{}ServiceResource".format(submodule["class_name"]),
                )
            )
            imports.append(
                "from mypy_boto3.{} import {}ServiceResource".format(
                    submodule["import_name"], submodule["class_name"],
                )
            )

    if not init_client_functions:
        init_client_functions.append(
            FUNCTION_TEMPLATE.format(
                overload="", name="client", service_name_type="str", return_type="Any",
            )
        )
    if not init_resource_functions:
        init_resource_functions.append(
            FUNCTION_TEMPLATE.format(
                overload="", name="resource", service_name_type="str", return_type="Any",
            )
        )
    if not session_client_functions:
        session_client_functions.append(
            METHOD_TEMPLATE.format(
                overload="", name="client", service_name_type="str", return_type="Any",
            )
        )
    if not session_resource_functions:
        session_resource_functions.append(
            METHOD_TEMPLATE.format(
                overload="", name="resource", service_name_type="str", return_type="Any",
            )
        )

    init_contents: List[str] = [
        "import sys",
        "from typing import overload, Any",
        "if sys.version_info >= (3, 8):",
        "    from typing import Literal",
        "else:",
        "    from typing_extensions import Literal",
    ]
    init_contents.extend(imports)
    init_contents.append("")
    init_contents.extend(init_client_functions)
    init_contents.extend(init_resource_functions)

    session_contents: List[str] = [
        "import sys",
        "from typing import overload, Any",
        "if sys.version_info >= (3, 8):",
        "    from typing import Literal",
        "else:",
        "    from typing_extensions import Literal",
    ]
    session_contents.extend(imports)
    session_contents.append("")
    session_contents.append("class Session:")
    session_contents.extend(session_client_functions)
    session_contents.extend(session_resource_functions)

    def write_text(path: pathlib.Path, text: str) -> None:
        logger.debug("Updating %s", path)
        path.write_text(text)

    for submodule in SUBMODULES:
        submodule_path = ROOT_PATH / submodule["import_name"]
        if submodule not in INSTALLED_SUBMODULES:
            if submodule_path.exists():
                logger.debug("Removing directory for deleted service %s", submodule_path)
                shutil.rmtree(submodule_path)
            continue

        if not submodule_path.exists():
            logger.debug("Creating directory %s", submodule_path)
            submodule_path.mkdir(exist_ok=True)

        write_text(
            submodule_path / "__init__.py", "from {} import *".format(submodule["module_name"])
        )
        write_text(
            submodule_path / "client.py", "from {}.client import *".format(submodule["module_name"])
        )
        write_text(
            submodule_path / "type_defs.py",
            "from {}.type_defs import *".format(submodule["module_name"]),
        )
        if submodule["has_resource"]:
            write_text(
                submodule_path / "service_resource.py",
                "from {}.service_resource import *".format(submodule["module_name"]),
            )
        if submodule["has_waiter"]:
            write_text(
                submodule_path / "waiter.py",
                "from {}.waiter import *".format(submodule["module_name"]),
            )
        if submodule["has_paginator"]:
            write_text(
                submodule_path / "paginator.py",
                "from {}.paginator import *".format(submodule["module_name"]),
            )

    write_text(ROOT_PATH / "boto3_init_gen.py", "\n".join(init_contents))
    write_text(ROOT_PATH / "boto3_session_gen.py", "\n".join(session_contents))

    if not INSTALLED_SUBMODULES:
        logger.warning(
            "No services submodules discovered, install the ones you use and run this command again"
        )
        logger.info("https://mypy-boto3.readthedocs.io/en/latest/#sub-modules")
        sys.exit()

    names_str = ""
    for i, submodule in enumerate(INSTALLED_SUBMODULES):
        name = submodule["boto3_name"]
        if not i:
            names_str = name
            continue
        if i < len(INSTALLED_SUBMODULES) - 1:
            names_str = "{}, {}".format(names_str, name)
            continue

        names_str = "{} and {}".format(names_str, name)

    logger.info("You can now use %s type annotations.", names_str)

"""
Dapp platform. https://github.com/dapphub/dapptools
"""

import os
import json
import logging
import glob
import re
import subprocess
from pathlib import Path

# Cycle dependency
from typing import TYPE_CHECKING, Dict

from crytic_compile.compiler.compiler import CompilerVersion
from crytic_compile.platform.types import Type
from crytic_compile.utils.naming import (
    extract_filename,
    extract_name,
    combine_filename_name,
    convert_filename,
)


# Handle cycle
if TYPE_CHECKING:
    from crytic_compile import CryticCompile


LOGGER = logging.getLogger("CryticCompile")


def compile(crytic_compile: "CryticCompile", target: str, **kwargs: str):
    """
    Compile the target
    :param crytic_compile:
    :param target:
    :param kwargs:
    :return:
    """
    crytic_compile.type = Type.DAPP
    dapp_ignore_compile = kwargs.get("dapp_ignore_compile", False) or kwargs.get("ignore_compile", False)
    directory = os.path.join(target, "out")

    if not dapp_ignore_compile:
        _run_dapp(target)

    crytic_compile.compiler_version = _get_version(target)

    files = glob.glob(directory + "/**/*.sol.json", recursive=True)
    for file in files:
        with open(file, encoding="utf8") as file_desc:
            targets_json = json.load(file_desc)

        if not "contracts" in targets_json:
            continue

        for original_contract_name, info in targets_json["contracts"].items():
            contract_name = extract_name(original_contract_name)
            contract_filename = extract_filename(original_contract_name)
            contract_filename = convert_filename(
                contract_filename, _relative_to_short, crytic_compile, working_dir=target
            )
            crytic_compile.contracts_names.add(contract_name)
            crytic_compile.contracts_filenames[contract_name] = contract_filename
            crytic_compile.abis[contract_name] = json.loads(info["abi"])
            crytic_compile.bytecodes_init[contract_name] = info["bin"]
            crytic_compile.bytecodes_runtime[contract_name] = info["bin-runtime"]
            crytic_compile.srcmaps_init[contract_name] = info["srcmap"].split(";")
            crytic_compile.srcmaps_runtime[contract_name] = info["srcmap-runtime"].split(";")

        for path, info in targets_json["sources"].items():
            path = convert_filename(path, _relative_to_short, crytic_compile, working_dir=target)
            crytic_compile.filenames.add(path)
            crytic_compile.asts[path.absolute] = info["AST"]


def export(crytic_compile: "CryticCompile", **kwargs: str) -> Dict:
    """
    Export the target
    :param crytic_compile:
    :param kwargs:
    :return:
    """
    # Obtain objects to represent each contract
    contracts = dict()
    for contract_name in crytic_compile.contracts_names:
        abi = str(crytic_compile.abi(contract_name))
        abi = abi.replace("'", '"')
        abi = abi.replace("True", "true")
        abi = abi.replace("False", "false")
        abi = abi.replace(" ", "")
        exported_name = combine_filename_name(
            crytic_compile.contracts_filenames[contract_name].used, contract_name
        )
        contracts[exported_name] = {
            "srcmap": "",
            "srcmap-runtime": "",
            "abi": abi,
            "bin": crytic_compile.bytecode_init(contract_name),
            "bin-runtime": crytic_compile.bytecode_runtime(contract_name),
        }

    sources = {filename: {"AST": ast} for (filename, ast) in crytic_compile.asts.items()}
    source_list = [filename.absolute for filename in crytic_compile.filenames]

    # Create our root object to contain the contracts and other information.
    output = {"sources": sources, "sourceList": source_list, "contracts": contracts}

    # If we have an export directory specified, we output the JSON to a file.
    export_dir = kwargs.get("export_dir", None)
    if export_dir:
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)
        path = os.path.join(export_dir, "combined_solc.json")
        with open(path, "w", encoding="utf8") as file_desc:
            json.dump(output, file_desc)
    return output


def is_dapp(target: str) -> bool:
    """
    Heuristic used: check if "dapp build" is present in Makefile
    :param target:
    :return:
    """
    makefile = os.path.join(target, "Makefile")
    if os.path.isfile(makefile):
        with open(makefile, encoding="utf8") as file_desc:
            txt = file_desc.read()
            return "dapp build" in txt
    return False


def is_dependency(path: str) -> bool:
    """
    Check if the path is a dependency
    :param path:
    :return:
    """
    return "lib" in Path(path).parts


def _run_dapp(target: str):
    """
    Run Dapp
    :param target:
    :return:
    """
    cmd = ["dapp", "build"]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=target)
    _, _ = process.communicate()


def _get_version(target: str) -> CompilerVersion:
    """
    Get the compiler version used
    :param target:
    :return:
    """
    files = glob.glob(target + "/**/*meta.json", recursive=True)
    version = None
    optimized = None
    compiler = "solc"
    for file in files:
        if version is None:
            with open(file, encoding="utf8") as file_desc:
                config = json.load(file_desc)
            if "compiler" in config:
                if "version" in config["compiler"]:
                    version = re.findall(r"\d+\.\d+\.\d+", config["compiler"]["version"])
                    assert version
            if "settings" in config:
                if "optimizer" in config["settings"]:
                    if "enabled" in config["settings"]["optimizer"]:
                        optimized = config["settings"]["optimizer"]["enabled"]

    return CompilerVersion(compiler=compiler, version=version, optimized=optimized)


def _relative_to_short(relative: Path) -> Path:
    """
    Translate relative path to short
    :param relative:
    :return:
    """
    short = relative
    try:
        short = short.relative_to(Path("src"))
    except ValueError:
        try:
            short = short.relative_to("lib")
        except ValueError:
            pass
    return short

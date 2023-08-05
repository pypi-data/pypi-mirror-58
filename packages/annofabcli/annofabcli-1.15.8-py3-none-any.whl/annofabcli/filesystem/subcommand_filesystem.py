import argparse

import annofabcli
import annofabcli.common.cli
import annofabcli.filesystem.write_annotation_image


def parse_args(parser: argparse.ArgumentParser):

    subparsers = parser.add_subparsers()

    # サブコマンドの定義
    annofabcli.filesystem.write_annotation_image.add_parser(subparsers)


def add_parser(subparsers: argparse._SubParsersAction):
    subcommand_name = "filesystem"
    subcommand_help = "ファイル操作関係（Web APIにアクセスしない）のサブコマンド"
    description = "ファイル操作関係（Web APIにアクセスしない）のサブコマンド"

    parser = annofabcli.common.cli.add_parser(subparsers, subcommand_name, subcommand_help, description)
    parse_args(parser)

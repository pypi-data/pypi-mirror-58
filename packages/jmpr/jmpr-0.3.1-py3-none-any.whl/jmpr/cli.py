# jmpr - Python tooling to enable and manage AWS account navigation
# Copyright (C) 2019  eGlobalTech

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
cli.py
====================================
This file manages the CLI call, arguments, and the CLI output
"""

import jmpr
import sys
import logging
import argparse


def main():
    """[summary]
    """
    jmpr_version = '0.3.1'

    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--identity_account_id", help="Identity account ID", type=int)
    parser.add_argument("-o", "--org_unit_id", help="Organization Org Unit containing accounts")
    parser.add_argument("-r", "--shared_role", help="Shared role for accounts")
    parser.add_argument("-y", "--yaml_file", help="YAML file with complete configuration, see (future) doc")
    parser.add_argument("-v", "--version", help="Returns the current jmpr version (" + jmpr_version + ")",
                        action='store_true')
    args = parser.parse_args()

    # Try the file style first
    parm_style = 'org_style'  # default
    if args.version:
        print("Version = " + jmpr_version)
        sys.exit(0)
    elif args.yaml_file:
        parm_style = "yaml_style"
        cloud_assets = jmpr.CloudAssets.from_yaml(args.yaml_file)
    elif args.org_unit_id:
        parm_style = "org_style"
        if args.identity_account_id is None:
            sys.exit("You need to supply --identity (your identity account ID)")
        if args.org_unit_id is None:
            sys.exit("You need to supply --org_unit_id when defaulting to accounts in an organization")
        if args.shared_role is None:
            sys.exit("You need to supply --shared_role when defaulting to accounts in an organization")
        cloud_assets = jmpr.CloudAssets.from_org(
            str(args.identity_account_id),
            args.org_unit_id,
            args.shared_role,
            args
        )
    else:
        sys.exit("Account list style not yet implemented")

    # Show what we have done
    print("Switches:")
    print(*cloud_assets.switches, sep="\n")

    print("\nConcerns:")
    if len(cloud_assets.concerns) > 0:
        print(*cloud_assets.concerns, sep="\n")
    else:
        print("None")

    print("\nPrincipals:")
    for principal in cloud_assets.principals:
        if principal.path == principal.desired_path:
            print(principal.path + principal.username + ' is ' + principal.arn)
        else:
            print(principal.path + principal.username + ' path changed to ' + principal.arn)
        try:
            print("Initial password is {}".format(principal.initial_pass))
        except Exception as e:
            pass
        principal.print_switchroles()

    print("\nAcquired target accounts and roles:")
    for account in cloud_assets.target_accounts.values():
        print("%s (%s)" % (account.id, account.name))
        for role in account.target_roles.values():
            if "Arn" not in role:
                print(
                    "- FAILED ACTION ON ACCOUNT {} and ROLE {}{}, see errors".
                    format(account.id, role["Path"], role["RoleName"])
                )
            else:
                print("-  " + role["Path"] + role["RoleName"] + '=' + role["Arn"])

    cloud_assets.print_actions()


if __name__ == "__main__":
    """[summary]
    """
    main()

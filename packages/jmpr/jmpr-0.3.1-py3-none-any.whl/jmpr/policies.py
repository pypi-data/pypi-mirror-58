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
policies.py
====================================
Provides a AWS IAM Policy Generator class that build complex IAM policies
"""


class Generator:
    """
    A class used to create an AWS IAM Policy Generator Object

    Parameters
    ----------
    account : str
        A string to represent the target AWS account to generate permissions for (default '*')
    user : str
        the name of the user to generate permissions for
    path : str
        the path for the user (default '*')
    bucket : str
        the s3 bucket to grant the user access to (default '')
    """

    def __init__(self, account: str = '*', user='${aws:username}', path='*', bucket=''):
        self.account = account
        if self.account is None:
            self.account = '*'
        self.user = user
        self.path = path
        self.bucket = bucket

    # SOME PRE-BUILT POLICIES
    def blank_policy(self):
        """Pre-built policy that generates a dict that represents a blank IAM policy document

        Returns:
            dict -- a dict representing a blank policy document

        """
        blank = {}
        blank['Version'] = '2012-10-17'
        blank['Statement'] = []

        return blank

    def self_service_policy(self):
        """Pre-built policy that generates a self service policy that allows the following actions:
            * ViewAccountInfo
            * ManageOwnPasswords
            * IndividualUserToListOnlyTheirOwnMFA
            * IndividualUserToManageTheirOwnMFA

        Returns:
            dict -- a dict representing the self service policy document
        """
        statement = []
        statement.append(self.ViewAccountInfo('Allow'))
        statement.append(self.ManageOwnPasswords('Allow'))
        statement.append(self.IndividualUserToListOnlyTheirOwnMFA('Allow'))
        statement.append(self.IndividualUserToManageTheirOwnMFA('Allow'))

        policy = self.blank_policy()
        policy["Statement"] = statement

        return policy

    def s3_home_dir_policy(self):
        """Pre-built policy that generates a S3 home directory policy that allows the following actions:
            * S3ViewBuckets
            * S3ViewBucketContents
            * S3ListHomeDir
            * S3ModifyHomeDir

        Returns:
            dict -- a dict representing the S3 home directory policy
        """
        statement = []

        if self.bucket:
            statement.append(self.S3ViewBuckets('Allow'))
            statement.append(self.S3ViewBucketContents('Allow'))
            statement.append(self.S3ListHomeDir('Allow'))
            statement.append(self.S3ModifyHomeDir('Allow'))

        policy = self.blank_policy()
        policy["Statement"] = statement

        return policy

    def enforceMFA(self, enforce_state=True):
        """Pre-built policy that generates a MFA policy based on the enforce_state argument

        Keyword Arguments:
            enforce_state {bool} -- Whether to generate a policy enforcing MFA or allowing no MFA (default: {True})

        Returns:
            dict -- a dict representing the MFA policy
        """
        statement = []

        if enforce_state:
            statement.append(self.MFAAllowDeny('Deny'))
        else:
            statement.append(self.MFAAllowDeny('Allow'))

        policy = self.blank_policy()
        policy["Statement"] = statement

        return policy

    # THE POLICY STATEMENT DEFINITIONS
    def ViewAccountInfo(self, effect):
        """Generates a policy allowing the user to view only their own account information

        Arguments:
            effect {str} -- Whether to allow or deny the given actions (default: 'Deny')

        Returns:
            [dict] -- A dict representing a dynamic policy allowing the user to view only their own account information
        """
        policy = {}
        policy['Sid'] = 'AllowViewAccountInfo'
        policy['Effect'] = effect
        policy['Action'] = []
        policy['Action'].append('iam:GetAccountPasswordPolicy')
        policy['Action'].append('iam:GetAccountSummary')
        policy['Action'].append('iam:ListVirtualMFADevices')
        policy['Resource'] = '*'

        return policy

    def ManageOwnPasswords(self, effect):
        """Generates a policy allowing the user to manage their own passwords

        Arguments:
            effect {str} -- Whether to allow or deny the given actions (default: 'Deny')

        Returns:
            A dict representing a dynamic policy allowing the user to manage their own passwords
        """
        policy = {}
        policy['Sid'] = 'AllowManageOwnPasswords'
        policy['Effect'] = effect
        policy['Action'] = []
        policy['Action'].append('iam:ChangePassword')
        policy['Action'].append('iam:GetUser')
        policy['Resource'] = []
        policy['Resource'].append('arn:aws:iam::' + str(self.account) + ':user/' + self.user)

        return policy

    def IndividualUserToListOnlyTheirOwnMFA(self, effect):
        """Generates a policy allowing the user to list their own MFA devices

        Arguments:
            effect {str} -- Whether to allow or deny the given actions (default: 'Deny')

        Returns:
            [dict] -- A dict representing a dynamic policy allowing the user to list their own MFA devices
        """
        policy = {}
        policy['Sid'] = 'AllowIndividualUserToListOnlyTheirOwnMFA'
        policy['Effect'] = effect
        policy['Action'] = []
        policy['Action'].append('iam:ListMFADevices')
        policy['Resource'] = []
        policy['Resource'].append('arn:aws:iam::' + str(self.account) + ':mfa/*')
        policy['Resource'].append('arn:aws:iam::' + str(self.account) + ':user' + self.path + self.user)

        return policy

    def IndividualUserToManageTheirOwnMFA(self, effect):
        """Generates a policy allowing the user to manage their own MFA devices

        Arguments:
            effect {str} -- Whether to allow or deny the given actions (default: 'Deny')

        Returns:
            [dict] -- A dict representing a dynamic policy allowing the user to list their own MFA devices
        """
        policy = {}
        policy['Sid'] = 'AllowIndividualUserToManageTheirOwnMFA'
        policy['Effect'] = effect
        policy['Action'] = []
        policy['Action'].append('iam:CreateVirtualMFADevice')
        policy['Action'].append('iam:DeleteVirtualMFADevice')
        policy['Action'].append('iam:EnableMFADevice')
        policy['Action'].append('iam:ResyncMFADevice')
        policy['Action'].append('iam:DeactivateMFADevice')
        policy['Resource'] = []
        policy['Resource'].append('arn:aws:iam::' + str(self.account) + ':mfa/' + self.user)
        policy['Resource'].append('arn:aws:iam::' + str(self.account) + ':user' + self.path + self.user)

        return policy

    def S3ViewBuckets(self, effect):
        """Generates a policy allowing the user to view home S3 Buckets

        Arguments:
            effect {str} -- Whether to allow or deny the given actions (default: 'Deny')

        Returns:
            [dict] -- A dict representing a dynamic policy allowing the user to view home S3 buckets
        """
        policy = {}
        policy['Sid'] = 'S3ViewBuckets'
        policy['Effect'] = effect
        policy['Action'] = []
        policy['Action'].append('s3:GetBucketLocation')
        policy['Action'].append('s3:ListAllMyBuckets')
        policy['Resource'] = []
        policy['Resource'].append('arn:aws:s3:::*')

        return policy

    def S3ViewBucketContents(self, effect):
        """Generates a policy allowing the user to view home S3 Bucket contents

        Arguments:
            effect {str} -- Whether to allow or deny the given actions (default: 'Deny')

        Returns:
            [dict] -- A dict representing a dynamic policy allowing the user to view home S3 bucket contents
        """
        policy = {}
        policy['Sid'] = 'S3ViewBucketContents'
        policy['Effect'] = effect
        policy['Action'] = []
        policy['Action'].append('s3:GetBucketLocation')
        policy['Action'].append('s3:ListAllMyBuckets')
        policy['Resource'] = []
        policy['Resource'].append('arn:aws:s3:::' + self.bucket)
        policy['Condition'] = {}
        policy['Condition']['StringEquals'] = {}
        policy['Condition']['StringEquals']['s3:prefix'] = []
        policy['Condition']['StringEquals']['s3:prefix'].append('')
        policy['Condition']['StringEquals']['s3:prefix'].append(self.path + '/')
        policy['Condition']['StringEquals']['s3:prefix'].append(self.path + '/home/')
        policy['Condition']['StringEquals']['s3:prefix'].append(self.path + '/home/' + self.user)
        policy['Condition']['StringEquals']['s3:delimiter'] = ['/']

        return policy

    def S3ListHomeDir(self, effect):
        """Generates a policy allowing the user to list their own home S3 Bucket contents

        Arguments:
            effect {str} -- Whether to allow or deny the given actions (default: 'Deny')

        Returns:
            [dict] -- A dict representing a dynamic policy allowing the user to list their own home S3 Bucket contents
        """
        policy = {}
        policy['Sid'] = 'S3ListHomeDir'
        policy['Effect'] = effect
        policy['Action'] = []
        policy['Action'].append('s3:ListBucket')
        policy['Resource'] = []
        policy['Resource'].append('arn:aws:s3:::' + self.bucket)
        policy['Condition'] = {}
        policy['Condition']['StringEquals'] = {}
        policy['Condition']['StringEquals']['s3:prefix'] = [self.path + '/home/' + self.user + '/*']

        return policy

    def S3ModifyHomeDir(self, effect):
        """Generates a policy allowing the user to modify their own home S3 Bucket contents

        Arguments:
            effect {str} -- Whether to allow or deny the given actions (default: 'Deny')

        Returns:
            [dict] -- A dict representing a dynamic policy allowing the user to modify their own home S3 Bucket contents
        """
        policy = {}
        policy['Sid'] = 'S3ModifyHomeDir'
        policy['Effect'] = effect
        policy['Action'] = []
        policy['Action'].append('s3:*')
        policy['Resource'] = []
        policy['Resource'].append('arn:aws:s3:::' + self.bucket + '/' + self.path + '/home/' + self.user + '/*')

        return policy

    def MFAAllowDeny(self, effect):
        """Generates the policy based on if MFA is allowed or denied

        Arguments:
            effect {str} -- Whether to allow or deny the given actions (default: 'Deny')

        Returns:
            [dict] -- A dict representing a dynamic policy base on if MFA is allowed or denied
        """
        policy = {}
        policy['Sid'] = 'MFAAllowDeny'
        policy['Effect'] = effect
        policy['Action'] = []
        policy['Action'].append('sts:AssumeRole')
        policy['Resource'] = '*'
        policy['Condition'] = {}
        policy['Condition']['Bool'] = {}
        policy['Condition']['Bool']['aws:MultiFactorAuthPresent'] = 'false'

        return policy

    def policyDiff(self, policy1, policy2):
        """compares two policies to determine if they are the same or not

        Arguments:
            policy1 {[dict]} -- An initial policy
            policy2 {[dict]} -- A policy to compare to the first policy

        Returns:
            [bool] -- If the polices are the same False is returned. If they are different True is returned
        """
        return not policy1 == policy2

import grp
import os
import pwd
import shlex
import subprocess
import sys
from typing import Set, List
from automatagl.helpers.ssh_key_object import SSHKeyObject
from automatagl.helpers.gitlab_operations import GitlabGroupConfig
from automatagl.helpers.config_operations import sanitize_sudoers_line, sanitize_username

__all__ = [
    "UserOps",
    "UOProtectedUserError",
    "UOProtectedGroupError",
    "UOUserAlreadyExistsError",
    "UOGroupAlreadyExistsError",
    "UOUserNotFoundError",
    "UOGroupNotFoundError",
]


class UserOps:
    """
    This handles user and file creation on the local system.
    """

    base_dir: str
    default_shell: int
    delete_system_groups: bool
    delete_system_users: bool
    host_env: dict
    protected_uid_start: int
    protected_gid_start: int

    def __init__(self,
                 host_env: dict = None,
                 default_shell: str = '/bin/bash',
                 base_dir: str = '/home',
                 delete_system_groups: bool = False,
                 delete_system_users: bool = False,
                 protected_uid_start: int = 1000,
                 protected_gid_start: int = 1000,) -> None:
        """
        Used to manipulate users and groups on a Linux/Unix system
        :param host_env: The environment of the host (defaults to os.environ.copy)
        :param default_shell: The default shell used to create users
        """
        self.default_shell = default_shell
        if host_env:
            self.host_env = host_env
        else:
            self.host_env = os.environ.copy()
        self.base_dir = base_dir
        self.delete_system_groups = delete_system_groups
        self.delete_system_users = delete_system_users
        self.protected_gid_start = protected_gid_start
        self.protected_uid_start = protected_uid_start

    def create_user(self,
                    user: str,
                    group: str,
                    groups: list = None,
                    shell: str = '') -> int:
        """
        Creates a user via the `useradd` command.
        :param user: The username of the user to be created
        :param group: The main group of the user
        :param groups: A list of supplementary groups to use
        :param shell: The default shell to use (defaults to '/bin/bash')
        :return: The UID of the user created
        :raises UOUserAlreadyExistsError: If the user being created already exists
        """
        if not shell:
            shell = self.default_shell
        if groups:
            command = "useradd -b {base_dir} -s {shell} -m -g {group} -G {groups} {user}".format(
                base_dir=self.base_dir,
                user=user,
                group=group,
                groups=','.join(groups),
                shell=shell,
            )
        else:
            command = "useradd -b {base_dir} -s {shell} -m -g {group} {user}".format(
                base_dir=self.base_dir,
                user=user,
                group=group,
                shell=shell,
            )
        try:
            subprocess.check_call(shlex.split(command), env=self.host_env)
        except subprocess.CalledProcessError as e:
            if e.returncode == 9:
                raise UOUserAlreadyExistsError
            else:
                sys.exit(10)
        return self.get_user_uid(user)

    def create_group(self, group: str) -> int:
        """
        Creates a group via the `groupadd` command.
        :param group: The group name of the group to be created
        :return: The GID of the group created
        :raises UOGroupAlreadyExistsError: If the group being created already exists
        """
        command = "groupadd {group}".format(group=group)
        try:
            subprocess.check_call(shlex.split(command), env=self.host_env)
        except subprocess.CalledProcessError as e:
            if e.returncode == 9:
                raise UOGroupAlreadyExistsError
        return self.get_group_gid(group)

    def delete_user(self, user: str) -> None:
        """
        Deletes a Linux/Unix user via username
        :param user: The username of the user to delete
        :raises UOProtectedUser: If the user being deleted is a system user
        """
        if self.get_user_uid(user) < self.protected_uid_start and not self.delete_system_users:
            raise UOProtectedUserError
        command = "userdel -f {user}".format(user=user)
        subprocess.check_call(shlex.split(command), env=self.host_env)

    def convert_user(self,
                    user: str,
                    group: str,
                    groups: list = None,
                    shell: str = '') -> None:
        """
        Convert an existing Linux/Unix user via username
        :param user: The username of the user to convert
        :raises UOProtectedUser: If the user being deleted is a system user
        """
        if self.get_user_uid(user) < self.protected_uid_start:
            raise UOProtectedUserError
        if groups:
            command = "usermod -g {group} -a -G {groups} {user}".format(
                user=user,
                group=group,
                groups=groups
            )
        else:
            command = "usermod -g {group} {user}".format(
                user=user,
                group=group
            )
        subprocess.check_call(shlex.split(command), env=self.host_env)



    @staticmethod
    def generate_sudoers_file(sudoers_file: str,
                              gitlab_groups: List[GitlabGroupConfig]) -> None:
        """
        Generates the sudoers file from a list of group configurations
        :param sudoers_file: The location of the sudoers file to create
        :param gitlab_groups: A list of GitlabGroupConfig objects to parse
        :return: None
        """
        with open(sudoers_file, 'w') as f:
            template = '%{group} {sudoers_line}\n'
            for group in gitlab_groups:
                f.write(
                    template.format(
                        group=sanitize_username(group.linux_group),
                        sudoers_line=sanitize_sudoers_line(group.sudoers_line),
                    )
                )

    @staticmethod
    def get_all_users() -> list:
        """
        Returns all of the usernames present in /etc/passwd
        :return: a list of all usernames present in /etc/passwd
        """
        user_info = pwd.getpwall()
        return [i[0] for i in user_info]

    @staticmethod
    def get_all_users_in_group(gid: int) -> Set[str]:
        """
        Gets all of the users associated with a Linux group.
        :param gid: The GID of the group
        :return: A Set of users associated with the group
        """
        group_info = grp.getgrgid(gid)
        passwd_users = set([sanitize_username(i[0]) for i in pwd.getpwall() if i[3] == gid])
        group_users = set([sanitize_username(i) for i in group_info[-1]])
        return group_users.union(passwd_users)

    @staticmethod
    def get_all_groups() -> list:
        """
        Returns all of the groups present in /etc/group
        :return: a list of all groups present in /etc/group
        """
        group_info = grp.getgrall()
        return [i[0] for i in group_info]

    @staticmethod
    def get_group_gid(group: str) -> int:
        """
        Return the GID of a given group name
        :param group: The name of the group
        :return: The GID of the group
        :raises UOGroupNotFoundError: If the group is not found in /etc/group
        """
        try:
            group_info = grp.getgrnam(group)
        except KeyError:
            raise UOGroupNotFoundError
        return group_info[2]

    @staticmethod
    def get_user_uid(user: str) -> int:
        """
        Return the UID of a given user name
        :param user: The name of the user
        :return: The UID of the user
        :raises UOUserNotFoundError: If the user is not found in /etc/passwd
        """
        try:
            user_info = pwd.getpwnam(user)
        except KeyError:
            raise UOUserNotFoundError
        return user_info[2]


class UOError(Exception):
    pass


class UOGroupNotFoundError(UOError):
    pass


class UOUserNotFoundError(UOError):
    pass


class UOProtectedGroupError(UOError):
    pass


class UOProtectedUserError(UOError):
    pass


class UOUserAlreadyExistsError(UOError):
    pass


class UOGroupAlreadyExistsError(UOError):
    pass


class UOCannotCreateDirectory(UOError):

    def __init__(self, message):
        self.message = message

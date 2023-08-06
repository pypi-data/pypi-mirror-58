import subprocess
from pathlib import Path

from requests import exceptions as requests_exceptions

from briefcase.commands import (
    BuildCommand,
    CreateCommand,
    PublishCommand,
    RunCommand,
    UpdateCommand
)
from briefcase.config import BaseConfig
from briefcase.exceptions import BriefcaseCommandError, NetworkFailure
from briefcase.platforms.linux import LinuxMixin


class LinuxAppImageMixin(LinuxMixin):
    output_format = 'appimage'

    def bundle_path(self, app):
        return self.platform_path / '{app.formal_name}.AppDir'.format(app=app)

    def binary_path(self, app):
        binary_name = app.formal_name.replace(' ', '_')
        return self.platform_path / '{binary_name}-{app.version}-{self.host_arch}.AppImage'.format(
            app=app,
            self=self,
            binary_name=binary_name,
        )

    def distribution_path(self, app):
        return self.binary_path(app)

    def verify_tools(self):
        """
        Verify that we're on Linux.
        """
        if self.host_os != 'Linux':
            raise BriefcaseCommandError("""
Linux AppImages can only be generated on Linux.
""")


class LinuxAppImageCreateCommand(LinuxAppImageMixin, CreateCommand):
    description = "Create and populate a Linux AppImage."

    @property
    def support_package_key_prefix(self):
        return 'python/{self.python_version_tag}/{self.platform}/{self.host_arch}/'.format(
            self=self,
        )


class LinuxAppImageUpdateCommand(LinuxAppImageMixin, UpdateCommand):
    description = "Update an existing Linux AppImage."


class LinuxAppImageBuildCommand(LinuxAppImageMixin, BuildCommand):
    description = "Build a Linux AppImage."

    @property
    def linuxdeploy_download_url(self):
        return (
            'https://github.com/linuxdeploy/linuxdeploy/'
            'releases/download/continuous/linuxdeploy-{self.host_arch}.AppImage'.format(
                self=self
            )
        )

    def verify_tools(self):
        super().verify_tools()

        try:
            print()
            print("Ensure we have the linuxdeploy AppImage...")
            self.linuxdeploy_appimage = self.download_url(
                url=self.linuxdeploy_download_url,
                download_path=Path.home() / '.briefcase' / 'tools'
            )
            self.os.chmod(str(self.linuxdeploy_appimage), 0o755)
        except requests_exceptions.ConnectionError:
            raise NetworkFailure('downloading linuxdeploy AppImage')

    def build_app(self, app: BaseConfig, **kwargs):
        """
        Build an application.

        :param app: The application to build
        """
        print()
        print("[{app.name}] Building AppImage...".format(app=app))

        try:
            print()
            # Build the AppImage.
            # For some reason, the version has to be passed in as an
            # environment variable, *not* in the configuration...
            env = self.os.environ.copy()
            env['VERSION'] = app.version
            self.subprocess.run(
                [
                    str(self.linuxdeploy_appimage),
                    "--appdir={appdir}".format(appdir=self.bundle_path(app)),
                    "-d", str(
                        self.bundle_path(app) / "{app.bundle}.{app.name}.desktop".format(
                            app=app,
                        )
                    ),
                    "-o", "appimage",
                ],
                env=env,
                check=True,
                cwd=str(self.platform_path)
            )

            # Make the binary executable.
            self.os.chmod(str(self.binary_path(app)), 0o755)
        except subprocess.CalledProcessError:
            print()
            raise BriefcaseCommandError(
                "Error while building app {app.name}.".format(app=app)
            )


class LinuxAppImageRunCommand(LinuxAppImageMixin, RunCommand):
    description = "Run a Linux AppImage."

    def run_app(self, app: BaseConfig, **kwargs):
        """
        Start the application.

        :param app: The config object for the app
        :param base_path: The path to the project directory.
        """
        print()
        print('[{app.name}] Starting app...'.format(
            app=app
        ))
        try:
            print()
            self.subprocess.run(
                [
                    str(self.binary_path(app)),
                ],
                check=True,
            )
        except subprocess.CalledProcessError:
            print()
            raise BriefcaseCommandError(
                "Unable to start app {app.name}.".format(app=app)
            )


class LinuxAppImagePublishCommand(LinuxAppImageMixin, PublishCommand):
    description = "Publish a Linux AppImage."


# Declare the briefcase command bindings
create = LinuxAppImageCreateCommand  # noqa
update = LinuxAppImageUpdateCommand  # noqa
build = LinuxAppImageBuildCommand  # noqa
run = LinuxAppImageRunCommand  # noqa
publish = LinuxAppImagePublishCommand  # noqa

# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.report.plugins import Plugin, RedHatPlugin


class Vsftpd(Plugin, RedHatPlugin):

    short_desc = 'Vsftpd server'

    plugin_name = 'vsftpd'
    profiles = ('services',)

    files = ('/etc/vsftpd',)
    packages = ('vsftpd',)

    def setup(self):
        self.add_copy_spec([
            "/etc/ftp*",
            "/etc/vsftpd"
        ])

# vim: set et ts=4 sw=4 :

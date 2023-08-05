
from os.path import join

from cbsettings import DjangoDefaults


class BaseSeoSettings(object):

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            'seo',
            'sitemetrics'
        ]

from securitas.representation import Representation

class User(Representation):
    @property
    def username(self):
        return self._attr('uid')

    @property
    def name(self):
        if 'displayname' in self.raw:
            return self._attr('displayname')
        if 'gecos' in self.raw:
            return self._attr('gecos')
        if 'cn' in self.raw:
            return self._attr('cn')
        return None

    @property
    def mail(self):
        return self._attr('mail')

    @property
    def timezone(self):
        return self._attr('fastimezone')

    @property
    def locale(self):
        return self._attr('faslocale')

    @property
    def ircnick(self):
        return self._attr('fasircnick')

    @property
    def gpgkeys(self):
        return self._attrlist('fasgpgkeyid')

    @property
    def groups(self):
        return self._attrlist('memberof_group')

from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin
from django.urls import reverse


class DjangoLedgerAccessMixIn(AccessMixin):

    def get_login_url(self):
        # return reverse('login')
        print("WENT TO MIXINS")
        pass


class DjangoLedgerPermissionMixIn(PermissionRequiredMixin):

    def has_permission(self):
        return self.request.user.is_authenticated


class DjangoLedgerSecurityMixIn(DjangoLedgerPermissionMixIn, DjangoLedgerAccessMixIn, LoginRequiredMixin):
    pass

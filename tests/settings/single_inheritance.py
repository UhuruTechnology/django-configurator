from .base import Base


class Inheritance(Base):
    @property
    def ALLOWED_HOSTS(self):
        try:
            allowed_hosts = super().ALLOWED_HOSTS[:]
        except Exception:
            allowed_hosts = []
        allowed_hosts.append("test")
        return allowed_hosts

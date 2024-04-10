from esmerald import Include, Gateway, Inject, Factory

from .controller import RoleAPIView


route_patterns = [
    Gateway(handler=RoleAPIView)
]

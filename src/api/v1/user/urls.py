from esmerald import Include, Gateway

from .user_controller import UserAPIView


route_patterns = [
    Gateway(handler=UserAPIView),
]

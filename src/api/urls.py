from esmerald import Include, Gateway, Router


route_patterns = [
    Include("/admin", routes=[
        Include("/roles", namespace="src.api.v1.role.urls"),
        Include("/users", namespace="src.api.v1.user.urls"),
    ]),

]


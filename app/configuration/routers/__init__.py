from app.configuration.routers.routers import Routers
from app.internal.example_route import example


__routes__ = Routers(routers=(example.router, ))

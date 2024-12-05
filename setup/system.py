import os
import importlib

def load_routers(app, options = {}):
    routers = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..', 'routers')
    routes = [ dict(path=f.path, name = f.name) for f in os.scandir(routers) if f.is_file()]
    for subfolder in routes:
        fname = os.path.join(subfolder['path'])
        if not os.path.isfile(fname) : continue
        print(fname)
        spec = importlib.util.spec_from_file_location(subfolder['name'], fname)
        router = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(router)
        app.include_router(router.router, prefix = f"/library/{subfolder['name']}")
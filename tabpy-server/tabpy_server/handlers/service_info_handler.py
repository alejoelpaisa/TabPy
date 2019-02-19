import simplejson
from tabpy_server.handlers import ManagementHandler


class ServiceInfoHandler(ManagementHandler):
    def initialize(self, tabpy_state, python_service):
        super(ServiceInfoHandler, self).initialize(tabpy_state, python_service)

    def get(self):
        self._add_CORS_header()
        info = {}
        info['description'] = self.tabpy_state.get_description()
        info['creation_time'] = self.tabpy_state.creation_time
        info['state_path'] = self.settings['state_file_path']
        info['server_version'] = self.settings['server_version']
        info['name'] = self.tabpy_state.name
        info['versions'] = self.settings['versions']
        self.write(simplejson.dumps(info))

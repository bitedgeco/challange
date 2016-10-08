# -*- coding: utf-8 -*-
class CDN(object):

    def __init__(self):
        """Initialize a CDN"""
        # This graph is a dictionary with server as keys and a list of conections (arcs) as values
        self.graph = {
            'New York': ['London', 'Seattle'],
            'Chicago': ['Washington D.C.', 'Austin', 'Buenos Ares'],
            'San Francisco': ['Washington D.C.', 'Montreal'],
            'Seattle': ['New York', 'Austin'],
            'Washington D.C.': ['New York', 'Montreal'],
            'Austin': ['Chicago', 'Mexico City'],
            'Montreal': ['San Francisco', 'Mexico City'],
            'Mexico City': ['Seattle'],

            'London': ['Cairo', 'Rome'],
            'Paris': ['Beijing', 'Moscow'],
            'Moscow': ['London', 'Berlin'],
            'Berlin': ['Paris', 'Berlin'],
            'Rome': ['Paris', 'Rome'],

            'Cairo': ['Tokyo', 'Johannesburg'],
            'Johannesburg': ['San Francisco', 'Cairo'],

            'Tokyo': ['Chicago', 'Mumbai'],
            'Beijing': ['Tokyo', 'Sydney'],
            'Bangkok': ['Beijing', 'Sydney'],
            'Mumbai': ['Bangkok', 'Sao Paulo', 'Seoul'],
            'Sydney': ['Bangkok', 'Seoul'],
            'Seoul': ['Mumbai', 'Tokyo'],

            'Buenos Ares': ['Moscow', 'Sao Paulo'],
            'Sao Paulo': ['Johannesburg', 'Buenos Ares']}

        # This dicionary has servers as keys and a list of files stored there as values
        self.content = {}
        for server in list(self.graph.keys()):
            self.content[server] = []

    def post(self, file, user_server):
        """posts content to every server on the network

        first argument 'file' is the content to upload.
        Second argument 'user_server' is ther users server they are posing from"""
        self.update_network(user_server, 'store_data', file)
        return (200, 'Distributed {}'.format(file))

    def get(self, file, user_server):
        """gets content from the network and shows the path used

        first argument 'file' is the content to get
        second argument ' user_server' is where we will get it from"""
        seen = []
        potential_paths = [[user_server, ]]
        while potential_paths:
            path = potential_paths[0]
            potential_paths = potential_paths[1:]
            source = path[0]
            if file in self.content[source]:
                return (200, 'Retrieved {} via {}'.format(file, path))
            for i in self.graph.get(source, []):
                if i not in seen:
                    potential_paths.append([i, ] + path)
                    seen.append(i)
        return (404, '{} does not exist'.format(file))

    def put(self, file, user_server):
        """replace content on servers

        first argument 'file' is the content to replace
        second argument 'user_server' is where we start"""
        if file in self.content[user_server]:
            self.update_network(user_server, 'update_data', file)
            return (200, 'Updated {}'.format(file))
        else:
            return (404, '{} does not exist'.format(file))

    def delete(self, file, user_server):
        """remove content

        first argument 'file' is the content to be removed
        second argument 'user_server' is where we start"""
        if file in self.content[user_server]:
            self.update_network(user_server, 'remove_data', file)
            return (200, 'Delete {}'.format(file))
        else:
            return (404, '{} does not exist'.format(file))

    def update_network(self, start_node, action, file):
        """stores, updates or removes data from the network depending on 'action' argument"""
        seen = [start_node]
        nodes = [start_node]
        while nodes:
            node = nodes.pop()
            if action == 'store_data':
                if node not in self.content:
                    self.content[node] = []
                self.content[node].append(file)
            if action == 'update_data':
                if node not in self.content:
                    self.content[node] = []
                    self.content[node].append(file)
            if action == 'remove_data':
                if node in self.content:
                    self.content[node].remove(file)
            for connected_node in self.graph.get(node, []):
                if connected_node not in seen:
                    seen.append(connected_node)
                    nodes.append(connected_node)

if __name__ == "__main__":
    cdn = CDN()
    print('initial state of cdn')
    print(cdn.content)
    print("")
    print('puting verious files on from various servers')
    print(cdn.post('vid', 'Tokyo'))
    print(cdn.post('book', 'London'))
    print(cdn.post('photo', 'Cairo'))
    print("")
    print('new state of cdn')
    print(cdn.content)
    print("")
    print('get file named "vid" from Tokyo server')
    print(cdn.get('vid', 'Tokyo'))
    print("")
    print('try to get file named "doc" from Tokyo server')
    print(cdn.get('doc', 'Tokyo'))
    print("")
    print('update file named "book" from Rome')
    print(cdn.put('book', 'Rome'))
    print("")
    print('try to update file named "doc" from Rome"')
    print(cdn.put('doc', 'Rome'))
    print("")
    print('delete file named "vid" from London')
    print(cdn.delete('vid', 'London'))
    print("")
    print('new state of cdn')
    print(cdn.content)
    print("")
    print('try to delete file named "scan" from Cairo')
    print(cdn.delete('scan', 'Cairo'))

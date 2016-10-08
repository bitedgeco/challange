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

            'London': ['Cairo', 'Moscow', 'Rome'],
            'Paris': ['Beijing', 'Moscow'],
            'Moscow': ['London', 'Berlin'],
            'Berlin': ['Paris', 'Berlin'],
            'Rome': ['Paris', 'Rome'],

            'Cairo': ['Tokyo', 'Johannesburg'],
            'Johannesburg': ['San Francisco', 'Cairo'],

            'Tokyo': ['Chicago', 'Mumbai'],
            'Beijing': ['Tokyo', 'Sydney'],
            'Bangkok': ['Beijing', 'Sydney'],
            'Mumbai': ['Bangkok', 'Sao Paulo'],
            'Sydney': ['Bangkok'],
            'Seoul': ['Mumbai'],

            'Buenos Ares': ['Moscow', 'Sao Paulo'],
            'Sao Paulo': ['Johannesburg', 'Buenos Ares']}

        # This dicionary has servers as keys and a list of files stored there as values
        self.content = {}
        for server in list(self.graph.keys()):
            self.content[server] = []

    def put(self, file, server):
        """puts content on the network

        first argument 'file' is the content to upload.
        Second argument 'server' is where it will be stored"""
        self.content[server].append(file)
        return 'Status:200, the file named "{}" was succesfuly distributed at {}.'\
            .format(file, server)

    def get(self, file, user_server):
        """gets content from the network and returns the path it took

        first argument 'file' is the content to get
        second argument ' user_server' is the users closest server"""
        for lsts in self.content.values():
            if file in lsts:
                for key, vals in self.content.items():
                    if file in vals:
                        file_server = key
                        path = self.find_path(file_server, user_server)
                return 'status:200, retrieved file named "{}" from {}. The path was{}'\
                    .format(file, file_server, path)
        return 'status 404, there is no file named "{}"'.format(file)

    def post(self, old_file, new_file):
        """update content on server

        first argument 'old_file' is the content to replace
        second argument 'new_file' is the content to replace is with"""
        for lsts in self.content.values():
            if old_file in lsts:
                for key, vals in self.content.items():
                    if old_file in vals:
                        server = key
                self.content[server].remove(old_file)
                self.content[server].append(new_file)
                return 'status:200, file named "{}" has been updated to file named "{}"'\
                    .format(old_file, new_file)
        return 'status 404 there is no file named "{}"'.format(old_file)

    def delete(self, file):
        """remove content

        first argument is the content to be removed"""
        for lsts in self.content.values():
            if file in lsts:
                for key, vals in self.content.items():
                    if file in vals:
                        server = key
                self.content[server].remove(file)
                return 'status:200, file named "{}" has been removed'.format(file)
        return 'status 404 there is no file named "{}"'.format(file)

    def find_path(self, start, end, path=[]):
        """Finds a path between start and end nodes in a graph"""
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

    def get_key_from_val(self, file):
        """We should use this every time we run the code contained in it,
        I am not sure why it always seems to return None"""
        for lsts in self.content.values():
            if file in lsts:
                for server, vals in self.content.items():
                    if file in vals:
                        return server
        return None


if __name__ == "__main__":
    cdn = CDN()
    print('initial state of cdn')
    print(cdn.content)
    print("")
    print('puting verious files on various servers')
    print(cdn.put('vid', 'Tokyo'))
    print(cdn.put('pic', 'Tokyo'))
    print(cdn.put('book', 'London'))
    print(cdn.put('photo', 'Cairo'))
    print(cdn.put('movie', 'New York'))
    print(cdn.put('music', 'Sydney'))
    print(cdn.put('tune', 'Rome'))
    print(cdn.put('doc', 'Paris'))
    print(cdn.put('scan', 'Tokyo'))
    print(cdn.put('speread sheet', 'Tokyo'))
    print("")
    print('new state of cdn')
    print(cdn.content)
    print("")
    print('current state of Tokyo server')
    print(cdn.content['Tokyo'])
    print("")
    print('get file named "scan" from Tokyo server while in London')
    print(cdn.get('scan', 'London'))
    print("")
    print('update file named "scan" to file named "Awsome scan!"')
    print(cdn.post('scan', 'Awsome scan!'))
    print("")
    print('new state of Tokyo server')
    print(cdn.content['Tokyo'])
    print("")
    print('delete file named "vid" from Tokyo server')
    print(cdn.delete('vid'))
    print("")
    print('new state of Tokyo server')
    print(cdn.content['Tokyo'])
    print("")
    print('find path from Sydney to Seattle')
    print(cdn.find_path('Sydney', 'Seattle'))

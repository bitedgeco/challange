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
        """puts content on every server on the network

        first argument 'file' is the content to upload.
        Second argument 'server' is ther users server"""
        for lsts in list(self.content.values()):
            lsts.append(file)
        return 'Status:200, the file named "{}" was succesfuly distributed from {}.'\
            .format(file, server)

    def get(self, file, server):
        """gets content from the network and returns the path it took

        first argument 'file' is the content to get
        second argument ' user_server' is where we will get it from"""
        if file in self.content[server]:
            return 'status:200, retrieved file named "{}" from {}'.format(file, server)
        else:
            return 'status 404, there is no file named "{}" on {} server'.format(file, server)

    def post(self, old_file, new_file):
        """update content on servers

        first argument 'old_file' is the content to replace
        second argument 'new_file' is the content to replace is with"""
        if old_file in self.content['Tokyo']:
            for lst in self.content.values():
                lst.remove(old_file)
                lst.append(new_file)
            return 'status:200, file named "{}" has been updated to file named "{}"'\
                .format(old_file, new_file)
        else:
            return 'status 404 there is no file named "{}"'.format(old_file)

    def delete(self, file):
        """remove content

        first argument is the content to be removed"""
        if file in self.content['Tokyo']:
            for lst in self.content.values():
                lst.remove(file)
            return 'status:200, file named "{}" has been deleted'.format(file)
        else:
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
    print('puting verious files on from various servers')
    print(cdn.put('vid', 'Tokyo'))
    print(cdn.put('book', 'London'))
    print(cdn.put('photo', 'Cairo'))
    print("")
    print('new state of cdn')
    print(cdn.content)
    print("")
    print('get file named "vid" from Tokyo server')
    print(cdn.get('vid', 'Tokyo'))
    print("")
    print('try to get file named "doc" from Tokyo server')
    print(cdn.get('scan', 'Tokyo'))
    print("")
    print('update file named "book" to file named "Awsome book!"')
    print(cdn.post('book', 'Awsome book!'))
    print("")
    print('new state of cdn')
    print(cdn.content)
    print("")
    print('try to update file named "doc" to file named "Awsome doc!"')
    print(cdn.post('doc', 'Awsome doc!'))
    print("")
    print('delete file named "vid"')
    print(cdn.delete('vid'))
    print("")
    print('new state of cdn')
    print(cdn.content)
    print("")
    print('try to delete file named "scan"')
    print(cdn.delete('scan'))
    print("")
    print('find path from Sydney to Seattle')
    print(cdn.find_path('Sydney', 'Seattle'))

# -*- coding: utf-8 -*-
class CDN(object):

    def __init__(self):
        """Initialize a CDN"""
        # This graph is a dictionary with nodes as keys and a list of arcs as values
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

        # This dicionary has nodes as keys and a list of files stored there as values
        self.content = {
            'New York': [],
            'Chicago': [],
            'San Francisco': [],
            'Seattle': [],
            'Washington D.C.': [],
            'Austin': [],
            'Montreal': [],
            'Mexico City': [],
            'London': [],
            'Paris': [],
            'Moscow': [],
            'Berlin': [],
            'Rome': [],
            'Cairo': [],
            'Johannesburg': [],
            'Tokyo': [],
            'Beijing': [],
            'Bangkok': [],
            'Mumbai': [],
            'Sydney': [],
            'Seoul': [],
            'Buenos Ares': [],
            'Sao Paulo': []}

    def put(self, file, server):
        """puts content on the network

        first argument 'file' is the content. Second argument 'server' is where it will be stored"""
        self.content[server].append(file)
        return 'Status:200, the file named "{}" was succesfuly distributed at {}.'.format(file, server)

    def get(self, file, server):
        """gets content from the network"""
        for lsts in self.content.values():
            if file in lsts:
                return 'status:200, retrieved file named "{}"'.format(file)
        return 'status 404, there is no file named "{}"'.format(file)

    def post(self, old_file, new_file):
        """update content"""
        for lsts in self.content.values():
            if old_file in lsts:
                for k, v in self.content.items():
                    if old_file in v:
                        key = k
                self.content[key].remove(old_file)
                self.content[key].append(new_file)
                return 'status:200, file named "{}" has been updated to file named "{}"'.format(old_file, new_file)
        return 'status 404 there is no file named "{}"'.format(old_file)

    def delete(self, file):
        """remove content"""
        for lsts in self.content.values():
            if file in lsts:
                for k, v in self.content.items():
                    if file in v:
                        key = k
                self.content[key].remove(file)
                return 'status:200, file named "{}" has been removed'.format(file)
        return 'status 404 there is no file named "{}"'.format(file)

    def find_path(self, start, end, path=[]):
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

    def get_key_from_val(self, val):
        for lsts in self.content.values():
            if val in lsts:
                for k, v in self.content.items():
                    if val in v:
                        key = k
            else:
                key = None
        return key









# if __name__ == "__main__":
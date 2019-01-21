import abc
import pickle


class Storage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_block(self, hash):
        raise NotImplementedError

    @abc.abstractmethod
    def put_block(self, block):
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_block(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_hash(self):
        raise NotImplementedError

    def empty(self):
        return self.get_last_hash() == None


class InMemoryStorage(Storage):

    def __init__(self):
        self.db = {}

    def get_block(self, hash):
        return self.db.get(hash)

    def put_block(self, block):
        self.db[block.hash] = block
        self.db['last'] = block.hash

    def get_last_block(self):
        last_hash = self.get_last_hash()
        return self.get_block(last_hash)

    def get_last_hash(self):
        return self.db.get('last')

    def empty(self):
        return super(InMemoryStorage, self).empty()


class FileStorage(Storage):
    def __init__(self, path):
        self.path = path

    def get_block(self, hash):
        with open(self.path, 'rb') as f:
            d = pickle.load(f)
            return d.get(hash)

    def put_block(self, block):
        d = {}
        try:
            with open(self.path, 'rb') as f:
                d = pickle.load(f)
        except FileNotFoundError:
            pass

        d[block.hash] = block
        d['last'] = block.hash

        with open(self.path, 'wb') as f:
            pickle.dump(d, f)

    def get_last_block(self):
        with open(self.path, 'rb') as f:
            d = pickle.load(f)
            last_hash = d.get('last')
            return d.get(last_hash)

    def get_last_hash(self):
        try:
            with open(self.path, 'rb') as f:
                d = pickle.load(f)
                return d.get('last')
        except FileNotFoundError:
            return None

    def empty(self):
        return super(FileStorage, self).empty()

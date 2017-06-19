"""
def processor(reader, converter, writer):
    while True:
        data = reader.read()
        if not data:
            break
        data = converter(data)
        writer.write(data)
"""


class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        """
        抽象超类.
        assert False 意味着调用该方法一定失败.
        """
        assert False, 'converter must be defined'


class UpperCase(Processor):
    def converter(self, data):
        if 'class' in data:
            return data.upper()
        else:
            return data.lower()
        # return data.upper()


if __name__ == '__main__':
    import sys
    obj = UpperCase(open('classtree.py'), sys.stdout)
    obj.process()

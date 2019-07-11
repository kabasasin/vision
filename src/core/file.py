# wrapper for file system

import os


class FileStorage(object):
    def __init__(self, directory):
        if not os.path.exists(directory):
            raise Exception("diretory `{}` is not exists".format(directory))
        self.directory = directory

    def access_check(self, premission):
        return os.access(self.directory, premission)

    def new(self, file_name, content):
        path = "{}/{}".format(self.directory, file_name)
        try:
            with open(path, "w") as f:
                f.write(content)
        except Exception as e:
            raise Exception(
                "create new file: `{}` failed: {}".format(file_name, e)
            )

    def delete(self, file_name):
        path = "{}/{}".format(self.directory, file_name)
        try:
            remove_result = os.remove(path)
            if remove_result:
                raise Exception(str(remove_result))
        except Exception as e:
            raise Exception("delete file: `{}` failed: {}".format(path, e))

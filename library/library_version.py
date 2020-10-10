
class LibraryVersion:

    def __init__(self, version):
        self.__major = 0
        self.__minor = 0
        self.__patch = 0

        snippets = version.split('.')
        if self.check_pattern(snippets):
            for _ in range(3 - len(snippets)):
                snippets.append('0')
            self.__major, self.__minor, self.__patch = map(int, snippets)

    @staticmethod
    def check_pattern(snippets):
        for snippet in snippets:
            if not snippet:
                return False
            for c in snippet:
                if not c.isdigit():
                    return False
        return True

    def is_older_than(self, version):
        if self.__major > version.get_major():
            return False
        elif self.__major == version.get_major():
            if self.__minor > version.get_minor():
                return False
            elif self.__minor == version.get_minor():
                if self.__patch >= version.get_patch():
                    return False
        return True

    def is_valid(self):
        return self.__major or self.__minor or self.__patch

    def get_major(self):
        return self.__major

    def get_minor(self):
        return self.__minor

    def get_patch(self):
        return self.__patch

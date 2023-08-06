import os
import datetime


class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger:
    """A class for logging data to a file"""

    def __init__(self, filename="log.txt", context=""):
        self.filename = filename
        self.lines = []
        self.set_context(context)

    def set_context(self, context):
        if not "[" in context and not "] " in context:
            if (context == "" or context == " "):
                self._context = ""
            else:
                self._context = f"[{context}] "
        else:
            self._context = context

    def save(self):
        """Saves log under specified filename"""
        self.file = open(self.filename, "w")
        self.file.writelines(self.lines)
        self.file.close()

    def timestamp_now(self, extra_long=False):
        now = datetime.datetime.now()
        string = f"[{now.hour}:{now.minute}:{now.second}"
        if extra_long:
            string += f":{now.microsecond}"
        string += "]"
        return string

    def get_success(self, text, display=True):
        if display:
            print(col.OKGREEN + self._context + self.timestamp_now() +
                  col.ENDC + " " + text)
        string = "[SUCCESS] " + self._context + \
            self.timestamp_now() + " " + text
        return string

    def get_debug(self, text, display=False):
        if display:
            print(col.OKBLUE + self._context + self.timestamp_now() +
                  col.ENDC + " " + text)
        string = "[DEBUG] " + self._context + self.timestamp_now() + " " + text
        return string

    def get_warning(self, text, display=False):
        if display:
            print(col.WARNING + self._context + self.timestamp_now() +
                  col.ENDC + " " + text)
        string = "[WARNING] " + self._context + \
            self.timestamp_now() + " " + text
        return string

    def get_error(self, text, display=True):
        if display:
            print(col.FAIL + self._context + self.timestamp_now() +
                  col.ENDC + " " + text)
        string = "[ERROR] " + self._context + self.timestamp_now() + " " + text
        return string

    def get_plain(self, text, display=True, extra_long=False):
        string = self._context + self.timestamp_now(extra_long) + " " + text
        if display:
            print(string)
        return string

    def success(self, text, display=True):
        string = self.get_success(text, display)
        string += "\n"
        self.lines.append(string)

    def debug(self, text, display=False):
        string = self.get_debug(text, display)
        string += "\n"
        self.lines.append(string)

    def warning(self, text, display=False):
        string = self.get_warning(text, display)
        string += "\n"
        self.lines.append(string)

    def error(self, text, display=True):
        string = self.get_error(text, display)
        string += "\n"
        self.lines.append(string)

    def plain(self, text, display=False, extra_long=False):
        string = self.get_plain(text, display, extra_long)
        string += "\n"
        self.lines.append(string)

    def clear(self):
        """Clear all lines"""
        self.lines = []

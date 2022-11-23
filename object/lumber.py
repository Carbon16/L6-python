import os
import time
from flask import Flask


def writeRiver(riverDir, message):
    path = riverDir + "/river.log"
    with open(path, 'a') as f:
        f.write(message)

class lumberjack:
    river = []
    infoRiver = []
    debugRiver = []
    warnRiver = []
    errorRiver = []
    criticalRiver = []
    fatalRiver = []

    def __init__(self, logName = "log", path = None, include = "LOG", verbose = False):
        if path == None:
            raise Exception("You must define the log directory!")
        self.dir = path
        self.name = logName
        self.include = include
        self.verbose = verbose
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
    
    def log(self, message, level="INFO", filename="", comment=""):
        path = self.dir + "/river.log"
        dt = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "level": level,
            "message": message,
            "comment": comment,
            "path": filename,
            "time": dt
        }
        message = dt + '   ' + self.name + '   ' + level + ":      " + message + "   " + filename + '     ' + comment + "\r\n"
        if self.verbose:
            # print(entry)
            # print(self.river)
            print(message)
        with open(path, "a") as f:
            f.write(message)
        if level == "INFO":
            self.infoRiver.append(entry)
        elif level == "DEBUG":
            self.debugRiver.append(entry)
        elif level == "WARN":
            self.warnRiver.append(entry)
        elif level == "ERROR":
            self.errorRiver.append(entry)
        elif level == "CRITICAL":
            self.criticalRiver.append(entry)
        elif level == "FATAL":
            self.fatalRiver.append(entry)
        self.river.append(entry)
        # save file
        path = self.dir + "/" + level + ".log"
        with open(path, "a") as f:
            f.write(message)
            
    def info(self, message, filename = "", comment = ""):
        path = self.dir + "/INFO.log"
        level = "INFO"
        dt = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "level": level,
            "message": message,
            "comment": comment,
            "path": filename,
            "time": dt
        }
        message = dt + '   ' + self.name + '   ' + level + ":      " + message + "   " + filename + '     ' + comment + "\r\n"
        if self.verbose:
            print(message)
        self.infoRiver.append(entry)
        self.river.append(entry)
        with open(path, "a") as f:
            f.write(message)
        writeRiver(self.dir, message)
    
    def debug(self, message, filename = "", comment = ""):
        path = self.dir + "/DEBUG.log"
        level = "DEBUG"
        dt = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "level": level,
            "message": message,
            "comment": comment,
            "path": filename,
            "time": dt
        }
        message = dt + '   ' + self.name + '   ' + level + ":      " + message + "   " + filename + '     ' + comment + "\r\n"
        if self.verbose:
            print(message)
        self.debugRiver.append(entry)
        self.river.append(entry)
        with open(path, "a") as f:
            f.write(message)
        writeRiver(self.dir, message)
        
    def warn(self, message, filename = "", comment = ""):
        path = self.dir + "/WARN.log"
        level = "WARN"
        dt = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "level": level,
            "message": message,
            "comment": comment,
            "path": filename,
            "time": dt
        }
        message = dt + '   ' + self.name + '   ' + level + ":      " + message + "   " + filename + '     ' + comment + "\r\n"
        if self.verbose:
            print(message)
        self.warnRiver.append(entry)
        self.river.append(entry)
        with open(path, "a") as f:
            f.write(message)
        writeRiver(self.dir, message)
        
    def error(self, message, filename = "", comment = ""):
        path = self.dir + "/ERROR.log"
        level = "ERROR"
        dt = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "level": level,
            "message": message,
            "comment": comment,
            "path": filename,
            "time": dt
        }
        message = dt + '   ' + self.name + '   ' + level + ":      " + message + "   " + filename + '     ' + comment + "\r\n"
        if self.verbose:
            print(message)
        self.errorRiver.append(entry)
        self.river.append(entry)
        with open(path, "a") as f:
            f.write(message)
        writeRiver(self.dir, message)
    
    def critical(self, message, filename = "", comment = ""):
        path = self.dir + "/CRITICAL.log"
        level = "CRITICAL"
        dt = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "level": level,
            "message": message,
            "comment": comment,
            "path": filename,
            "time": dt
        }
        message = dt + '   ' + self.name + '   ' + level + ":      " + message + "   " + filename + '     ' + comment + "\r\n"
        if self.verbose:
            print(message)
        self.criticalRiver.append(entry)
        self.river.append(entry)
        with open(path, "a") as f:
            f.write(message)
        writeRiver(self.dir, message)
        
    def fatal(self, message, filename = "", comment = ""):
        path = self.dir + "/FATAL.log"
        level = "FATAL"
        dt = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "level": level,
            "message": message,
            "comment": comment,
            "path": filename,
            "time": dt
        }
        message = dt + '   ' + self.name + '   ' + level + ":      " + message + "   " + filename + '     ' + comment + "\r\n"
        if self.verbose:
            print(message)
        self.fatalRiver.append(entry)
        self.river.append(entry)
        with open(path, "a") as f:
            f.write(message)
        writeRiver(self.dir, message)

hello = lumberjack("hello", "hello", True)
hello.log("hello", "hello", "hello")
hello.critical("hello", "hello", "hello")

class yeetus(lumberjack):
    def __init__(port, river, infoRiver, debugRiver, warnRiver, errorRiver, criticalRiver, fatalRiver):
        super().__init__(river, infoRiver, debugRiver, warnRiver, errorRiver, criticalRiver, fatalRiver)

    def startServer(self, port = 3000):
        from flask import Flask
        app = Flask(__name__)
        @app.route('/')
        def index():
            return river
        @app.route('/river')
        def river():
            return self.river
        @app.route('/info')
        def info():
            return self.infoRiver
        @app.route('/debug')
        def debug():
            return self.debugRiver
        @app.route('/warn')
        def warn():
            return self.warnRiver
        @app.route('/error')
        def error():
            return self.errorRiver
        @app.route('/critical')
        def critical():
            return self.criticalRiver
        @app.route('/fatal')
        def fatal():
            return self.fatalRiver
        app.run(port = port)
        
yeetus(3000).startServer()
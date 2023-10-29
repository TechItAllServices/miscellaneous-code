import time
import os
import psutil

def clearFile(x):
    f = open(x, "w")
    f.close()
def boot():
    os.system("cls")
    clearFile(r"Main-Log.log")
    os.system("cls")
boot()

class LogLevel:
    INFO = 1
    DEBUG = 2
    WARNING = 3
    ERROR = 4
    FATAL_ERROR = 5

class Logger:
    def __init__(self):
        self.log_level = LogLevel.INFO

    def set_log_level(self, log_level):
        self.log_level = log_level

    def log(self, log_level, message):
        if log_level >= self.log_level:
            color = self.get_color(log_level)
            timestamp = self.get_timestamp()
            print(f"{color}[{log_level}] {timestamp} {message}\033[0m")

    def get_color(self, log_level):
        if log_level == LogLevel.DEBUG:
            return "\033[92m"  # Green
        elif log_level == LogLevel.WARNING:
            return "\033[93m"  # Yellow
        elif log_level == LogLevel.ERROR:
            return "\033[91m"  # Red
        elif log_level == LogLevel.FATAL_ERROR:
            return "\033[31;2m"  # Dark Red
        else:
            return "\033[0m"  # White

    def get_timestamp(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class Info:
    def __init__(self, logger):
        self.logger = logger

    def log(self, message):
        self.logger.log(LogLevel.INFO, message)

class Debug:
    def __init__(self, logger):
        self.logger = logger

    def log(self, message):
        self.logger.log(LogLevel.DEBUG, message)

class Warning:
    def __init__(self, logger):
        self.logger = logger

    def log(self, message):
        self.logger.log(LogLevel.WARNING, message)

class Error:
    def __init__(self, logger):
        self.logger = logger

    def log(self, message):
        self.logger.log(LogLevel.ERROR, message)

class FatalError:
    def __init__(self, logger):
        self.logger = logger

    def log(self, message):
        self.logger.log(LogLevel.FATAL_ERROR, message)

# Example usage
logger = Logger()
info = Info(logger)
debug = Debug(logger)
warning = Warning(logger)
error = Error(logger)
fatal_error = FatalError(logger)

# Set the log level
logger.set_log_level(LogLevel.INFO)

# Thresholds for different log levels
DEBUG_THRESHOLD = 50
WARNING_THRESHOLD = 70
ERROR_THRESHOLD = 90
FATAL_ERROR_THRESHOLD = 100

# Generate log messages in an infinite loop
while True:
    cpu_usage = psutil.cpu_percent()
    log_level = None

    if cpu_usage >= FATAL_ERROR_THRESHOLD:
        log_level = fatal_error
    elif cpu_usage >= ERROR_THRESHOLD:
        log_level = error
    elif cpu_usage >= WARNING_THRESHOLD:
        log_level = warning
    elif cpu_usage >= DEBUG_THRESHOLD:
        log_level = debug
    else:
        log_level = info

    message = f"CPU usage: {cpu_usage}%"
    log_level.log(message)

    if log_level != info:
        with open("Main-Log.log", 'a') as f:
            timestamp = logger.get_timestamp()
            f.write(f"{log_level.__class__.__name__}: {timestamp} {message}\n")

    delay = 1.0  # Delay of 1 second between logs
    time.sleep(delay)

















































# import time
# import os
# import psutil

# def clearFile(x):
#     f = open(x, "w")
#     f.close()
# def boot():
#     os.system("cls")
#     clearFile(r"C:\Users\blues\Desktop\VSCode\Main-Log.log")
#     os.system("cls")
# boot()



# class LogLevel:
#     INFO = 1
#     DEBUG = 2
#     WARNING = 3
#     ERROR = 4
#     FATAL_ERROR = 5

# class Logger:
#     def __init__(self):
#         self.log_level = LogLevel.INFO

#     def set_log_level(self, log_level):
#         self.log_level = log_level

#     def log(self, log_level, message):
#         if log_level >= self.log_level:
#             color = self.get_color(log_level)
#             print(f"{color}[{log_level}] {message}\033[0m")

#     def get_color(self, log_level):
#         if log_level == LogLevel.DEBUG:
#             return "\033[92m"  # Green
#         elif log_level == LogLevel.WARNING:
#             return "\033[93m"  # Yellow
#         elif log_level == LogLevel.ERROR:
#             return "\033[91m"  # Red
#         elif log_level == LogLevel.FATAL_ERROR:
#             return "\033[31;2m"  # Dark Red
#         else:
#             return "\033[0m"  # White

# class Info:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.INFO, message)

# class Debug:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.DEBUG, message)

# class Warning:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.WARNING, message)

# class Error:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.ERROR, message)

# class FatalError:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.FATAL_ERROR, message)

# # Example usage
# logger = Logger()
# info = Info(logger)
# debug = Debug(logger)
# warning = Warning(logger)
# error = Error(logger)
# fatal_error = FatalError(logger)

# # Set the log level
# logger.set_log_level(LogLevel.INFO)

# # Thresholds for different log levels
# DEBUG_THRESHOLD = 50
# WARNING_THRESHOLD = 70
# ERROR_THRESHOLD = 90
# FATAL_ERROR_THRESHOLD = 100

# # Generate log messages in an infinite loop
# while True:
#     cpu_usage = psutil.cpu_percent()
#     log_level = None

#     if cpu_usage >= FATAL_ERROR_THRESHOLD:
#         log_level = fatal_error
#     elif cpu_usage >= ERROR_THRESHOLD:
#         log_level = error
#     elif cpu_usage >= WARNING_THRESHOLD:
#         log_level = warning
#     elif cpu_usage >= DEBUG_THRESHOLD:
#         log_level = debug
#     else:
#         log_level = info

#     message = f"CPU usage: {cpu_usage}%"
#     log_level.log(message)

#     if log_level != info:
#         with open("Main-Log.log", 'a') as f:
#             f.write(f"{log_level.__class__.__name__}: {message}\n")

#     delay = 1.0  # Delay of 1 second between logs
#     time.sleep(delay)

















































# import time
# import os
# import psutil

# os.system("cls")

# class LogLevel:
#     INFO = 1
#     DEBUG = 2
#     WARNING = 3
#     ERROR = 4
#     FATAL_ERROR = 5

# class Logger:
#     def __init__(self):
#         self.log_level = LogLevel.INFO

#     def set_log_level(self, log_level):
#         self.log_level = log_level

#     def log(self, log_level, message):
#         if log_level >= self.log_level:
#             color = self.get_color(log_level)
#             print(f"{color}[{log_level}] {message}\033[0m")

#     def get_color(self, log_level):
#         if log_level == LogLevel.DEBUG:
#             return "\033[92m"  # Green
#         elif log_level == LogLevel.WARNING:
#             return "\033[93m"  # Yellow
#         elif log_level == LogLevel.ERROR:
#             return "\033[91m"  # Red
#         elif log_level == LogLevel.FATAL_ERROR:
#             return "\033[31;2m"  # Dark Red
#         else:
#             return "\033[0m"  # White

# class Info:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.INFO, message)

# class Debug:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.DEBUG, message)

# class Warning:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.WARNING, message)

# class Error:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.ERROR, message)

# class FatalError:
#     def __init__(self, logger):
#         self.logger = logger

#     def log(self, message):
#         self.logger.log(LogLevel.FATAL_ERROR, message)

# # Example usage
# logger = Logger()
# info = Info(logger)
# debug = Debug(logger)
# warning = Warning(logger)
# error = Error(logger)
# fatal_error = FatalError(logger)

# # Set the log level
# logger.set_log_level(LogLevel.INFO)

# # Thresholds for different log levels
# DEBUG_THRESHOLD = 50
# WARNING_THRESHOLD = 70
# ERROR_THRESHOLD = 90
# FATAL_ERROR_THRESHOLD = 100

# # Generate log messages in an infinite loop
# while True:
#     cpu_usage = psutil.cpu_percent()
#     log_level = None

#     if cpu_usage >= FATAL_ERROR_THRESHOLD:
#         log_level = fatal_error
#     elif cpu_usage >= ERROR_THRESHOLD:
#         log_level = error
#     elif cpu_usage >= WARNING_THRESHOLD:
#         log_level = warning
#     elif cpu_usage >= DEBUG_THRESHOLD:
#         log_level = debug
#     else:
#         log_level = info

#     message = f"CPU usage: {cpu_usage}%"
#     log_level.log(message)

#     delay = 1.0  # Delay of 1 second between logs
#     time.sleep(delay)
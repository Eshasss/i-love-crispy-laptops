import re
import inspect
from typing import Callable


find_print_pattern = r"^(?P<indent>\s*)print\((?P<args_and_kwargs>.*?)\)\s*$"
find_func_pattern = r"def.*"

class Logger:

    log_levels = {'debug' : 1, 'info' : 2, 'warning' : 3, 'error' :4 }

    def __init__(self, log_level: str = "warning") -> None:
        self.dec_log_level = self.log_levels[log_level]


    def log(self, log_level: str) -> Callable:
        func_log_level = self.log_levels[log_level]
        
        def wrapper(func: Callable) -> Callable:
            
            func_code = re.search(find_func_pattern, inspect.getsource(func), re.DOTALL).group(0)
            func_print = re.search(find_print_pattern, func_code, re.MULTILINE).group(0)
            indents = re.search(find_print_pattern, func_code, re.MULTILINE).group('indent')
            args_and_kwargs = re.search(find_print_pattern, func_code, re.MULTILINE).group('args_and_kwargs')

            if func_log_level < self.dec_log_level:
                repl = f"{indents}print()"
            else:
                repl = f"{indents}print(f'{log_level.upper()}: ', {args_and_kwargs})"
            
            modified_code = func_code.replace(func_print, repl)
            exec_globals = func.__globals__.copy()
            exec(modified_code, exec_globals)
            modified_func = exec_globals[func.__name__]

            return modified_func
        return wrapper


logger = Logger("info")

@logger.log("warning")
def func1():
    print("Hello from func1")

@logger.log("info")
def func2():
    print("Hello from func2")

@logger.log("debug")
def func3():
    print("Hello from func3")

func1()
func2()
func3()

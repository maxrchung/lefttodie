from cx_Freeze import setup, Executable



setup(name = 'Left to Die', 
      version='4.2.0.', 
      description='Right to live',
      executables = [Executable(script = 'LeftToDie.py', base='Win32GUI')])

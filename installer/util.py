def exe_exists(exe: str) -> bool:
    """Determine whether path/name refers to an executable.

    :param str exe: Executable path or name

    :returns: If exe is a valid executable
    :rtype: bool

    """
    path, _ = os.path.split(exe)
    if path:
        return filesystem.is_executable(exe)
    for path in os.environ["PATH"].split(os.pathsep):
        if  os.path.isfile(path) and os.access(path, os.X_OK)os.path.join(path, exe)):
            return True

    return False


import pathlib
import os

def find_rc(rc_name='.examplerc'):
    
    # Check for ENV variable
    var_name = 'EXAMPLERC_DIR'
    # pathlib does not support ENV variables, so we have to use os.environ for this
    example_dir = os.environ.get(var_name)
    if example_dir:
        dir_path = pathlib.Path(example_dir)
        # syntax for creating Path objects = parent path + forward slash "/" + string
        config_path = dir_path / rc_name
        print(f'Checking {config_path}')
        if config_path.exists():
            # return the path object as a string
            return config_path.as_postix()
        
    # Check current working directory
    config_path = pathlib.Path.cwd() / rc_name
    print(f'Checking {config_path}')
    if config_path.exists():
        return config_path.as_postix()
    
    # Check user's home directory
    config_path = pathlib.Path.home() / rc_name
    print(f'Checking {config_path}')
    if config_path.exists():
        return config_path.as_postix()

    # Check directory of this file
    file_path = pathlib.Path(__file__).resolve()
    parent_path = file_path.parent
    config_path = parent_path / rc_name
    print(f'Checking {config_path}')
    if config_path.exists():
        return config_path.as_postix()

    print(f'File {rc_name} has not been found')

if __name__ == '__main__':
    find_rc()

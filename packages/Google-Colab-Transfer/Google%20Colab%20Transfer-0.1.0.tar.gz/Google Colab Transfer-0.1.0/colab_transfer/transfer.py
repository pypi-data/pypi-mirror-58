import glob
import os
import shutil
from pathlib import Path

from colab_transfer.utils import get_path_to_home_of_google_drive, get_path_to_home_of_local_machine


def copy_file(file_name,
              source=None,
              destination=None,
              verbose=True):
    if source is None:
        source = get_path_to_home_of_google_drive()

    if destination is None:
        destination = get_path_to_home_of_local_machine()
    else:
        Path(destination).mkdir(parents=True, exist_ok=True)

    input_file_name = source + file_name
    output_file_name = destination + file_name

    if Path(output_file_name).exists():
        if verbose:
            print('File {} already exists.'.format(output_file_name))
    else:
        if verbose:
            print('Copying {} to {}'.format(input_file_name,
                                            output_file_name))

        try:
            shutil.copyfile(input_file_name,
                            output_file_name)
        except FileNotFoundError:
            print('File {} could not be found.'.format(input_file_name))

    return


def copy_folder_structure(source,
                          destination,
                          verbose=True):
    files_and_folders = glob.glob(source + '*')

    root_files = glob.glob(source + '*.*')
    root_folders = set(files_and_folders).difference(root_files)

    if verbose:
        print('Files: {}'.format(root_files))
        print('Folders: {}'.format(root_folders))

    for f_name in root_files:
        file_name = os.path.basename(f_name)

        copy_file(file_name,
                  source=source,
                  destination=destination,
                  verbose=verbose)

    for f_name in root_folders:
        folder_name = os.path.basename(f_name) + '/'

        for file_name in glob.glob(f_name + '/*'):
            file_name = os.path.basename(file_name)

            copy_file(file_name,
                      source=source + folder_name,
                      destination=destination + folder_name,
                      verbose=verbose)

    return


def main():
    return True


if __name__ == '__main__':
    main()

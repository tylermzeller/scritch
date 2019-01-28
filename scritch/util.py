from os import listdir
from os.path import abspath, dirname, isfile, isdir, join
from re import sub

protocol_regex = r'^(https?:\/\/)'


def abs_path(filename):
    return dirname(abspath(filename))


def get_fs_names(path, test, set=False):
    if set: return { f for f in listdir(path) if test(join(path, f)) }
    return [f for f in listdir(path) if test(join(path, f))]


def get_filenames(path, **kwargs):
    return get_fs_names(path, isfile, **kwargs)


def get_dirnames(path, **kwargs):
    return get_fs_names(path, isdir, **kwargs)


def url_to_filename(url):
    return sub(r'\/', '_', sub(protocol_regex, '', url)).lower()

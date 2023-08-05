
__version__ = '0.1.0'

import tempfile
import os
import re

from subprocess import check_output, STDOUT
from shutil import which


def _exec(cmd, verbose = False):
    r'''
Execute command and return output.
    '''

    if verbose:
        print(cmd)

    output = check_output(cmd, shell = True, stderr = STDOUT).decode("utf-8")

    if verbose and len(output) > 0:
        print(output)

    return output


def _mkdir(dirname, verbose = False):
    r'''
Make directory if it does not yet exist.
    '''

    if os.path.isdir(dirname):
        return

    os.makedirs(dirname)

    if verbose:
        print('mkdir {0:s}'.format(dirname))


def _mv(orig, dest, verbose = False):
    r'''
Move file from "orig" to "dest".
    '''

    os.rename(orig, dest)

    if verbose:
        print('mv {0:s} {1:s}'.format(orig, dest))


def _check_get_abspath(filenames):
    r'''
Check if files exist, and return their path as absolute file-paths.
    '''

    if type(filenames) == str:
        filenames = [filenames]

    filenames = [os.path.abspath(f) for f in filenames]

    for filename in filenames:
        if not os.path.isfile(filename):
            raise IOError('"{0:s}" does not exist'.format(filename))

    return filenames


def _make_convert_tempdir(temp_dir = None, verbose = False):
    r'''
Make a temporary directory and returns its absolute file-path.
If not specified a directory-name is automatically generated.
    '''

    if temp_dir is None:
        temp_dir = tempfile.mkdtemp()
    else:
        temp_dir = os.path.abspath(temp_dir)

    _mkdir(temp_dir, verbose)

    return temp_dir


def _convert(filenames, options, append = None, temp_dir = None, verbose = False):
    r'''
Run convert on a batch of files.

Options:
- filenames: list of filenames (assumed to exist)
- options: the options for the convert command (string)
- append: if specified the "filenames" are not replaced, but appended (before the extension)
- temp_dir: temporary directory (assumed to exist)
- verbose: if true, all commands and output are printed to the screen
    '''

    if not which('convert'):
        raise IOError('"convert" not found, please install ImageMagick')

    for filename in filenames:

        temp_file = os.path.join(temp_dir, os.path.relpath(filename))

        _exec('convert {options:s} "{old:s}" "{new:s}"'.format(
            options = options,
            old = filename,
            new = temp_file),
            verbose = verbose)

        if append:
            base, ext = os.path.splitext(filename)
            dest = os.path.join(base, append, ext)
        else:
            dest = filename

        _mv(temp_file, dest, verbose)


def flatten(
        filenames,
        append = False,
        temp_dir = None,
        verbose = False):
    r'''
Flatten batch of images.

:arguments:

    **filenames** (``<list<str>>``)
        A list of filenames.

:options:

    **append** (``<str>``)
        If specified the original images are not overwritten. Rather the filename is
        appended with the string specified here. Note that this implies that there could be others
        files that are overwritten.

    **temp_dir** (``<str>``)
        If specified that directory is used as temporary directory. Otherwise, a directory is
        automatically selected.

    **verbose** ([``False``] | ``True``)
        If True, all commands are printed to the standard output.
    '''

    if not which('convert'):
        raise IOError('"convert" not found, please install ImageMagick')

    filenames = _check_get_abspath(filenames)
    temp_dir = _make_convert_tempdir(temp_dir, verbose)

    opt += ['-flatten']

    _convert(filenames, ' '.join(opt), append, verbose)


def set_background(
        filenames,
        background,
        flatten = False,
        append = False,
        temp_dir = None,
        verbose = False):
    r'''
Trim a batch of files.

:arguments:

    **filenames** (``<list<str>>``)
        A list of filenames.

    **background** (``<str>``)
        Apply a background colour (e.g. "none" or "white").

:options:

    **flatten** ([``False``] | ``True``)
        Flatten images: required for transparent PNG-files.

    **append** (``<str>``)
        If specified the original images are not overwritten. Rather the filename is
        appended with the string specified here. Note that this implies that there could be others
        files that are overwritten.

    **temp_dir** (``<str>``)
        If specified that directory is used as temporary directory. Otherwise, a directory is
        automatically selected.

    **verbose** ([``False``] | ``True``)
        If True, all commands are printed to the standard output.
    '''

    if not which('convert'):
        raise IOError('"convert" not found, please install ImageMagick')

    filenames = _check_get_abspath(filenames)
    temp_dir = _make_convert_tempdir(temp_dir, verbose)

    opt += ['-background {0:s}'.format(background)]

    if background != 'none':
        opt += ['-alpha remove']

    if flatten:
        opt += ['-flatten']

    _convert(filenames, ' '.join(opt), append, verbose)


def crop(
        filenames,
        background = 'none',
        flatten = False,
        append = False,
        temp_dir = None,
        verbose = False):
    r'''
Trim a batch of files.

:arguments:

    **filenames** (``<list<str>>``)
        A list of filenames.

:options:

    **background** ([``'none'``] | ``<str>``)
        Apply a background colour (e.g. "none" or "white").

    **flatten** ([``False``] | ``True``)
        Flatten images: required for transparent PNG-files.

    **append** (``<str>``)
        If specified the original images are not overwritten. Rather the filename is
        appended with the string specified here. Note that this implies that there could be others
        files that are overwritten.

    **temp_dir** (``<str>``)
        If specified that directory is used as temporary directory. Otherwise, a directory is
        automatically selected.

    **verbose** ([``False``] | ``True``)
        If True, all commands are printed to the standard output.
    '''

    if not which('convert'):
        raise IOError('"convert" not found, please install ImageMagick')

    filenames = _check_get_abspath(filenames)
    temp_dir = _make_convert_tempdir(temp_dir, verbose)

    # dry run to get trim size of each image

    split = lambda txt: \
        re.split(r'([0-9]*)(x)([0-9]*)(\ )([0-9]*)(x)([0-9]*)([\+][0-9]*)([\+][0-9]*)(.*)', txt)

    out = []

    for filename in filenames:
        out += [_exec('convert -trim -verbose  "{old:s}" "{new:s}"'.format(
            old = filename,
            new = os.path.join(temp_dir, 'tmp.png')),
            verbose = verbose)]

    out = [o.split('\n')[1] for o in out]

    # width of the original image
    w = [int(split(o)[1]) for o in out]

    # height of the original image
    h = [int(split(o)[3]) for o in out]

    # width of the trimmed image
    w0 = [int(split(o)[5]) for o in out]

    # height of the trimmed image
    h0 = [int(split(o)[7]) for o in out]

    # horizontal position at which the trimmed image starts
    x = [int(split(o)[8]) for o in out]

    # vertical position at which the trimmed image starts
    y = [int(split(o)[9]) for o in out]

    assert min(w0) == max(w0)
    assert min(h0) == max(h0)

    # select crop dimensions, add "convert" options to apply at the same time, and run "convert"

    dim = {
        'w': max(w) + (max(x) - min(x)),
        'h': max(h) + (max(y) - min(y)),
        'x': min(x),
        'y': min(y)}

    opt = ['-crop {w:d}x{h:d}{x:+d}{y:+d}'.format(**dim)]

    opt += ['-background {0:s}'.format(background)]

    if background != 'none':
        opt += ['-alpha remove']

    if flatten:
        opt += ['-flatten']

    _convert(filenames, ' '.join(opt), append, temp_dir, verbose)


[![Travis](https://travis-ci.org/tdegeus/batchcrop.svg?branch=master)](https://travis-ci.org/tdegeus/batchcrop)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/batchcrop.svg)](https://anaconda.org/conda-forge/batchcrop)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/python-batchcrop.svg)](https://anaconda.org/conda-forge/python-batchcrop)

# batchcrop

Crop a batch of images with the same margins.

# Contents

<!-- MarkdownTOC -->

- [Disclaimer](#disclaimer)
- [Getting batchcrop](#getting-batchcrop)
    - [Using conda](#using-conda)
    - [Using PyPi](#using-pypi)
    - [From source](#from-source)
- [Usage](#usage)

<!-- /MarkdownTOC -->

# Disclaimer

This library is free to use under the [MIT license](https://github.com/tdegeus/batchcrop/blob/master/LICENSE). Any additions are very much appreciated, in terms of suggested functionality, code, documentation, testimonials, word-of-mouth advertisement, etc. Bug reports or feature requests can be filed on [GitHub](https://github.com/tdegeus/batchcrop). As always, the code comes with no guarantee. None of the developers can be held responsible for possible mistakes.

Download: [.zip file](https://github.com/tdegeus/batchcrop/zipball/master) | [.tar.gz file](https://github.com/tdegeus/batchcrop/tarball/master).

(c - [MIT](https://github.com/tdegeus/batchcrop/blob/master/LICENSE)) T.W.J. de Geus (Tom) | tom@geus.me | www.geus.me | [github.com/tdegeus/batchcrop](https://github.com/tdegeus/batchcrop)

# Getting batchcrop

## Using conda

```bash
conda install -c conda-forge batchcrop
```

This will also install all necessary dependencies.

## Using PyPi

```bash
pip install batchcrop
```

This will also install the necessary Python modules, **but not GhostScript**.

## From source

```bash
# Download batchcrop
git checkout https://github.com/tdegeus/batchcrop.git
cd batchcrop

# Install
python -m pip install .
```

This will also install the necessary Python modules, **but not GhostScript**.

# Usage

The usage is as follows (see `batchcrop --help`):

```none
batchcrop
    Crop a batch of images with the same margins.

Usage:
    batchcrop [options] <image>...

Arguments:
    The images to crop.

Options:
    -a, --append=<str>
        Append filenames, if empty the input files are overwritten. [default: ]

    --background=<str>
        Apply a background color (e.g. "none" or "white").

    --flatten
        Flatten input images: required for transparent PNG-files.

    --temp-dir=<str>
        Output directory for temporary images (deleted if not specified).

    -v, --verbose
            Print all executed commands.

    -h, --help
        Show help.

    --version
        Show version.

(c-MIT) T.W.J. de Geus | tom@geus.me | www.geus.me | github.com/tdegeus
```

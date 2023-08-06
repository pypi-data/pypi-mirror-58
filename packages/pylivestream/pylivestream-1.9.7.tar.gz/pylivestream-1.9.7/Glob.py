#!/usr/bin/env python
"""
LIVE STREAM using FFMPEG -- Globbed input file list

NOTE: most video streaming sites REQUIRE you have to a video feed,
     so try the `-image` option with a favorite .JPG or other image.
"""
from pathlib import Path
from typing import List, Union
import pylivestream as pls
import random
import signal
from argparse import ArgumentParser
try:
    from tinytag import TinyTag
except ImportError:
    TinyTag = None


def playonce(flist: List[Path], image: Path, site: str, inifn: Path,
             shuffle: bool, usemeta: bool, yes: bool):

    if shuffle:
        random.shuffle(flist)

    caption: Union[str, None]

    for f in flist:
        if usemeta and TinyTag:
            try:
                caption = pls.meta_caption(TinyTag.get(str(f)))
                print(caption)
            except LookupError:
                caption = None
        else:
            caption = None

        s = pls.FileIn(inifn, site, infn=f, loop=False, image=image,
                       caption=caption, yes=yes)

        s.golive()


def fileglob(path: Union[str, Path], glob: str) -> List[Path]:
    path = Path(path).expanduser()

    if glob:
        if not path.is_dir():
            raise NotADirectoryError(path)
        flist = list(path.glob(glob))
    else:  # assume single file
        if not path.is_file():
            raise FileNotFoundError(path)
        flist = [path]

    if not flist:
        raise FileNotFoundError(f'did not find files with {path} {glob}')

    return flist


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    p = ArgumentParser(description="Livestream a globbed input file list")
    p.add_argument('path', help='path to discover files from')
    p.add_argument('websites', help='site to stream, e.g. localhost youtube periscope facebook twitch', nargs='+')
    p.add_argument('-glob', help='file glob pattern to stream.')
    p.add_argument('-i', '--ini', help='*.ini file with stream parameters')
    p.add_argument('-image',
                   help='static image to display, for audio-only files.')
    p.add_argument('-shuffle', help='shuffle the globbed file list',
                   action='store_true')
    p.add_argument('-loop', help='repeat the globbed file list endlessly', action='store_true')
    p.add_argument('-y', '--yes', help='no confirmation dialog', action='store_true')
    p.add_argument('-nometa', help='do not add metadata caption to video', action='store_false')
    p.add_argument('-t', '--timeout', help='stop streaming after --timeout seconds', type=int)
    P = p.parse_args()
# %% file / glob wranging
    flist = fileglob(P.path, P.glob)

    print('streaming these files. Be sure list is correct! \n')
    print('\n'.join(map(str, flist)))
    print()

    if P.yes:
        print('going live on', P.websites)
    else:
        input(f"Press Enter to go live on {P.websites}.    Or Ctrl C to abort.")

    usemeta = P.nometa

    if P.loop:
        while True:
            playonce(flist, P.image, P.websites, P.ini, P.shuffle, usemeta, P.yes)
    else:
        playonce(flist, P.image, P.websites, P.ini, P.shuffle, usemeta, P.yes)


if __name__ == '__main__':
    main()

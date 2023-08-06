#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

# @Time   : 2019/7/29 19:47
# @Author : Administrator
# @Software: PyCharm
# @License: BSD 3-Clause


"""
# Just a copy from xenonpy
for pictures use skimage.io.ImageCollection
"""

import glob
import re
from collections import defaultdict
from functools import partial
from pathlib import Path
from warnings import warn

import joblib
import pandas as pd
import requests
from skimage import io


class Call(object):
    """
    call file in paths
    """

    @staticmethod
    def extension(index_col=0):
        read_csv = partial(pd.read_csv, index_col=index_col)
        read_excel = partial(pd.read_excel, index_col=index_col)
        extension = dict(
            pkl_pd=('pkl_pd', pd.read_pickle),
            csv=('csv', read_csv),
            xlsx=('xlsx', read_excel),
            pkl_sk=('pkl_sk', joblib.load),
            png=("png", io.imread),
            jpg=("jpg", io.imread),
        )
        return extension

    __re__ = re.compile(r'[\s\-.]')

    def __init__(self, *paths, backend='pkl_pd', prefix_with_upper=None, index_col=0):
        """
        :param backend:default imported type to show
        :param prefix_with_upper: prefix_with_upper for all file add to file in this code to excape same name
        :type paths: None, ..|data_cluster, or F:data_cluster|data1
        """
        self._backend = backend
        self.index_col = index_col
        self._files = None
        self.__extension__ = self.extension(index_col)

        if len(paths) == 0:
            self._paths = ('.',)
        else:
            self._paths = paths

        if not prefix_with_upper:
            prefix_with_upper = ()
        self._prefix = prefix_with_upper

        self._make_index(prefix_with_upper=prefix_with_upper)

    def _make_index(self, *, prefix_with_upper):
        def make(path_):
            patten = self.__extension__[self._backend][0]
            files = glob.glob(str(path_ / ('*.' + patten)))

            def _nest(_f):
                f_ = _f
                return lambda s: s.__extension__[s._backend][1](f_)

            for f in files:
                # selection data_cluster
                f = Path(f).resolve()
                parent = re.split(r'[\\/]', str(f.parent))[-1]
                # parent = str(f.parent).split('\\/')[-1]
                fn = f.name[:-(1 + len(patten))]
                fn = self.__re__.sub('_', fn)
                if prefix_with_upper:
                    fn = '_'.join([parent, fn])

                if fn in self._files:
                    warn("file %s with x_name %s already bind to %s and will be ignored" %
                         (str(f), fn, self._files[fn]), RuntimeWarning)
                else:
                    self._files[fn] = str(f)
                    setattr(self.__class__, fn, property(_nest(str(f))))

        self._files = defaultdict(str)
        for path in self._paths:
            path = Path(path).expanduser().absolute()
            if not path.exists():
                raise RuntimeError('%s not exists' % str(path))
            make(path)

    @classmethod
    def from_http(cls, url, save_to, *, filename=None, chunk_size=256 * 1024, params=None,
                  **kwargs):
        """
        Get file object via a http request.

        Parameters
        ----------
        url: str
            The resource url.
        save_to: str
            The path of a dir to save the downloaded object into it.
        filename: str, optional
            Specific the file x_name when saving.
            Set to ``None`` (default) to use a inferred x_name from http header.
        chunk_size: int, optional
            Chunk size.
        params: any, optional
            Parameters will be passed to ``requests.get`` function.
            See Also: `requests <http://docs.python-requests.org/>`_
        kwargs: dict, optional
            Pass to ``requests.get`` function as the ``kwargs`` parameters.

        Returns
        -------
        str
            File path contains file x_name.
        """
        r = requests.get(url, params, **kwargs)
        r.raise_for_status()

        if not filename:
            if 'filename' in r.headers:
                filename = r.headers['filename']
            else:
                filename = url.split('/')[-1]

        if isinstance(save_to, str):
            save_to = Path(save_to)
        if not isinstance(save_to, Path) or not save_to.is_dir():
            raise RuntimeError('%s is not a legal path or not point to a dir' % save_to)

        file_ = str(save_to / filename)
        with open(file_, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

        return file_

    def __repr__(self):
        cont_ls = ['<{}> includes:'.format(self.__class__.__name__)]

        for k, v in self._files.items():
            cont_ls.append('"{}": {}'.format(k, v))

        return '\n'.join(cont_ls)

    def csv(self):
        return Call(*self._paths, backend='csv', prefix_with_upper=self._prefix, index_col=self.index_col)

    def pickle_pd(self):
        return Call(*self._paths, backend='pkl_pd', prefix_with_upper=self._prefix, index_col=self.index_col)

    def pickle_sk(self):
        return Call(*self._paths, backend='pkl_sk', prefix_with_upper=self._prefix, index_col=self.index_col)

    def xlsx(self):
        return Call(*self._paths, backend='xlsx', prefix_with_upper=self._prefix, index_col=self.index_col)

    def png(self):
        return Call(*self._paths, backend='png', prefix_with_upper=self._prefix, index_col=self.index_col)

    def jpg(self):
        return Call(*self._paths, backend='jpg', prefix_with_upper=self._prefix, index_col=self.index_col)

    def __call__(self, *args, **kwargs):
        return self.__extension__[self._backend][1](*args, **kwargs)

    def __getattr__(self, name):
        """
        Returns sub-dataset.

        Parameters
        ----------
        name: str
            Dataset x_name.

        Returns
        -------
        self
        """
        if name in self.__extension__:
            return self.__class__(*self._paths, backend=name, prefix=self._prefix)
        else:
            raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))

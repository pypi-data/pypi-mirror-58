# -*- coding: utf-8 -*-
# _zfp.pyx
# distutils: language = c
# cython: language_level = 3
# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True
# cython: nonecheck=False

# Copyright (c) 2019, Christoph Gohlke
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""ZFP codec for the imagecodecs package.

:Author:
  `Christoph Gohlke <https://www.lfd.uci.edu/~gohlke/>`_

:Organization:
  Laboratory for Fluorescence Dynamics. University of California, Irvine

:License: BSD 3-Clause

:Version: 2019.12.16

"""

__version__ = '2019.12.16'

include '_imagecodecs.pxi'

from libc.stdint cimport uint8_t


# ZFP #########################################################################

from zfp cimport *


class ZfpError(RuntimeError):
    """ZFP Exceptions."""


def zfp_encode(data, level=None, mode=None, execution=None, header=True,
               out=None):
    """Compress numpy array to ZFP stream.

    """
    cdef:
        numpy.ndarray src = data
        const uint8_t[::1] dst  # must be const to write to bytes
        size_t byteswritten
        ssize_t dstsize
        ssize_t srcsize = src.size * src.itemsize
        bitstream *stream = NULL
        zfp_stream *zfp = NULL
        zfp_field *field = NULL
        zfp_type ztype
        zfp_mode zmode
        zfp_exec_policy zexec
        uint ndim = data.ndim
        ssize_t itemsize = data.itemsize
        uint precision
        uint minbits, maxbits, maxprec, minexp
        uint nx, ny, nz, nw
        int sx, sy, sz, sw
        int ret
        double tolerance, rate
        int bheader = header

    if data is out:
        raise ValueError('cannot encode in-place')

    if data.dtype == numpy.int32:
        ztype = zfp_type_int32
    elif data.dtype == numpy.int64:
        ztype = zfp_type_int64
    elif data.dtype == numpy.float32:
        ztype = zfp_type_float
    elif data.dtype == numpy.float64:
        ztype = zfp_type_double
    else:
        raise ValueError('data type not supported by ZFP')

    if ndim == 1:
        nx = <uint>data.shape[0]
        sx = <int>(data.strides[0] // itemsize)
    elif ndim == 2:
        ny = <uint>data.shape[0]
        nx = <uint>data.shape[1]
        sy = <int>(data.strides[0] // itemsize)
        sx = <int>(data.strides[1] // itemsize)
    elif ndim == 3:
        nz = <uint>data.shape[0]
        ny = <uint>data.shape[1]
        nx = <uint>data.shape[2]
        sz = <int>(data.strides[0] // itemsize)
        sy = <int>(data.strides[1] // itemsize)
        sx = <int>(data.strides[2] // itemsize)
    elif ndim == 4:
        nw = <uint>data.shape[0]
        nz = <uint>data.shape[1]
        ny = <uint>data.shape[2]
        nx = <uint>data.shape[3]
        sw = <int>(data.strides[0] // itemsize)
        sz = <int>(data.strides[1] // itemsize)
        sy = <int>(data.strides[2] // itemsize)
        sx = <int>(data.strides[3] // itemsize)
    else:
        raise ValueError('data shape not supported by ZFP')

    if mode in (None, zfp_mode_null, zfp_mode_reversible, 'R', 'reversible'):
        zmode = zfp_mode_reversible
    elif mode in (zfp_mode_fixed_precision, 'p', 'precision'):
        zmode = zfp_mode_fixed_precision
        precision = _default_value(level, ZFP_MAX_PREC, 0, ZFP_MAX_PREC)
    elif mode in (zfp_mode_fixed_rate, 'r', 'rate'):
        zmode = zfp_mode_fixed_rate
        rate = level
    elif mode in (zfp_mode_fixed_accuracy, 'a', 'accuracy'):
        zmode = zfp_mode_fixed_accuracy
        tolerance = level
    elif mode in (zfp_mode_expert, 'c', 'expert'):
        zmode = zfp_mode_expert
        minbits, maxbits, maxprec, minexp = level
    else:
        raise ValueError('invalid ZFP mode')

    if execution is None or execution == 'serial':
        zexec = zfp_exec_serial
    elif execution == 'omp':
        zexec = zfp_exec_omp
    elif execution == 'cuda':
        zexec = zfp_exec_cuda
    else:
        raise ValueError('invalid ZFP execution policy')

    try:
        zfp = zfp_stream_open(NULL)
        if zfp == NULL:
            raise ZfpError('zfp_stream_open failed')

        if ndim == 1:
            field = zfp_field_1d(<void*>src.data, ztype, nx)
            if field == NULL:
                raise ZfpError('zfp_field_1d failed')
            zfp_field_set_stride_1d(field, sx)
        elif ndim == 2:
            field = zfp_field_2d(<void*>src.data, ztype, nx, ny)
            if field == NULL:
                raise ZfpError('zfp_field_2d failed')
            zfp_field_set_stride_2d(field, sx, sy)
        elif ndim == 3:
            field = zfp_field_3d(<void*>src.data, ztype, nx, ny, nz)
            if field == NULL:
                raise ZfpError('zfp_field_3d failed')
            zfp_field_set_stride_3d(field, sx, sy, sz)
        elif ndim == 4:
            field = zfp_field_4d(<void*>src.data, ztype, nx, ny, nz, nw)
            if field == NULL:
                raise ZfpError('zfp_field_4d failed')
            zfp_field_set_stride_4d(field, sx, sy, sz, sw)

        if zmode == zfp_mode_reversible:
            zfp_stream_set_reversible(zfp)
        elif zmode == zfp_mode_fixed_precision:
            precision = zfp_stream_set_precision(zfp, precision)
        elif zmode == zfp_mode_fixed_rate:
            rate = zfp_stream_set_rate(zfp, rate, ztype, ndim, 0)
        elif zmode == zfp_mode_fixed_accuracy:
            tolerance = zfp_stream_set_accuracy(zfp, tolerance)
        elif zmode == zfp_mode_expert:
            ret = zfp_stream_set_params(zfp, minbits, maxbits, maxprec, minexp)
            if ret == 0:
                raise ZfpError('zfp_stream_set_params failed')

        out, dstsize, outgiven, outtype = _parse_output(out)
        if out is None:
            if dstsize < 0:
                dstsize = zfp_stream_maximum_size(zfp, field)
            out = _create_output(outtype, dstsize)

        dst = out
        dstsize = dst.size * dst.itemsize

        with nogil:
            stream = stream_open(<void*>&dst[0], dstsize)
            if stream == NULL:
                raise ZfpError('stream_open failed')

            zfp_stream_set_bit_stream(zfp, stream)
            zfp_stream_rewind(zfp)

            ret = zfp_stream_set_execution(zfp, zexec)
            if ret == 0:
                raise ZfpError('zfp_stream_set_execution failed')

            if bheader != 0:
                byteswritten = zfp_write_header(zfp, field, ZFP_HEADER_FULL)
                if byteswritten == 0:
                    raise ZfpError('zfp_write_header failed')

            byteswritten = zfp_compress(zfp, field)
            if byteswritten == 0:
                raise ZfpError('zfp_compress failed')

    finally:
        if field != NULL:
            zfp_field_free(field)
        if zfp != NULL:
            zfp_stream_close(zfp)
        if stream != NULL:
            stream_close(stream)

    del dst
    return _return_output(out, dstsize, byteswritten, outgiven)


def zfp_decode(data, shape=None, dtype=None, out=None):
    """Decompress ZFP stream to numpy array.

    """
    cdef:
        numpy.ndarray dst
        const uint8_t[::1] src = data
        ssize_t srcsize = src.size
        zfp_stream *zfp = NULL
        bitstream *stream = NULL
        zfp_field *field = NULL
        zfp_type ztype
        ssize_t ndim
        size_t size
        uint nx, ny, nz, nw
        int ret

    if data is out:
        raise ValueError('cannot decode in-place')

    if dtype is None:
        ztype = zfp_type_none
    elif dtype == numpy.int32:
        ztype = zfp_type_int32
    elif dtype == numpy.int64:
        ztype = zfp_type_int64
    elif dtype == numpy.float32:
        ztype = zfp_type_float
    elif dtype == numpy.float64:
        ztype = zfp_type_double
    else:
        raise ValueError('dtype not supported by ZFP')

    ndim = -1 if shape is None else len(shape)
    if ndim == -1:
        pass
    elif ndim == 1:
        nx = <uint>shape[0]
    elif ndim == 2:
        nx = <uint>shape[1]
        ny = <uint>shape[0]
    elif ndim == 3:
        nx = <uint>shape[2]
        ny = <uint>shape[1]
        nz = <uint>shape[0]
    elif ndim == 4:
        nx = <uint>shape[3]
        ny = <uint>shape[2]
        nz = <uint>shape[1]
        nw = <uint>shape[0]
    else:
        raise ValueError('shape not supported by ZFP')

    # TODO: enable execution mode when supported
    # zfp_exec_policy zexec
    # if execution is None or execution == 'serial':
    #     zexec = zfp_exec_serial
    # elif execution == 'omp':
    #     zexec = zfp_exec_omp
    # elif execution == 'cuda':
    #     zexec = zfp_exec_cuda
    # else:
    #    raise ValueError('invalid ZFP execution policy')

    try:
        zfp = zfp_stream_open(NULL)
        if zfp == NULL:
            raise ZfpError('zfp_stream_open failed')

        field = zfp_field_alloc()
        if field == NULL:
            raise ZfpError('zfp_field_alloc failed')

        stream = stream_open(<void*>&src[0], srcsize)
        if stream == NULL:
            raise ZfpError('stream_open failed')

        zfp_stream_set_bit_stream(zfp, stream)
        zfp_stream_rewind(zfp)

        # ret = zfp_stream_set_execution(zfp, zexec)
        # if ret == 0:
        #     raise ZfpError('zfp_stream_set_execution failed')

        if ztype == zfp_type_none or ndim == -1:
            size = zfp_read_header(zfp, field, ZFP_HEADER_FULL)
            if size == 0:
                raise ZfpError('zfp_read_header failed')

        if ztype == zfp_type_none:
            ztype = field.dtype
            if ztype == zfp_type_float:
                dtype = numpy.float32
            elif ztype == zfp_type_double:
                dtype = numpy.float64
            elif ztype == zfp_type_int32:
                dtype = numpy.int32
            elif ztype == zfp_type_int64:
                dtype = numpy.int64
            else:
                raise ZfpError('invalid zfp_field type')
        else:
            ztype = zfp_field_set_type(field, ztype)
            if ztype == zfp_type_none:
                raise ZfpError('zfp_field_set_type failed')

        if ndim == -1:
            if field.nx == 0:
                raise ZfpError('invalid zfp_field nx')
            elif field.ny == 0:
                shape = field.nx,
            elif field.nz == 0:
                shape = field.ny, field.nx
            elif field.nw == 0:
                shape = field.nz, field.ny, field.nx
            else:
                shape = field.nw, field.nz, field.ny, field.nx
        elif ndim == 1:
            zfp_field_set_size_1d(field, nx)
        elif ndim == 2:
            zfp_field_set_size_2d(field, nx, ny)
        elif ndim == 3:
            zfp_field_set_size_3d(field, nx, ny, nz)
        elif ndim == 4:
            zfp_field_set_size_4d(field, nx, ny, nz, nw)

        out = _create_array(out, shape, dtype)
        dst = out

        with nogil:
            zfp_field_set_pointer(field, <void*>dst.data)
            size = zfp_decompress(zfp, field)

        if size == 0:
            raise ZfpError('zfp_decompress failed')

    finally:
        if field != NULL:
            zfp_field_free(field)
        if zfp != NULL:
            zfp_stream_close(zfp)
        if stream != NULL:
            stream_close(stream)

    return out


def zfp_version():
    """Return ZFP version string."""
    return 'zfp ' + ZFP_VERSION_STRING.decode('utf-8')

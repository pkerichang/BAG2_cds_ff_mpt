# -*- coding: utf-8 -*-
########################################################################################################################
#
# Copyright (c) 2014, Regents of the University of California
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
#   disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#    following disclaimer in the documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
########################################################################################################################


from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
# noinspection PyUnresolvedReferences,PyCompatibility
from builtins import *

import math
from typing import List, Tuple

from bag.layout import TechInfo
from bag.layout.template import TemplateBase


from .mos.base import MOSTechCDSFFMPT


class TechInfoCDSFFMPT(TechInfo):
    def __init__(self, process_params):
        process_params['layout']['mos_tech_class'] = MOSTechCDSFFMPT
        process_params['layout']['laygo_tech_class'] = None
        process_params['layout']['res_tech_class'] = None

        TechInfo.__init__(self, 0.001, 1e-6, 'cds_ff_mpt', process_params)
        self.idc_temp = process_params['layout']['em']['dc_temp']
        self.irms_dt = process_params['layout']['em']['rms_dt']

    @classmethod
    def get_implant_layers(cls, mos_type, res_type=None):
        if mos_type == 'nch':
            return []
        elif mos_type == 'ptap':
            return []
        elif mos_type == 'pch':
            return [('NW', 'drawing')]
        else:
            return [('NW', 'drawing')]

    @classmethod
    def add_cell_boundary(cls, template, box):
        pass

    @classmethod
    def draw_device_blockage(cls, template):
        # type: (TemplateBase) -> None
        pass

    @classmethod
    def get_idc_scale_factor(cls, temp, mtype, is_res=False):
        if is_res:
            return 1.0
        else:
            if mtype == 't':
                return 1.0
            else:
                return 1.0

    @classmethod
    def get_metal_idc_factor(cls, mtype, w, l):
        return 1

    @classmethod
    def get_via_drc_info(cls, vname, vtype, mtype, mw_unit, is_bot):
        # NOTE: we force space to be even in resolution units, because
        # openaccess is bad with odd spacing.
        arr_enc = None
        arr_test = None
        sp3 = None
        if vname == '1x' or vname == '4':
            if vtype == 'square':
                sp = [42, 42]
                dim = [32, 32]
                mw_enc = [(35, [(40, 0), (0, 40)]),
                          (51, [(2, 34), (34, 2)]),
                          (67, [(28, 10), (10, 28)]),
                          (float('inf'), [(18, 18)]),
                          ]
            elif vtype == 'hrect' or vtype == 'vrect':
                sp = [42, 42]
                dim = [64, 32]
                mw_enc = [(49, [(20, 0)]),
                          (51, [(12, 9)]),
                          (105, [(10, 10)]),
                          (float('inf'), [(10, 0)]),
                          ]
            else:
                raise ValueError('Unsupported vtype %s' % vtype)
        elif vname == '2x':
            if vtype != 'square':
                raise ValueError('Unsupported vtype %s' % vtype)

            sp3 = [78, 78]
            sp = [62, 62]
            dim = [42, 42]
            mw_enc = [(float('inf'), [(8, 8)])]
        else:
            raise ValueError('Unsupported vname %s' % vname)

        enc = None  # type: List[Tuple[int, int]]
        for mw_max, enc_list in mw_enc:
            if mw_unit <= mw_max:
                enc = enc_list
                break

        arr_test2 = arr_test
        if vtype == 'vrect':
            # flip X and Y direction parameters
            sp = [sp[1], sp[0]]
            dim = [dim[1], dim[0]]
            enc = [(yv, xv) for xv, yv in enc]
            if arr_enc is not None:
                # noinspection PyTypeChecker
                arr_enc = [(yv, xv) for xv, yv in arr_enc]
            if arr_test is not None:
                def arr_test2(nrow, ncol):
                    # noinspection PyCallingNonCallable
                    return arr_test(ncol, nrow)
            if sp3 is not None:
                sp3 = [sp3[1], sp3[0]]

        return sp, sp3, dim, enc, arr_enc, arr_test2
    
    def get_min_space(self, layer_type, width, unit_mode=False, same_color=False):
        if layer_type == '1x':
            if same_color:
                w_list = [1499, 749, 99]
                sp_list = [220, 112, 72]
                sp_default = 48
            else:
                w_list = sp_list = []
                sp_default = 32
        elif layer_type == '4':
            w_list = [1499, 749, 99]
            sp_list = [220, 112, 72]
            sp_default = 48
        elif layer_type == '2x':
            w_list = [89, 59]
            sp_list = [100, 80]
            sp_default = 68
        else:
            raise ValueError('Unsupported layer type: %s' % layer_type)

        if not unit_mode:
            width = int(round(width / self.resolution))

        ans = sp_default
        for w, sp in zip(w_list, sp_list):
            if width > w:
                ans = sp
                break

        if unit_mode:
            return ans
        else:
            return ans * self.resolution

    def get_min_line_end_space(self, layer_type, width, unit_mode=False):
        if layer_type == '1x':
            w_list = sp_list = []
            sp_default = 64
        elif layer_type == '4':
            w_list = sp_list = []
            sp_default = 64
        elif layer_type == '2x':
            w_list = sp_list = []
            sp_default = 74
        else:
            raise ValueError('Unsupported layer type: %s' % layer_type)

        if not unit_mode:
            width = int(round(width / self.resolution))

        ans = sp_default
        for w, sp in zip(w_list, sp_list):
            if width > w:
                ans = sp

        if unit_mode:
            return ans
        else:
            return ans * self.resolution

    def get_min_length(self, layer_type, width):
        res = self.resolution
        if layer_type == '1x' or layer_type == '4':
            return math.ceil(0.006176 / width / res) * res
        elif layer_type == '2x':
            return math.ceil(0.0082 / width / res) * res
        else:
            raise ValueError('Unsupported layer type: %s' % layer_type)

    def get_layer_id(self, layer_name):
        if layer_name == 'LiPo' or layer_name == 'LiAct':
            return 0
        return int(layer_name[1:])

    def get_layer_name(self, layer):
        if layer == 0:
            raise ValueError('Ambiguous layer name for layer ID = 0')
        return 'M%d' % layer

    def get_layer_type(self, layer_name):
        if layer_name == 'LiPo' or layer_name == 'LiAct':
            return layer_name
        layer_id = self.get_layer_id(layer_name)
        if 1 <= layer_id <= 3:
            return '1x'
        elif layer_id == 4:
            return '4'
        elif 5 <= layer_id <= 6:
            return '2x'
        else:
            raise ValueError('Unsupported layer ID: %d' % layer_id)

    def get_via_name(self, bot_layer_id):
        top_layer_name = self.get_layer_name(bot_layer_id + 1)
        return self.get_layer_type(top_layer_name)

    def _get_metal_idc(self, metal_type, w, l, vertical, **kwargs):
        if vertical:
            raise NotImplementedError('Vertical DC current not supported yet')

        inorm, woff = 1.0, 0.0
        idc = inorm * self.get_metal_idc_factor(metal_type, w, l) * (w - woff)
        idc_temp = kwargs.get('dc_temp', self.idc_temp)
        return self.get_idc_scale_factor(idc_temp, metal_type) * idc * 1e-3

    def _get_metal_irms(self, layer_name, w, **kwargs):
        b = 0.0443
        k, wo, a = 6.0, 0.0, 0.2

        irms_dt = kwargs.get('rms_dt', self.irms_dt)
        irms_ma = (k * irms_dt * (w - wo)**2 * (w - wo + a) / (w - wo + b))**0.5
        return irms_ma * 1e-3

    def get_metal_em_specs(self, layer_name, w, l=-1, vertical=False, **kwargs):
        metal_type = self.get_layer_type(layer_name)
        idc = self._get_metal_idc(metal_type, w, l, vertical, **kwargs)
        irms = self._get_metal_irms(layer_name, w, **kwargs)
        ipeak = float('inf')
        return idc, irms, ipeak

    def _get_via_idc(self, vname, via_type, bm_type, tm_type,
                     bm_dim, tm_dim, array, **kwargs):
        if bm_dim[0] > 0:
            bf = self.get_metal_idc_factor(bm_type, bm_dim[0], bm_dim[1])
        else:
            bf = 1.0

        if tm_dim[0] > 0:
            tf = self.get_metal_idc_factor(tm_type, tm_dim[0], tm_dim[1])
        else:
            tf = 1.0

        factor = min(bf, tf)
        if vname == '1x' or vname == '4':
            if via_type == 'square':
                idc = 0.1 * factor
            elif via_type == 'hrect' or via_type == 'vrect':
                idc = 0.2 * factor
            else:
                # we do not support 2X square via, as it has large
                # spacing rule to square/rectangle vias.
                raise ValueError('Unsupported via type %s' % via_type)
        elif vname == '2x':
            if via_type == 'square':
                idc = 0.4 * factor
            else:
                raise ValueError('Unsupported via type %s' % via_type)
        else:
            raise ValueError('Unsupported via name %s and bm_type %s' % (vname, bm_type))

        idc_temp = kwargs.get('dc_temp', self.idc_temp)
        return self.get_idc_scale_factor(idc_temp, bm_type) * idc * 1e-3

    def get_via_em_specs(self, via_name, bm_layer, tm_layer, via_type='square',
                         bm_dim=(-1, -1), tm_dim=(-1, -1), array=False, **kwargs):
        bm_type = self.get_layer_type(bm_layer)
        tm_type = self.get_layer_type(tm_layer)
        idc = self._get_via_idc(via_name, via_type, bm_type, tm_type, bm_dim,
                                tm_dim, array, **kwargs)
        # via do not have AC current specs
        irms = float('inf')
        ipeak = float('inf')
        return idc, irms, ipeak

    def get_res_rsquare(self, res_type):
        return 500

    def get_res_width_bounds(self, res_type):
        return 0.5, 5.0

    def get_res_length_bounds(self, res_type):
        return 0.5, 50.0

    def get_res_min_nsquare(self, res_type):
        return 1.0

    def get_res_em_specs(self, res_type, w, l=-1, **kwargs):
        idc_temp = kwargs.get('dc_temp', self.idc_temp)
        idc_scale = self.get_idc_scale_factor(idc_temp, '', is_res=True)
        idc = 1.0e-3 * w * idc_scale

        irms_dt = kwargs.get('rms_dt', self.irms_dt)
        irms = 1e-3 * (0.02 * irms_dt * w * (w + 0.5)) ** 0.5

        ipeak = 5e-3 * 2 * w
        return idc, irms, ipeak

    def get_res_info(self, res_type, w, l, **kwargs):
        # only one type of resistor
        rsq = self.get_res_rsquare(res_type)
        res = l / w * rsq
        idc, irms, ipeak = self.get_res_em_specs(res_type, w, l=l, **kwargs)

        return dict(
            resistance=res,
            idc=idc,
            iac_rms=irms,
            iac_peak=ipeak,
        )

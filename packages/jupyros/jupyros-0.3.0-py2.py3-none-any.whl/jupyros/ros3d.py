#############################################################################
# Copyright (c) Wolf Vollprecht, QuantStack                                 #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################

import os

import ipywidgets as widgets
from traitlets import *

try:
    from _version import version_info
except:
    from ._version import version_info

js_version = '^' + '.'.join([str(x) for x in version_info[:3]])


def _quick_widget(package_name, version, has_view=True):
    def quick_widget_decorator(cls):
        from traitlets import Unicode
        name = cls.__name__
        if name.endswith('Model'):
            name = name[:-5]

        cls._model_name = Unicode(name + 'Model').tag(sync=True)
        cls._model_name.class_init(cls, '_model_name')

        cls._model_module = Unicode(package_name).tag(sync=True)
        cls._model_module.class_init(cls, '_model_module')

        cls._model_module_version = Unicode(version).tag(sync=True)
        cls._model_module_version.class_init(cls, '_model_module_version')

        if has_view:
            cls._view_module = Unicode(package_name).tag(sync=True)
            cls._view_module.class_init(cls, '_view_module')

            cls._view_module_version = Unicode(version).tag(sync=True)
            cls._view_module_version.class_init(cls, '_view_module_version')

            cls._view_name = Unicode(name + 'View').tag(sync=True)
            cls._view_name.class_init(cls, '_view_name')

        cls = widgets.register(cls)
        return cls

    return quick_widget_decorator


register = _quick_widget('jupyter-ros', js_version)
register_noview = _quick_widget('jupyter-ros', js_version, False)
sync_widget = {'sync': True}
sync_widget.update(widgets.widget_serialization)

@register_noview
class ROSConnection(widgets.Widget):
    url = Unicode(os.environ.get("JUPYROS_WEBSOCKET_URL", "ws://{hostname}:9090")).tag(sync=True)

@register_noview
class TFClient(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    angular_treshold = Float(0.01).tag(sync=True)
    translational_treshold = Float(0.01).tag(sync=True)
    rate = Float(10.0).tag(sync=True)
    fixed_frame = Unicode('').tag(sync=True)

@register
class URDFModel(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    url = Unicode(
        os.environ.get("JUPYROS_ASSETS_URL", "http://{hostname}:3000")
    ).tag(sync=True)

@register
class GridModel(widgets.Widget):
    cell_size = Float(0.5).tag(sync=True)
    color = Unicode("#0181c4").tag(sync=True)
    num_cells = Int(20).tag(sync=True)

@register
class OccupancyGrid(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode("/map").tag(sync=True)
    continuous = Bool(False).tag(sync=True)
    compression = Unicode('cbor').tag(sync=True)
    color = Unicode('#FFFFFF').tag(sync=True)
    opacity = Float(1.0).tag(sync=True)
    # rootObject =
    # offsetPose =

@register
class InteractiveMarker(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode('/basic_controls').tag(sync=True)
    menu_font_size = Unicode('0.8em').tag(sync=True)
    # camera =
    # rootObject

@register
class Marker(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode('/visualization_marker').tag(sync=True)
    path = Unicode('/').tag(sync=True)
    lifetime = Float(0.0).tag(sync=True)

@register
class PoseArray(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode('/particle_cloud').tag(sync=True)
    color = Unicode('#CC00FF').tag(sync=True)
    length = Float(1.0).tag(sync=True)

@register
class Pose(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode('/particle_cloud').tag(sync=True)
    color = Unicode('#CC00FF').tag(sync=True)
    length = Float(1.0).tag(sync=True)

@register
class Polygon(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode('/path').tag(sync=True)
    color = Unicode('#CC00FF').tag(sync=True)

@register
class Path(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode('/path').tag(sync=True)
    color = Unicode('#CC00FF').tag(sync=True)

@register
class LaserScan(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode('/path').tag(sync=True)
    point_ratio = Float(1.0).tag(sync=True)
    message_ratio = Float(1.0).tag(sync=True)
    max_points = Int(200000).tag(sync=True)
    color_source = Unicode('intensities').tag(sync=True)
    color_map = Unicode('').tag(sync=True)
    point_size = Float(0.05).tag(sync=True)
    static_color = Unicode("#FF0000").tag(sync=True)

@register
class MarkerArrayClient(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode('/basic_controls').tag(sync=True)
    path = Unicode('/').tag(sync=True)

@register
class PointCloud(widgets.Widget):
    ros = Instance(ROSConnection).tag(**sync_widget)
    tf_client = Instance(TFClient).tag(**sync_widget)
    topic = Unicode('').tag(sync=True)
    message_ratio = Float(2.0).tag(sync=True)
    point_ratio = Float(3.0).tag(sync=True)
    max_points = Int(200000).tag(sync=True)
    point_size = Float(0.05).tag(sync=True)
    static_color = Unicode("#FF0000").tag(sync=True)
    # color_map = Unicode('').tag(sync=True)
    # color_source = Unicode('').tag(sync=True)

@register
class Viewer(widgets.DOMWidget):
    background_color = Unicode('#FFFFFF').tag(sync=True)
    alpha = Bool(True).tag(sync=True)
    height = Unicode('100%').tag(sync=True)
    objects = List(Instance(widgets.Widget)).tag(**sync_widget)

@register_noview
class DepthCloud(widgets.Widget):
    url = Unicode('').tag(sync=True)
    f = Float(525.0).tag(sync=True)

@register
class SceneNode(widgets.Widget):
    frame_id = Unicode('/base_link').tag(sync=True)
    tf_client = Instance(TFClient).tag(**sync_widget)
    object = Instance(DepthCloud).tag(**sync_widget)

def js_formatter(d_in):
    import json
    from traitlets import utils as tut
    def remove_undefined(d):
        for key in d:
            if type(d[key]) is tut.sentinel.Sentinel:
                d[key] = '##UNDEFINED##'
            if type(d[key]) is dict:
                remove_undefined(d[key])

    remove_undefined(d_in)
    s = '{\n'
    for key in sorted(d_in.keys()):
        val = d_in[key] if d_in[key] is not None else "null"
        if type(val) is str:
            val = '"' + val + '"'
        if type(val) is bool:
            val = 'true' if val else 'false'

        s += '    {}: {},\n'.format(key, val)
    # s = json.dumps(d_in, indent=4)
    s += '}\n'
    s = s.replace('"##UNDEFINED##"', 'null')
    return s


def js_extract_cls(cls):

    template = """
var {class_name}Defaults = {json_defaults}
    """

    name = cls.__name__
    if not name.endswith('Model'):
        name += 'Model'

    defd = cls.__base__.class_trait_names()
    base_class_name = cls.__base__.__name__
    defaults = {}
    # trait_values = cls()._trait_values
    trait_values = cls.__dict__
    forward_traits = ['_model_module', '_model_name', '_model_module_version', '_view_name', '_view_module', '_view_module_version']
    for key, item in trait_values.items():
        if key not in defd or key in forward_traits:
            if not item is traitlets.Instance:
                if issubclass(item.__class__, traitlets.TraitType):
                    defaults[key] = item.default_value
            else:
                defaults[key] = traitlets.Undefined

    jd = js_formatter(defaults)
    jd = '\n'.join([" " * 4 + l for l in jd.split('\n')])

    return (name, template.format(class_name=name,
                          base_class=base_class_name,
                          json_defaults=jd))

def js_extract():
    import sys, inspect, json
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    # print(clsmembers)
    def modulify(d, suffix=''):
        js = {key + suffix: key + suffix for key in d}
        s = "{\n"
        for key in sorted(d.keys()):
            s += "    {key}: {key},\n".format(key=key + suffix)
        return s + '}\n'

    for_export = {}
    for cls_name, cls in clsmembers:
        if cls.__module__ == __name__:
            cls_name, text = js_extract_cls(cls)
            for_export[cls_name] = text

    for key in for_export:
        print(for_export[key])

    export_template = """
module.exports = {exports_json}
    """
    print(export_template.format(exports_json=modulify(for_export, 'Defaults')))

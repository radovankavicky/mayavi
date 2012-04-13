# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class TreeMapToPolyData(PolyDataAlgorithm):
    """
    TreeMapToPolyData - converts a tree to a polygonal data
    representing a tree map
    
    Superclass: PolyDataAlgorithm
    
    This algorithm requires that the TreeMapLayout filter has already
    applied to the data in order to create the quadruple array (min x,
    max x, min y, max y) of bounds for each vertex of the tree.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeMapToPolyData, obj, update, **traits)
    
    level_delta_z = traits.Float(0.001, enter_set=True, auto_set=False, help=\
        """
        The spacing along the z-axis between tree map levels.
        """
    )
    def _level_delta_z_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevelDeltaZ,
                        self.level_delta_z)

    add_normals = traits.Bool(True, help=\
        """
        The spacing along the z-axis between tree map levels.
        """
    )
    def _add_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAddNormals,
                        self.add_normals)

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    def set_level_array_name(self, *args):
        """
        V.set_level_array_name(string)
        C++: virtual void SetLevelArrayName(const char *name)
        The field containing the level of each tree node. This can be
        added using TreeLevelsFilter before this filter. If this is
        not present, the filter simply calls tree->_get_level(v) for each
        vertex, which will produce the same result, but may not be as
        efficient.
        """
        ret = self._wrap_call(self._vtk_obj.SetLevelArrayName, *args)
        return ret

    def set_rectangles_array_name(self, *args):
        """
        V.set_rectangles_array_name(string)
        C++: virtual void SetRectanglesArrayName(const char *name)
        The field containing quadruples of the form (min x, max x, min y,
        max y) representing the bounds of the rectangles for each vertex.
        This array may be added to the tree using TreeMapLayout.
        """
        ret = self._wrap_call(self._vtk_obj.SetRectanglesArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('level_delta_z', 'GetLevelDeltaZ'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('add_normals', 'GetAddNormals'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'add_normals', 'level_delta_z', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeMapToPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeMapToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['add_normals', 'level_delta_z']),
            title='Edit TreeMapToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeMapToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

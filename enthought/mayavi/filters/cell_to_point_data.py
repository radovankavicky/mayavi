# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.filters.filter_base import FilterBase


######################################################################
# `CellToPointData` class.
######################################################################
class CellToPointData(FilterBase):

    """Transforms cell attribute data to point data by averaging the
    cell data from the cells at the point.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.CellDataToPointData, args=(), allow_none=False)

    def update_pipeline(self):
        # Do nothing if there is no input.
        inputs = self.inputs
        if len(inputs) == 0:
            return

        fil = self.filter
        input = inputs[0].outputs[0]
        fil.input = input
        fil.update()
        # This filter creates different outputs depending on the
        # input.
        out_map = {'vtkStructuredGrid': 'structured_grid_output',
                   'vtkRectilinearGrid': 'rectilinear_grid_output',
                   'vtkStructuredPoints': 'structured_points_output',
                   'vtkUnstructuredGrid': 'unstructured_grid_output',
                   'vtkPolyData': 'poly_data_output',
                   'vtkImageData': 'image_data_output'}
        # Find the input data type and pass that to our output..
        for type in out_map:
            if input.is_a(type):
                self._set_outputs([getattr(fil, out_map[type])])
                break


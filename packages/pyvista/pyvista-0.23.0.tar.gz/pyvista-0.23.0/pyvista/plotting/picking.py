"""Module managing picking events."""

import logging
import numpy as np
import vtk

import pyvista
from pyvista.utilities import try_callback

class PickingHelper(object):
    """An internal class to hold picking related features."""

    picked_cells = None
    picked_point = None
    picked_path = None
    picked_geodesic = None
    picked_horizon = None

    def get_pick_position(self):
        """Get the pick position/area as x0, y0, x1, y1."""
        return self.renderer.get_pick_position()


    def enable_cell_picking(self, mesh=None, callback=None, through=True,
                            show=True, show_message=True, style='wireframe',
                            line_width=5, color='pink', font_size=18,
                            start=False, **kwargs):
        """Enable picking at cells.

        Press "r" to enable retangle based selection.  Press "r" again to
        turn it off. Selection will be saved to ``self.picked_cells``. Also
        press "p" to pick a single cell under the mouse location.

        Uses last input mesh for input by default.

        Warning
        -------
        Visible cell picking (``through=False``) is known to not perform well
        and produce incorrect selections on non-triangulated meshes if using
        any grpahics card other than NVIDIA. A warning will be thrown if the
        mesh is not purely triangles when using visible cell selection.

        Parameters
        ----------
        mesh : pyvista.Common, optional
            UnstructuredGrid grid to select cells from.  Uses last
            input grid by default.

        callback : function, optional
            When input, calls this function after a selection is made.
            The picked_cells are input as the first parameter to this function.

        through : bool, optional
            When True (default) the picker will select all cells through the
            mesh. When False, the picker will select only visible cells on the
            mesh's surface.

        show : bool
            Show the selection interactively

        style : str
            Visualization style of the selection.  One of the following:
            ``style='surface'``, ``style='wireframe'``, ``style='points'``.
            Defaults to ``'wireframe'``.

        line_width : float, optional
            Thickness of selected mesh edges. Default 5.

        color : str
            The color of the selected mesh is shown.

        show_message : bool, str
            Show the message about how to use the cell picking tool. If this
            is a string, that will be the message shown.

        font_size : int
            Sets the size of the message.

        start : bool
            Automatically start the cell selection tool.

        kwargs : optional
            All remaining keyword arguments are used to control how the
            selection is intereactively displayed.

        """
        if hasattr(self, 'notebook') and self.notebook:
            raise AssertionError('Cell picking not available in notebook plotting')
        if mesh is None:
            if not hasattr(self, 'mesh'):
                raise Exception('Input a mesh into the Plotter class first or '
                                'or set it in this function')
            mesh = self.mesh


        def end_pick_helper(picker, event_id):
            if show:
                # Use try in case selection is empty
                try:
                    self.add_mesh(self.picked_cells, name='_cell_picking_selection',
                                  style=style, color=color,
                                  line_width=line_width, pickable=False,
                                  reset_camera=False, **kwargs)
                except RuntimeError:
                    pass

            if callback is not None and self.picked_cells.n_cells > 0:
                try_callback(callback, self.picked_cells)

            # TODO: Deactivate selection tool
            return


        def through_pick_call_back(picker, event_id):
            extract = vtk.vtkExtractGeometry()
            mesh.cell_arrays['orig_extract_id'] = np.arange(mesh.n_cells)
            extract.SetInputData(mesh)
            extract.SetImplicitFunction(picker.GetFrustum())
            extract.Update()
            self.picked_cells = pyvista.wrap(extract.GetOutput())
            return end_pick_helper(picker, event_id)


        def visible_pick_call_back(picker, event_id):
            x0,y0,x1,y1 = self.get_pick_position()
            selector = vtk.vtkOpenGLHardwareSelector()
            selector.SetFieldAssociation(vtk.vtkDataObject.FIELD_ASSOCIATION_CELLS)
            selector.SetRenderer(self.renderer)
            selector.SetArea(x0,y0,x1,y1)
            cellids = selector.Select().GetNode(0)
            if cellids is None:
                # No selection
                return
            selection = vtk.vtkSelection()
            selection.AddNode(cellids)
            extract = vtk.vtkExtractSelectedIds()
            extract.SetInputData(0, mesh)
            extract.SetInputData(1, selection)
            extract.Update()
            self.picked_cells = pyvista.wrap(extract.GetOutput())
            return end_pick_helper(picker, event_id)


        area_picker = vtk.vtkRenderedAreaPicker()
        if through:
            area_picker.AddObserver(vtk.vtkCommand.EndPickEvent, through_pick_call_back)
        else:
            # check if mesh is triangulated or not
            # Reference:
            #     https://github.com/pyvista/pyvista/issues/277
            #     https://github.com/pyvista/pyvista/pull/281
            message = "Surface picking non-triangulated meshes is known to "\
                      "not work properly with non-NVIDIA GPUs. Please "\
                      "consider triangulating your mesh:\n"\
                      "\t`.extract_geometry().triangulate()`"
            if (not isinstance(mesh, pyvista.PolyData) or
                    mesh.faces.size % 4 or
                    not np.all(mesh.faces.reshape(-1, 4)[:,0] == 3)):
                logging.warning(message)
            area_picker.AddObserver(vtk.vtkCommand.EndPickEvent, visible_pick_call_back)

        self.enable_rubber_band_style()
        self.iren.SetPicker(area_picker)

        # Now add text about cell-selection
        if show_message:
            if show_message is True:
                show_message = "Press R to toggle selection tool"
                if not through:
                    show_message += "\nPress P to pick a single cell under the mouse"
            self.add_text(str(show_message), font_size=font_size, name='_cell_picking_message')

        if start:
            self._style.StartSelect()

        return


    def enable_point_picking(self, callback=None, show_message=True,
                             font_size=18, color='pink', point_size=10,
                             use_mesh=False, show_point=True, tolerance=0.025,
                             **kwargs):
        """Enable picking at points.

        Enable picking a point at the mouse location in the render view
        using the ``P`` key. This point is saved to the ``.picked_point``
        attrbute on the plotter. Pass a callback function that takes that
        point as an argument. The picked point can either be a point on the
        first intersecting mesh, or a point in the 3D window.

        Parameters
        ----------
        callback : function, optional
            When input, calls this function after a pick is made.
            The picked point is input as the first parameter to this function.
            If ``use_mesh`` is ``True``, the callback function will be passed
            a pointer to the picked mesh and the point ID of the selected mesh.

        use_mesh : bool
            If ``True``, the callback function will be passed
            a pointer to the picked mesh and the point ID of the selected mesh.

        show_message : bool, str
            Show the message about how to use the point picking tool. If this
            is a string, that will be the message shown.

        font_size : int
            Sets the size of the message.

        point_size : int, optional
            Size of picked points if ``show_point`` is ``True``. Default 10.

        color : str
            The color of the selected mesh is shown.

        tolerance : float
            Specify tolerance for performing pick operation. Tolerance is
            specified as fraction of rendering window size. (Rendering window
            size is measured across diagonal.)

        kwargs : optional
            All remaining keyword arguments are used to control how the
            picked point is intereactively displayed

        """
        if hasattr(self, 'notebook') and self.notebook:
            raise AssertionError('Point picking not available in notebook plotting')

        def _end_pick_event(picker, event):
            self.picked_point = np.array(picker.GetPickPosition())
            self.picked_mesh = picker.GetDataSet()
            self.picked_point_id = picker.GetPointId()
            if show_point:
                self.add_mesh(self.picked_point, color=color,
                              point_size=point_size, name='_picked_point',
                              pickable=False, reset_camera=False, **kwargs)
            if hasattr(callback, '__call__'):
                if use_mesh:
                    try_callback(callback, self.picked_mesh, self.picked_point_id)
                else:
                    try_callback(callback, self.picked_point)

        point_picker = vtk.vtkPointPicker()
        point_picker.SetTolerance(tolerance)
        self.picker=point_picker
        point_picker.AddObserver(vtk.vtkCommand.EndPickEvent, _end_pick_event)

        self.enable_trackball_style()
        self.iren.SetPicker(point_picker)

        # Now add text about cell-selection
        if show_message:
            if show_message is True:
                show_message = "Press P to pick under the mouse"
            self.add_text(str(show_message), font_size=font_size, name='_point_picking_message')

        return


    def enable_path_picking(self, callback=None, show_message=True,
                            font_size=18, color='pink', point_size=10,
                            line_width=5, show_path=True, tolerance=0.025,
                            **kwargs):
        """Enable picking at paths.

        This is a convenience method for ``enable_point_picking`` to keep
        track of the picked points and create a line using those points.

        The line is saved to the ``.picked_path`` attribute of this plotter

        Parameters
        ----------
        callback : callable
            When given, calls this function after a pick is made.
            The entire picked path is passed as the only parameter to this
            function.

        show_message : bool, str
            Show the message about how to use the point picking tool. If this
            is a string, that will be the message shown.

        show_path : bool
            Show the picked path interactively

        font_size : int
            Sets the size of the message.

        point_size : int, optional
            Size of picked points if ``show_path`` is ``True``. Default 10.

        color : str
            The color of the selected mesh is shown.

        line_width : float, optional
            Thickness of path representation if ``show_path`` is ``True``.
            Default 5.

        tolerance : float
            Specify tolerance for performing pick operation. Tolerance is
            specified as fraction of rendering window size. (Rendering window
            size is measured across diagonal.)

        kwargs : optional
            All remaining keyword arguments are used to control how the
            picked path is intereactively displayed

        """
        kwargs.setdefault('pickable', False)

        def make_line_cells(n_points):
            # cells = np.full((n_points-1, 3), 2, dtype=np.int)
            # cells[:, 1] = np.arange(0, n_points-1, dtype=np.int)
            # cells[:, 2] = np.arange(1, n_points, dtype=np.int)
            cells = np.arange(0, n_points, dtype=np.int)
            cells = np.insert(cells, 0, n_points)
            return cells

        the_points = []
        the_ids = []


        def _the_callback(mesh, idx):
            if mesh is None:
                return
            the_ids.append(idx)
            the_points.append(mesh.points[idx])
            self.picked_path = pyvista.PolyData(np.array(the_points))
            self.picked_path.lines = make_line_cells(len(the_points))
            if show_path:
                self.add_mesh(self.picked_path, color=color, name='_picked_path',
                              line_width=line_width, point_size=point_size,
                              reset_camera=False, **kwargs)
            if hasattr(callback, '__call__'):
                try_callback(callback, self.picked_path)
            return

        def _clear_path_event_watcher():
            del the_points[:]
            del the_ids[:]
            self.remove_actor('_picked_path')
            return

        self.add_key_event('c', _clear_path_event_watcher)
        if show_message is True:
            show_message = "Press P to pick under the mouse\nPress C to clear"

        return self.enable_point_picking(callback=_the_callback, use_mesh=True,
                font_size=font_size, show_message=show_message,
                show_point=False, tolerance=tolerance)


    def enable_geodesic_picking(self, callback=None, show_message=True,
                                font_size=18, color='pink', point_size=10,
                                line_width=5, tolerance=0.025, show_path=True,
                                **kwargs):
        """Enable picking at geodesic paths.

        This is a convenience method for ``enable_point_picking`` to keep
        track of the picked points and create a geodesic path using those
        points.

        The geodesic path is saved to the ``.picked_geodesic`` attribute of
        this plotter

        Parameters
        ----------
        callback : callable
            When given, calls this function after a pick is made.
            The entire picked, geodesic path is passed as the only parameter
            to this function.

        show_path : bool
            Show the picked path interactively

        show_message : bool, str
            Show the message about how to use the point picking tool. If this
            is a string, that will be the message shown.

        font_size : int
            Sets the size of the message.

        point_size : int, optional
            Size of picked points if ``show_path`` is ``True``. Default 10.

        color : str
            The color of the selected mesh is shown.

        line_width : float, optional
            Thickness of path representation if ``show_path`` is ``True``.
            Default 5.

        tolerance : float
            Specify tolerance for performing pick operation. Tolerance is
            specified as fraction of rendering window size. (Rendering window
            size is measured across diagonal.)

        kwargs : optional
            All remaining keyword arguments are used to control how the
            picked path is intereactively displayed

        """
        kwargs.setdefault('pickable', False)

        self.picked_geodesic = pyvista.PolyData()
        self._last_picked_idx = None

        def _the_callback(mesh, idx):
            if mesh is None:
                return
            point = mesh.points[idx]
            if self._last_picked_idx is None:
                self.picked_geodesic = pyvista.PolyData(point)
            else:
                surface = mesh.extract_surface().triangulate()
                locator = vtk.vtkPointLocator()
                locator.SetDataSet(surface)
                locator.BuildLocator()
                start_idx = locator.FindClosestPoint(mesh.points[self._last_picked_idx])
                end_idx = locator.FindClosestPoint(point)
                self.picked_geodesic = self.picked_geodesic + surface.geodesic(start_idx, end_idx)
            self._last_picked_idx = idx

            if show_path:
                self.add_mesh(self.picked_geodesic, color=color, name='_picked_path',
                              line_width=line_width, point_size=point_size,
                              reset_camera=False, **kwargs)
            if hasattr(callback, '__call__'):
                try_callback(callback, self.picked_geodesic)
            return

        def _clear_g_path_event_watcher():
            self.picked_geodesic = pyvista.PolyData()
            self.remove_actor('_picked_path')
            self._last_picked_idx = None
            return

        self.add_key_event('c', _clear_g_path_event_watcher)
        if show_message is True:
            show_message = "Press P to pick under the mouse\nPress C to clear"

        return self.enable_point_picking(callback=_the_callback, use_mesh=True,
                font_size=font_size, show_message=show_message,
                tolerance=tolerance, show_point=False)



    def enable_horizon_picking(self, callback=None, normal=(0,0,1),
                               width=None, show_message=True,
                               font_size=18, color='pink', point_size=10,
                               line_width=5, show_path=True, opacity=0.75,
                               show_horizon=True, **kwargs):
        """Enable horizon picking.

        Helper for the ``enable_path_picking`` method to also show a ribbon
        surface along the picked path. Ribbon is saved under
        ``.picked_horizon``.

        Parameters
        ----------
        callback : callable
            When given, calls this function after a pick is made.
            The entire picked path is passed as the only parameter to this
            function.

        normal : tuple(float)
            The normal to the horizon surface's projection plane

        width : float
            The width of the horizon surface. Default behaviour will
            dynamically change the surface width depending on it's length.

        show_horizon : bool
            Show the picked horizon surface interactively

        show_path : bool
            Show the picked path that the horizon is built from interactively

        show_message : bool, str
            Show the message about how to use the horizon picking tool. If this
            is a string, that will be the message shown.

        font_size : int
            Sets the size of the message.

        point_size : int, optional
            Size of picked points if ``show_horizon`` is ``True``. Default 10.

        color : str
            The color of the horizon surface if shown.

        line_width : float, optional
            Thickness of path representation if ``show_horizon`` is ``True``.
            Default 5.

        opacity : float
            The opacity of the horizon surface if shown.

        tolerance : float
            Specify tolerance for performing pick operation. Tolerance is
            specified as fraction of rendering window size. (Rendering window
            size is measured across diagonal.)

        kwargs : optional
            All remaining keyword arguments are used to control how the
            picked path is intereactively displayed

        """
        name = '_horizon'
        self.add_key_event('c', lambda: self.remove_actor(name))

        def _the_callback(path):
            if path.n_points < 2:
                self.remove_actor(name)
                return
            self.picked_horizon = path.ribbon(normal=normal, width=width)

            if show_horizon:
                self.add_mesh(self.picked_horizon, name=name, color=color,
                              opacity=opacity, pickable=False,
                              reset_camera=False)

            if hasattr(callback, '__call__'):
                try_callback(callback, path)

        self.enable_path_picking(callback=_the_callback,
            show_message=show_message, font_size=font_size, color=color,
            point_size=point_size, line_width=line_width, show_path=show_path,
            **kwargs)


    def pick_click_position(self):
        """Get corresponding click location in the 3D plot."""
        if self.click_position is None:
            self.store_click_position()
        picker = vtk.vtkWorldPointPicker()
        picker.Pick(self.click_position[0], self.click_position[1], 0, self.renderer)
        return picker.GetPickPosition()


    def pick_mouse_position(self):
        """Get corresponding mouse location in the 3D plot."""
        if self.mouse_position is None:
            self.store_mouse_position()
        picker = vtk.vtkWorldPointPicker()
        picker.Pick(self.mouse_position[0], self.mouse_position[1], 0, self.renderer)
        return picker.GetPickPosition()


    def fly_to_mouse_position(self, focus=False):
        """Focus on last stored mouse position."""
        if self.mouse_position is None:
            self.store_mouse_position()
        click_point = self.pick_mouse_position()
        if focus:
            self.set_focus(click_point)
        else:
            self.fly_to(click_point)


    def enable_fly_to_right_click(self, callback=None):
        """Set the camera to track right click positions.

        A convenience method to track right click positions and fly to the
        picked point in the scene. The callback will be passed the point in
        3D space.

        """
        def _the_callback(*args):
            click_point = self.pick_mouse_position()
            self.fly_to(click_point)
            if hasattr(callback, '__call__'):
                try_callback(callback, click_point)

        self.track_click_position(callback=_the_callback, side="right")
        return

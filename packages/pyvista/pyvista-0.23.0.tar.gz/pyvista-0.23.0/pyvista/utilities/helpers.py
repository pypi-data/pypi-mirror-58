"""Supporting functions for polydata and grid objects."""

import collections
import ctypes
import logging
import warnings

import numpy as np
import scooby
import vtk
import vtk.util.numpy_support as nps

import pyvista

POINT_DATA_FIELD = 0
CELL_DATA_FIELD = 1
FIELD_DATA_FIELD = 2
ROW_DATA_FIELD = 6


def get_vtk_type(typ):
    """Look up the VTK type for a give python data type.

    Corrects for string type mapping issues.

    Return
    ------
        int : the integer type id specified in vtkType.h

    """
    typ = nps.get_vtk_array_type(typ)
    # This handles a silly string type bug
    if typ == 3:
        return 13
    return typ


def vtk_bit_array_to_char(vtkarr_bint):
    """Cast vtk bit array to a char array."""
    vtkarr = vtk.vtkCharArray()
    vtkarr.DeepCopy(vtkarr_bint)
    return vtkarr


def convert_string_array(arr, name=None):
    """Convert a numpy array of strings to a vtkStringArray or vice versa.

    Note that this is terribly inefficient - inefficient support
    is better than no support :). If you have ideas on how to make this faster,
    please consider opening a pull request.

    """
    if isinstance(arr, np.ndarray):
        vtkarr = vtk.vtkStringArray()
        ########### OPTIMIZE ###########
        for val in arr:
            vtkarr.InsertNextValue(val)
        ################################
        if isinstance(name, str):
            vtkarr.SetName(name)
        return vtkarr
    # Otherwise it is a vtk array and needs to be converted back to numpy
    carr = np.empty(arr.GetNumberOfValues(), dtype='O')
    ############### OPTIMIZE ###############
    for i in range(arr.GetNumberOfValues()):
        carr[i] = arr.GetValue(i)
    ########################################
    return carr.astype('|S')


def convert_array(arr, name=None, deep=0, array_type=None):
    """Convert a NumPy array to a vtkDataArray or vice versa.

    Parameters
    -----------
    arr : ndarray or vtkDataArry
        A numpy array or vtkDataArry to convert
    name : str
        The name of the data array for VTK
    deep : bool
        if input is numpy array then deep copy values

    Return
    ------
    vtkDataArray, ndarray, or DataFrame:
        the converted array (if input is a NumPy ndaray then returns
        ``vtkDataArray`` or is input is ``vtkDataArray`` then returns NumPy
        ``ndarray``). If pdf==True and the input is ``vtkDataArry``,
        return a pandas DataFrame.

    """
    if arr is None:
        return
    if isinstance(arr, np.ndarray):
        if arr.dtype is np.dtype('O'):
            arr = arr.astype('|S')
        arr = np.ascontiguousarray(arr)
        try:
            # This will handle numerical data
            arr = np.ascontiguousarray(arr)
            vtk_data = nps.numpy_to_vtk(num_array=arr, deep=deep, array_type=array_type)
        except ValueError:
            # This handles strings
            typ = get_vtk_type(arr.dtype)
            if typ == 13:
                vtk_data = convert_string_array(arr)
        if isinstance(name, str):
            vtk_data.SetName(name)
        return vtk_data
    # Otherwise input must be a vtkDataArray
    if not isinstance(arr, (vtk.vtkDataArray, vtk.vtkBitArray, vtk.vtkStringArray)):
        raise TypeError('Invalid input array type ({}).'.format(type(arr)))
    # Handle booleans
    if isinstance(arr, vtk.vtkBitArray):
        arr = vtk_bit_array_to_char(arr)
    # Handle string arrays
    if isinstance(arr, vtk.vtkStringArray):
        return convert_string_array(arr)
    # Convert from vtkDataArry to NumPy
    return nps.vtk_to_numpy(arr)



def is_pyvista_dataset(obj):
    """Return True if the Object is a PyVista wrapped dataset."""
    return isinstance(obj, (pyvista.Common, pyvista.MultiBlock))


def point_array(mesh, name):
    """Return point array of a vtk object."""
    vtkarr = mesh.GetPointData().GetAbstractArray(name)
    return convert_array(vtkarr)

def point_scalar(mesh, name):
    """Return point array of a vtk object.

    DEPRECATED: please use `point_array` instead.
    """
    warnings.warn("DEPRECATED: please use `point_array` instead.")
    return point_array(mesh, name)

def field_array(mesh, name):
    """Return field array of a vtk object."""
    vtkarr = mesh.GetFieldData().GetAbstractArray(name)
    return convert_array(vtkarr)

def field_scalar(mesh, name):
    """Return field array of a vtk object.

    DEPRECATED: please use `field_array` instead.
    """
    warnings.warn("DEPRECATED: please use `field_array` instead.")
    return field_array(mesh, name)

def cell_array(mesh, name):
    """Return cell array of a vtk object."""
    vtkarr = mesh.GetCellData().GetAbstractArray(name)
    return convert_array(vtkarr)

def cell_scalar(mesh, name):
    """Return cell array of a vtk object.

    DEPRECATED: please use `cell_array` instead.
    """
    warnings.warn("DEPRECATED: please use `cell_array` instead.")
    return cell_array(mesh, name)

def row_array(data_object, name):
    """Return row array of a vtk object."""
    vtkarr = data_object.GetRowData().GetAbstractArray(name)
    return convert_array(vtkarr)

def parse_field_choice(field):
    """Return the id of the given field."""
    if isinstance(field, str):
        field = field.strip().lower()
        if field in ['cell', 'c', 'cells']:
            field = CELL_DATA_FIELD
        elif field in ['point', 'p', 'points']:
            field = POINT_DATA_FIELD
        elif field in ['field', 'f', 'fields']:
            field = FIELD_DATA_FIELD
        elif field in ['row', 'r',]:
            field = ROW_DATA_FIELD
        else:
            raise RuntimeError('Data field ({}) not supported.'.format(field))
    elif isinstance(field, int):
        pass
    else:
        raise RuntimeError('Data field ({}) not supported.'.format(field))
    return field


def get_array(mesh, name, preference='cell', info=False, err=False):
    """Search point, cell and field data for an array.

    Parameters
    ----------
    name : str
        The name of the array to get the range.

    preference : str, optional
        When scalars is specified, this is the perfered array type to
        search for in the dataset.  Must be either ``'point'``, ``'cell'``, or
        ``'field'``

    info : bool
        Return info about the array rather than the array itself.

    err : bool
        Boolean to control whether to throw an error if array is not present.

    """
    if isinstance(mesh, vtk.vtkTable):
        arr = row_array(mesh, name)
        if arr is None and err:
            raise KeyError('Data array ({}) not present in this dataset.'.format(name))
        field = ROW_DATA_FIELD
        if info:
            return arr, field
        return arr

    parr = point_array(mesh, name)
    carr = cell_array(mesh, name)
    farr = field_array(mesh, name)
    preference = parse_field_choice(preference)
    if np.sum([parr is not None, carr is not None, farr is not None]) > 1:
        if preference == CELL_DATA_FIELD:
            if info:
                return carr, CELL_DATA_FIELD
            else:
                return carr
        elif preference == POINT_DATA_FIELD:
            if info:
                return parr, POINT_DATA_FIELD
            else:
                return parr
        elif preference == FIELD_DATA_FIELD:
            if info:
                return farr, FIELD_DATA_FIELD
            else:
                return farr
        else:
            raise RuntimeError('Data field ({}) not supported.'.format(preference))
    arr = None
    field = None
    if parr is not None:
        arr = parr
        field = POINT_DATA_FIELD
    elif carr is not None:
        arr = carr
        field = CELL_DATA_FIELD
    elif farr is not None:
        arr = farr
        field = FIELD_DATA_FIELD
    elif err:
        raise KeyError('Data array ({}) not present in this dataset.'.format(name))
    if info:
        return arr, field
    return arr


def vtk_points(points, deep=True):
    """Convert numpy points to a vtkPoints object."""
    if not points.flags['C_CONTIGUOUS']:
        points = np.ascontiguousarray(points)
    vtkpts = vtk.vtkPoints()
    vtkpts.SetData(nps.numpy_to_vtk(points, deep=deep))
    return vtkpts


def line_segments_from_points(points):
    """Generate non-connected line segments from points.

    Assumes points are ordered as line segments and an even number of points
    are

    Parameters
    ----------
    points : np.ndarray
        Points representing line segments. An even number must be given as
        every two vertices represent a single line segment. For example, two
        line segments would be represented as:

        np.array([[0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0]])

    Returns
    -------
    lines : pyvista.PolyData
        PolyData with lines and cells.

    Examples
    --------
    This example plots two line segments at right angles to each other line.

    >>> import pyvista
    >>> import numpy as np
    >>> points = np.array([[0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0]])
    >>> lines = pyvista.lines_from_points(points)
    >>> lines.plot() # doctest:+SKIP

    """
    if len(points) % 2:
        raise RuntimeError("An even number of points must be given to define each segment.")
    # Assuming ordered points, create array defining line order
    n_points = len(points)
    n_lines = n_points // 2
    lines = np.c_[(2 * np.ones(n_lines, np.int),
                   np.arange(0, n_points-1, step=2),
                   np.arange(1, n_points+1, step=2))]
    poly = pyvista.PolyData()
    poly.points = points
    poly.lines = lines
    return poly


def lines_from_points(points):
    """Make a connected line set given an array of points.

    Parameters
    ----------
    points : np.ndarray
        Points representing the vertices of the connected segments. For
        example, two line segments would be represented as:

        np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0]])

    Return
    ------
    lines : pyvista.PolyData
        PolyData with lines and cells.

    """
    poly = pyvista.PolyData()
    poly.points = points
    cells = np.full((len(points)-1, 3), 2, dtype=np.int)
    cells[:, 1] = np.arange(0, len(points)-1, dtype=np.int)
    cells[:, 2] = np.arange(1, len(points), dtype=np.int)
    poly.lines = cells
    return poly


def vector_poly_data(orig, vec):
    """Create a vtkPolyData object composed of vectors."""
    # shape, dimension checking
    if not isinstance(orig, np.ndarray):
        orig = np.asarray(orig)

    if not isinstance(vec, np.ndarray):
        vec = np.asarray(vec)

    if orig.ndim != 2:
        orig = orig.reshape((-1, 3))
    elif orig.shape[1] != 3:
        raise Exception('orig array must be 3D')

    if vec.ndim != 2:
        vec = vec.reshape((-1, 3))
    elif vec.shape[1] != 3:
        raise Exception('vec array must be 3D')

    # Create vtk points and cells objects
    vpts = vtk.vtkPoints()
    vpts.SetData(nps.numpy_to_vtk(np.ascontiguousarray(orig), deep=True))

    npts = orig.shape[0]
    cells = np.hstack((np.ones((npts, 1), 'int'),
                       np.arange(npts).reshape((-1, 1))))

    if cells.dtype != ctypes.c_int64 or cells.flags.c_contiguous:
        cells = np.ascontiguousarray(cells, ctypes.c_int64)
    cells = np.reshape(cells, (2*npts))
    vcells = vtk.vtkCellArray()
    vcells.SetCells(npts, nps.numpy_to_vtkIdTypeArray(cells, deep=True))

    # Create vtkPolyData object
    pdata = vtk.vtkPolyData()
    pdata.SetPoints(vpts)
    pdata.SetVerts(vcells)

    # Add vectors to polydata
    name = 'vectors'
    vtkfloat = nps.numpy_to_vtk(np.ascontiguousarray(vec), deep=True)
    vtkfloat.SetName(name)
    pdata.GetPointData().AddArray(vtkfloat)
    pdata.GetPointData().SetActiveVectors(name)

    # Add magnitude of vectors to polydata
    name = 'mag'
    scalars = (vec * vec).sum(1)**0.5
    vtkfloat = nps.numpy_to_vtk(np.ascontiguousarray(scalars), deep=True)
    vtkfloat.SetName(name)
    pdata.GetPointData().AddArray(vtkfloat)
    pdata.GetPointData().SetActiveScalars(name)

    return pyvista.PolyData(pdata)


def trans_from_matrix(matrix):
    """Convert a vtk matrix to a numpy.ndarray."""
    t = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            t[i, j] = matrix.GetElement(i, j)
    return t


def wrap(vtkdataset):
    """Wrap any given VTK data object to its appropriate PyVista data object.

    Other formats that are supported include:
    * 2D :class:`numpy.ndarray` of XYZ vertices
    * 3D :class:`numpy.ndarray` representing a volume. Values will be scalars.

    """
    wrappers = {
        'vtkUnstructuredGrid': pyvista.UnstructuredGrid,
        'vtkRectilinearGrid': pyvista.RectilinearGrid,
        'vtkStructuredGrid': pyvista.StructuredGrid,
        'vtkPolyData': pyvista.PolyData,
        'vtkImageData': pyvista.UniformGrid,
        'vtkStructuredPoints': pyvista.UniformGrid,
        'vtkMultiBlockDataSet': pyvista.MultiBlock,
        'vtkTable': pyvista.Table,
        # 'vtkParametricSpline': pyvista.Spline,
    }
    # Otherwise, we assume a VTK data object was passed
    if hasattr(vtkdataset, 'GetClassName'):
        key = vtkdataset.GetClassName()
    elif vtkdataset is None:
        return None
    elif isinstance(vtkdataset, np.ndarray):
        if vtkdataset.ndim == 1 and vtkdataset.shape[0] == 3:
            return pyvista.PolyData(vtkdataset)
        if vtkdataset.ndim > 1 and vtkdataset.ndim < 3 and vtkdataset.shape[1] == 3:
            return pyvista.PolyData(vtkdataset)
        elif vtkdataset.ndim == 3:
            mesh = pyvista.UniformGrid(vtkdataset.shape)
            mesh['values'] = vtkdataset.ravel(order='F')
            mesh.active_scalars_name = 'values'
            return mesh
        else:
            print(vtkdataset.shape, vtkdataset)
            raise NotImplementedError('NumPy array could not be converted to PyVista.')
    else:
        raise NotImplementedError('Type ({}) not able to be wrapped into a PyVista mesh.'.format(type(vtkdataset)))
    try:
        wrapped = wrappers[key](vtkdataset)
    except KeyError:
        logging.warning('VTK data type ({}) is not currently supported by pyvista.'.format(key))
        return vtkdataset # if not supported just passes the VTK data object
    return wrapped


def image_to_texture(image):
    """Convert ``vtkImageData`` (:class:`pyvista.UniformGrid`) to a ``vtkTexture``."""
    return pyvista.Texture(image)


def numpy_to_texture(image):
    """Convert a NumPy image array to a vtk.vtkTexture."""
    if not isinstance(image, np.ndarray):
        raise TypeError('Unknown input type ({})'.format(type(image)))
    return pyvista.Texture(image)


def is_inside_bounds(point, bounds):
    """Check if a point is inside a set of bounds.

    This is implemented through recursion so that this is N-dimensional.

    """
    if isinstance(point, (int, float)):
        point = [point]
    if isinstance(point, collections.Iterable) and not isinstance(point, collections.deque):
        if len(bounds) < 2 * len(point) or len(bounds) % 2 != 0:
            raise AssertionError('Bounds mismatch point dimensionality')
        point = collections.deque(point)
        bounds = collections.deque(bounds)
        return is_inside_bounds(point, bounds)
    if not isinstance(point, collections.deque):
        raise TypeError('Unknown input data type ({}).'.format(type(point)))
    if len(point) < 1:
        return True
    p = point.popleft()
    lower, upper = bounds.popleft(), bounds.popleft()
    if lower <= p <= upper:
        return is_inside_bounds(point, bounds)
    return False


def fit_plane_to_points(points, return_meta=False):
    """Fit a plane to a set of points.

    Parameters
    ----------
    points : np.ndarray
        Size n by 3 array of points to fit a plane through

    return_meta : bool
        If true, also returns the center and normal used to generate the plane

    """
    data = np.array(points)
    center = data.mean(axis=0)
    result = np.linalg.svd(data - center)
    normal = np.cross(result[2][0], result[2][1])
    plane = pyvista.Plane(center=center, direction=normal)
    if return_meta:
        return plane, center, normal
    return plane


def raise_not_matching(scalars, mesh):
    """Raise exception about inconsistencies."""
    if isinstance(mesh, vtk.vtkTable):
        raise Exception('Number of scalars ({})'.format(scalars.size) +
                        'must match number of rows ' +
                        '({}).'.format(mesh.n_rows) )
    raise Exception('Number of scalars ({}) '.format(scalars.size) +
                    'must match either the number of points ' +
                    '({}) '.format(mesh.n_points) +
                    'or the number of cells ' +
                    '({}). '.format(mesh.n_cells) )


def generate_plane(normal, origin):
    """Return a vtk.vtkPlane."""
    plane = vtk.vtkPlane()
    # NORMAL MUST HAVE MAGNITUDE OF 1
    normal = normal / np.linalg.norm(normal)
    plane.SetNormal(normal)
    plane.SetOrigin(origin)
    return plane


def generate_report(additional=None, ncol=3, text_width=54, sort=False):
    """Generate a report.

    DEPRECATED: Please use :class:`pyvista.Report` instead.

    """
    logging.warning('DEPRECATED: Please use `pyvista.Report` instead.')
    core = ['pyvista', 'vtk', 'numpy', 'imageio', 'appdirs', 'scooby']
    optional = ['matplotlib', 'PyQt5', 'IPython', 'colorcet',
                'cmocean']
    report = scooby.Report(core=core, optional=optional,
                           additional=additional, ncol=ncol,
                           text_width=text_width, sort=sort)
    return report


def try_callback(func, *args):
    """Wrap a given callback in a try statement."""
    try:
        func(*args)
    except Exception as e:
        logging.warning('Encountered issue in callback: {}'.format(e))
    return


def check_depth_peeling(number_of_peels=100, occlusion_ratio=0.0):
    """Check if depth peeling is available.

    Attempts to use depth peeling to see if it is available for the current
    environment. Returns ``True`` if depth peeling is available and has been
    successfully leveraged, otherwise ``False``.

    """
    # Try Depth Peeling with a basic scene
    source = vtk.vtkSphereSource()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    # requires opacity < 1
    actor.GetProperty().SetOpacity(0.5)
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetOffScreenRendering(True)
    renderWindow.SetAlphaBitPlanes(True)
    renderWindow.SetMultiSamples(0)
    renderer.AddActor(actor)
    renderer.SetUseDepthPeeling(True)
    renderer.SetMaximumNumberOfPeels(number_of_peels)
    renderer.SetOcclusionRatio(occlusion_ratio)
    renderWindow.Render()
    return renderer.GetLastRenderingUsedDepthPeeling() == 1

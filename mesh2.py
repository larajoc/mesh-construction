import numpy as np
import scipy.spatial
import pyvista as pv
import vtk

def generate_random_points(n, domain_size=(1, 1, 1)):
    x = np.random.rand(n) * domain_size[0]
    y = np.random.rand(n) * domain_size[1]
    z = np.random.rand(n) * domain_size[2]
    return np.vstack((x, y, z)).T

def delaunay_triangulation(points):
    return scipy.spatial.Delaunay(points)

def plot_triangulation(tri, points, title="3D Delaunay Triangulation"):
    
    # convert tetrahedrons to VTK format
    num_tets = tri.simplices.shape[0]
    cell_array = np.hstack([np.full((num_tets, 1), 4), tri.simplices]).astype(np.int64)
    
    # create an UnstructuredGrid with tetrahedral cells
    grid = pv.UnstructuredGrid(cell_array, np.full(num_tets, vtk.VTK_TETRA), points)
    
    #tetrahedral mesh
    plotter = pv.Plotter()
    plotter.add_mesh(grid, show_edges=True, opacity=0.6, color="lightblue")
    plotter.add_points(points, color="red", point_size=5)
    plotter.add_title(title)
    plotter.show()

num_points = 50
points = generate_random_points(num_points)
tri = delaunay_triangulation(points)
plot_triangulation(tri, points, title="Initial 3D Delaunay Mesh")

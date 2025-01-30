import numpy as np
import scipy.spatial
import pyvista as pv
import vtk

def generate_rectangular_grid(nx=5, ny=5, nz=5, spacing=0.2):
    x = np.linspace(0, spacing * (nx - 1), nx)
    y = np.linspace(0, spacing * (ny - 1), ny)
    z = np.linspace(0, spacing * (nz - 1), nz)
    
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    points = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T
    return points

def delaunay_triangulation(points):
    return scipy.spatial.Delaunay(points)

def adaptive_mesh_refinement(points, tri, threshold=0.3, max_iterations=2):


    for _ in range(max_iterations):
        new_points = []
        for simplex in tri.simplices:
            vertices = points[simplex]
            
            edge_lengths = [np.linalg.norm(vertices[i] - vertices[j]) 
                            for i in range(4) for j in range(i+1, 4)]
            
            if max(edge_lengths) > threshold:
                centroid = np.mean(vertices, axis=0)
                new_points.append(centroid)

        if not new_points:
            break  

        new_points = np.vstack(new_points)
        points = np.vstack((points, new_points))
        tri = delaunay_triangulation(points)

    return points, tri

def plot_triangulation(tri, points, title="3D Delaunay Triangulation"):

    num_tets = tri.simplices.shape[0]
    cell_array = np.hstack([np.full((num_tets, 1), 4), tri.simplices]).astype(np.int64)
    
    grid = pv.UnstructuredGrid(cell_array, np.full(num_tets, vtk.VTK_TETRA), points)
    
    plotter = pv.Plotter()
    plotter.add_mesh(grid, show_edges=True, opacity=0.6, color="lightblue")
    plotter.add_points(points, color="red", point_size=5)
    plotter.add_title(title)
    plotter.show()


points = generate_rectangular_grid(nx=5, ny=5, nz=10, spacing=0.2)

tri = delaunay_triangulation(points)

plot_triangulation(tri, points, title="Initial 3D Delaunay Mesh")

refined_points, refined_tri = adaptive_mesh_refinement(points, tri, threshold=0.3, max_iterations=2)

plot_triangulation(refined_tri, refined_points, title="Refined 3D Mesh with AMR")

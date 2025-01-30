import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial

def generate_random_points(n, domain_size=(1, 1)):
    a = np.random.rand(n) * domain_size[0]
    b = np.random.rand(n) * domain_size[1]
    return np.vstack((a, b)).T

def delaunay_triangulation(points):
    return scipy.spatial.Delaunay(points)

def plot_triangulation(tri, points, title="Delaunay Triangulation"):
    plt.triplot(points[:, 0], points[:, 1], tri.simplices, linewidth=0.5)
    plt.scatter(points[:, 0], points[:, 1], c="red", s=10)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def adaptive_mesh_refinement(points, tri, threshold=0.1):
    new_points = []
    for simplex in tri.simplices:
        vertices = points[simplex]
        edge_lengths = [np.linalg.norm(vertices[i] - vertices[j]) for i in range(3) for j in range(i+1, 3)]
        
        if max(edge_lengths) > threshold:
            centroid = np.mean(vertices, axis=0)
            new_points.append(centroid)
    
    if new_points:
        new_points = np.vstack(new_points)
        refined_points = np.vstack((points, new_points))
        return refined_points
    else:
        return points

num_points = 30
points = generate_random_points(num_points)

tri = delaunay_triangulation(points)

plot_triangulation(tri, points, title="Initial Delaunay Mesh")

refined_points = adaptive_mesh_refinement(points, tri, threshold=0.15)

tri_refined = delaunay_triangulation(refined_points)
plot_triangulation(tri_refined, refined_points, title="Refined Mesh with AMR")

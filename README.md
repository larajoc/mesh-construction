# Adaptive Mesh Refinement (AMR) in 3D

**Mesh Generation**: Creates a structured **3D rectangular grid**.
**Delaunay Triangulation**: Generates a **tetrahedral mesh**.
**AMR**: Refines the mesh dynamically based on element size.
**3D Visualization**: Uses **PyVista** to display the deformed mesh.

---

## Installation
Before running the project, install the required dependencies:

pip install uv
uv venv .venv
uv pip install numpy scipy matplotlib
pip install numpy scipy pyvista matplotlib
uv run python

uv is a lightweight Python virtual environment tool used in this project.


## Clarifications
First attempt is the test code given by the library;
Mesh_(number) are different attempts i tried to run;
Mesh_retangle.py is the final code;

We apply Adaptive Mesh Refinement (AMR) by adding new points in high-density regions
Threshold is the maximum tetrahedron edge length before refinement
Max_iterations limits excessive refinements
Visualization Toolkit (VTK) is an open-source library for scientific data vizualization, handeling unstructured meshes much better than other alternatives;
    -- Each tetrahedron is defined by 4 vertices, and PyVista uses vtk.VTK_TETRA to assign this type when building the 3D mesh;
    -- vtk.VTK_TETRA tells PyVista that the cells in the cell_array are used to form the tetrahedra.

Many thanks for the scipy and pyvista library, alongside with open source code that helped me base this small project.

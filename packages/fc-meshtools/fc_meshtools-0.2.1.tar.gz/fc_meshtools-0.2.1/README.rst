.. _fc-meshtools: http://www.math.univ-paris13.fr/~cuvelier/software/Python/fc-meshtools.html

.. _python: http://www.python.org
   

.. image:: http://www.math.univ-paris13.fr/~cuvelier/software/codes/Python/fc-meshtools/pyfc-meshtools_400.png
  :width: 400px
  :align: center

The **fc\_meshtools** Python package  contains some simplicial meshes
given by their vertices array **q** and connectivity array **me**. Theses meshes can be easily used in 
other Python codes for debugging or testing purpose. 

   
Introduction:
-------------   

A simplicial mesh is given by its vertices array **q** and its connectivity array **me**.
For demonstration purpose, some simplicial meshes are given in this package and stored in the fc_meshtools/data directory.  
They can be load by using the functions ``getMesh2D``, ``getMesh3D`` or ``getMesh3Ds``
of the ``fc_meshtools.simplicial`` module.
Here are the kind of simplicial meshes present in this package: 

  - a triangular mesh in dimension 2, made with 2-simplices (ie. triangles),
  - a tetrahedral mesh in dimension 3, made with 3-simplices (ie. tetrahedron),
  - a triangular mesh in dimension 3 (surface mesh), made with 2-simplices,
  - a line mesh in dimension 2 or 3 made with 1-simplices (ie. lines).

One can go to the dedicated web page `fc-meshtools`_ for more informations.

Installation:
-------------

The **fc\_meshtools** Python package is available from the Python Package Index. so to install/upgrade simply type

.. code:: 

   pip install fc_meshtools 
        
Examples
--------

first example
~~~~~~~~~~~~~

.. code:: python

      import fc_meshtools
      q,me,toG=fc_meshtools.simplicial.getMesh2D(2)
      vols=fc_meshtools.simplicial.Volumes(q,me)
      print(' q:%s, me:%s, vols:%s'%(str(q.shape),str(me.shape),str(vols.shape)))
      
The output of the ``print`` command is::

       q:(2, 9116), me:(3, 17638), vols:(17638,)
      
second example
~~~~~~~~~~~~~~

.. code:: python

      import fc_meshtools,numpy
      q3,me3=fc_meshtools.simplicial.getMesh3D(3)[:2]
      vols3=fc_meshtools.simplicial.Volumes(q3,me3)
      G3=fc_meshtools.simplicial.GradBaCo(q3,me3)
      print(' q3:%s, me3:%s, vols3:%s, G3:%s'%(str(q3.shape),str(me3.shape),str(vols3.shape),str(G3.shape)))
      q2,me2,toG2=fc_meshtools.simplicial.getMesh3D(2)
      vols2=fc_meshtools.simplicial.Volumes(q2,me2)
      G2=fc_meshtools.simplicial.GradBaCo(q2,me2)
      print(' q2:%s, me2:%s, vols2:%s, G2:%s'%(str(q2.shape),str(me2.shape),str(vols2.shape),str(G2.shape)))
      E=numpy.max(numpy.abs(q2-q3[:,toG2]))
      print(' E=%g'%E)
      
The output is::

      q3:(3, 14120), me3:(4, 67653), vols3:(67653,), G3:(67653, 3, 4)
      q2:(3, 6471), me2:(3, 12950), vols2:(12950,), G2:(12950, 3, 3)
      E=0.000000e+00

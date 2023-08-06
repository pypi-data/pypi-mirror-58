
Tencat
======

Tencat is a Python library that offers basic sparse tensor slicing capabilities.

Installation
------------

Use the package manager `pip <https://pip.pypa.io/en/stable/>`_ to install tencat.

.. code-block:: bash

   pip install tencat

Usage
-----

Tencat implements the coordinate format in SparseTensor using a (N,d) ndarray as indices, a (N,) ndarray as values and an optional d length size tuple.  

.. code-block:: python

   from tencat import tencat as tc

   nnz = 100 # Number of nonzero elements
   ndim = 4 # Number of dimensions

   indices = np.randint(100,(nnz,ndim)) # Create random indices
   values = np.random.rand(nnz,) # create random elements

   dense_shape = np.amax(indices,axis=0) + np.random.randint(5,size=(ndim,))

   sparse_tc = tc.SparseTensor(indices,values,dense_shape)

   sliced_tc = sparse_tc.slice((1,5,6,4),(3,2,10,5))

License
-------

`MIT <https://choosealicense.com/licenses/mit/>`_

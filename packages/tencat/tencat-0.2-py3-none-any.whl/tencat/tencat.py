import numpy as np


class SparseTensor:
	def __init__(self, indices, values, size=None):
		'''
        indices : numpy.ndarray (ndim, nnz)
            An array holding the index locations of every value
        values : numpy.ndarray (nnz,)
            An array of Values
        shape : tuple[int], (ndim,),  optional
            The shape of the array
        '''

		def check_indices(indices):
			_NUMERIC_KINDS = set('ui')
			if not type(indices) is np.ndarray:
				try:
					indices = np.asarray(indices)
				except: 
					raise TypeError("The indices are not given in a proper format.")
					
			if not indices.dtype.kind in _NUMERIC_KINDS:
				raise TypeError("Given indices are not integers.")
				
			if np.any(indices < 0):
				raise ValueError("Given indices contain negative values.")
			
			return indices
			
				
		def check_size(size): 
			if not type(size) is tuple:
				try:
					size = tuple(size)
				except: 
					raise TypeError("The shape is not given in a proper format.")
					
			if not all(isinstance(n, (int, np.integer)) for n in size):
				raise TypeError("Given shape contains elements which are not integers.") 
				
			if any(n < 1 for n in size):
				raise ValueError("Given shape contains non positive values.")
				
			return size 

		indices = check_indices(indices)
		
		if size is not None:
			size = check_size(size)
		else: 
			size = tuple(np.amax(indices,axis=0))

		if not indices.shape[0] == values.shape[0]:
			raise ValueError("indices and values must have same length (number of rows)!")
		if not indices.shape[1] == len(size):
			raise ValueError("Wrong number of indices for this tensor size!")


		if (not indices.size == 0):
			if np.any(np.amax(indices,axis=0) > np.array(size)):
				raise ValueError("The indices of elements exceed the specified tensor size.")


		self._indices = indices
		self._values = values
		self._size = size



	def get_size(self): 
		return self._size
	
	def get_values(self):
		return self._values

	def get_indices(self):
		return self._indices
	
	def create_from_tensorflow(self,tensorflow_sparse): pass
		
	def to_tensorflow(): pass



	def slice(self, start, size): 
		'''
		start : tuple[int], (ndim,)
			 Indices of the starting point
		size : tuple[int], (ndim,)
			The shape of the sliced tensor
		'''  

		ndim = len(self._size)
		
		if not ndim == len(start):
			raise ValueError("Dimension mismatch")

		if not ndim == len(size):
			raise ValueError("Dimension mismatch")


		end = np.add(start,size)

		if np.any(end > np.array(self._size)):
			raise ValueError("Slice is bigger than original tensor")

		if np.any(np.array(start) < 0):			
			raise ValueError("Negative indices not surported")

		nnz = self._indices.shape[0]

		sliced_tensor_size = size

		slice_idx = np.arange(nnz)
		
		for d in range(ndim):
			above_idx = np.argwhere(self._indices[:,d] >= start[d])
			below_idx = np.argwhere(self._indices[:,d] < end[d])
			range_idx = np.intersect1d(above_idx,below_idx)
			slice_idx = np.intersect1d(slice_idx,range_idx)
			if not slice_idx.shape[0]:
				return SparseTensor(np.zeros((0,ndim),dtype=np.int),np.asarray([]),sliced_tensor_size)
			
		sliced_tensor_indices = self._indices[slice_idx,:] - np.array(start)
		sliced_tensor_values = self._values[slice_idx]

		return SparseTensor(sliced_tensor_indices,sliced_tensor_values,sliced_tensor_size)
	
	
	def reduce_dim(self): pass
	
	def get_value(self,indices): pass
	
	def to_dense(self): pass

import numpy as np

class SparseTensor:
	def __init__(self, indices, values, size):
		'''
		indices : numpy.ndarray (ndim, nnz)
			An array holding the index locations of every value
		values : numpy.ndarray (nnz,)
			An array of Values
		shape : tuple[int], (ndim,),  optional
			The shape of the array
		'''  
		
		# Check if dimensions (n,d) match
		# Check types
		# Indices within size bounds and INT
		# size all INT
		
		self._indices = indices
		self._values = values
		self._size = size
		
		
	def get_size(self): pass 
	
	def create_from_tensorflow(self,tensorflow_sparse): pass
		#ind = tensorflow_sparse.get_indices()
		
		#self.__init__(ind,)
		
	def to_tensorflow(): pass
		
	def slice(self, start, size):
		'''
		start : tuple[int], (ndim,)
			 Indices of the starting point
		size : tuple[int], (ndim,)
			The shape of the sliced tensor
		'''  
		ndim = len(self._size)
		sliced_tensor_indices = self._indices
		sliced_tensor_values = self._values
		sliced_tensor_size = size
		
		end = np.add(start,size)

		for d in range(ndim):
			above_idx = np.argwhere(sliced_tensor_indices[:,d] >= start[d])
			below_idx = np.argwhere(sliced_tensor_indices[:,d] < end[d])
			range_idx = np.intersect1d(above_idx,below_idx)
			if not range_idx.shape[0]:
				return SparseTensor(np.zeros((0,ndim)),np.asarray([]),sliced_tensor_size)
			sliced_tensor_indices = sliced_tensor_indices[range_idx,:]
			sliced_tensor_values = sliced_tensor_values[range_idx]
			print(sliced_tensor_indices)
			print(sliced_tensor_values)

		return SparseTensor(sliced_tensor_indices,sliced_tensor_values,sliced_tensor_size)


	
	
	def reduce_dim(self): pass
	
	def get_value(self,indices): pass
	
	def to_dense(self): pass
	
		
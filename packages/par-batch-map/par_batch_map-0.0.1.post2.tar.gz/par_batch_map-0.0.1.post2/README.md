# parallel_batch
This is package for parallel batch processing.

* Function batch_map in functionality is equivalent of map functor.
* Result of map(callable, iterable) should be the same as batch_map(callable, iterable),
* batch_map function allows parallel computation in batches, especially useful when iterable is stream data (iterator) and we don't know size of the data.

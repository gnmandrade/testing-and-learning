# testing-and-learning
Repository to test pieces of code and learn specific concepts.


# Contents
+ Dataviz_and_models
+ Tensorflow
+ Parallel Computing (multiprocessing, ProcessPoolExecuter)


## Parallel Computing
This learning folder contains a main file (python_parallel.py)
and auxiliar files that are called inside this one.

It explores two different multiprocessing tutorials.

1) https://www.machinelearningplus.com/python/parallel-processing-python/
2) https://analyticsindiamag.com/run-python-code-in-parallel-using-multiprocessing/

The first one was relying on the Pool function of the
multiprocessing library, and was not possible to run on the
current setup.

The second tutorial was based on the same package, but used
the Process class. it was much more successfull, and it
was possible to create a class called newProcess that used a
function defined by us and prepared a specific process.


TODO: Create class that can receive a generic function or
object.

TODO: Learn how to communicate between processes.


In addition to the Process class, the second tutorial also
exemplified the multiprocessing using the ProcessToolExecutor.
*This method is reported to be more efficient than the Process
Class, at least according to the tutorial page*
This can be found in the second part of the main code.
Finally, we test this ProcessToolExecutor in a simple image
processing code, comparing sequential and parallel runs.

Sample images were downloaded from [Pexels](https://www.pexels.com/search/nature/)

### Pool workarounds
Several workarounds were tried on the pool functionality, like
checking that __name__ == '__main__', but the program always got
stuck.


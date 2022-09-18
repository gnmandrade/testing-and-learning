# testing-and-learning
Repository to test pieces of code and learn specific concepts.


# Contents
+ Dataviz_and_models
+ Tensorflow
+ Parallel_Computing (multiprocessing, ProcessPoolExecuter)
+ TradingAPI
+ Design_Paterns
+ UnitTest
+ GUI using Tkinter


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

Sample images were downloaded from [Pexels](https://www.pexels.com/search/nature/).

### Pool workarounds
Several workarounds were tried on the pool functionality, like
checking that
```
__name__ == '__main__'
```
but the program always got stuck.

A solution using Process or ProcessToolExecutor ended up being
adopted in the end.


## Trading API
This folders contains tests made with trading APIs.
At the moment, the first tests were done using the Interactive Brokers
Trader WorkStation (TWS) trial version.

It also contains a folder called Market Data, which contains sample
functions of market data APIs. The current ones are Yahoo Finance and Investing.com

### Interactive Brokers Python API
The first implemented test code. It pressuposes the installation
of the IBAPI python package that may be downloaded from their
website after the creation of a trial account on the
[Broker's website](https://www.interactivebrokers.ie/en/home.php).

Also relevant might be the
[API documentation](https://interactivebrokers.github.io/tws-api/initial_setup.html)
that can be found in their website.

After downloading and impacking, the API is installed using
pip and the setup.py file that was included in the source folder.



## Design Paterns
A sample implementation of each Design Patern present in the folder.
The directory also contains a more detailled ReadMe file
with the specifications of each Patern.
At the moment we can find there an implementation of a simple card game
based on a tutorial that can be found in the local notes.

## UnitTest
This section has a simple implementation of some functions and a class with
methods, as well as some tests that could be preformed on them.

The way to execute all the tests simultaneously can be seen in the local
readme file.

## GUI Tkinter
Test how to build a GUI using the tkinter package.

We currently only have a button that displays a message when pressed.
TODO: develop more useful GUIs.
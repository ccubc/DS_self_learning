## Managing Virtual Environment with Anaconda

* `conda create -n my_first_env python=3.8`: create an environment based on python 3.8 (if not creating environments, it's hard to manage different python versions on one single machine)
* `conda active my_first_env`: activate the environment my_first_env
* `conda deactivate`: deactivate current environment
* `conda list`: list all the packages installed on current virtual environment
* `conda env list`: list all conda environments
* `conda env remove -n my_first_env`: remove an environment

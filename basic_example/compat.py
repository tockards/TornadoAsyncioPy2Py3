import future
from future.standard_library import install_aliases
install_aliases()

if future.utils.PY2:
    from basic_example_python2 import BasicExampleClass

else:
    from basic_example_python3 import BasicExampleClass

BasicExampleClass = BasicExampleClass


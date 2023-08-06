# coding=utf-8
from __future__ import absolute_import, print_function

import os

if os.system('python -c "import tensorflow"') == 0:
    import tensorflow

    print("Tensorflow: ", tensorflow.__version__)  # pylint: disable=no-member
else:
    print("Import tensorflow error. Try to reinstall tensorflow.")
    os.system(
        "pip install tensorflow=={}".format(
            os.environ.get("TENSORFLOW_VERSION", "1.12.0")
        )
    )
    import tensorflow

    print("Tensorflow: ", tensorflow.__version__)  # pylint: disable=no-member

# Description:
#   Build rule for Python and Numpy.
#   This rule works for Debian and Ubuntu. Other platforms might keep the
#   headers in different places, cf. 'How to build DeepMind Lab' in build.md.
#   python3.5 or python 3.6


# hdrs starts its path from /usr
# therefore, the absolute path of 
# "include/python3.6/*.h" will be "/usr/include/python3.6/*.h"
# following the same logic, the absolute path of 
# "lib/python3/dist-packages/numpy/core/include/numpy/*.h" will be "/usr/lib/python3/dist-packages/numpy/core/include/numpy/*.h"


cc_library(
    name = "python",
    hdrs = glob([
        "include/python3.6/*.h",
        "lib/python3/dist-packages/numpy/core/include/numpy/*.h", # in a normal desktop ubuntu 16.04
        #"local/lib/python3.5/dist-packages/numpy/core/include/numpy/*.h", # in some other ubuntu
    ]),
    includes = [
        "include/python3.6",
        "lib/python3/dist-packages/numpy/core/include", # in a normal desktop ubuntu 16.04
        #"local/lib/python3.5/dist-packages/numpy/core/include", # in some other ubuntu
    ],
    visibility = ["//visibility:public"],
)

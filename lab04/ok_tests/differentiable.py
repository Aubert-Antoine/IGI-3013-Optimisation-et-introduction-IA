test = {
    "name": "differentiable",
    "points": 6,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.round([f1(x) for x in [-1,0,1]], decimals=3)\narray([6.25, 0.25, 2.25])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.round([f2(x) for x in [-1,0,1]], decimals=3)\narray([-0.5,  0. ,  1.5])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.round([f3(x) for x in [-1,0.1,1]], decimals=3)\narray([-1.   ,  0.316,  1.   ])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.round([f4(x) for x in [-1,0.1,1]], decimals=3)\narray([0.731, 0.   , 0.269])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.round([f5(x) for x in [-1,0,1]], decimals=3)\narray([ 0.   ,  0.693, 10.   ])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.round([f6(x) for x in [-1,0.1,1]], decimals=3)\narray([ 0.544, -0.005, -0.544])",
                    "hidden": False,
                    "locked": False
                }
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}
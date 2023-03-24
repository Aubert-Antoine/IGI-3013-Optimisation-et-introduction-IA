test = {
    "name": "autograd",
    "points": 6,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.round([fun1(-1), fun1(0.), fun1(1)], decimals=3)\narray([ 0.   ,  0.693, 10.   ])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> [np.abs(g1_formula(x) - g1_auto(x)) < 1e-7 for x in [-1., 0., 1.]]\n[True, True, True]",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.round([fun2([-1,-1]), fun2([0,0]), fun2([1,1])], decimals=3)\narray([ 1,  0, -1])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> [np.linalg.norm(g2_formula(x) - g2_auto(np.array(x))) < 1e-7 for x in [[-1.,-1.], [0.,0.], [1.,1.]]]\n[True, True, True]",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.round([fun3([-1,-1]), fun3([0,0]), fun3([1,0])], decimals=3)\narray([4, 0, 1])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> [np.linalg.norm(g3_formula(x) - g3_auto(np.array(x))) < 1e-7 for x in [[-1.,-1.], [0.,0.], [1.,0.]]]\n[True, True, True]",
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
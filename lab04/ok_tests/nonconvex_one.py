test = {
    "name": "nonconvex_one",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.round((cost_fun(-1), cost_fun(0), cost_fun(1)), decimals=3)\narray([ 0.74,  0.54, -0.79])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.abs(w - w_bar) < 1e-5\nTrue",
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
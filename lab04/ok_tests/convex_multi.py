test = {
    "name": "convex_multi",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.round((cost_fun([-1,-1]), cost_fun([0,0]), cost_fun([1,1])), decimals=3)\narray([13.,  3., 31.])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.linalg.norm(w - w_bar) < 1e-5\nTrue",
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
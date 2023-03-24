test = {
    "name": "convex_one",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> cost_fun(-1), cost_fun(0), cost_fun(1)\n(-0.16, 0.0, 0.24)",
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
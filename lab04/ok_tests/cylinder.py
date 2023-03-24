test = {
    "name": "cylinder",
    "points": 3,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> cost_fun(0.1), cost_fun(1), cost_fun(2)\n(660.0628318530718, 72.2831853071796, 58.132741228718345)",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.abs(radius - radius_bar) < 1e-5\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.abs(height - 2*radius_bar) < 1e-5\nTrue",
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
test = {
    "name": "grid_search",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.random.seed(42);\n>>> \n>>> x = np.random.rand(20);\n>>> y = 0.5*x + 2 + 0.05 * np.random.randn(20);\n>>> w = np.array([1.,1.]);\n>>> \n>>> cost  = lambda w: np.sum((w[0]*x + w[1] - y)**2);\n>>> w_min = [0,1];\n>>> w_max = [1,3];\n>>> \n>>> w, _ = grid_search(cost, w_min, w_max);\n>>> \n>>> np.round(w, decimals=4)\narray([0.4453, 2.0296])",
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
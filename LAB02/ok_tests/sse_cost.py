test = {
    "name": "sse_cost",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.random.seed(42);\n>>> \n>>> x = np.random.rand(20);\n>>> y = 0.5*x + 2 + 0.05 * np.random.randn(20);\n>>> w = np.array([1.,1.]);\n>>> \n>>> c = sse_cost(w, x, y);\n>>> \n>>> np.round(c, decimals=4)\n12.0125",
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
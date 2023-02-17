test = {
    "name": "cross_entropy",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.random.seed(42);\n>>> \n>>> x = np.random.rand(20);\n>>> y = 0.5*x + 2 + 0.05 * np.random.randn(20);\n>>> w = np.array([0,0]);\n>>> \n>>> cost = lambda w: np.sum((w[0]*x + w[1] - y)**2);\n>>> \n>>> alpha  = 0.1;\n>>> epochs = 100;\n>>> n_points = 50;\n>>> \n>>> w, _ = cross_entropy_method(cost, w, alpha, epochs, n_points);\n>>> \n>>> np.round(w, decimals=3)\narray([0.464, 2.004])",
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
test = {
    "name": "random_search",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.random.seed(42);\n>>> \n>>> x = np.random.rand(20);\n>>> y = 0.5*x + 2 + 0.05 * np.random.randn(20);\n>>> w = np.array([0.5,0.7]);\n>>> \n>>> cost = lambda w: np.sum((w[0]*x + w[1] - y)**2);\n>>> alpha  = 0.1;\n>>> epochs = 30;\n>>> dirs   = 10;\n>>> \n>>> w, _ = random_search(cost, w, alpha, epochs, dirs);\n>>> \n>>> np.round(w, decimals=4)\narray([0.5445, 1.9832])",
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
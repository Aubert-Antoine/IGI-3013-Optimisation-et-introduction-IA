test = {
    "name": "gradient_descent",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.random.seed(42);\n>>> \n>>> x = np.random.rand(20);\n>>> y = 0.5*x + 2 + 0.05 * np.random.randn(20);\n>>> cost = lambda w: np.sum((w[0]*x + w[1] - y)**2);\n>>> \n>>> w, _ = gradient_descent(cost, init=[0.,0.], alpha=0.01, epochs=100);\n>>> \n>>> np.round(w, decimals=4)\narray([0.4952, 1.9878])",
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
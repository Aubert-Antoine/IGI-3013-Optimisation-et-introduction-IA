test = {
    "name": "distance_matrix",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.random.seed(24);\n>>> \n>>> X = np.random.randint(20,size=(4,5));\n>>> Y = np.random.randint(20,size=(3,5));\n>>> \n>>> dist = distance_matrix(X, Y);\n>>> \n>>> np.round(dist, decimals=2)\narray([[19.54, 11.49, 24.86],\n       [23.87, 21.21, 18.92],\n       [23.47, 24.76, 27.04],\n       [18.25, 16.22, 12.37]])",
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
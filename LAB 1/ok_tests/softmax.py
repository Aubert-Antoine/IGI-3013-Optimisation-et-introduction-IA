test = {
    "name": "softmax",
    "points": 3,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> np.round(s_all, decimals=4)\narray([[8.525e-01, 8.000e-04, 1.560e-02],\n       [1.154e-01, 1.560e-02, 1.000e-04]])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.round(s_cols, decimals=4)\narray([[0.8808, 0.0474, 0.9933],\n       [0.1192, 0.9526, 0.0067]])",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.round(s_rows, decimals=4)\narray([[9.811e-01, 9.000e-04, 1.800e-02],\n       [8.801e-01, 1.191e-01, 8.000e-04]])",
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
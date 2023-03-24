test = {
    "name": "kmeans_optimization",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> cost_fun(c) < 50\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> points, y = datasets.make_blobs(n_samples=30, random_state=42);\n>>> \n>>> y_gd = np.linalg.norm(points[:,None] - c[None,:], axis=2).argmin(1);\n>>> \n>>> c_pred = np.stack([np.mean(points[y_gd==i], axis=0) for i in range(3)], axis=0);\n>>> c_True = np.stack([np.mean(points[y==i], axis=0) for i in range(3)], axis=0);\n>>> \n>>> error = lambda i: np.linalg.norm(c_pred[i] - c_True, axis=1).min();\n>>> \n>>> error(0), error(1), error(2)\n(0.0, 0.0, 0.0)",
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
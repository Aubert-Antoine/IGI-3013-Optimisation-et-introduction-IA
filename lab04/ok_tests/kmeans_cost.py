test = {
    "name": "kmeans_cost",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> points, y = datasets.make_blobs(n_samples=30, random_state=42);\n>>> c_True = np.stack([np.mean(points[y==i], axis=0) for i in range(3)], axis=0);\n>>> \n>>> np.round(kmeans_cost(c_True, points), decimals=4)\n48.0203",
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
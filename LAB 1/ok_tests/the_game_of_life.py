test = {
    "name": "the_game_of_life",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> board = np.array([[0,0,0,0,0,0],\n...                   [0,0,0,1,0,0],\n...                   [0,1,0,1,0,0],\n...                   [0,0,1,1,0,0],\n...                   [0,0,0,0,0,0],\n...                   [0,0,0,0,0,0]]);\n>>> \n>>> count = neighbor_counting(board);\n>>> \n>>> new_board = evolution_rules(board, count);\n>>> \n>>> new_board\narray([[0, 0, 0, 0, 0, 0],\n       [0, 0, 1, 0, 0, 0],\n       [0, 0, 0, 1, 1, 0],\n       [0, 0, 1, 1, 0, 0],\n       [0, 0, 0, 0, 0, 0],\n       [0, 0, 0, 0, 0, 0]])",
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
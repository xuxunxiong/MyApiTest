import api_server
import multiprocessing
import unittest
import time


class apiserverUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        "Hook method for setting up class fixture before running tests in the class."
        cls.api_server_process = multiprocessing.Process(
            target=api_server.app.run()

        )
        cls.api_server_process.start()
        time.sleep(0.1)
        api_server.clear_users()



    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        cls.api_server_process.terminate()



import time
import unittest

from mandarina.benchmark import Benchmark
from mandarina.benchmark import timer
from mandarina.benchmark import get_process_memory_usage

class TestBenchmark(unittest.TestCase):
    def test(self):
        pass

    def test_benchmark(self):
        execution_time = 0.1
        result = Benchmark.run(lambda: time.sleep(execution_time), 10, print_output=False)
        self.assertAlmostEqual(result[0], execution_time, 2)
        self.assertAlmostEqual(result[1], execution_time, 2)

    def test_timer(self):
        # Call to test if function runs without errors
        @timer
        def f():
            time.sleep(0.1)

    def test_get_process_memory_usage(self):
        # Call to test if function runs without errors
        get_process_memory_usage()
        get_process_memory_usage(readable=False)


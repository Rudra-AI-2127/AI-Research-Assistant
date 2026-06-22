from concurrent.futures import ThreadPoolExecutor


class ParallelExecutor:

    def run_parallel(
        self,
        func1,
        arg1,
        func2,
        arg2
    ):

        with ThreadPoolExecutor(
            max_workers=2
        ) as executor:

            future1 = executor.submit(
                func1,
                arg1
            )

            future2 = executor.submit(
                func2,
                arg2
            )

            result1 = future1.result()
            result2 = future2.result()

        return result1, result2
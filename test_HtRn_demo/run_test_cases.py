import pytest
import test_HtRn_demo.test_get_request_demo
import test_HtRn_demo.test_post_request_demo

class TestCases:
    test_HtRn_demo.test_get_request_demo
    test_HtRn_demo.test_post_request_demo


if __name__ == "__main__":

    TestCases()
    cmd_list = ['-v', '--html=report.html']
    pytest.main(cmd_list)



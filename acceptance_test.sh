#!/bin/bash
test "$(curl -v http://172.17.0.1:8765/sum?a=1\&b=2)" == 3
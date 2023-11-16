#!/bin/bash
test "$(curl -v http://172.17.0.1:8765/)" -eq "Hello NateDogg, Spring Boot Here!"
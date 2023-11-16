#!/bin/bash
test $(curl -v http://localhost:8765/hello) == "Hello NateDogg, Spring Boot Here!"
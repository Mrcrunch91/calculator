#!/bin/bash
test $(curl -v http://localhost:8765/hello) -eq "Hello NateDogg, Spring Boot Here!"
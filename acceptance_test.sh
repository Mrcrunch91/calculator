#!/bin/bash
test $(curl localhost:8765/hello) -eq "Hello NateDogg, Spring Boot Here!"
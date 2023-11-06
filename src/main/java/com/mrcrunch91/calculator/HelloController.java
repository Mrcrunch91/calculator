package com.mrcrunch91.calculator;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// @Controller
// @ResponseBody
@RestController
public class HelloController {

    @RequestMapping("/")
    String hello() {
        return "Hello NateDogg, Spring Boot Here!";
    }
}
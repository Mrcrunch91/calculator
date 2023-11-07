package com.mrcrunch91.calculator;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CalculatorApplication {

	public static void main(String[] args) {
		final String constant_test = "constant";
		SpringApplication.run(CalculatorApplication.class, args);
	}

}

package com.mrcrunch91.calculator;
import org.springframework.stereotype.Service;

@Service
public class Calculator {
    int sum(int a, int b){
        return a + b;
    }
}

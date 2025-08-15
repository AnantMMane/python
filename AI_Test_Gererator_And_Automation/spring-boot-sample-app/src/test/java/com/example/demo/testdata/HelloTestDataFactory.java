package com.example.demo.testdata;

import java.util.HashMap;
import java.util.Map;

public class HelloTestDataFactory {
    public static Map<String, Object> validHelloRequest() {
        Map<String, Object> data = new HashMap<>();
        data.put("name", "Alice");
        return data;
    }

    public static Map<String, Object> emptyNameHelloRequest() {
        Map<String, Object> data = new HashMap<>();
        data.put("name", "");
        return data;
    }

    public static Map<String, Object> longNameHelloRequest() {
        Map<String, Object> data = new HashMap<>();
        data.put("name", "A".repeat(1000));
        return data;
    }
} 
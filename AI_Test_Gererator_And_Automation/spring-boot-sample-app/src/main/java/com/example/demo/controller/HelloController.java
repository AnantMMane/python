package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/hello")
public class HelloController {
    
    @GetMapping
    public Map<String, String> hello() {
        return Map.of("message", "Hello from Spring Boot!");
    }

    @PostMapping
    public Map<String, Object> postHello(@RequestBody Map<String, Object> payload) {
        return Map.of(
            "message", "POST received!",
            "received", payload
        );
    }

    @PutMapping("/{id}")
    public Map<String, Object> putHello(@PathVariable String id, @RequestBody Map<String, Object> payload) {
        return Map.of(
            "message", "PUT received!",
            "id", id,
            "updated", payload
        );
    }
} 
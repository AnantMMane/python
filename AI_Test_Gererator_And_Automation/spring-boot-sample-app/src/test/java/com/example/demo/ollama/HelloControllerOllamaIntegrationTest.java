package com.example.demo.ollama;

import com.example.demo.controller.HelloController;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;

import java.util.HashMap;
import java.util.Map;

import static org.hamcrest.Matchers.equalTo;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(HelloController.class)
class HelloControllerOllamaIntegrationTest {

    @Autowired
    private MockMvc mvc;
    private ObjectMapper objectMapper = new ObjectMapper();

    @Test
    void hello() throws Exception {
        ResultActions result = mvc.perform(get("/hello"));
        result.andExpect(status().isOk())
                .andExpect(jsonPath("$.message", equalTo("Hello from Spring Boot!")));
    }

    @Test
    void postHello() throws Exception {
        Map<String, Object> payload = new HashMap<>();
        payload.put("name", "John Doe");
        ResultActions result = mvc.perform(post("/hello")
                                .contentType(MediaType.APPLICATION_JSON)
                                .content(objectMapper.writeValueAsString(payload)));
        result.andExpect(status().isOk())
                .andExpect(jsonPath("$.message", equalTo("POST received!")))
                .andExpect(jsonPath("$.received").value(payload));
    }

    @Test
    void putHello() throws Exception {
        Map<String, Object> payload = new HashMap<>();
        payload.put("name", "Jane Doe");
        ResultActions result = mvc.perform(put("/hello/123")
                                .contentType(MediaType.APPLICATION_JSON)
                                .content(objectMapper.writeValueAsString(payload)));
        result.andExpect(status().isOk())
                .andExpect(jsonPath("$.message", equalTo("PUT received!")))
                .andExpect(jsonPath("$.id").value("123"))
                .andExpect(jsonPath("$.updated").value(payload));
    }
}
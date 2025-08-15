package com.example.demo.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Map;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(HelloController.class)
class HelloControllerTest {
    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @Test
    void testGetHello() throws Exception {
        mockMvc.perform(get("/hello"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message").value("Hello from Spring Boot!"));
    }

    private String readJson(String path) throws Exception {
        return new String(Files.readAllBytes(Paths.get("test-data/" + path)));
    }

    @Test
    void testPostHelloWithSampleData() throws Exception {
        String json = readJson("sample-hello-request.json");
        mockMvc.perform(post("/hello")
                .contentType(MediaType.APPLICATION_JSON)
                .content(json))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message").value("POST received!"))
                .andExpect(jsonPath("$.received.name").value("Alice"));
    }

    @Test
    void testPostHelloWithEmptyName() throws Exception {
        String json = readJson("edge-case-hello-request-empty.json");
        mockMvc.perform(post("/hello")
                .contentType(MediaType.APPLICATION_JSON)
                .content(json))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message").value("POST received!"))
                .andExpect(jsonPath("$.received.name").value(""));
    }

    @Test
    void testPostHelloWithLongName() throws Exception {
        String json = readJson("edge-case-hello-request-long.json");
        mockMvc.perform(post("/hello")
                .contentType(MediaType.APPLICATION_JSON)
                .content(json))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message").value("POST received!"))
                .andExpect(jsonPath("$.received.name").isString());
    }

    @Test
    void testPutHello() throws Exception {
        Map<String, Object> payload = Map.of("status", "active");
        mockMvc.perform(put("/hello/123")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(payload)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message").value("PUT received!"))
                .andExpect(jsonPath("$.id").value("123"))
                .andExpect(jsonPath("$.updated.status").value("active"));
    }
} 